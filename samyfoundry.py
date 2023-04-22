#pip install cfscrape  #installing Cloudflare-scrape to bypass Cloudflare security and captcha
#0. Set up requirements
import cfscrape
import requests
from bs4 import BeautifulSoup

url=input('Enter Sanf*undry page URL containing all Topic links of a Chapter: ')
#1. Get the HTML
scraper = cfscrape.create_scraper()  # returns a CloudflareScraper instance
r=scraper.get(url)
htmlContent=r.content

#2. Parse the HTML
soup=BeautifulSoup(htmlContent, 'html5lib')

#3. HTML Tree Traversal
divs=soup.find('div', class_='entry-content')

lists=divs.find_all('table')

filename=url.split('/')[3]
f=open( filename + '.txt','ab')

topics_total=0
qna_total=0
for l in lists:
    topics=l.find_all('a')
    for t in topics:
        topics_total+=1
        links=t['href']
        topicnames=t.text
        f=open( filename + '.txt','ab')
        f.write("\n\n\t\t".encode()+"Topic ".encode()+str(topics_total).encode()+". ".encode()+topicnames.encode()+'\n\n'.encode())
        f.seek(0)

        url=links
        #1. Get the HTML
        scraper = cfscrape.create_scraper()  # returns a CloudflareScraper instance
        r=scraper.get(url)
        htmlContent=r.content

        #2. Parse the HTML
        soup=BeautifulSoup(htmlContent, 'html5lib')

        #3. HTML Tree Traversal
        divs=soup.find('div', class_='entry-content')

        #Remove code of banner ads
        for child in divs.find_all("div", class_="sf-mobile-ads"):
            child.decompose()

        for child in divs.find_all("div", class_="sf-desktop-ads"):
            child.decompose()

        #Remove all extra links
        for child in divs.find_all("a"):
            child.decompose()

        #Remove un necessary p tags
        for child in divs.find_all("p"):
            # fetching text from tag and remove whitespaces
            if len(child.text.strip()) == 0:
                # Remove empty tag
                child.decompose()

        #Remove un necessary div tags
        for child in divs.find_all("div"):
            # fetching text from tag and remove whitespaces
            if len(child.text.strip()) == 0:
                # Remove empty tag
                child.decompose()
        
        #removing extra divs with no class (specially sanfoundry ad links)
        for child in divs.find_all("div", class_=False):
            child.decompose()

        for child in divs.find_all("div", class_="desktop-content"):
            child.decompose()

        for child in divs.find_all("div", class_="mobile-content"):
            child.decompose()

        for child in divs.find_all("div", class_="sf-nav-bottom"):
            child.decompose()
        
        #questions
        questions=divs.find_all('p')[1:]   #no need, was needed for some earlier version of the code
        #print(questions)
        #answers
        ans=divs.findAll('div',class_='collapseomatic_content')

        #total no. of Q/A
        questions_total=len(ans)
        print("Topic ",topics_total,"Total q ",questions_total)

        for child in divs:
            if child in ans:
                qna_total+=1
            if child == ans[-1]:
                f.write(child.text.encode())
                f.seek(0)
                break
            else:
                f.write(child.text.encode())
                f.seek(0)
print("End")
      
f.close()
print('Total Topics Found: ',topics_total)
print('Total Q/A Found: ',qna_total)
