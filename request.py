import requests
from requests.auth import HTTPDigestAuth
from .camera import Camera

class Request:
    def __init__(self):
        self.cam: Camera = None
        self.path = None
        self.action = None
        self.head = None
        self.args = None

    def check(self, path, action):
        if self.path is None:
            self.path = path 
        else:
            if self.path != path:
                return False
        
        if self.action is None:
            self.action = action 
        else:
            if self.action != action:
                return False
        return True

    def merge(self):
        args = dict({"action": self.action})
        if self.args is not None:
            args.update(self.args)
        ret = [
            "http://",
            self.cam.getAuthInfo(),
            self.path,
        ]
        tmp=[]
        for k, v in args.items():
            tmp.append("=".join([k,v]))
        tmp = "&".join(tmp)
        ret.append(tmp)
        ret = ''.join(ret)
        return ret

    def __str__(self):
        return self.merge()

    def send(self):
        try:
            response = requests.get(self.merge(), auth= HTTPDigestAuth(self.cam.username, self.cam.password))
            return response
        except requests.exceptions.ConnectionError:
            response = requests.Response()
            response.__setattr__("status_code", 404)
            utf_string = "ERROR"
            bytes_string = utf_string.encode('utf-8')
            response._content = bytes_string
            return response