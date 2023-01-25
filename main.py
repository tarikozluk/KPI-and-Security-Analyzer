import dash
import pandas as pd
import numpy as np
from elasticsearch import Elasticsearch
from dash.dependencies import Output, Input
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from re import search
import pyodbc
from templates.main_page import main_layout
from Elasticsearch_Factory import elasticsearch_logging


load_dotenv()

#sql to pandas dataframe

conn = pyodbc.connect(os.getenv("CONNECTION_STRING"))
cursor = conn.cursor()
df = pd.read_sql_query(os.getenv("SQL_KPI_SELECT_QUERY"), conn)

#todo: add datasource from test elasticsearch for response time logging

elastic_url = os.getenv("ELASTIC_URL")
elastic_user = os.getenv("ELASTIC_USER")
elastic_pass = os.getenv("ELASTIC_PASSWORD")

es = Elasticsearch([elastic_url], basic_auth=(elastic_user, elastic_pass))

#todo: get response time for each application from elasticsearch


external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = "KPI Analyzer: Lead Your Application!"


Application = df.Application.unique().tolist()

#todo: add new block side by side with sql table
app.layout = main_layout.get_layout(app,Application,df)

#todo: filtering must be improved
@app.callback(
    Output("table-container", "data"),
    Input("filter_dropdown", "value")
)

def display_table(Application):
    dff = df[df.Application.isin(Application)]
    return dff.to_dict("records")



#todo: target kpi values from database which already exists







if __name__ == "__main__":
    app.run_server(debug=True)
