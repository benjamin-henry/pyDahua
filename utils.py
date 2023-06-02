import requests
from requests.auth import HTTPDigestAuth


def add_args(data):
    ret = []
    for k, v in data.items():
        ret.append(''.join([str(k),"=",str(v)]))
    return "&".join(ret)

def make_request(url, cam_instance):
    response = requests.get(url, auth=HTTPDigestAuth(cam_instance.username, cam_instance.password))
    return response