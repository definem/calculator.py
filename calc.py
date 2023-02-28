
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.value1 = ''
        self.value2 = ''
        self.operation = ''

        self.setWindowTitle("Calc.ex")
        self.setGeometry(100,100,200,300)
        self.setStyleSheet("background-color: #1C1C1C")
        
        #1-box

        self.h_box1 = QHBoxLayout()
        self.input = QLineEdit()
        self.input.setStyleSheet("background-color: white")
        self.h_box1.addWidget(self.input)

        #2-box

        self.h_box2 = QHBoxLayout()
        self.btn_AC = QPushButton('AC')
        self.btn_AC.setStyleSheet("background-color: white")  

        self.btn_divide = QPushButton('/')
        self.btn_divide.setStyleSheet("background-color: white")

        self.btn_percent = QPushButton('%')
        self.btn_percent.setStyleSheet("background-color: white")  

        self.btn_clear = QPushButton('\u232b')
        self.btn_clear.setStyleSheet("background-color: white")

        self.h_box2.addWidget(self.btn_AC)
        self.h_box2.addWidget(self.btn_divide)
        self.h_box2.addWidget(self.btn_percent)
        self.h_box2.addWidget(self.btn_clear)

        #3-box

        self.h_box3 = QHBoxLayout()
        self.btn_7 = QPushButton('7')
        self.btn_7.setStyleSheet("background-color: gray")

        self.btn_8 = QPushButton('8')
        self.btn_8.setStyleSheet("background-color: gray")

        self.btn_9 = QPushButton('9')
        self.btn_9.setStyleSheet("background-color: gray")

        self.btn_multiplication = QPushButton('x')
        self.btn_multiplication.setStyleSheet("background-color: #FF9500")

        self.h_box3.addWidget(self.btn_7) 
        self.h_box3.addWidget(self.btn_8)  
        self.h_box3.addWidget(self.btn_9)  
        self.h_box3.addWidget(self.btn_multiplication)

        #4-box

        self.h_box4 = QHBoxLayout()
        self.btn_4 = QPushButton('4')
        self.btn_4.setStyleSheet("background-color: gray")

        self.btn_5 = QPushButton('5')
        self.btn_5.setStyleSheet("background-color: gray")

        self.btn_6 = QPushButton('6')
        self.btn_6.setStyleSheet("background-color: gray")

        self.btn_minus = QPushButton('-')
        self.btn_minus.setStyleSheet("background-color: #FF9500")

        self.h_box4.addWidget(self.btn_4)  
        self.h_box4.addWidget(self.btn_5)  
        self.h_box4.addWidget(self.btn_6)  
        self.h_box4.addWidget(self.btn_minus)

        #5-box

        self.h_box5 = QHBoxLayout()
        self.btn_1 = QPushButton('1')
        self.btn_1.setStyleSheet("background-color: gray")

        self.btn_2 = QPushButton('2')
        self.btn_2.setStyleSheet("background-color: gray")

        self.btn_3 = QPushButton('3')
        self.btn_3.setStyleSheet("background-color: gray")
        
        self.btn_plus = QPushButton('+')
        self.btn_plus.setStyleSheet("background-color: #FF9500")

        self.h_box5.addWidget(self.btn_1)  
        self.h_box5.addWidget(self.btn_2) 
        self.h_box5.addWidget(self.btn_3)  
        self.h_box5.addWidget(self.btn_plus)

        #6-box

        self.h_box6 = QHBoxLayout()
        self.btn_0 = QPushButton('0')
        self.btn_0.setStyleSheet("background-color: #FF9500")

        self.btn_equal = QPushButton('=')
        self.btn_equal.setStyleSheet("background-color: #FF9500")

        self.btn_exit = QPushButton("exit")
        self.btn_exit.setStyleSheet("bacground-color: FFA500")

        self.btn_dot = QPushButton('.')
        self.btn_dot.setStyleSheet("background-color: #FF9500")  

        self.h_box6.addWidget(self.btn_0)  
        self.h_box6.addWidget(self.btn_equal)  
        self.h_box6.addWidget(self.btn_dot)
        self.h_box6.addWidget(self.btn_exit)

        self.v_box = QVBoxLayout()
        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)
        self.v_box.addLayout(self.h_box5)
        self.v_box.addLayout(self.h_box6)

        self.setLayout(self.v_box)

        self.btn_0.clicked.connect(lambda : self.on_click(self.sender().text()))
        self.btn_1.clicked.connect(lambda : self.on_click(self.sender().text()))
        self.btn_2.clicked.connect(lambda : self.on_click(self.sender().text()))
        self.btn_3.clicked.connect(lambda : self.on_click(self.sender().text()))
        self.btn_4.clicked.connect(lambda : self.on_click(self.sender().text()))
        self.btn_5.clicked.connect(lambda : self.on_click(self.sender().text()))
        self.btn_6.clicked.connect(lambda : self.on_click(self.sender().text()))
        self.btn_7.clicked.connect(lambda : self.on_click(self.sender().text()))
        self.btn_8.clicked.connect(lambda : self.on_click(self.sender().text()))
        self.btn_9.clicked.connect(lambda : self.on_click(self.sender().text()))
        self.btn_dot.clicked.connect(lambda : self.on_click(self.sender().text()))

        self.btn_AC.clicked.connect(self.ac_clicked)
        self.btn_clear.clicked.connect(self.ac_1by1_click)
        self.btn_exit.clicked.connect(self.exit_clicked)
        self.btn_plus.clicked.connect(lambda: self.operation_chosen("+"))
        self.btn_minus.clicked.connect(lambda: self.operation_chosen("-"))
        self.btn_divide.clicked.connect(lambda: self.operation_chosen("/"))
        self.btn_multiplication.clicked.connect(lambda: self.operation_chosen("*"))
        self.btn_percent.clicked.connect(lambda: self.operation_chosen("%"))
        self.btn_equal.clicked.connect(self.get_result)

        self.show()

    # metodla

    def on_click(self, number):
        if not self.operation:
            self.value1 += number
            self.input.setText(self.value1)
        else:
            self.value2 += number
            self.input.setText(self.value2)


    def ac_clicked(self):
        self.value1 = self.value2 = self.operation = ""
        self.input.setText(self.value1)
    

    def ac_1by1_click(self):
        if self.value1 and self.value2 == "":
            numbers = list(self.value1)
            numbers.pop(-1)
            self.value1 = ''.join(numbers)
            self.input.setText(self.value1)
        elif self.value1 != "" and self.value2 != "":
            numbers = list(self.value2)
            numbers.pop(-1)
            self.value2 = ''.join(numbers)
            self.input.setText(self.value2)



    def get_result(self):
        if self.operation == "+":
            self.value1 = str(float(self.value1) + float(self.value2))
            self.value2 = self.operation = ""
            self.value_1()
        elif self.operation == "-":
            self.value1 = str(float(self.value1) - float(self.value2))
            self.value2 = self.operation = ""
            self.value_1()
        elif self.operation == "/":
            self.value1 = str(float(self.value1) / float(self.value2))
            self.value2 = self.operation = ""
            self.value_1()
        elif self.operation == "*":
            self.value1 = str(float(self.value1) * float(self.value2))
            self.value2 = self.operation = ""
            self.value_1()
        else:
            if self.value1 and self.value2 == "":
                self.value1 = str(float(self.value1) / 100)
                self.value2 = self.operation = ""
                self.value_1()
            else:
                error = "Malformed expression"
                self.input.setText(error)
                self.value1 = self.value2 = self.operation = ""

    def value_1(self):
        if str(self.value1).split(".")[-1] == "0":
            self.value1 = self.value1.split(".")[0]
        self.input.setText(self.value1)

    def operation_chosen(self, oper):
        self.operation = oper
        self.value2 = ""

    def exit_clicked() -> None:
        sys.exit()


app = QApplication([])
win = Window()
sys.exit(app.exec_())
