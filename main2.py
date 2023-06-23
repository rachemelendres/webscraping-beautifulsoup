from bs4 import BeautifulSoup
import requests
import time
import csv

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
  html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

  soup = BeautifulSoup(html_text, 'lxml')
  jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
 
  # for job in jobs:
  #   posted_date = job.find('span', class_="sim-posted").span.text
  #   if 'few' in posted_date:
  #     company_name = job.find('h3', class_="joblist-comp-name").text.strip()
  #     skills = job.find('span', class_="srp-skills").text.replace(" ","").replace(",", ", ").strip()
  #     more_info = job.header.h2.a['href']
  #     if unfamiliar_skill not in skills:
  #       with open(f'posts/filtered_posts.txt', 'a') as f:
  #         print(f"Company Name: {company_name}")
  #         f.write(f"Company Name: {company_name}")
  #         print(f"Required Skills: {skills}")
  #         f.write(f"Required Skills: {skills}")
  #         f.write(f"More Info: {more_info}\n")
  #         print(f"More Info: {more_info}\n")
  header = ['Company Name', 'Required Skills', 'More Info']
  with open('posts/filtered_posts.txt', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(header)

    for job in jobs:
        posted_date = job.find('span', class_="sim-posted").span.text
        if 'few' in posted_date:
            company_name = job.find('h3', class_="joblist-comp-name").text.strip()
            skills = job.find('span', class_="srp-skills").text.replace(" ","").replace(",", ", ").strip()
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                writer.writerow([company_name, skills, more_info])
    print('File Saved')
  
      
if __name__ == '__main__':
  while True:
    find_jobs()
    time_wait = 10
    print (f'Waiting {time_wait} minutes')
    time.sleep(time_wait*60)