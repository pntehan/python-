import requests
import urllib
from bs4 import BeautifulSoup
import os
from tqdm import *

def get_info(url):
	res = requests.get(url)
	res.encoding = res.apparent_encoding
	soup = BeautifulSoup(res.text)
	content = soup.find('div', class_='clearfix dirconone')
	info = []
	for i in content.find_all('a'):
		info.append({'url':i.get('href'), 'name':i.get('title')})
	return info

def get_text(url):
	res = requests.get(url)
	res.encoding = res.apparent_encoding
	soup = BeautifulSoup(res.text)
	content = soup.find('div', id='content')
	txt = content.text
	return txt


url = "http://www.quanshuwang.com/book/44/44683"
print('开始获取章节地址...')
info = get_info(url)
print('开始下载斗罗大陆...')
story = open('C:/Users/Administrator/Desktop/斗罗大陆.txt','ab+')
for i in tqdm(info):
	txt =  get_text(i['url'])
	story.write((i['name']+'\n'+txt+'\n').encode('utf-8'))
print('下载完成...')

