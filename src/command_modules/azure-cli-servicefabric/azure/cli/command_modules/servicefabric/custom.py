
import json
import contextlib
import OpenSSL.crypto
import os
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import ssl

from azure.cli.core._config import set_global_config_value
from azure.cli.core._environment import get_config_dir
import shelve

CONFIG_PATH = os.path.join(get_config_dir(), "config.db")

base_uri = 'http://seabreeze-demo.westus.cloudapp.azure.com'
rg = 'sbzrg'
subscriptionId = '13ad2c84-84fa-4798-ad71-e70c07af873f'
path = '/subscriptions/{}/resourcegroups/{}/providers/Microsoft.Seabreeze/applications/'.format(subscriptionId,rg)

app_url = '{}?api-version=2017-07-01'

full_uri = base_uri + path + app_url


def pfx_to_pem(pfx_path, pfx_password):
    dir_name = os.path.dirname(pfx_path)
    tmp = os.path.join(dir_name,'temp.pem')
    f_pem = open(tmp,'wb')
    pfx = open(pfx_path, 'rb').read()
    p12 = OpenSSL.crypto.load_pkcs12(pfx, pfx_password)
    f_pem.write(OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, p12.get_privatekey()))
    f_pem.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, p12.get_certificate()))
    ca = p12.get_ca_certificates()
    if ca is not None:
        for cert in ca:
            f_pem.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, cert))
    f_pem.close()
    d = shelve.open(CONFIG_PATH)
    d['pem'] = f_pem.name  

def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except:
    return False
  return True

def is_secure(url):
    return url.lower().startswith('https')

def load(client,cert,pwd):
    pfx_to_pem(cert,pwd)

	
def get(client, app_name):
    
    url = full_uri.format(app_name)
    if is_secure(url):
        d = shelve.open(CONFIG_PATH)
        cert = d['pem']
        if cert is None:
            raise Exception('run \'load\' to load cert')	
        ret = requests.get(url, cert=cert, verify=False)
    else:
        ret =  requests.get(url,verify=False)
    if is_json(ret.text):
        return ret.json()
    else:
        print(ret.text)

    
def put(client,app_name, content):
    headers = {'Content-type': 'application/json'}	
    url = full_uri.format(app_name)
    if is_secure(url):
        d = shelve.open(CONFIG_PATH)
        cert = d['pem']
        if cert is None:
            raise Exception('run \'load\' to load cert') 
        ret = requests.put(url,data = content, cert=cert,verify=False,headers = headers)
    else:
        ret =  requests.put(url,data = content,verify=False,headers = headers)
    if is_json(ret.text):
        return ret.json()
    else:
        print(ret.text)

    
def post(client, app_name):
    headers = {'Content-type': 'application/json'}
    url = full_uri.format(app_name)
    response = requests.get(url,verify=False)
    while response.json()['properties']['applicationHealthState'].lower() != 'ok':
        import time
        time.sleep(10)
        print('applicationHealthState is ' + response.json()['properties']['applicationHealthState'])
        response = requests.get(url,verify=False)
    endpoint = response.json()['properties']['clusterEndpoint']
    app = response.json()['properties']['deployedApplicationName']
    apps = app.split(":/")
    cluster_endpoint = 'http://' + endpoint + ':19080/'
    get_service_url = cluster_endpoint + 'Applications/{}/$/GetServices?&api-version=3.0'.format(apps[1])
    get_service_respone =  requests.get(get_service_url,verify=False)
    service = get_service_respone.json()['Items'][0]['Id']
    if is_secure(url):
        d = shelve.open(CONFIG_PATH)
        cert = d['pem']
        if cert is None:
            raise Exception('run \'load\' to load cert') 
        ret = requests.post(url,json = content, cert=cert,verify=False,headers = headers)
    else:
        import json  
        content = json.loads('{"Flags": "1", "ServiceKind": "Stateless", "InstanceCount": 10}')
        url = cluster_endpoint + 'Services/{}/$/Update?api-version=3.0'.format(service)
        ret =  requests.post(url,json = content,verify=False,headers = headers)
    if is_json(ret.text):
        return ret.json()
	

def delete(client, app_name):
    url = full_uri.format(app_name)
    # response = requests.get(url,verify=False)
    # endpoint = response.json()['properties']['clusterEndpoint']
    # url = 'http://' + endpoint + path + '{}'.format(app_name)
    url = base_uri + path + app_name
    print(url)
    if is_secure(url):
        d = shelve.open(CONFIG_PATH)
        cert = d['pem']
        if cert is None:
            raise Exception('run \'load\' to load cert') 
        ret = requests.delete(url,cert=cert,verify=False)
    else:
        ret =  requests.delete(url,verify=False)
    if is_json(ret.text):
        return ret.json()
    else:
        print(ret.text)