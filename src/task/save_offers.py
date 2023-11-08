import csv
from pathlib import Path
from prefect import task
from decouple import config

DATA_PATH = Path(config('PYTHON_PATH') + '/data/offers.csv')

@task(name='SAVES JOBS OFFERS IN CSV')
def save_offers(list_offers):
    with open(DATA_PATH,'w') as data:
        writer = csv.DictWriter(
            data,
            fieldnames=[
                'job',
                'location',
                'url'
            ]
        )
        writer.writerows(list_offers)
