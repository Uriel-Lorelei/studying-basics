import requests
from bs4 import BeautifulSoup #required import from bs4

def q_and_a():
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    for q, a in zip(quotes, authors):  #zip combine the each quote with corresponding author
        data = f"{q.text} - {a.text}\n" #adds them to a variable and write these variable in a file
        with open("dest.txt", "a") as f:
            f.write(data)

base_url = "https://quotes.toscrape.com"
url = base_url 

while True:
    response = requests.get(url)  #first use the base url and then afte it finds next_li and gets the /page/2/ it makes the url to baseurl with new page and repeats the loop
    html = response.text  
    soup = BeautifulSoup(html, "html.parser")

    q_and_a()

    next_li = soup.find("li", class_="next")
    if next_li:
        next_page = next_li.find("a").get("href")
        url = base_url + next_page
    else:
        break



# for i in range(1,6):
#     params = {"page": f"{i}"}
#     response = requests.get(base_url, params=params)
#     html = response.text

#     soup = BeautifulSoup(html, "html.parser")

#     quotes = soup.find_all("span", class_="text")
#     authors = soup.find_all("small", class_="author")

#     for q, a in zip(quotes, authors):
#         print(q.text, "-", a.text)