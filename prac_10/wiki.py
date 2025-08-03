"""
wiki.py
A simple Wikipedia search tool using the wikipedia module.
"""

import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

def main():
    while True:
        title = input("Enter page title: ").strip()
        if title == "":
            print("Thank you.")
            break

        try:
            # Compatible version without autosuggest
            page = wikipedia.page(title)
            print(f"\n{page.title}")
            print(f"{page.summary}\n")
            print(page.url)
        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')

main()
