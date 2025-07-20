from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

Window.size = (400, 200)


class MilesConverterApp(App):
    result = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.result = ""
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        try:
            miles = float(self.root.ids.input_miles.text)
            kilometres = miles * 1.60934
            self.result = f"{kilometres:.5f}"
        except ValueError:
            self.result = "Invalid input"

    def handle_increment(self, amount):
        try:
            value = float(self.root.ids.input_miles.text)
        except ValueError:
            value = 0.0
        value += amount
        self.root.ids.input_miles.text = str(value)
        self.handle_convert()


MilesConverterApp().run()
