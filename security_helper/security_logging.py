from tenable.sc import TenableSC
from dotenv import load_dotenv
import os
from re import search
from tenable.io import TenableIO
from Elasticsearch_Factory import elasticsearch_logging
from datetime import datetime, timedelta


#get .env path from root
load_dotenv("../.env")

sc = TenableSC(os.getenv("SECURITYCENTER_NETWORK_ADDRESS"),access_key=os.getenv("ACCESS_KEY"),secret_key=os.getenv("SECRET_KEY"))
sc.login(access_key=os.getenv("ACCESS_KEY"),secret_key=os.getenv("SECRET_KEY"))



vulnebilities = []

#get vulnerabilities from asset_lists.list()


# for vuln in sc.analysis.vulns():
#     vulnebilities.append(vuln)
#     print(vuln)
isimler=sc.asset_lists.list()

for item in isimler['usable']:
    if search("Manual",item['name']):
        print(item['id'])
        print(item['name'])
        elasticsearch_logging.company_name_create(company=item['name'],company_id=item['id'])
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