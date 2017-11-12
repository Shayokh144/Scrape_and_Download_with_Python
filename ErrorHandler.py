"""
Created on Tue Sep 12 23:40:45 2017

@author: Asif
"""

import urllib
from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup


def get_status_code(url):
    
    hdr = {'User-Agent': 'Mozilla/5.0'}
    try: 
        req = Request(url,headers=hdr)
        response =  urlopen(req)
        
        responseCode = response.getcode()
        response.close()
    
        #print(response.getcode())
        return responseCode
    except urllib.error.HTTPError as err:
        
        if err.code == 404:
            #print ("Page not found!")
            return  err.code
        elif err.code == 403:
            #print ("Access denied!")
            return  err.code
        else:
            #print ("Something happened! Error code", err.code)
            return  0
    except urllib.error.URLError as err:
            #print ("Some other error happened:", err.reason)
            return  0




    
    






'''
if __name__ == "__main__":
    status_code = get_status_code('https://intellipaat.com/tutorial/data-science-tutorial/')
    #print(status_code)
'''