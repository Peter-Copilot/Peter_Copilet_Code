import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = '登录/注册'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)

        self.label_username = QLabel('用户名', self)
        self.label_username.move(20, 20)
        self.textbox_username = QLineEdit(self)
        self.textbox_username.move(80, 20)
        self.textbox_username.resize(200, 20)

        self.label_password = QLabel('密码', self)
        self.label_password.move(20, 50)
        self.textbox_password = QLineEdit(self)
        self.textbox_password.move(80, 50)
        self.textbox_password.resize(200, 20)

        self.button_login = QPushButton('登录', self)
        self.button_login.move(20, 80)
        self.button_login.clicked.connect(self.on_click_login)

        self.button_register = QPushButton('注册', self)
        self.button_register.move(120, 80)
        self.button_register.clicked.connect(self.on_click_register)

        self.show()

    @pyqtSlot()
    def on_click_login(self):
        username = self.textbox_username.text()
        password = self.textbox_password.text()
        with open('Users.md', 'r') as f:
            users = f.readlines()
        if f'{username} {password}\n' in users:
            QMessageBox.question(self, '成功', '登录成功', QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.question(self, '错误', '用户名或密码错误', QMessageBox.Ok, QMessageBox.Ok)

    @pyqtSlot()
    def on_click_register(self):
        username = self.textbox_username.text()
        password = self.textbox_password.text()
        with open('Users.md', 'r') as f:
            users = f.readlines()
        if f'{username} {password}\n' in users:
            QMessageBox.question(self, '错误', '用户已存在', QMessageBox.Ok, QMessageBox.Ok)
        else:
            with open('Users.md', 'a') as f:
                f.write(f'{username} {password}\n')
            QMessageBox.question(self, '成功', '注册成功', QMessageBox.Ok, QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
