# Developed by Daniel Locatelli
# daniel.nlocatelli@gmail.com

'''CumInCAD PDF scraper'''
# ----------------------------------------------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
import os
import time
import random
# ----------------------------------------------------------------------------------------------------------------------

''' Series available:
ACADIA, ASCAAD, AVOCAAD, Architectural%20Intelligence, CAAD%20Futures, CAADRIA, CADline, DDSS, EAEA, SIGRADI, SIGraDi
book, cdrf, eCAADe, eCAADeSIGraDi, journal, journal%20paper, other, plCAD, report, thesis%3aMSc, thesis%3aPhD

You can see all the series here:
http://papers.cumincad.org/cgi-bin/works/BrowseTree?field=series&order=AZ
'''

series = "eCAADe" 
folder = series + "/"
baseUrl = 'http://papers.cumincad.org'


#this also did't work. The filename changes
#it has to get the pdf icon path
#if there is no pdf icon, then enter the paper link and download from there

def getPaperUrls(main_soup):
    '''find all papers link and return the list of papers'''
    form = main_soup.find('form', attrs={'name': 'main'})
    tables = form.find_all('tr')
    paperUrls = []
    for table in tables:
        if table.has_attr('bgcolor'):
            # check if there is a pdf icon
            pdfImg = table.find(attrs = {'src':'/img/pdf.png'})
            
            # if there is a pdf icon, then get the Url
            if pdfImg != None:
                pdfHref = pdfImg.parent.get('href')
                workingUrl = baseUrl + pdfHref

            # if there isn't, then enter paper page
            else:
                paperPageUrl = table.a.get('href')
                response = requests.get(paperPageUrl)
                paperSoup = BeautifulSoup(response.text, 'html.parser')

                # and look for another pdf icon
                pdfIconUrl = paperSoup.find(attrs = {'src':'/woda/icons/flat-noborder/pdf.gif'})
                # if there is a pdf icon
                if pdfIconUrl != None:
                    pdfHref = pdfIconUrl.parent.get('href')
                    pdfHref = pdfHref.replace('	', '') # remove href arrow icons
                    pdfUrl = baseUrl + pdfHref
                    responsePdf = requests.get(pdfUrl)
                    # check if the link actually works
                    if responsePdf.status_code != 404:
                        # if there is an icon and the pdf file is available, then pdfUrl is added to paperUrls list
                        workingUrl = pdfUrl
                    else:
                        # if there is an icon but the pdf file is not available, then add paper page url to paperUrls list
                        workingUrl = paperPageUrl
                else:
                    # if there is no pdf icon, then add paper page url to paperUrls list
                    workingUrl = paperPageUrl

            paperUrls.append(workingUrl)
    return paperUrls

def downloadPapers(url):
    '''download papers'''
    # fix file name
    originalFileName = url.split("/")[-1]                   # extract the original file name with extension
    originalFileNameSplit = originalFileName.split('.')     # extract file name only to prevent mistakes with extension '.pdf' like '.pdf_'
    fileName = ''

    # check if a working pdf url is available
    if '.pdf' in url:
        # file name
        count = 0
        for segment in originalFileNameSplit:
            count += 1
            if count < len(originalFileNameSplit):
                fileName += segment + '.'

        response = requests.get(url)
        print ('Downloading paper {}pdf...'.format(fileName))
        print (url)
        with open(folder + fileName + 'pdf', 'wb') as f:
            f.write(response.content)
    else:
        fileName += originalFileName
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        core = soup.find(attrs = {'class':'CORE'})
        paperText = '### Paper could not be downloaded from cumincad.org ###' + '\n' + '\n'
        print ('Paper {} could not be downloaded, {}.txt will be created instead...'.format(fileName, fileName))
        for string in core.strings:
            if string != '\n':
                paperText += string + '\n'
        with open(folder + fileName + '.txt', 'w', encoding="utf-8") as f:
            f.write(paperText)
        

def countPapers(folder):
    '''count the number of currently scraped paper'''
    return len(os.listdir(folder))

def main(total=3383):
    '''wrapper function of scraper'''
    page_number = 0
    while page_number <= total:
        # access series page, e.g. ACADIA
        series_page = "http://papers.cumincad.org/cgi-bin/works/BrowseTree?field=series&separator=:&recurse=0&order=AZ&value={}&first={}".format(series, page_number)
        # page of archive
        print('Page number: ' + str(page_number))
        print('Checking if page is available...')
        main_response = requests.get(series_page)
        if main_response.status_code != 404:
            main_soup = BeautifulSoup(main_response.text, 'html.parser')
            print('Page is available, retrieving list of paper urls to download...')
        else:
            print('Page is not available. Maybe they changed the url format.')
            exit
        # get the papers in the page
        papersUrl = getPaperUrls(main_soup)
        # download paper
        for url in papersUrl:
            start = time.time()
            downloadPapers(url)
            end = time.time()
            downloadTime = round(end - start, 2)
            print("{} out of 3383 papers downloaded,      {} sec".format(countPapers(folder), downloadTime))
            time.sleep(random.randint(2, 3)) # a buffer to not flood the site 
        page_number += 20
        print ('\n')

if __name__ == "__main__":
    main()
