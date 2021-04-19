from urllib.parse import urljoin
import requests


class ResponseStatusCodeException(Exception):
    pass


class ApiClient:
    def __init__(self):
        self.base_url = 'https://target.my.com/'
        self.session = requests.Session()
        self.csrf_token = None
        self.login('kamabulletez@mail.ru', 'bibletump123')

    def _request(self, method, location, headers=None, data=None, expected_status=200, params=None, json=None,
                 jsonify=True):

        url = urljoin(self.base_url, location)

        response = self.session.request(method, url, headers=headers, params=params, json=json, data=data)

        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f' Got {response.status_code} {response.reason} for URL "{url}"')
        if jsonify:
            return response.json()
        return response

    def login(self, email, password):
        location = 'https://auth-ac.my.com/auth'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://target.my.com/'}

        data = {
            'email': email,
            'password': password,
            'continue': 'https://account.my.com/login_continue'}

        response = self._request('POST', location, headers=headers, data=data, jsonify=False)
        self.get_token()
        return response

    def get_token(self):
        location = 'https://target.my.com/csrf'
        return self._request('GET', location, jsonify=False)

    def post_create_campaign(self, name):
        location = 'https://target.my.com/api/v2/campaigns.json'
        data = {
            "age_restrictions": None,
            "autobidding_mode": "second_price_mean",
            "banners": [{"content": {"image_240x400": {"id": 8678801}},
                         "name": "",
                         "textblocks": {},
                         "urls": {"primary": {"id": 47176916}}
                         }],
            "budget_limit": None,
            "budget_limit_day": None,
            "conversion_funnel_id": None,
            "date_end": None,
            "date_start": None,
            "enable_offline_goals": False,
            "enable_utm": True,
            "max_price": "0",
            "mixing": "fastest",
            "name": name,
            "objective": "traffic",
            "package_id": 961,
            "targetings": {
                "age": {
                    "age_list": [0, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
                                 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45,  46, 47, 48, 49, 50, 51, 52, 53,
                                 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75],
                    "expand": True
                },
                "fulltime": {
                    "flags": [
                        "use_holidays_moving",
                        "cross_timezone"
                    ],
                    "fri": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                    "mon": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                    "sat": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                    "sun": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                    "thu": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                    "tue": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                    "wed": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
                },
                "geo": {
                    "regions": [
                        188
                    ]
                },
                "interests": [],
                "interests_soc_dem": [],
                "mobile_operators": [],
                "mobile_types": [
                    "tablets",
                    "smartphones"
                ],
                "mobile_vendors": [],
                "pads": [
                    102643
                ],
                "segments": [],
                "sex": [
                    "male",
                    "female"
                ],
                "split_audience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            },
            "utm": None
        }
        headers = {'Content-Type': 'application/json',
                   'X-CSRFToken': self.session.cookies['csrftoken']
                   }
        response = self._request('POST', location, headers=headers, json=data)
        return response['id']

    def post_create_segment(self, name):
        location = 'api/v2/remarketing/segments.json'
        data = {'name': name,
                'pass_condition': 1,
                'relations': [{'object_type': 'remarketing_player',
                               'params': {'type': 'positive',
                                          'left': 365,
                                          'right': 0}}],
                'logicType': 'or'}
        headers = {'Content-Type': 'application/json',
                   'X-CSRFToken': self.session.cookies['csrftoken']
                   }
        response = self._request('POST', location, headers=headers, json=data)
        return response['id']

    def get_check_campaign(self):
        location = 'api/v2/campaigns.json?fields=id%2Cname%2Cdelivery%2Cprice%2Cbudget_limit%2Cbudget_limit_day%2' \
                   'Cpads_ots_limits%2Ccreated%2Cissues%2Cprices%2Cstatus%2Cpackage_id%2Cinterface_read_only%2' \
                   'Cobjective%2Cuser_id%2Ctargetings__split_audience%2Ctargetings__pads%2Cenable_utm%2Cutm%2' \
                   'Cage_restrictions%2Cpackage_priced_event_type%2Cautobidding_mode&sorting=-id&limit=100' \
                   '&offset=0&_status__in=active'
        campaign_json_id = self._request('GET', location)
        return [response['id'] for response in campaign_json_id['items']]

    def get_check_segment(self):
        location = 'api/v2/remarketing/segments.json'
        segment_json_id = self._request('GET', location)
        return [response['id'] for response in segment_json_id['items']]

    def delete_campaign(self, id_campaign):
        location = f'api/v2/campaigns/{id_campaign}.json'
        headers = {'X-CSRFToken': self.session.cookies['csrftoken']}
        self._request('DELETE', location, expected_status=204, headers=headers, jsonify=False)

    def delete_segment(self, id_segment):
        location = f'api/v2/remarketing/segments/{id_segment}.json'
        headers = {'X-CSRFToken': self.session.cookies['csrftoken']}
        self._request('DELETE', location, expected_status=204, headers=headers, jsonify=False)
