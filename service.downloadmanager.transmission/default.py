import xbmc
from os import system


class MyMonitor(xbmc.Monitor):
    def __init__(self, *args, **kwargs):
        xbmc.Monitor.__init__(self)
    
    def onSettingsChanged(self):
        system("systemctl stop service.downloadmanager.transmission")
        xbmc.sleep(2000)
        system("systemctl start service.downloadmanager.transmission")


monitor = MyMonitor()
while not monitor.abortRequested():
    if monitor.waitForAbort():
        break
