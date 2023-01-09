import win32serviceutil
from gevent.pywsgi import WSGIServer

from api import app


class FlaskService(win32serviceutil.ServiceFramework):
    # 服务名
    _svc_name_ = "flask_gevent_service_test"
    # 显示服务名
    _svc_display_name_ = "flask gevent service test display name"
    # 描述
    _svc_description_ = "flask gevent service test description"

    def __init__(self, *args):
        super().__init__(*args)
        # host和ip绑定
        self.http_server = WSGIServer(('0.0.0.0', 5000), app)
        self.SvcStop = self.http_server.stop
        self.SvcDoRun = self.http_server.serve_forever
