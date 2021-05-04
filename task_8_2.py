import re
import requests

url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
PARSE_ADD = re.compile(r'((?:\d+.){3}\d+) - - [[](\d{2}/[A-Za-z]+/\d{4}:(?:\d{2}:){2}\d{2} \+\d{4})[]] '
                           r'[\"](\w+) ([/]\w+[/]\w+ \w+[/]\d+.\d+)[\"] (s*\d{3}) (\d+)')

data = requests.get(url).text
for raw in PARSE_ADD.findall(data):
    ip_add, date, res_type, resource, type_code, size = raw
    data_url = (f'{ip_add}', f'{date}', f'{res_type}', f'{resource}', f'{type_code}', f'{size}')
    print(data_url)