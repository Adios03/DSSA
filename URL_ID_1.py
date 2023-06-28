import requests 
from bs4 import BeautifulSoup 
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'} 
url = "https://insights.blackcoffer.com/is-telehealth-the-future-of-healthcare-3/" 

r = requests.get(url,headers=headers) 
htmlContent = r.content 
# print(htmlContent) 

soup = BeautifulSoup(htmlContent, 'html.parser') 
# print(soup.prettify()) 

html = soup.html.text
# print(html) 


file = open("URL_ID_1.txt", "w") 

h1 = soup.h1.text
soup_h1 = str(h1) 
print(soup_h1) 
file.write(soup_h1) 

paras = soup.find_all('p')
# print(paras) 
soup_paras = str(paras) 
for i in paras:
    print(i.text) 
file.write(soup_paras)  


file.flush() 
file.close() 