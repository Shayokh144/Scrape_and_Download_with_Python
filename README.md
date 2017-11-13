# Scrap_and_Download_with_Python
* Python3 and BeautifulSoup is used here. 
* Scrapy is also a good choice for scraping with python.

#### [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#)
#### [Install BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

### Aim
* To scrap and collect data from a website
* For example [ESPNcricinfo](http://www.espncricinfo.com/) 

### Note 
* Before scraping any website please check if there is any API to provide data. If API exists there's no need to scrap.

### Before Starting
* Here, we scrap the page "http://www.espncricinfo.com/"
* Before scraping we have to check the [status code](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) of the link. To check,

***
```python
from urllib.request import urlopen, Request

hdr = {'User-Agent': 'Mozilla/5.0'}
url = "http://www.espncricinfo.com/"
req = Request(url, headers=hdr)
response = urlopen(req)
statusCode = response.getcode()
print ('status code = ',statusCode)
```
***

* if the status code is 200, it means our request is successful.

### Its time to Scrap
* Now, we scrap all the headlines of the page

***
```python
from bs4 import BeautifulSoup
if statusCode == 200:
    soupObject = BeautifulSoup(response, "lxml")
    allHeadlines = soupObject.find_all("h1") # find all the h1 tag
    for headLines in allHeadlines:
        try:
            print(headLines.get_text()) # find the text inside the h1 tag
        except:
            pass

    allLinks = soupObject.find_all("a") # find all "a" tag
    for link in allLinks:
        try:
            print(link['href'])    # print "href" attribute from "a" tag
        except:
            print("no link found")

```
***

* For specific information first, we must have a look through the inspect element option of the browser. Let, we want to scrap all the headlines from "TOP HEADLINES" section. To do this first look at the below picture 

![alt text][logo]

* our target is marked red in the picture. Here we go for the "div" that contains data.

```python

    topHeadlinesDiv = soupObject.find_all("div",{"class":"headlineStack"})
    print('number of div found = ',len(topHeadlinesDiv))

```
* holy crap !! there are more than one "div" like that. So, its not gonna work. we have to do something more.





[logo]: https://github.com/Shayokh144/Scrap_and_Download_with_Python/blob/master/TopHeadlinesEdited.png 

