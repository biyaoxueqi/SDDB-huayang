import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui
# from EcuLog import EcuLog, SwDIDMap, EcuAddressMap
import json

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Read DIDs")

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "中国人"]
        self.button1 = QtWidgets.QPushButton("Select Log File!")
        self.button2 = QtWidgets.QPushButton('Read out DIDs!')
        self.text = QtWidgets.QLabel("Read ME:\nStep1: Select the log file;\nStep2: Read DID and then Create .json file")
        # self.text.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.setLayout(self.layout)

        self.button1.clicked.connect(self.selectTargetFile)
        self.button2.clicked.connect(self.readDids)

    def selectTargetFile(self):
        # path = QtWidgets.QFileDialog.getExistingDirectory(self, '选择文件', './')
        path = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', './')
        print(path[0])
        self.targetFile = path[0]
        self.text.setText("The following log file is selected:\n{0}".format(self.targetFile))

    def readDids(self):
        # eculog = EcuLog()
        # eculog.getResponseList(self.targetFile)
        # eculog.createStorage()
        # ecuBom = {}
        # for ecuName in EcuAddressMap:
        #     ecuBom[ecuName] = eculog.getF1AEbyName(ecuName)
        #     for swDID in SwDIDMap:
        #         ecuBom[ecuName].update(eculog.getNumberByName(ecuName, swDID))
        
        with open('swBOM.json', 'w') as f:
            json.dump(ecuBom, f, indent=4)
        self.text.setText("Read sucessfully and swBOM.json is generated!")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(400,300)
    widget.show()

    sys.exit(app.exec_())
