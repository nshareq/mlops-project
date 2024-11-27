import os
import pandas as pd

@dataclass
class DataIngestionConfig:
    train_data_path: os.path.join("artifacts/data_ingestion", "train.csv")
    test_data_path: os.path.join("artifacts/data_ingestion", "test.csv")
    raw_data_path: os.path.join("artifacts/data_ingestion", "raw.csv")

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    def initiate_data_ingestion(self):
        try:
            data = pd.read_csv(os.path.join("data-source", "income_clean_data.csv"))

            os.makedirs(os.path.join("artifacts", "data_ingestion"), exist_ok=True)
            data.to_csv(self.config.raw_data_path, index=False)

            train_set, test_set = train_test_split(data, test_size=0.2, random_state=42)
            train_set.to_csv(self.config.train_data_path, index=False)
            test_set.to_csv(self.config.test_data_path, index=False)

        except Exception as e:
            raise CustomException("Error occurred during data ingestion", sys)
            logging.error(e)
            sys.exit(1) 

if __name__ == "__main__":
    config = DataIngestionConfig()
    data_ingestion = DataIngestion(config)
    data_ingestion.initiate_data_ingestion()