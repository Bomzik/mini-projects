from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


class MyApp(App):
    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if self.formula == '0':
            self.formula = ''

        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        self.formula += str(instance.text)
        self.update_label()

    def clr_number(self, instance):
        self.formula = [i for i in self.formula]
        del self.formula[-1]
        self.formula = ''.join(self.formula)
        self.update_label()

    def clr_all(self, instance):
        self.formula = ''
        self.update_label()

    def calc_res(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        if '(' and ')' in self.lbl.text:
            self.lbl.text = self.lbl.text[1:-1]
        self.formula = self.lbl.text


    def build(self):
        self.formula = '0'
        bl = BoxLayout(orientation='vertical', padding=10)
        gl = GridLayout(cols=3, spacing=10, size_hint=(1, .75))

        self.lbl = Label(text='0', size_hint=(1, .25), font_size=35)
        bl.add_widget(self.lbl)

        gl.add_widget(Button(text='<', on_press=self.clr_number))
        gl.add_widget(Button(text='C', on_press=self.clr_all))
        gl.add_widget(Button(text='=', on_press=self.calc_res))

        gl.add_widget(Button(text='7', on_press=self.add_number))
        gl.add_widget(Button(text='8', on_press=self.add_number))
        gl.add_widget(Button(text='9', on_press=self.add_number))

        gl.add_widget(Button(text='4', on_press=self.add_number))
        gl.add_widget(Button(text='5', on_press=self.add_number))
        gl.add_widget(Button(text='6', on_press=self.add_number))

        gl.add_widget(Button(text='1', on_press=self.add_number))
        gl.add_widget(Button(text='2', on_press=self.add_number))
        gl.add_widget(Button(text='3', on_press=self.add_number))

        gl.add_widget(Button(text='+', on_press=self.add_operation))
        gl.add_widget(Button(text='-', on_press=self.add_operation))
        gl.add_widget(Button(text='*', on_press=self.add_operation))

        gl.add_widget(Button(text=',', on_press=self.add_number))
        gl.add_widget(Button(text='0', on_press=self.add_number))
        gl.add_widget(Button(text='/', on_press=self.add_operation))


        bl.add_widget(gl)

        return bl

if __name__ == '__main__':
    MyApp().run()
