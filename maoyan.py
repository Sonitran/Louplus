#Some User Agents
#hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
#{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
#{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]

import requests
import re
import time
import random
def getHtmltext(url):
    kv={'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'}
    try:
        r=requests.get(url,headers=kv,timeout=30)
        r.raise_for_status
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return""
def parsehtml(html):
    pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?title="(.*?)".*????(.*?)</p>.*?releasetime">?????(.*?)</p>',re.S)
    addmissions=re.findall(pattern,html)
    return addmissions
def printout(html):
    admissions=parsehtml(html)
    for each in admissions:
        print(tplt.format(each[0],each[1],each[2].strip(),each[3],chr(12288)))
    
    
url="https://maoyan.com/board/4"
#print(getHtmltext(url))
tplt='{0:<4}\t{1:<20}\t{2:{4}<30}{3:<20}'
print(tplt.format("??","????","??","????",chr(12288)))
htmltext=getHtmltext(url)
printout(htmltext)
num=0
time.sleep(random.random()*3)
while True:
    num=num+10
    realurl=url+'?offset='+str(num)
    htmltext=getHtmltext(realurl)
    printout(htmltext)
    time.sleep(random.random()*3)
    if (num==100):
        break
