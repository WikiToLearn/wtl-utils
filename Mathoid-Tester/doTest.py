import requests
import time
from bs4 import BeautifulSoup
import os 

MATHOID_URL = os.environ.get('MATHOID_URL') or "http://localhost:10044/" 


with open('wikitext.txt', 'r') as f:
    wikitext = f.read();

soup = BeautifulSoup(wikitext, 'html.parser')

formulas = soup.find_all(['dmath','math'])

print("Mathoiding " + str(len(formulas)) + " formulas");

startT = time.time()

for formula in formulas:
    startPartial = time.time()
    
    fText = formula.get_text().strip()
    
    print("Mathoiding " + fText)
    r = requests.post(MATHOID_URL, data={'q' : fText})

    endPartial = time.time() - startPartial
    
    print("\tComplete in " + str(endPartial))

endT = time.time() - startT

print("Mathoiding complete in " + str(endT))