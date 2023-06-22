import requests
from bs4 import BeautifulSoup

base_url = "https://www.boxofficemojo.com/"

# this is the url where the list starts
url = "https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW"

while True:
    # get request the html page, parse the page using BeautifulSoup
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # find the table element that holds the data we want
    results = soup.find(id='table')

    # find all table rows within the table element
    rows = results.find_all("tr")

    # example row from src
    # <tr>
    #   <td class="a-text-right mojo-header-column mojo-truncate mojo-field-type-rank">1</td>
    #   <td class="a-text-left mojo-field-type-title"><a class="a-link-normal" href="/title/tt0499549/?ref_=bo_cso_table_1">Avatar</a></td>
    #   <td class="a-text-right mojo-field-type-money">$2,923,706,026</td><td class="a-text-left mojo-field-type-year"><a class="a-link-normal" href="/year/world/2009/?ref_=bo_cso_table_1">2009</a></td>
    # </tr>

    # loop through all table rows to parse out the rank, title and revenue based on element and class
    # slices first row headers
    for row in rows[1:]:
        rank = row.find("td", class_="mojo-field-type-rank").text
        title = row.find("td", class_="mojo-field-type-title").text
        revenue = row.find("td", class_="mojo-field-type-money").text
        print(rank, title, revenue)
    try:
        url = base_url + soup.find("li", class_='a-last').find("a")['href']
    except TypeError:
        break
