#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9696/predict'

customer_id = 'xyz-123'
customer = {"job": "retired", "duration": 445, "poutcome": "success"}


response = requests.post(url, json=customer).json()
print(response)

#if response['churn'] == True:
#    print('sending promo email to %s' % customer_id)
#else:
#    print('not sending promo email to %s' % customer_id)

customer = {"job": "unknown", "duration": 270, "poutcome": "failure"}

response = requests.post(url, json=customer).json()
print(response)

client = {"job": "retired", "duration": 445, "poutcome": "success"}
response = requests.post(url, json=client).json()
print(response)