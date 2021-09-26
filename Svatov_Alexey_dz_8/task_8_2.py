import re

RE_ADDR = re.compile(r'(\d|\.|\:|[0-9A-Fa-f])*')
RE_RDATETIME = re.compile(r'[^[]+]')
RE_RTYPE = re.compile(r'[A-Z]{3,7}')
RE_RRESOURCE = re.compile(r'/downloads/product_1 HTTP/1.1')
# RE_RCODE = re.compile()
# RE_RSIZE = re.compile()
logs_list = []

with open('nginx_logs.txt', 'r', encoding='utf-8') as nginx_logs:
    for line in nginx_logs:
        parsed_raw = RE_ADDR.search(line).group(), \
                     RE_RDATETIME.search(line).group().replace(']',''), \
                     RE_RTYPE.search(line).group(), RE_RRESOURCE.search(line)
        logs_list.append(parsed_raw)

#     for line in nginx_logs:
#         _ = line.split(' ')[0], line.split(' ')[5][1:], line.split(' ')[6]
#         logs_list.append(_)
print(logs_list[0:10])