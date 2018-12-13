import sys
from os.path import expanduser
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.player = QMediaPlayer()
        self.userAction = -1  # 0- стоп, 1- проигрывать 2-пауза
        self.player.setVolume(60) #Начальное кол-во единиц громкости


        self.Screen()

    def Screen(self):                      #Функция, которая создаёт окно программы
        self.setWindowTitle('YandexPlayer')
        controlBar = self.addControls()
        centralWidget = QWidget()
        centralWidget.setLayout(controlBar)
        self.setCentralWidget(centralWidget)
        self.resize(200, 100)
        self.show()


    def createToolbar(self):
        pass


    def addControls(self):
        controlArea = QVBoxLayout()  # Центральный виджет
        seekSliderLayout = QHBoxLayout()
        controls = QHBoxLayout()
        playlistCtrlLayout = QHBoxLayout()

        # Создание кнопок
        playBtn = QPushButton('Play')  # play button
        pauseBtn = QPushButton('Pause')  # pause button
        stopBtn = QPushButton('Stop')  # stop button







        # Горизонтальный макет
        controls.addWidget(playBtn)
        controls.addWidget(pauseBtn)
        controls.addWidget(stopBtn)



        # Вертикальный макет
        controlArea.addLayout(seekSliderLayout)
        controlArea.addLayout(controls)
        controlArea.addLayout(playlistCtrlLayout)
        return controlArea


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())