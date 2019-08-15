import os
from utils import crawl

def crawl_92():
	from _92_ import request
	
	criterias = [
		"Aucun rendez-vous n'est disponible",
		"vous reconnecter"
	]
	crawl(criterias, request)
	return

def crawl_94():
	from _94_ import request
	
	url_to_send = os.environ["URL_TO_SEND_94"]
	criterias = ["Aucun rendez-vous n\\'est disponible", 'message:"Error"']
	crawl(criterias, request)
	return

def crawl_mariage():
	from mariage import request

	message = "링크 : http://www.hauts-de-seine.gouv.fr/booking/create/4485"
	criterias = ["Il n'existe plus de plage horaire libre"]
	crawl(criterias, request, message)
	return
