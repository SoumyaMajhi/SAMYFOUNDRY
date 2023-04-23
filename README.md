# SAMYFOUNDRY
A Sanf*undry Scraper for use in 2023 and after

## Instructions to use the code:
1. Download the `samyfoundry.py` file from this Github repo.
2. Install the required libraries in command prompt for windows:
```
pip install cfscrape
pip install beautifulsoup4
pip install requests
```
3. Run the `samyfoundry.py` file with `python samyfoundry.py` or `python3 samyfoundry.py` in command prompt
4. Enter the Sanf*undry page link containing all the topics of a particular chapter.

## Working of the Code:
1. The `cfscrape` module bypasses the Cloudflare security and captcha present while entering the site of the provided link.
2. Then it parses the HTML content of the webpage with the help of `BeautifulSoup`.
3. The code automatically creates a text file within the same folder as the code file `samyfoundry.py`, with the name scraped from the provided link
4. It scrapes the initial page containing all the topic links and gathers all of them in a list.
5. Then it parses each topic link and scrapes all the questions and answers, avoiding all the sticky banner ads, links and extra advertisements on the site
6. And stores/appends each topic's Q/A in the text file created at the beginning.
7. After it has completed parsing and scraping all the topics links, it stops the scraping loop, prints `End`, closes the file, prints `Total Topics Found: `, `Total Q/A Found: `, and stops the execution.
8. In the meantime, while the code is being executed, it keeps printing the topic numbers and its total questions numbers, which has been successfully scraped and extracted into the file.


**Note:** This code was written by me(Soumya Majhi / Samy) in April 2023 for my own personal academic purposes, as all other codes available in Github and elsewhere to scrape this website was outdated and didn't provide proper outputs. So, it should only be used for personal/academic purposes, and not for any type of commercial reasons.
And, if anyone would like to use this code anywhere, just provide a link to this repository of mine there, that will be all needed.
