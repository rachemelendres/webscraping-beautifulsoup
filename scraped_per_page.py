from bs4 import BeautifulSoup
import requests
import time
import csv

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('> ')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    with open('posts/filtered_posts.txt', mode='a') as file:  # Open file in append mode
        writer = csv.writer(file)
        for i in range(1, 4):
            html_text = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence={i}&startPage={i}').text
            soup = BeautifulSoup(html_text, 'lxml')
            jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
            if i == 1:  # Write header only for the first page
                header = ['Company Name', 'Required Skills', 'More Info']
                writer.writerow(header)

            for job in jobs:
                posted_date = job.find('span', class_="sim-posted").span.text
                if 'few' in posted_date:
                    company_name = job.find('h3', class_="joblist-comp-name").text.strip()
                    skills = job.find('span', class_="srp-skills").text.replace(" ","").replace(",", ", ").strip()
                    more_info = job.header.h2.a['href']
                    if unfamiliar_skill not in skills:
                        writer.writerow([company_name, skills, more_info])
            print(f'Page {i} Saved')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes')
        time.sleep(time_wait * 60)
