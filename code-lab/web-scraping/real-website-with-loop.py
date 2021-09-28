from bs4 import BeautifulSoup
import requests

# Get the HTML from the URL
html_text = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    job_pub_date = job.find('span', class_='sim-posted').text

    if 'few' in job_pub_date:
        company_name = job.find(
            'h3', class_='joblist-comp-name').text.strip()
        skills = job.find(
            'span', class_='srp-skills').text.strip().replace(' ', '')

        print(f'''
            Company Name: {company_name}
            Required Skills: {skills}
        ''')
