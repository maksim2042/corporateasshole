#!/usr/bin/python

import sys
import requests
import re

def getAddress(symbol):
	"""
	requires NASDAQ symbol
	returns HQ information
	"""
	r = requests.get('http://finance.yahoo.com/q/pr?s='+symbol)
	#address = re.compile(r'<b>(.*?)<\/b><br>.*?<br>.*?<br>(.+?),\s+(\w{2})\s(\d{5})<br>United States - ')
	address = re.compile(r'modtitlew1"><b>(.*?)</b><br>(.*?)<br>(.*?)<br>(.+?),\s+(\w{2})\s(\d{5})<br>United States - ')
	res = address.findall(r.text)
	return res[0]

#print getAddress('TWTR')