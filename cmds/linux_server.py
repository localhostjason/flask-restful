from flask import Blueprint

import os
import time

server_cmd = Blueprint('server', __name__)


# start | stop 只适合linux
class ServerCommand(object):
    @staticmethod
    def _get_pid():
        pid_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../gunicorn.pid')
        try:
            with open(pid_file, 'r') as f:
                return int(f.read())
        except Exception as e:
            return None

    def get_status(self):
        pid = self._get_pid()
        if not pid:
            return False
        try:
            os.kill(pid, 0)
            return True
        except ProcessLookupError as e:
            return False
        except Exception as e:
            return True


class Start(ServerCommand):
    """
    start gunicorn web server
    """

    def run(self):
        if self.get_status():
            return
        cmd = 'gunicorn -c gun.py main:app --daemon'
        os.system(cmd)


class Stop(ServerCommand):
    """
    stop gunicorn web server
    """

    def run(self):
        pid = self._get_pid()
        if not pid:
            print('web server stopped')
            return
        try:
            os.kill(pid, 15)
        except ProcessLookupError as e:
            print('failed to kill pid:{},{}'.format(pid, str(e)))
        except PermissionError:
            pass
            print('no permission to kill pid {}'.format(pid))
        for i in range(3):
            if self.get_status():
                time.sleep(1)
        if self.get_status():
            print('web server failed to stop')


@server_cmd.cli.command("start")
def start_server():
    Start().run()


@server_cmd.cli.command("stop")
def start_server():
    Stop().run()
