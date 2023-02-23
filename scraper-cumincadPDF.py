# Developed by Daniel Locatelli
# all rights reserved by Daniel Locatelli
# daniel.nlocatelli@gmail.com

'''CumInCAD PDF scraper'''
# ----------------------------------------------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
import os
import time
import random
import pdfkit
# ----------------------------------------------------------------------------------------------------------------------

series = "eCAADe" 

folder = series + "/"

pdfBaseUrl = 'http://papers.cumincad.org'

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
                workingUrl = pdfBaseUrl + pdfHref

            # if there isn't, then enter paper page
            else:
                paperPageUrl = table.a.get('href')
                response = requests.get(paperPageUrl)
                paperSoup = BeautifulSoup(response.text, 'html.parser')

                # and look for another pdf icon
                pdfIconUrl = paperSoup.find(attrs = {'src':'/woda/icons/flat-noborder/pdf.gif'})
                pdfHref = pdfIconUrl.parent.get('href')
                pdfUrl = pdfBaseUrl + pdfHref
                responsePdf = requests.get(pdfUrl)

                # if there is a pdf icon
                if pdfUrl != None:
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
    if url.split(".")[-1] == 'pdf':
        response = requests.get(url)
        fileName = url.split("/")[-1]
        with open(folder + fileName, 'wb') as f:
            f.write(response.content)
    else:
        print ("I am here for the next step")

def countPapers(folder):
    '''count the number of currently scraped paper'''
    return len(os.listdir(folder))

def main(total=599):
    '''wrapper function of scraper'''
    page_number = 580
    count = 0
    while page_number <= total:
        # access series site, e.g. ACADIA
        series_site = "http://papers.cumincad.org/cgi-bin/works/BrowseTree?field=series&separator=:&recurse=0&order=AZ&value={}&first={}".format(series, page_number)
        # the first page of archive
        print('Page number: ' + str(page_number))
        main_request = requests.get(series_site)
        main_soup = BeautifulSoup(main_request.text, 'html.parser')
        # get the papers in the page
        papersUrl = getPaperUrls(main_soup)
        # download paper
        for url in papersUrl:
            start = time.time()
            print (url)
            downloadPapers(url)
            count += 1
            end = time.time()
            print("{}/3383        {} papers,      {} sec".format(count, countPapers(folder), end - start))
            time.sleep(random.randint(1, 3))
        page_number += 20


if __name__ == "__main__":
    main()
