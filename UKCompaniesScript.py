"""
Test the API functionality
"""
import requests
import csv
import json
import time

# Global variables

URL = 'http://duedil.io/v3/uk/companies/'  # The number is the company number
API_KEY = {'api_key': 'uq4wy8z7hkra5nnfqu9yuv7j'}
TIME_SLEEP = 0  # time interval between two call in sec. Can be in float number
INFILE = './DuedilListFinal.csv'
OUTFILE = './result.json'


def get_list_company(infile):
    """ yield the company number from the txt file
    """
    # outlist = list()
    with open(infile, 'r') as f:
        csvreader = csv.reader(f)
        next(csvreader)  # to skip the header
        for l in csvreader:
            yield l[0]  # csv reader return a list, just yield the unique element of the list to return un str
            # outlist.append(l)
    # return outlist


def create_url(*args):
    """ Return an URL from the element, add them in order
    """
    url = args[0] + args[1]
    return url


def parse_company(url, api_key=API_KEY):
    """ Get the URL, api_key and company number
        Return result if receive a 200 and that the response
        is a json format otherwise print error and return empty dict otherwise
    """
    response = requests.get(url, data=api_key)
    resp = dict()
    if response.status_code == 200:
        if response.headers['content-type'] == 'application/json':
            resp = response.json()['response']
        else:
            print('Error in the type of answer received: {} with the URL: {}'.format(response.headers['content-type'], url))
    else:
        print('Error {} in accessing service with the URL: {}'.format(response.status_code, url))
    return response.status_code, resp


def company_result():
    for company in get_list_company(INFILE):
        time.sleep(TIME_SLEEP)
        url = create_url(URL, company, API_KEY)
        status, response = parse_company(url)
        print(response)
        yield company, response


def main():
    # to reinitialise the file, comment if you don't want that behaviour
    with open(OUTFILE, 'w') as out:
        out.write('[')
    n = 0
    for company, response in company_result():
        proper_resp = dict()
        proper_resp['response'] = response
        proper_resp['request_id'] = company  # add our own field in the response dict
        with open(OUTFILE, 'a') as out:
            if n > 0:
                out.write(',')
            json.dump(proper_resp, out)
        n +=1
    with open(OUTFILE, 'a') as out:
        out.write(']')

if __name__ == '__main__':
    main()
