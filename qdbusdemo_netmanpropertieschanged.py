import sys
from PySide6.QtWidgets import QMainWindow
from PySide6 import QtDBus, QtCore
from PySide6.QtCore import QLibraryInfo, qVersion, Slot
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        service = "org.freedesktop.NetworkManager"
        #service="org.mpris.MediaPlayer2.spotifyd.instance7453"
        path = "/org/freedesktop/NetworkManager"
        #path="/org/mpris/MediaPlayer2"
        iface = "org.freedesktop.DBus.Properties"
        conn = QtDBus.QDBusConnection.systemBus()

        #without this, the conn.connect call hangs, seems to be a bug, is already reported and fixed.
        conn.registerObject('/', self)
        
        #bus.connect(service, path, iface, "PropertiesChanged", self, QtCore.SLOT("dbuspropertieschanged(QString,QVariantMap,QStringList)"))    
        #qt.dbus.integration: Could not connect "org.freedesktop.DBus.Properties" to dbuspropertieschanged(QString,QVariantMap,QStringList)

        conn.connect(service, path, iface, "PropertiesChanged", self, QtCore.SLOT("dbuspropertieschanged(QString, QVariantMap, QVariantList)"))    
        pass

    @Slot(str, dict, list)
    def dbuspropertieschanged(self, arg1:str, arg2:dict, arg3:list) -> None:
        print(arg1)
        print(arg2)
        print(arg3)
        pass

if __name__ == '__main__':
    print('Python {}.{}.{} {}'.format(sys.version_info[0], sys.version_info[1],
                                       sys.version_info[2], sys.platform))
    print(QLibraryInfo.build())
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle(qVersion())
    window.resize(800, 480)
    window.show()
    sys.exit(app.exec())
