from prefect import flow
import logging
from task.get_offers import(
    get_offers
)
from task.save_offers import(
    save_offers
)

log = logging.getLogger()

SKILL = 'python'

@flow(name='LINKEDIN SCRAPPER')
def main_flow():
    log.info(f"SCRAPPER PROCESS")
    offers = get_offers(SKILL)
    save_offers(offers)

if __name__ == '__main__':
    main_flow()
