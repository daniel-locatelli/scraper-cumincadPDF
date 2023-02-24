<h1># scraper-cumincadPDF</h1>

<p>Batch download PDFs from CuminCAD for each series e.g eCAADe</p>

<p>This tool was developed for studying purposes. It is not intended to flood cumincad website.<br />
By using it you agree you are aware that by reducing or eliminating the waiting time from the code you can potentially cause flooding requests and damage the website&#39;s performance!</p>

<h2>To use it, you will need to install the following</h2>

<ul>
	<li>BeautifulSoup (type on your Command Prompt &#39;pip install Beautifulsoup&#39;)</li>
</ul>

<h2>To execute the code</h2>

<ul>
	<li>Type the series you want to scrape e.g <strong>eCAADe</strong>&nbsp;on line 21 of the code.</li>
	<li>You also have to create a folder for your series in the same place the python code is saved.
	<ul>
		<li>&nbsp; For example, you saved the python file at C:\Users\yourName\Desktop\scraper-cumincadPDF</li>
		<li>&nbsp; There you have to create another folder C:\Users\yourName\Desktop\scraper-cumincadPDF\<strong>eCAADe</strong></li>
	</ul>
	</li>
	<li>Go to cumincad.org and check on the last page o the series what is the total number of papers.</li>
	<li>Then add this number in place of the number on line 112 of the code.</li>
</ul>

<p>You are good to go.</p>

<h2>In case the code stops and you want to continue from the last downloaded paper</h2>

<p>Go to the series folder your created earlier and see how many files are there.<br />
Get this number and add it to the <strong>page_number</strong> on line 114 of the code.<br />
&nbsp;</p>
