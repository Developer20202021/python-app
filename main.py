
from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.uix.boxlayout import BoxLayout


class Wbox(BoxLayout):
    def on_button_click(self):
        print('done')


class MainWidget(Widget):
    pass

class Thelabapp(App):
    pass

Thelabapp().run()