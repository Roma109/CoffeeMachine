import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QApplication


class CoffeeMachine(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("films_db.sqlite")
        self.pushButton.clicked.connect(self.select_data)
        self.textEdit.setPlainText("SELECT * FROM films")
        self.select_data()

    def select_data(self):
        # Получим результат запроса,
        # который ввели в текстовое поле
        query = self.textEdit.toPlainText()
        res = self.connection.cursor().execute(query).fetchall()
        # Заполним размеры таблицы
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        # При закрытии формы закроем и наше соединение
        # с базой данных
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffeeMachine()
    ex.show()
    sys.exit(app.exec())
