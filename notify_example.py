#!/usr/bin/python

# dependencies: libnotify and python-gobject

import gi

gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("New day message")

Message = Notify.Notification.new(
    "Hello programmer",
    "Have a nice day!",
    "dialog-information")

Message.show()
