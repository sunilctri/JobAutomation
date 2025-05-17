
import pandas as pd
import requests
from bs4 import BeautifulSoup



url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Data%2BAnalyst&location=Sydney&geoId=104769905&distance=25&f_TPR=r604800&f_E=2&start=0"

Headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36 Edg/135.0.0.0"
}

def gethtml(link):
    response = requests.get(link, headers=Headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def extract_job_details(soup):
    job_listings = []
    job_elements = soup.find_all('li')

    for job_element in job_elements:
        job_card = job_element.find('div', class_='job-search-card')
        if job_card:
            data_entity_urn = job_card.get('data-entity-urn')
            job_id = data_entity_urn.split(':')[-1] if data_entity_urn else None
            if not job_id:
                continue

            # Job Description
            Desc_url = f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{job_id}"
            desc_response = requests.get(Desc_url, headers=Headers)
            desc_soup = BeautifulSoup(desc_response.text, 'html.parser')
            description_div = desc_soup.find('div', class_='description__text description__text--rich')
            if description_div:
                description_text_elements = description_div.find_all(string=True, recursive=True)
                description = "\n".join(text.strip() for text in description_text_elements if text.strip())
            else:
                description = "No description found."

            title_element = job_card.find('h3', class_='base-search-card__title')
            company_element = job_card.find('h4', class_='base-search-card__subtitle')
            link_element = job_card.find('a', class_='base-card__full-link')

            job_name = title_element.text.strip() if title_element else None
            company_name = company_element.text.strip() if company_element else None
            job_link = link_element.get('href') if link_element else None

            job_listings.append({
                'id': job_id,
                'name': job_name,
                'company': company_name,
                'link': job_link,
                'description': description
            })

    return job_listings

# Run


