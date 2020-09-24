from urllib.request import urlopen
from bs4 import BeautifulSoup
url="https://lol.gamepedia.com/Category:Champion_Square_Images"
html=urlopen(url)
soup=BeautifulSoup(htlm)
for res in soup.findAll('img'):
    print(res.get('src'))
    resource = urlopen(list_var[0]+"//"+list_var[2]+res.get('src'))
    output = open(res.get('src’).split(‘//‘)[-1],"wb")
    output.write(resource.read())
    output.close()
