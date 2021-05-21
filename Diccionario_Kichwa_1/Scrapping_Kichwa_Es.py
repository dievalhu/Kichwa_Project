from ast import Str
import re
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
completo = []
lista = []
lista2 = []
for cont in range(1,123):
    req = Request('https://www.kichwa.net/glossword/index.php/list/1/'+str(cont)+'.xhtml', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    print(webpage)
    soup = BeautifulSoup(webpage, "html.parser" )

    for links in soup.find_all("dt"):
        lista.append(links.get_text())

    for sig in soup.find_all("dd"):
        lista2.append(sig.get_text())


l1= []
l2= []
l3 = []
for n in lista2:
    l2.append(re.sub('[,]', '-', n))

for n in l2:
    l3.append(re.sub('[()]', '', n))

for n in lista:
    l1.append(re.sub('[,]', '-', n))

print(l1)
print(len(l1))
print(l2)
print(len(l2))

lista3= []
for i in range(len(lista)):
    pos = i+1
    concatenado =str(pos)+"," + l1[i] + ","+ l3[i]
    lista3.append(concatenado)

print(lista3)

np.savetxt("output.csv",
          lista3,
           fmt='%s',
           delimiter=",")
