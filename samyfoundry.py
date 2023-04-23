#pip install cfscrape  #installing Cloudflare-scrape to bypass Cloudflare security and captcha

'''
#---------FOR GOOGLE COLAB TO INSTALL PDFKIT AND WKHTMLTOPDF-------

#!cat /etc/os-release
#!uname -m
!pip install pdfkit
!wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.bionic_amd64.deb
!cp wkhtmltox_0.12.6-1.bionic_amd64.deb /usr/bin
!sudo apt install /usr/bin/wkhtmltox_0.12.6-1.bionic_amd64.deb
'''

#0. Set up requirements
import cfscrape
from bs4 import BeautifulSoup
import pdfkit

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
f=open( filename + '.html','ab')  #create html file for storing the scraped data
f.write('<!DOCTYPE html> \n <html>\n <head> \n <meta charset="UTF-8"> \n </head> \n <body>'.encode())
f.seek(0)

topics_total=0
qna_total=0
for l in lists:
    topics=l.find_all('a')
    for t in topics:
        topics_total+=1
        links=t['href']
        topicnames=t.text
        f=open( filename + '.html','ab')
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
        
        #removing extra divs with no class (specially sanf*undry ad links)
        for child in divs.find_all("div", class_=False):
            child.decompose()

        for child in divs.find_all("div", class_="desktop-content"):
            child.decompose()

        for child in divs.find_all("div", class_="mobile-content"):
            child.decompose()

        for child in divs.find_all("div", class_="sf-nav-bottom"):
            child.decompose()
        
        #questions
        questions=divs.find_all('p')[1:]
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
                f.write(str(child).encode())
                f.seek(0)
                break
            else:
                f.write(str(child).encode())
                f.seek(0)

f.write('\n\n\t\t'.encode() + 'Total Topics Found: '.encode() + str(topics_total).encode())
f.seek(0)
f.write('\n\t\t'.encode() + 'Total Q/A Found: '.encode() + str(qna_total).encode())
f.seek(0)

f.write('</body> \n </html>'.encode())
f.seek(0)

f.close()

#convert html to pdf
pdfkit.from_file( filename + '.html', filename + '.pdf')

print("End")
print('Total Topics Found: ',topics_total)
print('Total Q/A Found: ',qna_total)
      
f.close()
print('Total Topics Found: ',topics_total)
print('Total Q/A Found: ',qna_total)
