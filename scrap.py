# importing dependencies
import requests
import random
from bs4 import BeautifulSoup
from csv import writer


# scraping function
def scapp():
    #run the articles in sequence
    for i in range(50000, 58679):
        num = i
    # url that its pulling
        response = requests.get('https://avas.mv/' + str(num))
    # parsing the html
        soup = BeautifulSoup(response.text, 'html.parser')
    # pulling the main class
        posts = soup.find_all(class_='rtl container mx-auto mb-7 mt-8 px-4 md:px-0')
    # looping it to get individual elements
        for post in posts:
        # grabbing the header
          title = post.find('h1').get_text().replace('\n', '')
        # grabbing the link
          link = response.url
        # grabbing the date
          date = post.find(class_='ltr text-sm text-grey-dark pl-2').get_text().replace('\n', '')
        # output
          print(title, link, date)

        # Writing to a fileS
        file = open('testfile.txt', 'a+', encoding="utf-8")
        file.write(title + "\n")
        file.write("")
        file.write(link + "\n")
        file.close()


# looping function
def text():
    x = 1
    while x == 1:
        scapp()


text()
