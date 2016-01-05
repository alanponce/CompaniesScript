"""
Test the API functionality
"""
import requests
import time


URL = 'http://duedil.io/v3/uk/companies/'  # The number is the company number
API_KEY = {'api_key': 'uq4wy8z7hkra5nnfqu9yuv7j'}
TIME_SLEEP = 1  # time interval between two call in sec. Can be in float number
INFILE = './DuedilListFinal.csv'

def get_list_company(infile):
    """ yield the company number from the txt file
    """
    # outlist = list()
    with open(infile, 'r') as f:
        for l in f:
            yield l[:-1]  # skyp the \r from the new line
            # outlist.append(l)
    # return outlist


def create_url(*args):
    """ Return an URL from the element, add them in order
    """
    url = args[0] + args[1]
    return url


def parseCompany(url, api_key=API_KEY):
    """ Get the URL, api_key and company number
        Return result if receive a 200 and that the response
        is a json format otherwise print error and return None
    """
    response = requests.get(url, data=api_key)
    resp = None
    if response.status_code == 200:
        if response.headers['content-type'] == 'application/json':
            resp = response.json()['response']
        else:
            print('Error in the type of answer received: {} with the URL: {}'.format(response.headers['content-type'], url))
    else:
        print('Error {} in accessing service with the URL: {}'.format(response.status_code, url))
    return response.status_code, resp

def main():
    for company in get_list_company(INFILE):
        print(company)
        url = create_url(URL, company, API_KEY)
        status, response = parseCompany(url)

if __name__ == '__main__':
    main()
