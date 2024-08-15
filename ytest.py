from PyQt6.QtWidgets import QApplication,  QWidget, QLabel, QPushButton, QVBoxLayout
import random
app = QApplication([])
 

window = QWidget()
window.setGeometry(100,100,200,200)
text1 = QLabel('Натисни, щоб дізнатися переможця')
text2 = QLabel('?')
button = QPushButton('Згенерувати')
layout =QVBoxLayout()
layout.addWidget(text1)
layout.addWidget(text2)
layout.addWidget(button)
window.setLayout(layout)

def click():
    n = random.randint(1, 100)
    text2.setText(str(n))

button.clicked.connect(click)
    

window.show()
app.exec()