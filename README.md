# scraper-cumincadPDF
Batch download PDFs from CuminCAD for each series e.g eCAADe

This tool was developed for studying purposes. It is not intended to be used to flood cumincad website.
Reducing or eliminating the waiting time in the code could potentially cause a flooding requests and damaging the wesite performance!

To use it, you will need to install:
Beautifulsoup (simply type on your Command Prompt 'pip install Beautifulsoup')

To execute the code:
Type the series you want to scrape e.g eCAADe on line 21 of code.
You also have to create a folder for your series in the same place the python code is saved.
  For exemple you saved the python file at C:\Users\yourName\Desktop\scraper-cumincadPDF
  There you have to create another folder C:\Users\yourName\Desktop\scraper-cumincadPDF\eCAADe
Go to cumincad.org and check in the last page o the series what is the total number of papers.
Then add this number in place of the number on line 112 of the code.

You are good to go.

In case the code stops at some point and you want to continue from the last downloaded paper:
Go to the series folder your created earlier and see how many files are there.
Get this number and add it to the page_number on line 114 of the code.
