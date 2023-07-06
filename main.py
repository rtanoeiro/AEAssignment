from utils.sql.event_ingestion import ingest_data
from utils.sql.reports import create_reports
from utils.aws.aws_functions import get_daily_data, upload_reports
from config.config import data_folder, reports_folder, folder_alias
from os import getcwd

import datetime

if __name__ == "__main__":
    TODAY = datetime.datetime.now().strftime("%Y-%m-%d")
    working_dir = getcwd()

    get_daily_data(
        download_from=f"{data_folder}/platform_transactions.csv",
        download_to=f"{working_dir}/platform_transactions.csv",
    )

    ingest_data()
    create_reports()

    upload_reports(
        upload_from=f"{data_folder}/finance_report.csv",
        upload_to=f"{reports_folder}/{folder_alias}/finance_report_{TODAY}.csv",
    )
    upload_reports(
        upload_from=f"{data_folder}/marketing_report.csv",
        upload_to=f"{reports_folder}/{folder_alias}/marketing_report_{TODAY}.csv",
    )
