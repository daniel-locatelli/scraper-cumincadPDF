<h1># scraper-cumincadPDF</h1>

<p>Batch download PDFs from CuminCAD for each series e.g ACADIA</p>

<h2>Prerequisite</h2>

<ul>
	<li>BeautifulSoup (type on your Command Prompt &#39;pip install Beautifulsoup&#39;)</li>
</ul>

<h2>To execute the code</h2>

<ul>
	<li>Choose the <strong>series</strong>&nbsp;you want to scrape e.g &quot;ACADIA&quot;.</li>
	<li>You also have to create a folder for your series in the same place the python code is saved.<br />
	For example&nbsp;C:\Users\yourName\Desktop\scraper-cumincadPDF\<strong>ACADIA</strong></li>
	<li>Go to cumincad.org and check what is the total number of papers in that series.<br />
	Then assign this value to <strong>totalNumberPapers</strong></li>
</ul>

<p>You are good to go.</p>

<h2>In case the code stops and you want to continue from the last downloaded paper</h2>

<p>Go to the series folder your created earlier and see how many files are there.<br />
Assign this value to <strong>papersAlreadyDownloaded</strong>.</p>

<h2>In case the code doesn&#39;t find a pdf for the paper</h2>

<p>Sometimes the pdf is missing, or simply there is no pdf at all. In this case, the code generates a .txt file with the information available.</p>

<h2>Disclaimer</h2>

<p>This tool was developed for studying purposes.<br />
By using it you agree you are aware that by reducing or eliminating the waiting time from the code you can potentially cause flooding requests and damage the website&#39;s performance!.<br />
I do not assume any responsabilities for its use.</p>
