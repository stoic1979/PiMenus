#
# class for communicating with server via REST APIs
#
import requests
import json
import traceback


class ApiManager:

    def __init__(self, key):
        self.key = key

    def get_token(self):
        """
        function gets access token from greenrush server
        """
        url = 'https://www.greenrush.com/api/v2/authorize'
        #token = '$2y$10$ehNDTqORidMNnL4xDW.bTemFH3/YENp7qzlrXRRx971tielybhNE6'
        try:
            headers = {'accept': 'application/vnd.greenrush.v2+json',
                       'content-type': 'application/json'}
            data = {"token": self.key}

            print "data:", data

            r = requests.post(url, headers=headers, data=json.dumps(data))
            print r.status_code
            print r.headers
            print r.content

            resp = json.loads(r.content)
            token = resp['token']
            print "[INFO] token:", token
            return token
        except Exception as exp:
            print "get_token() :: Got exception: %s" % exp
            print(traceback.format_exc())

    def get_products_xml(self, token, limit=100):
        """
        Function gets xml for products from server by given limit.

        It needs access token for authorization by server
        """
        xml = ''

        url = 'https://www.greenrush.com/api/v2/products/?limit=%d' % limit

        print "[INFO] get_products_xml() getting xml for url: %s" % url

        headers = {'accept': 'application/vnd.greenrush.v2+xml',
                   'authorization': 'Bearer %s' % token}

        r = requests.get(url, headers=headers)
        print r.status_code
        print r.headers
        print r.content
        xml = r.content
        return xml

if __name__ == '__main__':
    key = '$2y$10$ehNDTqORidMNnL4xDW.bTemFH3/YENp7qzlrXRRx971tielybhNE6'
    am = ApiManager(key)
    token = am.get_token()
    am.get_products_xml(token, 10)
