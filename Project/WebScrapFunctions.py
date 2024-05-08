import requests
from bs4 import BeautifulSoup


# Extract the title for each product
def websitecontent(page_num):
    result = requests.get(f"https://getpalma.com/collections/all-bags?page={page_num}")

    # Create soup object to parse content
    soup = BeautifulSoup(result.text, "html.parser")
    return soup


#################################################
# Extract the title for each product
def product_links(soup):
    global prod_link
    prod_link = []
    # result = requests.get(soup)
    # soup = BeautifulSoup(result.text, "html.parser")
    product_link = soup.find_all("div", class_= "cc-quick-buy-btn-container")

    for i in range(len(product_link)):
        prod_link.append('https://getpalma.com/'+product_link[i].find("a").attrs['href'])
        print(prod_link)

    return prod_link


def product_titles(soup):
    global prod_titles
    prod_titles = []
    # soup = websiteContent(page_num)
    product_title = soup.find_all("span", class_= "title")

    for i in range(len(product_title)):
        prod_titles.append(product_title[i].text)

    return prod_titles

#################################################

# Extract the price for each product

def product_price(soup):
    global prod_money
    prod_money = []
    product_money = soup.find_all("span", class_= "money")

    for i in range(len(product_money)):
        prod_money.append(product_money[i].text)

    return prod_money

#################################################
# Extrct the description for each product
def product_description(page_links):
    global descrip
    descrip =[]
    #page_links = product_links(soup)
    result = requests.get()
    # Create soup object to parse content
    soup = BeautifulSoup(result.text, "html.parser")
    # To get the data from inside each product
    for link in page_links:
        result = requests.get(link)
        soup = BeautifulSoup(result.text, "html.parser")
        description = soup.find("div", class_="cc-tabs__tab")
        descrip.append(description.text)
        print(descrip)
    return descrip
