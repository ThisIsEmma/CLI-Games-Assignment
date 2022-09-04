# cli-games/asciiart.py
import requests

text = input('ASCII Art Text > ')
font = input('ASCII Art Font > ')

#r = requests.get(f'http://artii.herokuapp.com/make?text={text}')

r = requests.get(f'http://patorjk.com/software/taag/#p=display&f={font}&t={text}%0A')
print(r.text)

