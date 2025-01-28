import requests
import json
import pandas as pd
from pandas import json_normalize


#Use this API
api_url = "https://fakestoreapi.com/products"

def fetch_result(api_ur):
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

def result_to_dataframe(result):
    df = pd.DataFrame(result)
    return df

def clean_dataframe(dataframe):
    dataframe['rate'] = dataframe['rating'].apply(lambda x: x['rate'])
    dataframe['count'] = dataframe['rating'].apply(lambda x: x['count'])
    dataframe = dataframe.drop(columns=['rating'])
    return dataframe


result = fetch_result(api_url)

dataframe = result_to_dataframe(result)

cleaned_dataframe = clean_dataframe(dataframe)

print(cleaned_dataframe)