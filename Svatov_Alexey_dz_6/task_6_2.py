with open('nginx_logs.txt', 'r', encoding='utf-8') as nginx_logs:
    ip_set = set()
    for line in nginx_logs:
        ip_set.add(line.split(' ')[0])

print(ip_set)
