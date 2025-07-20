from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """An app that creates labels dynamically based on a list of names."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Model data: list of names
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a label for each name and add it to the layout."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicLabelsApp().run()
