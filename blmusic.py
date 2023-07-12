import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import QTimer
import bluetooth

class BluetoothController(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

      
        self.timer = QTimer(self)
       
        self.timer.setInterval(2000)
        
        self.timer.timeout.connect(self.disconnectBluetooth)
        
        self.timer.start()

    def initUI(self):
        self.target_device_address_entry = QLineEdit(self)
        self.target_device_address_entry.move(50, 20)
        self.target_device_address_entry.resize(200, 30)

        disconnectBtn = QPushButton('قطع اتصال', self)
        disconnectBtn.clicked.connect(self.disconnectBluetooth)
        disconnectBtn.resize(disconnectBtn.sizeHint())
        disconnectBtn.move(50, 70)

        self.setGeometry(300, 300, 300, 120)
        self.setWindowTitle('کنترل بلوتوث')

    def disconnectBluetooth(self):
        try:
            target_device_address = self.target_device_address_entry.text()
            bt_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            bt_socket.connect((target_device_address, 1))
            bt_socket.close()
            QMessageBox.information(self, 'پیغام', 'اتصال بلوتوث قطع شد.')
        except bluetooth.btcommon.BluetoothError as error:
            print("hello")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BluetoothController()
    window.show()
    sys.exit(app.exec_())
