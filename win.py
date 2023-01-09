import win32serviceutil
from cmds.win_server import FlaskService

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(FlaskService)
