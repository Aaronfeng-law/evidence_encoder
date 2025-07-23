import sys  # 导入 sys 模块，用于与 Python 解释器交互

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QVBoxLayout, QPushButton, QHBoxLayout, QGridLayout # 从 PyQt5 中导入所需的类
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Example")  # 设置窗口标题为 "PyQt5 Example"
        
        # Central_widget = QWidget(self)
        # self.setCentralWidget(Central_widget)  # 将   标签设置为中心部件
        
        # vbox_layout = QVBoxLayout()
        
        # label = QLabel("This is a label")
        # vbox_layout.addWidget(label)
        
        # hbox_layout = QHBoxLayout()
        
        # button1 = QPushButton("Button 1")  # 创建一个按钮，文本为 "Button 1"
        # button2 = QPushButton("Button 2")  # 创建一个按钮，文本为 "Button 1"
        # hbox_layout.addWidget(button1)  # 将按钮添加到布局中
        # hbox_layout.addWidget(button2)
        2
        # vbox_layout.addLayout(hbox_layout)
        
        # Central_widget.setLayout(vbox_layout)
        
        layout = QGridLayout()
        
        layout.addWidget(QLabel("label 1"), 0, 0)
        layout.addWidget(QPushButton("Button 1"), 0, 1)
        layout.addWidget(QLabel("label 2"), 1, 0)
        layout.addWidget(QPushButton("Button 2"), 1, 1)
        
        self.setLayout(layout)
        
        
        
        
        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
        