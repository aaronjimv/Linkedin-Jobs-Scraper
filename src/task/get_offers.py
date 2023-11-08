import logging
import requests
from bs4 import BeautifulSoup
from prefect import task

LINKEDIN_URL = 'https://www.linkedin.com/jobs/search/?keywords=#&position=1&pageNum=0'

@task(name='get job offers')
def get_offers(skill):
    url = requests.get(LINKEDIN_URL.replace('#',skill))
    
    if(url.status_code == 200):
        print(f"DATA SCRAPPER...")
        html = BeautifulSoup(url.text,'html.parser')
        data_offers = html.find('ul',{'class':'jobs-search__results-list'})
        offers_list = data_offers.find_all('li')
        results = []
        for offer in offers_list:
            title = offer.find('h3',{'class':'base-search-card__title'})
            company = offer.find('span',{'class':'job-search-card__location'})
            urloffer = offer.find('a',{'class':'base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]'})
            offers_finded = {
                'job':title.get_text().strip(),
                'location':company.get_text().strip(),
                'url': urloffer['href'].strip()
            }
            results.append(offers_finded)
        return results
		
    else:
        print("error " + str(url.status_code))
