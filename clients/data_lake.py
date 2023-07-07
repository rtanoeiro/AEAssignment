import sqlalchemy
from sqlalchemy import create_engine

def connect_data_lake(user,password,host,database):
    # create a connection string
    connection_string = f'postgresql://{user}:{password}@{host}/{database}'
    
    # create and return a database engine
    return create_engine(connection_string)