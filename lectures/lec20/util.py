import zipfile
import requests
import os

def safe_download(url):
    '''
    download data file at url to directory data.
    '''
    
    fname = os.path.join('data', os.path.basename(url))

    # create data dir if doesn't exist
    if not os.path.exists('data'):
        os.mkdir('data')

    # only download if the file exists
    if not os.path.exists(fname):
        resp = requests.get(url)
        resp.raise_for_status()

        with open(fname, 'wb') as f:
            f.write(resp.content)

    # if the file is zipped, unzip it
    dirname, ext = os.path.splitext(fname)
    if ext == '.zip':
        with zipfile.ZipFile(fname, 'r') as zip_ref:
            zip_ref.extractall(dirname)

        fname = dirname

    return fname


def anonymize_names(salaries):
    salaries['Employee Name'] = salaries['Employee Name'].str.split().str[0] + ' Xxxx'
