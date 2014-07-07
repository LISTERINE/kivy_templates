#!/usr/bin/python
import kivy
kivy.require('1.0.5')
#from android.broadcast import BroadcastReceiver
#from jnius import autoclass, cast

# get the argument passed. Just for fun.
arg = loads(os.getenv('PYTHON_SERVICE_ARGUMENT'))
print arg


# Keep the service alive
while 1:
    time.sleep(60*5)
