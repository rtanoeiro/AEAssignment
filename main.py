from utils.sql.event_ingestion import ingest_data
from utils.sql.reports import create_reports
from utils.aws.aws_functions import get_daily_data, upload_reports
import datetime
from config.dev import data_folder, reports_folder

if __name__ == "__main__":
    TODAY = datetime.datetime.now().strftime("%Y-%m-%d")
    get_daily_data(
        download_from=f"{data_folder}/{TODAY}/platform_transactions.csv",
        download_to=f"{data_folder}/platform_transactions.csv",
    )
    ingest_data()
    create_reports()
    upload_reports(
        upload_from=f"{data_folder}/finance_report.csv",
        upload_to=f"{reports_folder}/finance_report.csv",
    )
    upload_reports(
        upload_from=f"{data_folder}/marketing_report.csv",
        upload_to=f"{reports_folder}/marketing_report.csv",
    )
