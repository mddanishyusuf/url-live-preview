#author = Mohd Danish Yusuf(@mddanishyusuf)
#Internet Architecture Internship @ Anant Corporation

from flask import Flask, jsonify, abort, flash, redirect, render_template, request, url_for
from bs4 import BeautifulSoup
import requests
import json
from PIL import Image
from io import BytesIO
#import urlparse

app = Flask(__name__)
@app.route("/api", methods=['GET'])
def scrapper():
	url = request.args.get('url')
	if url == '':
		return jsonify({'Name':'Live Preview of any url','Author':'mddanishyusuf','Position':'Internet Architecture Internship @ Anant Corporation','Usage':'pass any url as get param'})
	response = requests.get(url)
	if response.status_code == 200:
		scraped = BeautifulSoup(response.content, 'html.parser')
		result = {}
		result['title'] = scraped.title.string
		#hostname = urlparse(url).hostname
		#result['hostname'] = hostname
		#@result['favicon'] = scraped.find("link", rel="icon")['href']
		#if bool(urlparse(fav_link).netloc):
		#	result['favicon'] = fav_link
		#else:
		#	result['favicon'] = hostname + fav_link
		scrap_list = [['description','description','name'],['keywords','keywords','name'],['author','author','name'],['og:site_name','site_name','property'],['og:url','url','property'],['og:image','image','property'],['og:description','description','property'],['og:type','type','property'],['og:video:url','video_url','property'],['og:video:secure_url','embed_video_url','property'],['og:video:width','width','property'],['og:video:height','height','property'],['og:video:tag','tags','property']]
		for a in scrap_list:
			res = scraped.find("meta",attrs={a[2]:a[0]})
			if res == None:
				result[a[1]] = ''
			elif a[0] == 'og:image' and res != '':
				data = requests.get(res['content']).content
				im = Image.open(BytesIO(data))
				result['img_width'] = im.size[0]
				result['img_height'] = im.size[0]
				if result['img_width'] >= 600:
					result['img_loc'] = 1
				else:
					result['img_loc'] = 0
					result[a[1]] = res['content']
			else:
				result[a[1]] = res['content']
		return jsonify(result)
	else:
		return 'Error to scrap'

if __name__ == "__main__":
	app.run()