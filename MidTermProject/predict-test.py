#!/usr/bin/env python
# coding: utf-8

import requests
import json

url = 'http://localhost:9696/predict'

sample_id = 'xyz-123'

f = open('B-CELL_ALL_MLL.json') 
sample = json.load(f)

response = requests.post(url, json=sample).json()
print(response)

f = open('B-CELL_ALL_HYPERDIP.json') 
sample = json.load(f)

response = requests.post(url, json=sample).json()
print(response)

f = open('B-CELL_ALL_HYPO.json') 
sample = json.load(f)

response = requests.post(url, json=sample).json()
print(response)

f = open('B-CELL_ALL_T-ALL.json') 
sample = json.load(f)

response = requests.post(url, json=sample).json()
print(response)

f = open('B-CELL_ALL_ETV6-RUNX1.json') 
sample = json.load(f)

response = requests.post(url, json=sample).json()
print(response)
