from models import *


class MySQLBuilder:
    def __init__(self, client):
        self.client = client

    def add_total_requests(self, count):
        total_req_count = TotalRequests(count=count)
        self.client.session.add(total_req_count)
        self.client.session.commit()

    def add_total_requests_by_type(self, total_requests_by_type):
        for req_type, count in total_requests_by_type.items():
            self.client.session.add(TotalRequestsByType(type=req_type, count=count))
        self.client.session.commit()

    def add_top_most_frequent_queries(self, top_most_frequent_queries):
        for url, count in top_most_frequent_queries.items():
            self.client.session.add(TopMostFrequentQueries(url=url, count=count))
        self.client.session.commit()

    def add_top_requests_by_size_with_client_error(self, top_requests_by_size_with_client_error):
        for url, code, size, ip in top_requests_by_size_with_client_error:
            self.client.session.add(TopRequestsBySizeWithClientError(url=url, status_code=code, size=size, ip=ip))
        self.client.session.commit()

    def add_top_users_by_number_requests_with_server_error(self, top_users_by_number_requests_with_server_error):
        for ip, count in top_users_by_number_requests_with_server_error.items():
            self.client.session.add(TopUsersByNumberRequestsWithServerError(ip=ip, count=count))
        self.client.session.commit()
