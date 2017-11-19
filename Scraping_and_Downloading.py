

from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup
hdr = {'User-Agent': 'Mozilla/5.0'}



def downloadPdf( listOfPdfName, listOfLink):
    for idx, (link, name) in enumerate(zip(listOfLink, listOfPdfName)):
        try:
            r = requests.get(link, stream = True)
            name = name + ".pdf"  # this is important , and be careful
            with open(name,"wb") as pdf:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        pdf.write(chunk)
        except Exception as error:
            print(error)





def getPdfDownloadableLink(baseUrl, pageUrl):
    req = Request(pageUrl, headers=hdr)
    response = urlopen(req)
    statusCode = response.getcode()
    print ('status code = ',statusCode)
    if statusCode == 200:
        listOfPdfDownloadableLink = []
        listOfPdf = []
        soupObject = BeautifulSoup(response, "lxml")
        allATag = soupObject.find_all("a")
        for aTag in allATag:
            link = aTag['href']
            link = str(link)
            if link.endswith('.pdf'):
                link = baseUrl + link
                '''
                we need to add this baseUrl , 
                because the url we get by scraping is not complete without it
                '''
                name = aTag.get_text()
                listOfPdfDownloadableLink.append(link)
                listOfPdf.append(name)
        #print(listOfPdf,'\n', listOfPdfDownloadableLink)
    return listOfPdf, listOfPdfDownloadableLink




if __name__ == '__main__':
    baseUrl = "https://ocw.mit.edu"
    pageUrl = "https://ocw.mit.edu/courses/mathematics/18-781-theory-of-numbers-spring-2012/lecture-notes/"
    listOfPdf, listOfPdfDownloadableLink = getPdfDownloadableLink(baseUrl, pageUrl)
    l1=[]
    l2=[]
    l1.append(listOfPdf[0])
    l2.append(listOfPdfDownloadableLink[0])

    '''
    passing only the first pair of name and link of pdf otherwise it will download all
    '''

    downloadPdf(l1, l2)