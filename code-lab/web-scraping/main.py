from bs4 import BeautifulSoup
import requests
import time

# Get the HTML from the URL
html_text = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

print("Put some skill that you are not familiar with: ")
unfamiliar_skill = input('> ')
print(f'Filtering out {unfamiliar_skill}')


def find_jobs():
    for index, job in enumerate(jobs):
        job_pub_date = job.find('span', class_='sim-posted').text

        if 'few' in job_pub_date:
            company_name = job.find(
                'h3', class_='joblist-comp-name').text.strip()
            skills = job.find(
                'span', class_='srp-skills').text.strip().replace(' ', '')
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name}\n")
                    f.write(f"Required Skills: {skills}\n")
                    f.write(f"More Info: {more_info}\n")
                print("File Saved.")

if __name__ == "__main__":
    while True:
        find_jobs()
        print("Waiting for 200 seconds...")
        time.sleep(200)
  