# covid-brazil-globo-webscrap
A webscraper for listing cities and nr of cases per city in Brazil
Source: https://especiais.g1.globo.com/bemestar/coronavirus/mapa-coronavirus/?_ga=2.48817062.1083509909.1584787216-1227695381.1584787197#/

You need to download the link as html-page and specify the folder where you are saving (line 8)
Currently the script has 3 variables:

1. 'cities' - brings a list of cities with confirmed cases in Brazil from highest to lowest, followed by the state code from which it belongs to. Example: "Curitiba, PR"

2. 'cases' - brings a of nr of cases. From highest to lowest. Following the same index from the variable 'cities'.

3. 'cityandcases' - a list of strings with the city, followed by the nr of cases. 

There is still improvements to be made such as:
1. Get the time from last update
2. Get the nr of deaths per city and state
3. Spit out the info in json and csv format

