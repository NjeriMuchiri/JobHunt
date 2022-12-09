from bs4 import BeautifulSoup
import requests
import time

print('Kashee list the skills you are good at: ')
familiarSkills = input('> ')
jobHunt = familiarSkills.split(", ")
print(f"Filtering Out {familiarSkills} ")

def findJob():
    __finder = requests.get('https://www.linkedin.com/jobs/')
    print(__finder)