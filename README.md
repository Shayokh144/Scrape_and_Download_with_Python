# Scrap_and_Download_with_Python
* Python3 and BeautifulSoup is used here. 
* Scrapy is also a good choice for scraping with python.

#### [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#)
#### [Install BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

### Aim
#### Part 1
* To scrap and collect data from a website
* For example [ESPNcricinfo](http://www.espncricinfo.com/) 
#### Part 2
* To scrap and download pdf from a website
* For example [MITOPENCOURSEWARE](https://ocw.mit.edu/index.htm) 

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

## Part 1
### Its time to Scrap
* Now, some sample scraping code is given here

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

* For specific information first, we must have a look through the inspect element option of the browser. Let, we want to scrap all the headlines from "Top Headlines" section. To do this first look at the below picture 

![alt text][TopHeadlinesEdited]

* our target is marked red in the picture. Here we go for the "div" that contains data.

```python

    topHeadlinesDiv = soupObject.find_all("div",{"class":"headlineStack"})
    print('number of div found = ',len(topHeadlinesDiv))

```
* holy crap !! there are more than one "div" like that. So, its not gonna work. we have to do something more.
* All those "div" s we found here not contains the text "Top Headlines", so this is really useful.

***
```python

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
                    print(li.get_text()) # print the desired result
        except:
            pass

```
***

* Done ! we get our desired result. [Complete Code Here](https://github.com/Shayokh144/Scrap_and_Download_with_Python/blob/master/TopHeadlines.py)


## Part 2
### Here we go for both scraping and downloading
* First, we visit this [page](https://ocw.mit.edu/courses/mathematics/18-781-theory-of-numbers-spring-2012/lecture-notes/)
* There are lots of lecture notes which we want to download
* As mentioned earlier, we must have a look through the inspect element option of the browser.

![alt text][DownloadPdf]

* The yellow marked area contains our desired information, but not in the exact format. Here, "href" attribute of
the "a" tag contains link like this "/courses/mathematics/18-781-theory-of-numbers-spring-2012/lecture-notes/MIT18_781S12_lec2.pdf",
which is not a downloadable link.
* If we click that link from webpage we will find the link like "https://ocw.mit.edu/courses/mathematics/18-781-theory-of-numbers-spring-2012/lecture-notes/MIT18_781S12_lec2.pdf"
* So, the missing part is this "https://ocw.mit.edu" , that we have to add with the scraped one.
* Done !! Now we can download easily from this links.  [Complete Code Here](https://github.com/Shayokh144/Scrap_and_Download_with_Python/blob/master/Scraping_and_Downloading.py)

[TopHeadlinesEdited]: https://github.com/Shayokh144/Scrap_and_Download_with_Python/blob/master/TopHeadlinesEdited.png 
[DownloadPdf]: https://github.com/Shayokh144/Scrap_and_Download_with_Python/blob/master/DownloadPdf.PNG
