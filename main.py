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


def cmd():

	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('--time', help='Time stamps separated by "," in the format HH:MM', type = str)

	args = parser.parse_args()
	time_stamps = [i.strip() for i in args.time.split(",")]
	print(time_stamps)


if __name__ == '__main__':
	cmd()