class Camera:
    """
    Python Wrapper for Dahua HTTP API

    cam = DahuaCam("admin", "123ABC", "192.168.10.42")

    Args :

    -   username : a valid username
    -   password : user's password
    -   ip : IP address of the camera
    """
    def __init__(self, username="admin", password="admin", ip="192.168.1.108"):
        self.username = username
        self.password = password
        self.ip = ip
        
    def getAuthInfo(self):
        """Returns <cam.username>:<cam.password>@<cam.ip>"""
        return ''.join([self.username,":",self.password,"@",self.ip])

    def rtsp_url(self, channel=0, subtype=0):
        return ''.join(["rtsp://", self.getAuthInfo(),"/cam/realmonitor?channel=",str(channel),"&subtype=",str(subtype)])
