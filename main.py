# Code Updated By SoloDev

import requests, time
import os
import sys
pastebin = 'https://pastebin.com/raw/jB285Hxc'

username = input('Enter Your Username > ')
os.system('cls')
password = input('Enter Your Password > ')
os.system('cls')

response = requests.get(pastebin).text

for line in response.split('\n'):
  if username and password in line:
    print('Correct password and username')
    start()
print('Invalid password or username.')
sys.exit()

# Your Code Below

def start():
  print('hello world')
  while True:
    input()
