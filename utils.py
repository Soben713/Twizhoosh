import os

def log(text):
	print(text)

def debug(text):
	DEBUG = int(os.environ.get('DEBUG', 1))
	if DEBUG:
		log(text)
