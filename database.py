"""
Functions and code related to retrieval of data from either local storage 
or PostgreSQl database.
"""



import pandas as pd
import numpy as np
import datetime as dt
# from psycopg2 import connect


countries = [
    'us','brazil','russia','spain',
    'italy','france','germany',
    'turkey','india','iran','peru',
    'canada','chile','china','mexico',
    'saudi-arabia','pakistan','belgium',
    'qatar', 'bangladesh',
    'belarus', 'ecuador', 'sweden'
]

# def connect_database(dbname, user='hp', password='test1234', host='127.0.0.1', autocommit=False):
#     """
#     Connect to the PostgreSQL database based on the parameters.
    
#     parameters:
#         dbname: str.
#         Name of the database.
        
#         user: str.
#         Name of the user. Default hp.
        
#         password: str.
#         Password for the user to connect.
        
#         host: str.
#         The IP address of the hosted database. Default 127.0.0.1 (localhost).
        
#         autocommit: Boolean.
#         Set autocommit to True or False. Default False
        
#     returns:
#         conn: connection object.
#         A connection object to the database.
#     """
    
#     conn = connect("dbname="+dbname+" user="+user+" password="+password+" host="+host)
#     conn.autocommit = True
    
#     return conn

def read_dataset(country):
	"""
	Read dataset from local location.

	parameters:
		country: str.
		The country for which data is required.

	returns:
		data: DataFrame.
		A dataframe of the read dataset.
	"""

	data = pd.read_csv('./Data/covid19_'+country+'_stats.csv')
	data['month'] = data.date.apply(lambda x: dt.datetime.strptime(x,'%Y-%m-%d').month)

	return data

def read_database(country):
	"""
	Read dataset from PostgreSQL database.

	parameters:
		country: str.
		The country for which data is required.

	returns:
		data: DataFrame.
		A dataframe of the read relation from database.
	"""

	conn = connect_database('covid19_stats')
	data = pd.read_sql("SELECT * FROM "+country+"_stats;", conn)

	return data



df = read_dataset('us')
df['month'] = df.date.apply(lambda x: dt.datetime.strptime(x,'%Y-%m-%d').month)

overall_df = pd.read_csv('./Data/covid19_overall_stat.csv')
total_cases_world = overall_df.total_cases.sum()
total_recovered_world = overall_df.total_recoveries.sum()
total_deaths_world = overall_df.total_deaths.sum()