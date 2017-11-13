
from urllib.request import urlopen, Request

hdr = {'User-Agent': 'Mozilla/5.0'}
url = "http://www.espncricinfo.com/"
req = Request(url, headers=hdr)
response = urlopen(req)
statusCode = response.getcode()
print ('status code = ',statusCode)

from bs4 import BeautifulSoup
if statusCode == 200:
    soupObject = BeautifulSoup(response, "lxml")
    topHeadlinesDiv = soupObject.find_all("div",{"class":"headlineStack"})
    print('number of div found = ',len(topHeadlinesDiv))

    for div in topHeadlinesDiv:
        try:
            headTxt = div.find("h1",{"class":"module__header"}).get_text()
            headTxt = headTxt.strip().lower() # remove unnecesary space and convert text to lower case to match easily
            if headTxt == "top headlines":
                topHeadlinesUl = div.find("ul",{"class":"headlineStack__list"}) # find the specific "ul" tag that contains data
                topHeadlinesLi = topHeadlinesUl.find_all("li") # find all the "li" tag inside the "ul" tag
                for li in topHeadlinesLi:
                    print(li.get_text()) # print the sedired result
        except:
            pass

''' output:

status code =  200
number of div found =  16
De Villiers blitzes 19-ball 50 in Lions rout
Nepal upset India in Under-19 Asia Cup
Mott critical of England women's slow approach
'Hat-tricks not my best form' - Starc
Lehmanns can make it work - Alec Stewart
Karachi in line to host next PSL final
ICC begins recruitment for female director
England coach Bayliss wants 160s, not 60s

'''