"""
Test the API functionality
"""
from unittest import main, TestCase
from urllib import urlopen

import os

import duedil

api_key ='uq4wy8z7hkra5nnfqu9yuv7j'

url = 'http://duedil.io/v3/uk/companies/06999618' #The number is the company number
url +='?api_key=' + api_key

print (url)
