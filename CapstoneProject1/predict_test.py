#!/usr/bin/env python
# coding: utf-8

import requests
import json

url = 'http://localhost:9696/predict'

sample_id = 'xyz-123'

f = open('sample_path_all.json') 
sample = json.load(f)

response = requests.post(url, json=sample).json()
print('expected class: ALL', response)

f = open('sample_path_hem.json') 
sample = json.load(f)

response = requests.post(url, json=sample).json()
print('expected class: HEM',response)