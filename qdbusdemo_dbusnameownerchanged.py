import sys
from PySide6.QtWidgets import QMainWindow
from PySide6 import QtDBus, QtCore
from PySide6.QtCore import QLibraryInfo, qVersion, Slot
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        service = "org.freedesktop.DBus"
        path = "/org/freedesktop/DBus"
        iface = "org.freedesktop.DBus"
        conn = QtDBus.QDBusConnection.systemBus()

        #without this, the conn.connect call hangs, seems to be a bug, is already reported and fixed.
        conn.registerObject('/', self)

        conn.connect(service, path, iface, "NameOwnerChanged", self, QtCore.SLOT("nameownerchanged(QString, QString, QString)"))    
        pass

    @Slot(str, str, str)
    def nameownerchanged(self, arg1:str, arg2:str, arg3:str) -> None:
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
