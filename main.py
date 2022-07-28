# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import re

import requests
from bs4 import BeautifulSoup


URL = "https://glints.com/id/lowongan-kerja"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


def main_function():
    # badges = soup.body.find('div', attrs={'class': 'badges'})
    results = soup.find_all("div", attrs={'aria-label': 'Job Card'})
    for element in results:
        company = element.find("a", attrs={'aria-label': re.compile('Job card company*')})
        title = element.find("h3", attrs={'aria-label': re.compile('Job card title*')})
        child_el = element.find_all("div", attrs={'class': re.compile('CompactOpportunityCardsc__OpportunityInfo-sc*')})
        location, salary = child_el[0], child_el[1]
        print(f"company {company.text} - open job: {title.text}, loc: {location.text}, salary: {salary.text}")
        print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_function()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
