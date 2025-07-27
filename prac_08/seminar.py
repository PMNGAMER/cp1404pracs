"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class CustomLayoutApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='horizontal')

        # Left Column (full height)
        left_column = BoxLayout(orientation='vertical')
        left_column.add_widget(Button(text='Left Side'))

        # Right Column
        right_column = BoxLayout(orientation='vertical')

        # Top Row (3 columns)
        top_row = BoxLayout(orientation='horizontal')
        top_row.add_widget(Button(text='A'))
        top_row.add_widget(Button(text='B'))
        top_row.add_widget(Button(text='C'))

        # Bottom Rows (2 vertical rows)
        bottom_rows = BoxLayout(orientation='vertical')
        bottom_rows.add_widget(Button(text='D'))
        bottom_rows.add_widget(Button(text='E'))

        # Assemble right column
        right_column.add_widget(top_row)
        right_column.add_widget(bottom_rows)

        # Add both to main layout
        main_layout.add_widget(left_column)
        main_layout.add_widget(right_column)

        return main_layout


CustomLayoutApp().run()
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class RootWidget(BoxLayout):
    pass


class BibleApp(App):
    def build(self):
        return RootWidget()


BibleApp().run()
