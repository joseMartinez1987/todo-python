import webbrowser

term = input("Enter a search term: ")

webbrowser.open('https://www.google.com/search?q=' + term.replace(' ', '+'))