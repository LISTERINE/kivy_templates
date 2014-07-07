#!/bin/python
import kivy
kivy.require('1.0.5')
from android import activity
from jnius import autoclass, cast
#from android.broadcast import BroadcastReceiver
# Kivy imports
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
from kivy.app import App

class MyApp(App):

    def build(self):
        # init
        return Controller(info='HI!')


    def on_pause(self):
        return True


class Controller(FloatLayout):
    '''Create a controller that receives a custom widget from the kv lang file.

    Add an action to be called from the kv lang file.
    '''
    label_wid = ObjectProperty()
    info = StringProperty()

    def do_action(self):
        self.label_wid.text = 'My label after button press'
        self.info = 'New info text'



if __name__ == '__main__':
    MyApp().run()
