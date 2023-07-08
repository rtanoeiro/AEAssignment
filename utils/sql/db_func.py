import datetime

from dateutil.relativedelta import relativedelta

from config.config import datatypes

def define_columns():
  """Define column names and data type of database"""
  column_definition = ",\n".join(
        f"{column_name} {column_type}" for column_name, column_type in datatypes.items()
    )
  return column_definition

def join_columns():
  """Prepare column tuple for inserting data"""
  column_tuple = ", ".join(datatypes.keys())
  return column_tuple

def month_period():
  """Set month period"""
  month_beggining = datetime.date.today().replace(day=1)
  month_end = month_beggining + relativedelta(day=31)
  return month_beggining, month_end
