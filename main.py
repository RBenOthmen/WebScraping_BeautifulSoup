import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title = []
company_name = []
location_name = []
job_skill = []

result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")
src = result.content

soup = BeautifulSoup(src, "lxml")

job_titles = soup.find_all("h2", {"class": "css-m604qf"})
companies_names = soup.find_all("a", {"class": "css-17s97q8"})
locations_names = soup.find_all("span", {"class": "css-5wys0k"})
# job_skills = soup.find_all("a", {"class": "css-5x9pm1"})

for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    company_name.append(companies_names[i].text)
    location_name.append(locations_names[i].text)

# print(job_title)
# print(company_name)
# print(location_name)
# print(job_skill)

file_list = [job_title, company_name, location_name]
exported = zip_longest(*file_list)
with open("G:/my_projects/WebScraping_BeautifulSoup/wuzzuf.csv", "w") as wuzzuf:
    wr = csv.writer(wuzzuf)
    wr.writerow(["job title", "company name", "location name"])
    wr.writerows(exported)
