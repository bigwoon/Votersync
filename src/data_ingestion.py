import pandas as pd
from sqlalchemy import create_engine

class DataIngestion:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)

    def ingest_data(self, file_path, table_name):
        data = pd.read_csv(file_path)
        if data is not None:
            self.save_to_db(data, table_name)

    def save_to_db(self, data, table_name):
        data.to_sql(table_name, self.engine, if_exists='replace', index=False)

if __name__ == "__main__":
    db_url = 'sqlite:///voter_sync_app.db'
    file_path = 'voter_data.csv'
    table_name = 'voters'

    ingestion = DataIngestion(db_url)
    ingestion.ingest_data(file_path, table_name)