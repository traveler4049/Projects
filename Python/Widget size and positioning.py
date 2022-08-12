from kivy.app import App
from kivy.uix.button import Button


class LangaugeLearnerApp(App):
    def build(self):
        return Button(
            text='Hello World',
            pos=(50,50),
            size=(500,500),
            size_hint=(None,None))

if __name__ == '__main__':
    LangaugeLearnerApp().run()