"""

COVID Cleanser

"""




#importing required modules from kivy

from kivy.app import App

from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from kivy.uix.widget import Widget

from kivy.graphics import Color, Ellipse, Line

from kivy.core.window import Window

from kivy.uix.button import Button

from kivy.config import Config



#Setting canvas color

Window.clearcolor=(1,0,0,0)



#Defining the instructions screen and cleaning screen

KV = '''

ScreenManagement:

    MainScreen:

    PaintScreen:



<MainScreen>:

    name:"main"



    FloatLayout:

        Button:

            text: ""

            font_size: 50

            color: 0,1,0,1

            background_normal: 'instructions.png'

            background_down: 'instructions.png'

            size_hint: self.size_hint

            pos_hint: self.pos_hint

            on_release:

                root.manager.current = 'paint'



<PaintScreen@Screen>:

    name: 'paint'



    FloatLayout:

        Painter:

'''



#Codinng the cleaning screen

class Painter(Widget):

    def on_touch_down(self, touch):



        with self.canvas:

            Color(0,128,0)



            d = 50

            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))

            touch.ud['line'] = Line(points=(touch.x - d / 2, touch.y - d / 2))



    def on_touch_move(self, touch):



        with self.canvas:

            Color(0,128,0)



            d = 50

            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))

            touch.ud['line'] = Line(points=(touch.x - d / 2, touch.y - d / 2))



class MainScreen(Screen):

    pass


class ScreenManagement(ScreenManager):

    pass



#Running the app

class COVID_cleanser(App):

    def build(self):

        return Builder.load_string(KV)



if __name__=="__main__":

    COVID_cleanser().run()
