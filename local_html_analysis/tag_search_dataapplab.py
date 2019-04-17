from bs4 import BeautifulSoup
#import urllib3

#url = "https://www.pythonforbeginners.com"


content = open("dataapplab_BA.html", encoding="utf8")
content.close;

soup = BeautifulSoup(content, 'html.parser')

links = soup.findAll("a", {"class": "media_thumb_link"})
titles = soup.findAll("span", {"class": "editable"})

results = []
link_titles = []

file_results = open('results.txt', 'w', encoding="utf8")
title_results = open('titles.txt', 'w', encoding="utf8")

for link in links:
    convert_link = 'https://dataapplab.wistia.com/embed/iframe'+link.get('href')[36:]
    results.append(convert_link)
    file_results.write(convert_link+'\n')

for title in titles:
    title_text = title.get_text()
    link_titles.append(title_text)
    title_results.write(title_text + '\n')

print(results)
print(link_titles)
file_results.close;



