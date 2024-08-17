from PyQt5.QtWidgets import QApplication,  QWidget, QLabel, QRadioButton, QPushButton, QButtonGroup, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
app = QApplication([])


window = QWidget()
window.setGeometry(100,100,200,200)

text = QLabel('Яка столиця США?')
btn_answer1 = QRadioButton('Нью-Йорк')
btn_answer2 = QRadioButton('Вашигтон')
btn_answer3 = QRadioButton('Маямі')
btn_answer4 = QRadioButton('Сан-Франциско')

button_check = QPushButton('перевіти')
v_layout = QVBoxLayout()
h_layout1 = QHBoxLayout()
h_layout2 = QHBoxLayout()

h_layout1.addWidget(btn_answer1)
h_layout1.addWidget(btn_answer2)
h_layout2.addWidget(btn_answer3)
h_layout2.addWidget(btn_answer4)
v_layout.addWidget(text)
v_layout.addLayout(h_layout1)
v_layout.addLayout(h_layout2)
v_layout.addWidget(button_check)
window.setLayout(v_layout)
def show_win():
    win = QMessageBox()
    win.setText('ріспєкт!! Столиця США це Вашигтон!!!!!!!')

def click():
    if btn_answer2.isChecked():
        show_win()



button_check.connect(click)

window.show()
app.exec()