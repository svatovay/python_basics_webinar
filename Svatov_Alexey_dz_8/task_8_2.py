import re

RE_ALL = re.compile(r'((?:\d|\.|:|[0-9A-Fa-f])*)\s-\s-\s\['
                    r'([^[]+)\]\s"'
                    r'([A-Z]{3,7})\s'
                    r'(/(?:[a-z]|[A-Z]|\d|_)*/(?:[a-z]|[A-Z]|\d|_)*\s[A-Z]{3,5}/\d\.\d)"\s'
                    r'([\d]{3})\s'
                    r'([\d]{1,4})')

with open('nginx_logs.txt', 'r', encoding='utf-8') as nginx_logs:
    parsed_raw = RE_ALL.findall(nginx_logs.read())
print(parsed_raw[10])
