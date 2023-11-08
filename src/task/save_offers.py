import csv
from pathlib import path
from prefect import task

@task(name='SAVES JOBS OFFERS')
def save_offers(list_offers):
    pass
