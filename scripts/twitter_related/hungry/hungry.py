# -*- coding: utf-8 -*-
__author__ = 'mjafar'

import re
import urllib

from bs4 import BeautifulSoup

from core.twitter_related_scripts_runner import EventDispatcherSingleton
from core.scripts.twitter_related import on_demand
from core.utils.logging import log
from core.utils.regex import combine_regexes


class Hungry(on_demand.BaseOnDirectMessageOrTimelineDemandScript):
    command_pattern = combine_regexes([
        r'چ(ی|ه) بخوری?م',
        r'گ(رس|ش)نمه',
        r'چ(ی|ه) بپزم',
        r'hungry'])

    def received_command(self, command, data, reply_message, *args, **kwargs):
        match = re.search(self.command_pattern, command, re.IGNORECASE)

        if match:
            if not self.st_memory.is_person_marked('hungry', data, 3):
                # Mark them
                self.st_memory.mark_person('hungry', data)

                log("{0} is hungry".format(data['user']['screen_name']))

                url = 'http://chibepazam.com/'
                page = BeautifulSoup(urllib.request.urlopen(url).readall().decode('utf-8'))
                food_name = page.select('div.title')[0].string.replace('\r|\n','')
                recipe_url = page.select('img[src$=ok.gif]')[0].parent['href']

                response = '{0} {1}'.format(food_name, recipe_url)
                reply_message(response)
                EventDispatcherSingleton().terminate_scripts()
            else:
                self.twitter.reply_to(data, ':)')
