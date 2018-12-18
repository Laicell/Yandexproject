import sys
from PyQt5.QtWidgets import *  # импорт всего из QtWidgets
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.Screen()

    def Screen(self):                      # Виджеты
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        self.mediaPlayer.setVolume(60)
        self.vol = 1

        # Создание кнопок
        self.playButton = QPushButton('Play')
        self.playButton.setEnabled(True)
        self.playButton.clicked.connect(self.play)  # play button

        self.pauseButton = QPushButton('Pause')  # pause button
        self.pauseButton.setEnabled(True)
        self.pauseButton.clicked.connect(self.pause)

        self.stopButton = QPushButton('Stop')  # pause button
        self.stopButton.setEnabled(True)
        self.stopButton.clicked.connect(self.stop)

        self.muteButton = QPushButton()
        self.muteButton.setEnabled(True)
        self.muteButton.setIcon(self.style().standardIcon
                                (QStyle.SP_MediaVolumeMuted))
        self.muteButton.clicked.connect(self.mute)

        # Слайдер
        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setRange(0, 100)
        self.volumeSlider.sliderMoved.connect(self.setVolume)

        # Открыть файл
        openAction = QAction(QIcon('open.png'), '&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open movie')
        openAction.triggered.connect(self.openFile)

        # Менюбар
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(openAction)

        # Создание виджета для содержимого окна
        wid = QWidget(self)
        self.setCentralWidget(wid)

        # Создание макета для размещения внутри окна
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.pauseButton)
        controlLayout.addWidget(self.stopButton)
        controlLayout.addWidget(self.positionSlider)
        controlLayout.addWidget(self.muteButton)
        controlLayout.addWidget(self.volumeSlider)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)

        wid.setLayout(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)

        self.mediaPlayer.setMedia(QMediaContent(QUrl('picture.jpg')))

        self.setWindowTitle('YandexPlayer')

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                                                  QDir.homePath())

        if fileName != '':
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)

    def play(self):
        if self.mediaPlayer.state() != QMediaPlayer.PlayingState:
            self.mediaPlayer.play()

    def pause(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()

    def stop(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.stop()
        else:
            self.mediaPlayer.stop()

    def mute(self):
        return self.mediaPlayer.setVolume(0)

    def setVolume(self, volume):
        self.mediaPlayer.setVolume(volume)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Exit', 'Закрыть YandexPlayer?',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            qApp.quit()
        else:
            try:
                event.ignore()
            except AttributeError:
                pass

    def mediaStateChanged(self, state):  # Значок play pause
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def positionVolume(self, position):
        self.volumeSlider.setValue(position)

    def durationVolume(self):
        self.volumeSlider.setRange(0, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    app.setStyleSheet("QToolTip { color: #ffffff;"
                      "background-color: #2a82da; border: 1px solid white; }")
    ex = MainWindow()
    ex.resize(640, 480)

    ex.show()
    sys.exit(app.exec_())