with open('nginx_logs.txt', 'r', encoding='utf-8') as nginx_logs:
    logs_list = []
    for line in nginx_logs:
        _ = line.split(' ')[0], line.split(' ')[5][1:], line.split(' ')[6]
        logs_list.append(_)
print(*logs_list, sep='\n')
