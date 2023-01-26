from tenable.sc import TenableSC
from dotenv import load_dotenv
import os
from re import search
from datetime import datetime, timedelta
from Elasticsearch_Factory import elasticsearch_logging

#get .env path from root
load_dotenv("../.env")

sc = TenableSC(os.getenv("SECURITYCENTER_NETWORK_ADDRESS"),access_key=os.getenv("ACCESS_KEY"),secret_key=os.getenv("SECRET_KEY"))
sc.login(access_key=os.getenv("ACCESS_KEY"),secret_key=os.getenv("SECRET_KEY"))



vulnebilities = []
info_count = 0
warning_count = 0
medium_count = 0
high_count = 0
critical_count = 0
#get specific vulnerability from security center



#get vulnerabilities from asset_lists.list()


for vuln in sc.analysis.vulns():
    if vuln['ip'] == 'IP BLOK':
        vulnebilities.append(vuln)
        #print(vulnebilities)
        print(vuln['ip'])
        print(vuln['pluginName'])
        print(vuln['severity']['name'])
        if vuln['severity']['name'] == 'Info':
            info_count += 1
        elif vuln['severity']['name'] == 'Warning':
            warning_count += 1
        elif vuln['severity']['name'] == 'Medium':
            medium_count += 1
        elif vuln['severity']['name'] == 'High':
            high_count += 1
        elif vuln['severity']['name'] == 'Critical':
            critical_count += 1
        else:
            print("Severity not found")


#todo: get the count of vulnerabilities from security center and send it to elasticsearch
#cronjob will run after all the vulnerabilities are collected, cyber security team'll deliver the dates
elasticsearch_logging.elastic_monthly_log_count(info_count,warning_count,medium_count,high_count,critical_count)
isimler=sc.asset_lists.list()

# for item in isimler['usable']:
#     if search("Manual",item['name']):
#         print(item['id'])
#         print(item['name'])
#         print(item)
        #elasticsearch_logging.company_name_create(company=item['name'],company_id=item['id'])
#todo: add security logger

# elasticsearch_logging.log_getter(company="{}".format(ip_command_array[3]),
#                                 command="{}".format(ip_command_array[0]),
#                                 db="Elasticsearch Index",
#                                 username="{}".format(message.from_user.username),
#                                 chat_title="{}".format(message.chat.title))

"""
DB'de bir tablo tutulacak. Vulnerabilitylerin toplamı iştirak bazlı ve severitye göre sınıflandırılacak.
Bu cıkan oranlar kritiklik skorları belirlenerek security score hesaplanacak. ve tabloda hedef kpi'lar ile birlikte sunulacak.
DB'de bu veri yoksa api'dan veri çekilip veri basılacak, veri mevcutsa bu işleme gerek kalmayaacaktır.


"""