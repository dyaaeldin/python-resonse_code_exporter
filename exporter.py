import http.client
import prometheus_client
import time
import json
import os

while True:
  # prometheus variables
  update_period = 300
  response_code = prometheus_client.Gauge('response_code', 'response_code', ['instance'])

  # Request variables
  token = os.environ['TOKEN']
  token_file = open('token', 'r')
  token = token_file.read().replace('\n', '')

  con = http.client.HTTPSConnection('url_without_https://')
  headers = {'Authorization': token, 'Content-Type' : 'application/json'}
  data = {"":""}

  json_data = json.dumps(data)
  con.request("POST", '/path', json_data, headers)
  response = con.getresponse() #needfunction get o/p
  read = response.read()
  json_to_dic = json.loads(read)
  code = json_to_dic["Message"]["Header"]["responseCode"]


  if __name__ == '__main__':
    prometheus_client.start_http_server(9999)

  while True:
    response_code.labels('gg').set(code)
    time.sleep(update_period)
    con.close()
time.sleep("180")
