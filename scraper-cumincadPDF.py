# Developed by Daniel Locatelli
# all rights reserved by Daniel Locatelli
# daniel.nlocatelli@gmail.com

'''CumInCAD PDF scraper'''
# ----------------------------------------------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import re
import time
# ----------------------------------------------------------------------------------------------------------------------

Source = "ACADIA" 

folder = Source + "/" 

def getPaperLinks(main_soup):
    '''find all papers link and return the list of papers'''
    form = main_soup.find('form', attrs={'name': 'main'})
    children = form.find_all('b')       #gets tag <b>
    paperLinks = []
    for child in children:              #gets the parent of tag <b>, which is tag <a>. This removes other unecessary <a> tags
        parent = child.parent
        if parent.get('href') != None:  #if tag <a> has a valid url
            paperNames.append(parent)       #then add tag <a> to the list
    return papersNames

def downloadPapers(paperLinks):
    '''download papers''' 

def countPapers(folder):
    '''count the number of currently scraped paper'''
    return len(os.listdir(folder))

def main(total=16336):
    '''wrapper function of scraper'''
    page_number = 0
    count = 0
    while page_number <= total:
        # access series site, e.g. ACADIA
        series_site = "".format(series, page number)
        # the first page of archive
        print(page_number)
        main_request = requests.get(main_site)
        main_soup = BeautifulSoup(main_request.text, 'html.parser')
        # get the papers in the page
        papers = getPapers(main_soup)
        # extract paper info
        for paper in papers:
            start = time.time()
            getPaperInfo(paper)
            count += 1
            end = time.time()
            print("{}/16336        {} papers,      {} sec".format(count, countPapers(folder), end - start))
        page_number += 20


if __name__ == "__main__":
    main()
