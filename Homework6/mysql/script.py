from collections import Counter


path = open("access.log")
requests = path.readlines()
for i, value in enumerate(requests):
    requests[i] = value.split()
path.close()


def total_requests():
    """Общее количество запросов"""
    return len(requests)


def total_requests_by_type():
    """Общее количество запросов по типу"""
    type_requests = []
    for i in requests:
        type_requests.append(i[5])
    return dict(Counter(type_requests))


def top_most_frequent_queries():
    """Топ 10 самых частых запросов"""
    location = []
    for i in requests:
        location.append(i[6])
    return dict(Counter(location).most_common(10))


def top_requests_by_size_with_client_error():
    """Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой"""
    error_req = []
    result = []
    for req in requests:
        if (400 <= int(req[8]) < 500):
            error_req.append(req)
    top_req = sorted(error_req, key=lambda req: int(req[9].replace("-", "0")), reverse=True)[:10]
    for i in range(5):
        new_req = (top_req[i][6], top_req[i][8], top_req[i][9], top_req[i][0])
        result.append(new_req)
    return result


def top_users_by_number_requests_with_server_error():
    """Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой"""
    errors = []
    for i in requests:
        if (500 <= int(i[8]) < 600):
            errors.append(i)
    users = []
    for k in errors:
        users.append(k[0])
    return dict(Counter(users).most_common(5))
