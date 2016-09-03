# -*- coding: utf-8 -*-
from selenium import webdriver
import requests
import json

import sys

argvs = sys.argv
if len(argvs) != 4:
	print('Usage: python %s username password slack_webhocks_url' % argvs[0])
	quit()

driver = webdriver.PhantomJS()
driver.get('https://www.facebook.com/')

# ログイン
form = driver.find_element_by_css_selector("form#login_form")
user_login = form.find_element_by_css_selector("input[name='email']")
user_login.send_keys(argvs[1])
password = form.find_element_by_css_selector("input[name='pass']")
password.send_keys(argvs[2])
form.submit()

pinnedNav = driver.find_element_by_css_selector("#pinnedNav")
for elem in pinnedNav.find_elements_by_css_selector("li > a"):
	data = json.loads(elem.get_attribute('data-gt'))
	if int(data['count']) > 0:
		requests.post(argvs[3], data=json.dumps({
			'text': '%s %s' % (elem.get_attribute('title'), data['count']),
			'username': 'ghost',
			'icon_emoji': ':ghost:',
			'link_names': 1
		}))

driver.quit()
