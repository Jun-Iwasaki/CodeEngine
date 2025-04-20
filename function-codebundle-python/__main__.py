# ======================================================= #
#  IBM Cloud Code Engine - Functions-as-a-Service Sample  #
#                                                         #
#  __main.py__ (Python sample function)                   #
#                                                         #
#  This sample code uses an external module "lorem"       #
#  to generate an arbitrary result message. IBM code      #
#  engine functions code with references to external      #
#  modules have to be deployed as code-bundles.           # 
#
#  This sample shows how to access URL parameters in a    #
#  function.                                              #
#                                                         #
#  This sample shows how an external reference is coded   #
#  in the source file (__main__.py) and how the modul     #
#  is referenced in the requirements.txt.                 #
#                                                         #
# ======================================================= #

##
import ibm_db
import requests
import os
def main(dict):
    # パーソナライズ用のテーブルにselect文を発行する
    if dict["action"] == "select":
        ssldsn = "DATABASE=BLUDB;HOSTNAME=a25e0deb-8892-4080-8646-5f11a321fed6-jptok.bt1ibm.db2.ibmappdomain.cloud;PORT=30227;PROTOCOL=TCPIP;UID=cfe1c59d;PWD=u3f2tO8D4RlgsPAI;Security=SSL"
        db_conn = ibm_db.connect(ssldsn,"","")
        sql = "SELECT * FROM ACCOUNT.ACCOUNT_DATA WHERE ID = ?"
        db_stmt = ibm_db.prepare(db_conn,sql)
        id = dict["id"]
        ibm_db.bind_param(db_stmt,1,id)
        ibm_db.execute(db_stmt)
        rows = ibm_db.fetch_tuple(db_stmt)
        ibm_db.close(db_conn)
        return {
            "headers": {
            "Content-Type": "application/json;charset=utf-8",
            },
            "statusCode": 200,
            "body" : {'result' : [rows] }
        }
        
    if dict["action"] == "studio":
        payload_scoring = {
            'age': dict["age"],
            'category': '婦人服03',
            'product': '9900172'
        }
        #response_scoring = requests.post('http://node-assistant-showcase.roks-customercare-tokyo-2-45fd50251ba6e6694c802802d1291f6a-0000.jp-tok.containers.appdomain.cloud', json=payload_scoring, headers={'Content-Type': 'application/json'})
        response_scoring = requests.post('https://application-wa-ws.1g76rmif3lvq.jp-tok.codeengine.appdomain.cloud', json=payload_scoring, headers={'Content-Type': 'application/json'})
        return {
            "headers": {
            "Content-Type": "application/json;charset=utf-8",
            },
            "body" : response_scoring.json()
        }
