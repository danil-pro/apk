from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class MyApp(App):
    def build(self):
        f1 = FloatLayout()
        f1.add_widget((Button(text = "Набери максимальное число", on_press = self.btn_press, background_color = [1, 0, 0, 1])))

        return f1

    global count
    count = 0
    def btn_press(self, instance):
        global count

        count = count + 1
        instance.text = str(count)


if __name__ == "__main__":
    MyApp().run()
