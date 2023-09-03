from bs4 import BeautifulSoup
import pandas as pd
import requests

all_links = pd.read_csv('./input.csv')

for i in all_links.index:
    #print(all_links['URL'][i])

    url = all_links['URL'][i]
    res = requests.get(url)
    html = res.content

    soup = BeautifulSoup(html, 'html.parser')
    text = soup.find_all(["p","title"], class_=None)

    output = ''
    whatwewant = ['title', 'p']

    for t in text:
        if t.name in whatwewant:
            output += '{} '.format(t.text)

    fname = './files/' + str(all_links['URL_ID'][i]) + '.txt'
    with open(fname, 'w') as f:
        f.write(output)
    print(fname, "done")

"""link = 'https://insights.blackcoffer.com/rise-of-telemedicine-and-its-impact-on-livelihood-by-2040-3-2/'
page = requests.get(link)

soup = BeautifulSoup(page.content, "html.parser")

text = soup.find_all(["p","title"], class_=None)

whatwewant = ["p", "title"]
output = ''

#print(text)
for t in text:
    if t.name in whatwewant:
        
        output += '{} '.format(t.text)

print(output)"""