from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv("../.env")
def company_name_create(company,company_id):
    print("Connection Okeydir")
    load_dotenv()
    elastic_url = os.getenv("ELASTIC_URL")
    elastic_user = os.getenv("ELASTIC_USER")
    elastic_pass = os.getenv("ELASTIC_PASSWORD")
    es = Elasticsearch([elastic_url], basic_auth=(elastic_user, elastic_pass))
    es.index(
        index='tenable_security_test_{}'.format(datetime.now().strftime("%Y.%m.%d")),
        document={
            'Company_name': '{}'.format(company),
            'company_id': '{}'.format(company_id),
            'LogDate': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            '@timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

def log_getter(company, command, db,username,chat_title):
    print("Connection Okeydir")
    load_dotenv()
    elastic_url = os.getenv("ELASTIC_URL")
    elastic_user = os.getenv("ELASTIC_USER")
    elastic_pass = os.getenv("ELASTIC_PASSWORD")
    es = Elasticsearch([elastic_url], basic_auth=(elastic_user, elastic_pass))
    es.index(
        index='bot_auto_operation_test_{}'.format(datetime.now().strftime("%Y.%m.%d")),
        document={
            'CommandResult': 'Success',
            'username': username,
            'Forwarded_DB': '{}'.format(db),
            'Company': '{}'.format(company),
            'LogDate': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'Group Name' : '{}'.format(chat_title),
            'Command': '{}'.format(command)
        })



def elastic_monthly_log_count(info_count,warning_count,medium_count,high_count,critical_count):
    print("Connection Okeydir")
    load_dotenv()
    elastic_url = os.getenv("ELASTIC_URL")
    elastic_user = os.getenv("ELASTIC_USER")
    elastic_pass = os.getenv("ELASTIC_PASSWORD")
    es = Elasticsearch([elastic_url], basic_auth=(elastic_user, elastic_pass))
    es.index(
        index='monthly_log_count_{}'.format(datetime.now().strftime("%Y.%m.%d")),
        document={
            'info_count': '{}'.format(info_count),
            'warning_count_medium_count': '{}'.format(warning_count),
            'high_count': '{}'.format(high_count),
            'medium_count': '{}'.format(medium_count),
            'critical_count': '{}'.format(critical_count),
            'LogDate': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            '@timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
