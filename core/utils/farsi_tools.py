#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

import settings


def normalize(farsi_text):
    farsi_text = farsi_text.replace('ي', 'ی')
    farsi_text = farsi_text.replace('ك', 'ک')
    farsi_text = farsi_text.replace('ٔ', '')
    return farsi_text


def add_dummy_spaces(text, num):
    """
    :return: Adds dummy spaces and zero width delimiters to prevent duplicate message error by twitter
    """
    while len(text) < settings.TWEET_LENGTH and num > 0:
        text += random.choice([' ', '‌'])
        num -= 1
    return text