import csv
import gzip
import io
import json
from urllib.parse import urlencode, urljoin
from urllib.request import Request, urlopen

url = 'https://data.brasil.io/dataset/covid19/caso_full.csv.gz'
request = Request(url, headers={"User-Agent": "python-urllib/brasilio-client-0.1.0"})
response = urlopen(request)

fobj = io.TextIOWrapper(gzip.GzipFile(fileobj=response), encoding="utf-8")
reader = csv.DictReader(fobj)

data = [line for line in reader]