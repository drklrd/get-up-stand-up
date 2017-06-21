import os
import signal
import json

from urllib2 import Request, urlopen, URLError

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify

import threading
import time


APPINDICATOR_ID = 'myappindicator'	

def repeat():
	print("REATET")
	notify.Notification.new("<h1>Joke 2</h1>", "ha ha", None).show()


def joke(_):
	notify.Notification.new("<b>Joke</b>", "ha ha", None).show()
	threading.Timer(20.0,repeat).start()



def main():
	indicator = appindicator.Indicator.new(APPINDICATOR_ID,  gtk.STOCK_DIALOG_INFO, appindicator.IndicatorCategory.SYSTEM_SERVICES)
	indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
	indicator.set_menu(build_menu())
	notify.init(APPINDICATOR_ID)
	gtk.main()


def build_menu():
	menu = gtk.Menu()
	item_joke = gtk.MenuItem('Joke')
	item_joke.connect('activate', joke)
	menu.append(item_joke)
	item_quit = gtk.MenuItem('Quit')
	item_quit.connect('activate', quit)
	menu.append(item_quit)
	menu.show_all()
	return menu

def fetch_joke():
	request = Request('http://api.icndb.com/jokes/random?limitTo=[nerdy]')
	response = urlopen(request)
	joke = json.loads(response.read())['value']['joke']
	return joke



def quit(_):
	notify.uninit()
	gtk.main_quit()

if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	main()