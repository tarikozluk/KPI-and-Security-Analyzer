from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv("../.env")
elastic_url = os.getenv("ELASTIC_URL")
elastic_user = os.getenv("ELASTIC_USER")
elastic_pass = os.getenv("ELASTIC_PASSWORD")



#todo: calculate the values in elastic acc to the formula
#resource: https://snyk.io/blog/website-security-score-explained/ to calculate the score(just an idea)

def get_score_values():

    es = Elasticsearch([elastic_url], basic_auth=(elastic_user, elastic_pass))
    #todo: kibana language query will be improved. this case just for all the data to test the score, after that we are going to filter the data
    query_score_data = {
        "query": {
            "bool": {
                "must": [
                    {
                        "range": {
                            "@timestamp": {
                                "gte": "now-1d/d",
                                "lte": "now/d"
                            }
                        }
                    }
                ]
            }
        }
    }
    security_scan = scan(client=es, index='monthly_log_count_{}'.format(datetime.now().strftime("%Y.%m.%d")), query=query_score_data)
    result = list(security_scan)

    score_from_elastic = []

    # We need only '_source', which has all the fields required.
    # This elimantes the elasticsearch metdata like _id, _type, _index.
    for hit in result:
        score_from_elastic.append(hit['_source'])
    security_score_data = pd.DataFrame(score_from_elastic)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    security_score_data.columns.values.tolist()

    return security_score_data


security_score_data = get_score_values()

info_count = security_score_data['info_count']
warning_count = security_score_data['warning_count']
medium_count = security_score_data['medium_count']
high_count = security_score_data['high_count']
critical_count = security_score_data['critical_count']

#todo: calculate the score (the method must be reliable)
info_score = 0.25
warning_score = 0.5
medium_score = 0.75
high_score = 1
critical_score = 2

info_severity_score = info_count * info_score
warning_severity_score = warning_count * warning_score
medium_severity_score = medium_count * medium_score
high_severity_score = high_count * high_score
critical_severity_score = critical_count * critical_score

#this is just for selected servers, filter the score data according to the related company

server_score = info_severity_score + warning_severity_score + medium_severity_score + high_severity_score + critical_severity_score
#todo: after improved calculation method we are going to improve server_score
#then with this score we will display the score in the dashboard for selected companies. That's why filtering is so important(researchable)(get some support from cyber security team)
