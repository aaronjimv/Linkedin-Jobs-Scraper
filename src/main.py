from prefect import flow
import logging

log = logging.getLogger()

@flow(name='LINKEDIN SCRAPPER')
def main_flow():
    log.info(f"SCRAPPER PROCESS")

if __name__ == '__main__':
    main_flow()
