import os
import signal
import json

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify
from gi.repository import GObject

APPINDICATOR_ID = 'getup_standup'	

# timer in minutes
MINUTES = 15

# getup timer in milliseconds
TIMER = MINUTES  * 1000

def repeat_getup():
	print("Get Up !")
	icon = os.getcwd() + "/resources/stop.png"
	notify.Notification.new("HEY ! Its time to stretch a bit !", "Stop Coding , get up and stretch yourself a bit !", icon).show()
	return True

def get_up(_):
	icon = os.getcwd() + "/resources/timer.gif"
	notify.Notification.new("Get up will now make you stretch-up every {} minutes".format(MINUTES), "", icon).show()
	GObject.timeout_add(TIMER,repeat_getup)

def main():
	indicator = appindicator.Indicator.new(APPINDICATOR_ID,  os.path.abspath('./resources/clock.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
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