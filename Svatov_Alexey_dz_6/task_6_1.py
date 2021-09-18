with open('nginx_logs.txt', 'r', encoding='utf-8') as nginx_logs:
    # logs_list = [line for line in nginx_logs]
    # a = logs_list[0].split(' ')
    logs_list = []
    for line in nginx_logs:
        _ = line.split(' ')[0], line.split(' ')[5][1:], line.split(' ')[6]
        logs_list.append(_)
        # logs_list.append(line.split(' ')[0])
        # logs_list.append(line.split(' ')[5][1:])
        # logs_list.append(line.split(' ')[6])
print(logs_list[0:5])
