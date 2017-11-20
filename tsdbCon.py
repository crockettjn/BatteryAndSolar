import time
import requests
import json
# Random only needed for testing, not the actual tsdbWrite class
import random


class tsdbWrite:
    def __init__(self, target):
        self.create_session()
        self.host = target
        self.url = self.host + '/api/put?details=1'

    def create_session(self):
        self.request_session = requests.Session()
        self.request_session.headers.update(
            {'Content-Type': 'application/json', 'Accept': 'application/json'}
            )

    def push_metric(self, host, metric_name,
                    metric_value, timestamp=None, **kwargs):
        data = {}
        data["metric"] = metric_name
        if timestamp is None:
            data["timestamp"] = time.time()
        else:
            data["timestamp"] = timestamp
        data["value"] = metric_value
        data["tags"] = {}
        data["tags"]["host"] = host
        for tag, value in kwargs.items():
            data["tags"][tag] = value
        data = json.dumps(data)
        try:
            r = self.request_session.post(self.url, data=data, verify=False)
        except requests.exceptions.RequestException as e:
            print("Recreating Requests session")
            print(e)
            self.create_session()
            self.push_metric(self, host, metric_name,
                             metric_value, timestamp, kwargs)
        if r.status_code != 204:
            print(r.status_code, r.content)
        else:
            print("Sucessfully pushing metric for %s." % metric_name)


# This file not meant to be run as a script, this method and execution of it
# is just for testing and as an example of how to use it.
def main():
    metric = tsdbWrite('http://crockett.info:4242')
    while True:
        metric.push_metric("rpi", "CPU", random.randrange(1, 99))
        metric.push_metric("rpi", "Memory", random.randrange(1, 10))
        metric.push_metric("rpi", "Disk", random.randrange(1, 30))
        time.sleep(1)


if __name__ == "__main__":
    main()
