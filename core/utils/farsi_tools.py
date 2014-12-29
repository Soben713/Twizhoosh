#!/usr/bin/python
# -*- coding: utf-8 -*-

def normalize(farsi_text):
	farsi_text = farsi_text.replace('ي', 'ی')
	farsi_text = farsi_text.replace('ك', 'ک')
	farsi_text = farsi_text.replace('ٔ', '')
	return farsi_text

