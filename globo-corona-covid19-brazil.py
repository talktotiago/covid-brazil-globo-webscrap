import json
import re
from bs4 import BeautifulSoup

from os import listdir
from os.path import isfile, join

input_path = "/home/jack/Documents/gotrends/corona/input/"
output_file = "/home/jack/Documents/gotrends/corona/output/report_brazil.json"

onlyfiles = [f for f in listdir(input_path) if isfile(join(input_path, f))]
data = {}
data['report_brazil'] = []
data = {}
data['report_brazil'] = []

for f in onlyfiles: #Usar "[:2]" para processar apenas os dois primeiros arquivos - ex.: for f in onlyfiles[:2] - caso contrario remover o '[:2]' para processar tudo
    full_path = join(input_path, f)
    soup = BeautifulSoup(open(full_path), "html.parser")
    print (f)

 #1. GET CITIES INFECTED
cities = soup.find_all ('div', attrs={'class':'places__cell'})
for i in range (2, len(cities), 2):
        print (cities[i].get_text())
#2. GET NR OF CASES PER CITY
cases = soup.find_all ('div', attrs={'class':'places__cell'})
for i in range (3, len(cases), 2):
        print (cases[i].get_text())

#3. GET CITIES AND NR OF CASES
cityandcases = soup.find_all ('div', attrs={'class':'places__cell'})
for i in range (2, len(cityandcases), 3):
        print (cityandcases[i].get_text())

