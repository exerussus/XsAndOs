from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 300)
Config.set('graphics', 'height', 300)
Config.write()


class XsAndOsApp(App):

    data = {

        'turn': 'x',

        '1': '',
        '2': '',
        '3': '',
        '4': '',
        '5': '',
        '6': '',
        '7': '',
        '8': '',
        '9': '',

        'win': 'None'
    }

    def build(self):
        gl = GridLayout(cols=3, rows=3)
        gl.add_widget(Button(text=' ', font_size=52, on_press=self.action_1))
        gl.add_widget(Button(text=' ', font_size=52, on_press=self.action_2))
        gl.add_widget(Button(text=' ', font_size=52, on_press=self.action_3))

        gl.add_widget(Button(text=' ', font_size=52, on_press=self.action_4))
        gl.add_widget(Button(text=' ', font_size=52, on_press=self.action_5))
        gl.add_widget(Button(text=' ', font_size=52, on_press=self.action_6))

        gl.add_widget(Button(text=' ', font_size=52, on_press=self.action_7))
        gl.add_widget(Button(text=' ', font_size=52, on_press=self.action_8))
        gl.add_widget(Button(text=' ', font_size=52, on_press=self.action_9))

        if self.data['win'] == 'x':
            bl = BoxLayout()
            lbl = Label(text='Xs won!', font_size=55)
            bl.add_widget(lbl)
            return bl
        elif self.data['win'] == 'o':
            bl = BoxLayout()
            lbl = Label(text='Os won!', font_size=55)
            bl.add_widget(lbl)
            return bl
        else:
            return gl

    def action_1(self, instance):
        if self.data['turn'] == 'x':
            instance.text = 'X'
            self.data['1'] = 'x'
            self.check_for_win()
            self.data['turn'] = 'o'
        else:
            self.data['turn'] == 'o'
            instance.text = 'O'
            self.data['1'] = 'o'
            self.check_for_win()
            self.data['turn'] = 'x'

    def action_2(self, instance):
        if self.data['turn'] == 'x':
            instance.text = 'X'
            self.data['2'] = 'x'
            self.check_for_win()
            self.data['turn'] = 'o'
        else:
            self.data['turn'] == 'o'
            instance.text = 'O'
            self.data['2'] = 'o'
            self.check_for_win()
            self.data['turn'] = 'x'

    def action_3(self, instance):
        if self.data['turn'] == 'x':
            instance.text = 'X'
            self.data['3'] = 'x'
            self.check_for_win()
            self.data['turn'] = 'o'
        else:
            self.data['turn'] == 'o'
            instance.text = 'O'
            self.data['3'] = 'o'
            self.check_for_win()
            self.data['turn'] = 'x'


    def action_4(self, instance):
        if self.data['turn'] == 'x':
            instance.text = 'X'
            self.data['4'] = 'x'
            self.check_for_win()
            self.data['turn'] = 'o'
        else:
            self.data['turn'] == 'o'
            instance.text = 'O'
            self.data['4'] = 'o'
            self.check_for_win()
            self.data['turn'] = 'x'

    def action_5(self, instance):
        if self.data['turn'] == 'x':
            instance.text = 'X'
            self.data['5'] = 'x'
            self.check_for_win()
            self.data['turn'] = 'o'
        else:
            self.data['turn'] == 'o'
            instance.text = 'O'
            self.data['5'] = 'o'
            self.check_for_win()
            self.data['turn'] = 'x'

    def action_6(self, instance):
        if self.data['turn'] == 'x':
            instance.text = 'X'
            self.data['6'] = 'x'
            self.check_for_win()
            self.data['turn'] = 'o'
        else:
            self.data['turn'] == 'o'
            instance.text = 'O'
            self.data['6'] = 'o'
            self.check_for_win()
            self.data['turn'] = 'x'

    def action_7(self, instance):
        if self.data['turn'] == 'x':
            instance.text = 'X'
            self.data['7'] = 'x'
            self.check_for_win()
            self.data['turn'] = 'o'
        else:
            self.data['turn'] == 'o'
            instance.text = 'O'
            self.data['7'] = 'o'
            self.check_for_win()
            self.data['turn'] = 'x'

    def action_8(self, instance):
        if self.data['turn'] == 'x':
            instance.text = 'X'
            self.data['8'] = 'x'
            self.check_for_win()
            self.data['turn'] = 'o'
        else:
            self.data['turn'] == 'o'
            instance.text = 'O'
            self.data['8'] = 'o'
            self.check_for_win()
            self.data['turn'] = 'x'

    def action_9(self, instance):
        if self.data['turn'] == 'x':
            instance.text = 'X'
            self.data['9'] = 'x'
            self.check_for_win()
            self.data['turn'] = 'o'
        else:
            self.data['turn'] == 'o'
            instance.text = 'O'
            self.data['9'] = 'o'
            self.check_for_win()
            self.data['turn'] = 'x'

    def check_for_win(self):
        if self.data['1'] == 'x' and self.data['2'] == 'x' and self.data['3'] == 'x':
            print('Xs won!')
            self.data['win'] = 'x'
        if self.data['1'] == 'x' and self.data['4'] == 'x' and self.data['7'] == 'x':
            print('Xs won!')
            self.data['win'] = 'x'
        if self.data['1'] == 'x' and self.data['5'] == 'x' and self.data['9'] == 'x':
            print('Xs won!')
            self.data['win'] = 'x'
        if self.data['2'] == 'x' and self.data['5'] == 'x' and self.data['8'] == 'x':
            print('Xs won!')
            self.data['win'] = 'x'
        if self.data['3'] == 'x' and self.data['6'] == 'x' and self.data['9'] == 'x':
            print('Xs won!')
            self.data['win'] = 'x'
        if self.data['4'] == 'x' and self.data['5'] == 'x' and self.data['6'] == 'x':
            print('Xs won!')
            self.data['win'] = 'x'
        if self.data['7'] == 'x' and self.data['8'] == 'x' and self.data['9'] == 'x':
            print('Xs won!')
            self.data['win'] = 'x'
        if self.data['3'] == 'x' and self.data['5'] == 'x' and self.data['7'] == 'x':
            print('Xs won!')
            self.data['win'] = 'x'

        if self.data['1'] == 'o' and self.data['2'] == 'o' and self.data['3'] == 'o':
            print('Os won!')
            self.data['win'] = 'o'
        if self.data['1'] == 'o' and self.data['4'] == 'o' and self.data['7'] == 'o':
            print('Os won!')
            self.data['win'] = 'o'
        if self.data['1'] == 'o' and self.data['5'] == 'o' and self.data['9'] == 'o':
            print('Os won!')
            self.data['win'] = 'o'
        if self.data['2'] == 'o' and self.data['5'] == 'o' and self.data['8'] == 'o':
            print('Os won!')
            self.data['win'] = 'o'
        if self.data['3'] == 'o' and self.data['6'] == 'o' and self.data['9'] == 'o':
            print('Os won!')
            self.data['win'] = 'o'
        if self.data['4'] == 'o' and self.data['5'] == 'o' and self.data['6'] == 'o':
            print('Os won!')
            self.data['win'] = 'o'
        if self.data['7'] == 'o' and self.data['8'] == 'o' and self.data['9'] == 'o':
            print('Os won!')
            self.data['win'] = 'o'
        if self.data['3'] == 'o' and self.data['5'] == 'o' and self.data['7'] == 'o':
            print('Os won!')
            self.data['win'] = 'o'

        if self.data['win'] == 'x':
            pass
        if self.data['win'] == 'o':
            pass



if __name__ == '__main__':
    XsAndOsApp().run()
