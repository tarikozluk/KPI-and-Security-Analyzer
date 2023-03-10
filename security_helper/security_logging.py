from tenable.sc import TenableSC
from dotenv import load_dotenv
import os
from re import search
from datetime import datetime, timedelta
from Elasticsearch_Factory import elasticsearch_logging
import json


#get .env path from root
load_dotenv("../.env")

sc = TenableSC(os.getenv("SECURITYCENTER_NETWORK_ADDRESS"),access_key=os.getenv("ACCESS_KEY"),secret_key=os.getenv("SECRET_KEY"))
sc.login(access_key=os.getenv("ACCESS_KEY"),secret_key=os.getenv("SECRET_KEY"))


vulnebilities = []
#severity_count = {'Info': 0, 'Low': 0, 'Medium': 0, 'High': 0, 'Critical': 0}
#todo: scorecarddaki iştiraklerin verilerin olduğu sadece uygulama sunucuları eklenecek; iştiraK:ip eşleştirmesi yaparak gerekli parametreleri get edecek.
for vuln in sc.analysis.vulns():
    if vuln['ip'] == 'IP BLOK':
        #vulnebilities.append(vuln)
        vulnebilities_ip = vuln['ip']
        vulnebilities_plugin= vuln['pluginName']
        severity = vuln['severity']['name']
        json_vulnebility = {
            'IP_adress' : vulnebilities_ip,
            'Plugin_Name': vulnebilities_plugin,
            'severity' : severity
        }
        vulnebilities.append(json_vulnebility)
    #print(json.dumps(vulnebilities))
        #print(severity)
    # if severity in severity_count:
    #     severity_count[severity] += 1
    # else:
    #     print("Severity not found")

#elasticsearch_logging.elastic_monthly_log_count(**severity_count)
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