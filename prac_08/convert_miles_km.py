from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILESTOKM = 1.609344


class ConverttoKmApp(App):
    output_text = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        value = self.validate_input()
        result = value * MILESTOKM
        self.root.ids.output_value.text = str(result)

    def handle_increment(self, change):
        value = self.validate_input() + change
        self.root.ids.input_value.text = str(value)
        self.handle_calculate()

    def validate_input(self):
        try:
            value = float(self.root.ids.input_value.text)
            return value
        except ValueError:
            return 0


ConverttoKmApp().run()
