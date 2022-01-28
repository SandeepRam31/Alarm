from selenium import webdriver
import random
import argparse


def play():
	driver = webdriver.Chrome(r'./chromedriver.exe')
	with open(r'./urls.txt', 'r') as f:
		f = f.read()
		links = f.splitlines()

	URL = random.choice(links)
	driver.get(URL)


play()