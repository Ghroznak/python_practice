import selenium
from selenium import webdriver

#input
n = input("Hvor mange linjer med svada vil du ha :>>>   ")

#init
browser = webdriver.Ie()
url = "http://svadagenerator.no/"
i = 0;
svada = "Hei!" + "\n";

browser.get(url)

while i < int(n):
	tilfeldigtekst = browser.find_element_by_id("sentence")
	rngknapp = browser.find_element_by_id("randomizebutton")
	tekst = tilfeldigtekst.get_attribute('innerHTML')
	svada = svada + tekst + "\n"
	rngknapp.click()
	i += 1

print(svada)
	
