from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os




def get_response_time():
    load_dotenv("../.env")
    elastic_url = os.getenv("ELASTIC_URL")
    elastic_user = os.getenv("ELASTIC_USER")
    elastic_pass = os.getenv("ELASTIC_PASSWORD")
    print("Connection Okeydir")
    es = Elasticsearch([elastic_url], basic_auth=(elastic_user, elastic_pass))
    # elasticsearch query
    query = {
        "query": {
            "wildcard": {
                "sitename.keyword": "*turkuaz*"
            }
        }
    }
    part_of_index = scan(client=es,
                         query=query,
                         index=('kpi_metrics_logs_{}'.format(datetime.now().strftime('%Y.%m.%d'))),
                         raise_on_error=True,
                         preserve_order=False,
                         clear_scroll=True
                         )

    result = list(part_of_index)

    temp = []

    # We need only '_source', which has all the fields required.
    # This elimantes the elasticsearch metdata like _id, _type, _index.
    for hit in result:
        temp.append(hit['_source'])
    df = pd.DataFrame(temp)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    df.columns.values.tolist()


    return df


df = get_response_time()
print(df)
