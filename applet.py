import os
import signal
import json

from urllib2 import Request, urlopen, URLError

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify
from gi.repository import GObject

import threading
import time


APPINDICATOR_ID = 'getup_standup'	

# getup timer in milliseconds
TIMER = 15 * 1000


def repeat_getup():
	print("REAPEAT !")
	notify.Notification.new("HEY ! Its time to stretch a bit !", "Get up and stretch yourself up !", None).show()
	return True

def get_up(_):
	notify.Notification.new("Get up will now make you stretch-up every {} minutes".format(TIMER), "", None).show()
	GObject.timeout_add(TIMER,repeat_getup)



def main():
	indicator = appindicator.Indicator.new(APPINDICATOR_ID,  gtk.STOCK_DIALOG_INFO, appindicator.IndicatorCategory.SYSTEM_SERVICES)
	indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
	indicator.set_menu(build_menu())
	notify.init(APPINDICATOR_ID)
	gtk.main()


def build_menu():
	
	menu = gtk.Menu()
	
	getup_item = gtk.MenuItem('Start Get-Up')
	getup_item.connect('activate', get_up)
	menu.append(getup_item)

	quit_item = gtk.MenuItem('Quit')
	quit_item.connect('activate', quit)
	menu.append(quit_item)
	menu.show_all()

	return menu


def quit(_):
	notify.uninit()
	gtk.main_quit()

if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	main()