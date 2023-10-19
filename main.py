from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


class MainApp(App):
    #Window.size=(360, 720)
    def build(self):
        layout=BoxLayout(padding=10, orientation='vertical')
        #################################################
        self.textEdit=TextInput(text='')
        button=Button(text='Click', size_hint=(0.2, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.5}, font_size=15)
        button.bind(on_press=self.click)
        self.label = Label(
            text='Fivex',
            size_hint=(0.5, 0.5),
            pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(self.label)
        layout.add_widget(self.textEdit)
        layout.add_widget(button)
        return layout
    def click(self, obj):
        self.label.text=self.textEdit.text

if __name__ == '__main__':
    app = MainApp()
    app.run()