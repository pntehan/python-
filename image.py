import requests
import urllib
import json
from bs4 import BeautifulSoup
import re
import os

def get_html(url):
	res = requests.get(url)
	res.encoding = res.apparent_encoding
	soup = BeautifulSoup(res.text)
	html = soup.find_all('a', class_='MMPic')
	info = []
	for i in html:
		info.append({'url':i.get('href'), 'name':i.get('title')})
	return info

def get_img(url):
	img = []
	resp = requests.get(url)
	resp.encoding = resp.apparent_encoding
	sp = BeautifulSoup(resp.text)
	new = sp.find('img')
	img.append(new.get('src'))
	while True:
		if sp.find('a', class_='rightFix') == None:
			break
		else:
			path = url[:-11] + sp.find('a', class_='rightFix').get('href')
			resp = requests.get(path)
			sp = BeautifulSoup(resp.text)
			new = sp.find('img')
			img.append(new.get('src'))
	return img

def Downlord_img(info):
	for i in info:
		url = i['url']
		name = i['name']
		if not os.path.exists("E:/Downlord/美女图片/"+name):
			os.makedirs("E:/Downlord/美女图片/"+name)
		img = get_img(url)
		print('开始下载%s的图片...'%name)
		k = 0
		for j in img:
			try:
				print("****** 正在下载第%d张图片 ******"%(k+1))
				urllib.request.urlretrieve(j, 'E:/Downlord/美女图片/%s/%s%d.jpg'%(name, name, k+1))
				k += 1
			except:
				print("****** 第%d张下载失败 ******"%(k+1))

def main():
	url = "https://www.27270.com/ent/meinvtupian/"
	info = get_html(url)
	Downlord_img(info)

main()

'''
url = "https://www.27270.com/ent/meinvtupian/"
res = requests.get(url)
soup = BeautifulSoup(res.text)
html = soup.find_all('a', class_='MMPic')
dirs = []
for i in html:
	dirs.append(i.get('href'))

for i in dirs:
	img = []
	print(i)
	resp = requests.get(i)
	sp = BeautifulSoup(resp.text)
	new = sp.find('img')
	img.append(new.get('src'))
	while True:
		if sp.find('a', class_='rightFix') == None:
			break
		else:
			path = i[:-11] + sp.find('a', class_='rightFix').get('href')
			resp = requests.get(path)
			sp = BeautifulSoup(resp.text)
			new = sp.find('img')
			img.append(new.get('src'))
	print(img)
'''
