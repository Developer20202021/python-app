from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.uix.boxlayout import BoxLayout
from  kivy.uix.button import Button

class registration(BoxLayout):
       pass
       
       

            


# btn2.bind(on_press=registration().callback)
def callback(instance):
    print('The button  is being pressed')

class bdschool(App):
    def build(self):
        t = registration()
        b = Button(text="This I want to show on test class!")
        t.add_widget(b)  
        btn1 = Button(text='Hello world 1')
        btn1.height=10
        btn1.bind(on_press=callback)
        t.add_widget(btn1)
        btn2 = Button(text='Hello world 2')
        t.add_widget(btn2)   
        return t


bdschool().run()