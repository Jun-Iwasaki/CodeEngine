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

import ibm_db
import requests
import os
def main(dict):
    result_body = {'result': [(111, '山田', 45, 'M', '03-3333-4444', '中央区日本橋箱崎町 19-21', 'マルゲリータ', 'L', 'コーラ', '唐揚げ', 'P', None)]}
    return {
        "headers": {
        "Content-Type": "application/json;charset=utf-8",
        },
        "statusCode": 200,
        "body": {'result' : [dict] }
    }
