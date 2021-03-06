

from urllib.request import urlopen
from bs4 import BeautifulSoup
from xml.etree.ElementTree import tostring

html = urlopen("http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=0&f=S&l=50&d=PTXT&OS=car&RS=car&Query=car&TD=195492&Srch1=car&NextList1=Next+50+Hits")
bsObj = BeautifulSoup(html, "html5lib")
cont = int(bsObj.findAll("strong")[2].get_text())
quant_pags = int(cont / 50 ) + 1
for i in range(quant_pags):
    html = urlopen("http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=0&f=S&l=50&d=PTXT&OS=car&RS=car&Query=car&TD=195492&Srch1=car&NextList"+str(i)+"=Next+50+Hits")
    bsObj = BeautifulSoup(html, "html5lib")
    verify = 1
    for link in bsObj.findAll("a"):
        if 'href' in link.attrs and 'd=PTXT' in link.attrs['href'] and 'Page=Prev' not in link.attrs['href'] and 'Page=Next' not in link.attrs['href']:
            if verify % 2 == 0:
                print(link.get_text())
                print("http://patft.uspto.gov"+ link.attrs['href'])
            verify = verify + 1
            