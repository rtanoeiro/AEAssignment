from utils.sql.event_ingestion import ingest_data
from utils.sql.reports import create_reports
from utils.aws.aws_functions import get_daily_data, upload_reports
import datetime
from config.config import data_folder, reports_folder, folder_alias

if __name__ == "__main__":
    TODAY = datetime.datetime.now().strftime("%Y-%m-%d")
    get_daily_data(
        download_from=f"{data_folder}/platform_transactions.csv",
        download_to=f"{data_folder}/platform_transactions.csv",
    )
    ingest_data()
    create_reports()
    upload_reports(
        upload_from=f"{data_folder}/finance_report.csv",
        upload_to=f"{reports_folder}/{folder_alias}/finance_report_{TODAY}.csv",
    )
    upload_reports(
        upload_from=f"{data_folder}/marketing_report.csv",
        upload_to=f"{reports_folder}{folder_alias}/marketing_report_{TODAY}.csv",
    )
