import requests
import urllib
import json
from pandas import DataFrame
import pandas as pd
from bs4 import BeautifulSoup
import re
import os

def get_img(url):
	img = []
	res = requests.get(url)
	res.encoding = res.apparent_encoding
	soup = BeautifulSoup(res.text)
	content = soup.find('div', id='main')
	jpg = content.find('img').get('src')
	name = content.find('strong').text
	if not os.path.exists('E:/Downlord/漫画/'+name):
		os.makedirs('E:/Downlord/漫画/'+name)
	img.append(jpg)
	html = content.find('a', class_='linkpage').get('href')
	new_url = url[:-18]+html
	resp = requests.get(new_url)
	resp.encoding = resp.apparent_encoding
	sp = BeautifulSoup(resp.text)
	content = sp.find('div', id='main')
	while True:
		if len(content.find_all('a', class_='linkpage')) == 1:
			break
		else:
			jpg = content.find('img').get('src')
			img.append(jpg)
			html = content.find_all('a', class_='linkpage')[1].get('href')
			new_url = url[:-18]+html
			resp = requests.get(new_url)
			resp.encoding = resp.apparent_encoding
			sp = BeautifulSoup(resp.text)
			content = sp.find('div', id='main')
			print(new_url)
	return name, img

def DownlordImg(name, img):
	k = 0
	print('正在下载%s...'%name)
	for i in img:
		#print(i[1])
		try:
			print("****** 正在下载第%d张图片 ******"%(k+1))
			urllib.request.urlretrieve(i[1], 'E:/Downlord/漫画/%s/%d.jpg'%(name, k+1))
			k += 1
		except:
			print("****** 第%d张下载失败 ******"%(k+1))
			k += 1

def main():
	'''
	url = '''你的网页链接'''
	print('正在获取图片地址...')
	name, img = get_img(url)
	img = DataFrame({"img":img})
	img.to_csv('E:/Downlord/漫画/{文件夹}/{名字}.csv')
	'''
	new_img = pd.read_csv('E:/Downlord/漫画/%s.csv'%name, engine='python').values
	DownlordImg(name, new_img)

main()
