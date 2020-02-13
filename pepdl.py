 #!/bin/env python
'''
    download files from http://bp.pep.com.cn/jc/.
'''
from bs4 import BeautifulSoup
import requests
import urllib
import os
import time

def downloadFileToPath(name, file, dir):
    suffix = file[file.rfind("."):]
    finalPath = os.path.join(dir, name + suffix)
    print finalPath
    f = requests.get(file)
    with open(finalPath, "wb") as handler:
        handler.write(f.content)

def downloadFiles(url, dir):
    if not os.path.exists(dir):
        os.mkdir(dir)
    htmlx = requests.get(urlx)
    soupx = BeautifulSoup(htmlx.content,'html.parser')
    fileLinks = soupx.find_all('li', class_='fl')
    for fileLink in fileLinks:
        bookName = fileLink.h6.a.get('title').replace(" ", "")
        bookPath = os.path.join(urlx, fileLink.find_all('a', class_='btn_type_dl')[0].get('href'))
        print bookPath
        downloadFileToPath(bookName, bookPath, dir)

if __name__ == '__main__':
#     rootUrl = 'http://bp.pep.com.cn/jc/'
#     rootDir = '/home/hedj/pep/'
#     if not os.path.exists(rootDir):
#         os.mkdir(rootDir)
#     html = requests.get(rootUrl)
#     soup = BeautifulSoup(html.content,'html.parser')
#
#     links = soup.find_all('li', class_='fl')
#     for link in links:
#         dir = os.path.join(rootDir, link.a.string)
#         dir = dir.replace(" ", "")
#         urlx = os.path.join(rootUrl, link.a.get('href'))
#         downloadFiles(urlx, dir)
    downlaodFiles('http://bp.pep.com.cn/jc/ywjygjkcjc/xdjc/', 'tmp/')
