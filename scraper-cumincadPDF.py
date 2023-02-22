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
# ----------------------------------------------------------------------------------------------------------------------

series = "eCAADe" 

folder = series + "/"

pdfBaseUrl = 'http://papers.cumincad.org/data/works/att/'

def getPaperUrls(main_soup):
    '''find all papers link and return the list of papers'''
    form = main_soup.find('form', attrs={'name': 'main'})
    children = form.find_all('b')               #gets tag <b>
    linksList = []
    for child in children:                      #gets the parent of tag <b>, which is tag <a>. This removes other unecessary <a> tags
        parent = child.parent
        if parent.get('href') != None:          #if tag <a> has a valid url
            paperUrl = parent.get('href')
            paperName = paperUrl.split("/")[-1]
            pdfUrl = pdfBaseUrl + paperName
            linksList.append(pdfUrl)         #then add tag <a> to the list
    return linksList

def downloadPapers(url):
    '''download papers'''
    response = requests.get(url + '.pdf')
    if response.status_code == 404:
        response = requests.get(url + '.content.pdf')
        fileName = url.split("/")[-1]
        with open(folder + fileName + '.content.pdf', 'wb') as f:
            f.write(response.content)
    else:
        fileName = url.split("/")[-1]
        with open(folder + fileName + '.pdf', 'wb') as f:
            f.write(response.content)

def countPapers(folder):
    '''count the number of currently scraped paper'''
    return len(os.listdir(folder))

def main(total=3383):
    '''wrapper function of scraper'''
    page_number = 0
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
        # extract paper info
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
