"""
Test the API functionality
"""
from unittest import main, TestCase
from urllib import urlopen

import os

import duedil

api_key ='XXXXX'

url = 'http://duedil.io/v3/uk/companies/06999618' #The number is the company number
url +='?api_key=' + api_key

print (url)
