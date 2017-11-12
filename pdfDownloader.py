# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 16:12:00 2017

@author: Asif
"""

import requests
from bs4 import BeautifulSoup

from urllib.request import Request, urlopen
import ErrorHandler as eh

def DownloadPDF(ListOfLink, ListOfBookName):
    #file_url = "http://www.wuperbooks.com/uploads/5/6/4/5/56458159/public_finance_by_kareem.pdf"

    for idx, (link, name) in enumerate(zip(ListOfLink, ListOfBookName)):
        if  idx >=37:
            try:         
                r = requests.get(link, stream = True)    
                with open(name,"wb") as pdf:
                    for chunk in r.iter_content(chunk_size=1024):
                    # writing one chunk at a time to pdf file
                         if chunk:
                             pdf.write(chunk)
                print('end of -> ',idx)
            except:
                print('problem in ->',idx)
                pass
    





def FindLinks(BaseDownloadLink):
    ListOfLink = []
    ListOfBookName = []

    url = 'http://www.wuperbooks.com/medical-books.html'
    #BaseDownloadLink = 'http://www.wuperbooks.com'
    responseCode = eh.get_status_code(url)
    if responseCode == 200:
        try:
            hdr = {'User-Agent': 'Mozilla/5.0'}
            req = Request(url,headers=hdr)
            page = urlopen(req)
            soup = BeautifulSoup(page,"lxml")
            #print(soup)
            allLink = soup.find_all("a")
            #print(allLink)
            for aTag in allLink:
                try:
                    link = aTag['href']
                    link = str(link)
                    if link.endswith('.pdf'):
                        TempName = link
                        TempName = TempName.split('/')
                        ListOfBookName.append(TempName[len(TempName)-1])
                        link = BaseDownloadLink + link
                        ListOfLink.append(link)
                except:
                    print('A exc')


            #print('length=',len(ListOfLink),'\n',ListOfLink)
        except:
            print('Exception')
    return ListOfLink, ListOfBookName

if __name__ == '__main__':
    
    '''
    '''
    ListOfLink, ListOfBookName = FindLinks('http://www.wuperbooks.com')
    print(len(ListOfLink))
    DownloadPDF(ListOfLink, ListOfBookName)
    
