import os
from utils import crawl

def crawl_92():
	from _92_ import is_page_opened, request
	
	url_to_send = os.environ["URL_TO_SEND_92"]
	crawl(url_to_send, is_page_opened, request)
	return

def crawl_94():
	from _94_ import is_page_opened, request, get_cookie
	
	req = request()
	if req:
		print (req.getText())
	return
