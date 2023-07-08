from sqlalchemy import create_engine


def connect_data_lake(user,password,host,database):
    """Connects to Postgresql Database"""
    connection_string = f'postgresql://{user}:{password}@{host}/{database}'
    return create_engine(connection_string)