import random

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

from FramelessWindow import FramelessWindow  # Для того что бы убрать верхнюю панель и добавить туда кнопку
from equalizer_bar.equalizer_bar import EqualizerBar

from My_styles import *
from Radio_db import *


class Radio(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(Radio, self).__init__(*args, **kwargs)
        # Создание и настройка окна без рамок

        self.objectTitleBar = args[0].titleBar
        self.MainWindow = args[0]
        self.MainWindow.setWindowTitle("<b>Радио</b>")
        self.MainWindow.setWindowIcon(QtGui.QIcon('images/icon.png'))

        # Вспомогательные переменные
        self.now_style = None  # Определяет нынешний стиль night/day или None
        self.stl = ""  # Переменная для стилей(по умолчанию ночная тема)
        self.form_list = None
        self.open_add_l = False  # Открыта ли вкладка добавления радиостанции
        self.playing_radio = False  # Играет ли сейчас что-либо
        self.added_radio = []
        self.form_dic_added = {}  # Форма для создания кнопок снизу
        self.dic = {}
        self.added_radio_dic = {}  # Добавленные радиостанции
        self._def_radio_dic = {}  # Радиостанции по умолчанию

        # Выполнение функций инициализации и установка стилей
        self.radio_init()  # Инициализация всех встроенных радиостанций
        self.init_ui()  # Инициализация всех элементов интерфейса
        self.ui_setting()  # Установка всех параметров интерфейса

        self.set_style(self.objectTitleBar)  # Установка всех стилей интерфейса(Ночная тема по умолчанию)

    def init_ui(self):
        # Инициализация всех элементов интерфейса
        self.vbox = QtWidgets.QVBoxLayout(self)
        self.vbox1 = QtWidgets.QVBoxLayout(self)
        self.vbox2 = QtWidgets.QVBoxLayout(self)
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.hbox1 = QtWidgets.QHBoxLayout(self)
        self.label3 = QtWidgets.QLabel(self)  # Радиостанции по умолчанию
        self.form = self.form_def_radio(self._def_radio_dic)

        self.display = QtWidgets.QLCDNumber(self)
        self.label2 = QtWidgets.QLabel(self)  # Громкость
        self.label1 = QtWidgets.QLabel(self)
        self.label5 = QtWidgets.QLabel(self)  # Нынешняя радиостанция
        self.volume_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.volume = self.volume_slider.value()

        self.play_btn = QtWidgets.QPushButton("Пуск", self)

        self.add_radio_btn = QtWidgets.QPushButton("Добавить радиостанцию", self)

        self.equalizer = EqualizerBar(7, ['#0C0786', '#40039C', '#6A00A7', '#8F0DA3', '#B02A8F', '#CA4678', '#E06461',
                                          '#F1824C', '#FCA635', '#FCCC25', '#EFF821'])

    def radio_create(self, url):
        name = QMediaPlayer(self, QMediaPlayer.StreamPlayback)
        name.setMedia(QMediaContent(QtCore.QUrl(url)))
        return name

    def set_style(self, obj):
        if self.now_style != "night" or None:
            self.stl = "* {background-color: black; color: white;}"
            self.setStyleSheet("* {background-color: black;}")
            self.label3.setStyleSheet(self.stl)
            self.label5.setStyleSheet(self.stl)
            for i in self.dic:
                self.dic[i][1].setStyleSheet(self.stl)
            for i in self.form_dic_added:
                self.form_dic_added[i][1].setStyleSheet(self.stl)
            if len(self.added_radio_dic) > 0:
                self.label4.setStyleSheet('color: white')
            self.play_btn.setStyleSheet("* {color: white; border: 1px solid white; padding: 3px;}")
            self.add_radio_btn.setStyleSheet("* {color: white; border: 1px solid white; padding: 3px;}")
            if self.form_list is not None:
                self.add_new_radio(new_style=True)
            self.label1.setStyleSheet(self.stl)
            self.label2.setStyleSheet(self.stl)
            self.display.setStyleSheet("* {color: white; border: none; margin: 0px; padding: 0px}")
            self.volume_slider.setStyleSheet(SLIDERS_STYLE_NIGHT)
            self.equalizer.setColors(EQUALIZER_NIGHT)
            self.equalizer.setBackgroundColor('black')

            self.MainWindow.setStyleSheet("* {background-color: black;}")
            obj.titleLabel.setStyleSheet("* {color: white;}")
            obj.now_date_label.setStyleSheet(self.stl)
            obj.setStyleSheet("* {background-color: black;}")
            obj.buttonMinimum.setStyleSheet(self.stl)
            obj.buttonMy.setStyleSheet(self.stl)
            obj.buttonMaximum.setStyleSheet(self.stl)
            obj.buttonClose.setStyleSheet(self.stl)
            obj.shazam_btn.setStyleSheet(self.stl)

            self.now_style = "night"

        elif self.now_style != "day":
            self.stl = "* {background-color: white; color: black; border: none;}"
            self.setStyleSheet("* {background-color: white;}")
            for i in self.dic:
                self.dic[i][1].setStyleSheet(self.stl)
            for i in self.form_dic_added:
                self.form_dic_added[i][1].setStyleSheet(self.stl)
            if len(self.added_radio_dic) > 0:
                self.label4.setStyleSheet('color: black')

            self.play_btn.setStyleSheet(
                "* {background-color: white; color: black; border: 1px solid black; padding: 3px;}")
            self.add_radio_btn.setStyleSheet("* {color: black; border: 1px solid black; padding: 3px;}")
            if self.form_list is not None:
                self.add_new_radio(new_style=True)
            self.label1.setStyleSheet(self.stl)
            self.label2.setStyleSheet(self.stl)
            self.label3.setStyleSheet(self.stl)
            self.label5.setStyleSheet(self.stl)
            self.display.setStyleSheet(
                "* {background-color: white; color: black; border: none; margin: 0px; padding: 0px}")
            self.volume_slider.setStyleSheet(SLIDERS_STYLE_DAY)
            self.equalizer.setColors(EQUALIZER_DAY)
            self.equalizer.setBackgroundColor('white')

            self.MainWindow.setStyleSheet("* {background-color: white;}")
            obj.setStyleSheet("* {background-color: white;}")
            obj.titleLabel.setStyleSheet(self.stl)
            obj.now_date_label.setStyleSheet(self.stl)
            obj.buttonMinimum.setStyleSheet(self.stl)
            obj.buttonMy.setStyleSheet(self.stl)
            obj.buttonMaximum.setStyleSheet(self.stl)
            obj.buttonClose.setStyleSheet(self.stl)
            obj.shazam_btn.setStyleSheet(self.stl)
            self.now_style = "day"

    def radio_init(self):
        db_def_radio_dict = {96.3: ['http://icecast.vgtrk.cdnvideo.ru/vestifm_mp3_192kbps', "радио 'Вести'"],
                             103.0: ['http://chanson.hostingradio.ru:8041/chanson256.mp3', "радио 'Шансон'"],
                             104.3: ['https://dfm.hostingradio.ru/dfm128.mp3', "радио 'DFM'"],
                             99.1: ["https://pub0301.101.ru:8443/stream/air/mp3/256/102", "радио 'Юмор FM'"],
                             94.9: ["https://pub0301.101.ru:8443/stream/air/mp3/256/200", "радио 'Relax FM'"],
                             87.9: ["https://pub0301.101.ru:8443/stream/air/mp3/256/219", "радио 'Like FM'"],
                             89.1: ['https://nashe1.hostingradio.ru:80/jazz-128.mp3', "радио 'JAZZ FM'"],
                             100.3: ["http://ep256.hostingradio.ru:8052/europaplus256.mp3", 'радио "Европа плюс"'],
                             102.3: ['http://dor2server.streamr.ru:8000/dorognoe1945.mp3', '"Дорожное радио"'],
                             105.3: ['http://retroserver.streamr.ru:8043/retro256.mp3', 'радио "Ретро FM"'],
                             105.7: ['http://icecast.vgtrk.cdnvideo.ru/mayakfm_mp3_192kbps', 'радио "Маяк"'],
                             99.5: ['https://radio-holding.ru:9433/marusya_default', 'радио "Маруся Fm"']}
        for i in db_def_radio_dict:
            url = db_def_radio_dict[i][0]
            name = db_def_radio_dict[i][1]
            self._def_radio_dic[i] = [self.radio_create(url), name]

        con = sql_con("radioDataBase.db")
        sql_table(con, 'default_radio')
        insert_func(con, db_def_radio_dict, 'default_radio')
        sql_table(con, 'added_radio')

    def ui_setting(self):
        # Настройка всех элементов интерфейса
        font = self.display.font()
        font.setBold(True)

        self.objectTitleBar.buttonMy.clicked.connect(self.new_style_btn)

        self.display.setFont(font)
        self.display.display("88.0")
        self.display.setNumDigits(5)
        self.display.setSegmentStyle(QtWidgets.QLCDNumber.Flat)

        self.label2.setText("FM")
        self.label2.setFont(font)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)

        self.label5.setText('Выберете радиостанцию')
        self.label5.setFont(font)
        self.label5.setAlignment(QtCore.Qt.AlignCenter)

        self.label1.setText("Громкость")
        self.label1.setFont(font)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)

        self.volume_slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.volume_slider.valueChanged[int].connect(self.change_volume)
        self.volume_slider.setValue(100)

        self.play_btn.clicked.connect(self.play)

        self.add_radio_btn.clicked.connect(self.add_new_radio)

        self.label3.setText('Доступные радиостанции')

        self.equalizer.setDecayFrequencyMs(0)
        self.equalizer.setValues([15, 30, 45, 60, 75, 90, 100])

        self._timer = QtCore.QTimer()
        self._timer.setInterval(100)
        self._timer.timeout.connect(self.update_eq_values)

        # Добавление всех элементов в их ячейки
        self.hbox.addWidget(self.play_btn)
        self.hbox1.addLayout(self.form)
        if check_added_radio() is True:
            self.cr_added_radio_dic()
            self.label4 = QtWidgets.QLabel('Добавленные радиостанции', self)
            self.form2 = self.form_added_radio()
            self.hbox1.addLayout(self.form2)

        self.vbox.addWidget(self.display)
        self.vbox.addWidget(self.label2)
        self.vbox.addWidget(self.label5)
        self.vbox.addWidget(self.equalizer)
        self.vbox.addWidget(self.label1)
        self.vbox.addWidget(self.volume_slider)
        self.vbox.addLayout(self.hbox)
        self.vbox1.addWidget(self.add_radio_btn)
        self.vbox.addLayout(self.vbox1)
        self.vbox.addLayout(self.hbox1)
        self.setLayout(self.vbox)

    def new_style_btn(self):
        self.set_style(self.objectTitleBar)

    def set_fm(self):
        # Функция для того что бы при нажатии на частоту снизу включалась соответсвующая станция
        self.display.display(float(self.sender().text().split('F')[0]))
        if self.play_btn.text() == "Пауза":
            self.play_btn.setText("Пуск")
            for i in self._def_radio_dic.items():
                i[1][0].pause()
            for i in self.added_radio_dic.items():
                i[1][0].pause()
        self.play()

    def change_volume(self, volume):
        for i in self._def_radio_dic.items():
            i[1][0].setVolume(volume)
        if len(self.added_radio_dic) > 0:
            for i in self.added_radio_dic.items():
                i[1][0].setVolume(volume)

    def update_eq_values(self):
        self.equalizer.setValues([
            min(100, v+random.randint(0, 50) if random.randint(0, 5) > 2 else v)
            for v in self.equalizer.values()
            ])

    def play(self):
        if self.play_btn.text() == "Пуск":
            self.play_btn.setText("Пауза")
            self._timer.start()
            self.equalizer.setDecayFrequencyMs(100)
            if self.display.value() in self._def_radio_dic:
                self._def_radio_dic[self.display.value()][0].play()
                self.playing_radio = True
                self.label5.setText(f"Сейчас играет: {self._def_radio_dic[self.display.value()][1]}")

            elif self.display.value() in self.added_radio_dic:
                self.added_radio_dic[self.display.value()][0].play()
                self.playing_radio = True
                self.label5.setText(f"Сейчас играет: {self.added_radio_dic[self.display.value()][1]}")

            else:
                self.play_btn.setText("Пуск")
                self._timer.stop()
                self.equalizer.setDecayFrequencyMs(0)

        else:
            self.play_btn.setText("Пуск")
            for i in self._def_radio_dic.items():
                i[1][0].pause()

            for i in self.added_radio_dic.items():
                i[1][0].pause()
            self.label5.setText(f"Выберете радиостанцию")
            self._timer.stop()
            self.equalizer.setDecayFrequencyMs(0)

    def radio_database(self, radio_settings):
        con = sql_con("radioDataBase.db")
        sql_table(con, 'added_radio')
        fm_is_new = check(con, 'added_radio', radio_settings[0])
        if fm_is_new is True:
            sql_create(con, 'added_radio', radio_settings)
        else:
            error = QtWidgets.QMessageBox(self)
            error.setStyleSheet("* {background-color: white;}")
            error.setWindowTitle("Ошибка")
            error.setText('<h2><font color="red";>Данная частота уже занята!</font></h2>')
            error.addButton('Окей', QtWidgets.QMessageBox.AcceptRole)
            error.show()

    def add_new_radio(self, new_style=False):
        if new_style is False:  # Что бы при нажатии кнопки смены стилей стили в этом окне тоже менялись
            if self.open_add_l is False:
                # Создаю всплывающее поле для заполнения информации
                self.form_add_radio = QtWidgets.QFormLayout(self)
                self.name_lbl = QtWidgets.QLabel("Введите название радиостанции", self)
                self.url_lbl = QtWidgets.QLabel("Введите URL(ссылку) радиостанции", self)
                self.fm_lbl = QtWidgets.QLabel("Введите частоту(fm) радиостанции", self)
                self.name_lne = QtWidgets.QLineEdit(self)
                self.url_lne = QtWidgets.QLineEdit(self)
                self.fm_lne = QtWidgets.QDoubleSpinBox(self)
                self.fm_lne.setMinimum(87)
                self.fm_lne.setMaximum(110)
                self.save_btn = QtWidgets.QPushButton("Добавить", self, clicked=self.save_new_radio)
                if self.now_style == "night" or None:
                    self.name_lbl.setStyleSheet("* {background-color: black; color: white;}")
                    self.url_lbl.setStyleSheet("* {background-color: black; color: white;}")
                    self.fm_lbl.setStyleSheet("* {background-color: black; color: white;}")
                    self.name_lne.setStyleSheet("* {border: 1px solid white; color: white;}")
                    self.url_lne.setStyleSheet("* {border: 1px solid white; color: white;}")
                    self.fm_lne.setStyleSheet("* {border: 1px solid white; color: white;}")
                    self.save_btn.setStyleSheet("* {color: white; border: 1px solid white; padding: 3px;}")
                else:
                    self.name_lbl.setStyleSheet("* {background-color: white; color: black;}")
                    self.url_lbl.setStyleSheet("* {background-color: white; color: black;}")
                    self.fm_lbl.setStyleSheet("* {background-color: white; color: black;}")
                    self.name_lne.setStyleSheet("* {border: 1px solid black; color: black;}")
                    self.url_lne.setStyleSheet("* {border: 1px solid black; color: black;}")
                    self.fm_lne.setStyleSheet("* {border: 1px solid black; color: black;}")
                    self.save_btn.setStyleSheet("* {border: 1px solid black; padding: 3px; color: black;}")

                self.form_list = [self.name_lne, self.name_lbl, self.url_lne,
                                  self.url_lbl, self.fm_lne, self.fm_lbl, self.save_btn]

                for i in range(0, len(self.form_list), 2):
                    if self.form_list[i] != self.save_btn:
                        self.form_add_radio.addRow(self.form_list[i + 1], self.form_list[i])
                self.form_add_radio.addRow(self.save_btn)
                vbox3 = QtWidgets.QVBoxLayout(self)
                vbox3.addLayout(self.form_add_radio)
                self.vbox1.addLayout(vbox3)
                self.open_add_l = True
                self.add_radio_btn.setText('Свернуть')

            elif self.open_add_l is True:
                for i in self.form_list:
                    i.deleteLater()
                self.form_add_radio.deleteLater()
                self.open_add_l = False
                self.add_radio_btn.setText('Добавить радиостанцию')

        elif self.open_add_l is True:
            if self.now_style != "night":
                self.name_lbl.setStyleSheet("* {background-color: black; color: white;}")
                self.url_lbl.setStyleSheet("* {background-color: black; color: white;}")
                self.fm_lbl.setStyleSheet("* {background-color: black; color: white;}")
                self.name_lne.setStyleSheet("* {border: 1px solid white; color: white;}")
                self.url_lne.setStyleSheet("* {border: 1px solid white; color: white;}")
                self.fm_lne.setStyleSheet("* {border: 1px solid white; color: white;}")
                self.save_btn.setStyleSheet("* {border: 1px solid white; padding: 3px; color: white; }")
            else:
                self.name_lbl.setStyleSheet("* {background-color: white; color: black;}")
                self.url_lbl.setStyleSheet("* {background-color: white; color: black;}")
                self.fm_lbl.setStyleSheet("* {background-color: white; color: black;}")
                self.name_lne.setStyleSheet("* {border: 1px solid black; color: black;}")
                self.url_lne.setStyleSheet("* {border: 1px solid black; color: black;}")
                self.fm_lne.setStyleSheet("* {border: 1px solid black; color: black;}")
                self.save_btn.setStyleSheet("* {border: 1px solid black; padding: 3px; color: black;}")

    def update_form(self, inf_added_dict):
        url = inf_added_dict[2]
        name = inf_added_dict[1]
        fm = inf_added_dict[0]
        lbl = QtWidgets.QLabel(name)
        fm_btn = QtWidgets.QPushButton(f"{fm} Fm")
        fm_btn.setStyleSheet('* {border: none; color: blue}')
        fm_btn.clicked.connect(self.set_fm)
        if self.now_style == 'night' or None:
            lbl.setStyleSheet('"* {background-color: black; color: white;}"')
        self.form2.addRow(fm_btn, lbl)
        self.added_radio_dic[fm] = [self.radio_create(url), name]
        self.form_dic_added[f'btn' + str(len(self.form_dic_added) + 1)] = [fm_btn, lbl]

    def save_new_radio(self):
        if self.url_lne.text() == "" or self.name_lne.text() == "":
            pass

        elif round(float(self.fm_lne.value()), 2) in self._def_radio_dic:
            error = QtWidgets.QMessageBox(self)
            error.setStyleSheet("* {background-color: white;}")
            error.setWindowTitle("Ошибка")
            error.setText('<h2><font color="red";>Введенная вами частота уже занята!</font></h2>')
            error.addButton('Окей', QtWidgets.QMessageBox.AcceptRole)
            error.show()

        else:
            dct = [round(float(self.fm_lne.value()), 2), self.name_lne.text(), self.url_lne.text()]
            con = sql_con("radioDataBase.db")
            sql_table(con, 'added_radio')
            flag = add_insert_func(con, dct, 'added_radio', True)
            if flag is True:
                error = QtWidgets.QMessageBox(self)
                error.setStyleSheet("* {background-color: white;}")
                error.setWindowTitle("Ошибка")
                error.setText('<h2><font color="red";>Вы уже добавляли радио с такой частотой!</font></h2>')
                error.addButton('Окей', QtWidgets.QMessageBox.AcceptRole)
                error.show()
            else:
                self.update_form(dct)
            for i in self.form_list:
                i.deleteLater()
            self.form_add_radio.deleteLater()
            self.open_add_l = False

    def form_def_radio(self, radio_dct):
        # Заполнение текстового поля снизу
        form = QtWidgets.QFormLayout(self)
        form.addWidget(self.label3)
        i = 0
        for v in radio_dct:
            lbl = QtWidgets.QLabel(radio_dct[v][1])
            self.dic["btn" + str(i)] = [QtWidgets.QPushButton(f"{v} Fm"), lbl]
            self.dic["btn" + str(i)][0].setStyleSheet('* {border: none; color: blue}')
            self.dic["btn" + str(i)][0].clicked.connect(self.set_fm)
            form.addRow(self.dic["btn" + str(i)][0], lbl)

            i += 1
        return form

    def cr_added_radio_dic(self):
        con = sql_con('radioDataBase.db')
        curs = con.cursor()
        curs.execute('SELECT * FROM added_radio')
        dct = curs.fetchall()
        self.added_radio_dic = {}
        for i in dct:
            name = i[1]
            fm = i[2]
            url = i[3]
            self.added_radio_dic[fm] = [self.radio_create(url), name]

    def form_added_radio(self):
        form = QtWidgets.QFormLayout(self)
        form.addWidget(self.label4)

        i = 0
        for k in self.added_radio_dic:
            lbl = QtWidgets.QLabel(self.added_radio_dic[k][1])
            self.form_dic_added["btn" + str(i)] = [QtWidgets.QPushButton(f"{k} Fm"), lbl]
            self.form_dic_added["btn" + str(i)][0].setStyleSheet('* {border: none; color: blue}')
            self.form_dic_added["btn" + str(i)][0].clicked.connect(self.set_fm)
            form.addRow(self.form_dic_added["btn" + str(i)][0], lbl)

            i += 1
        return form


if __name__ == "__main__":
    from sys import argv, exit
    from PyQt5.QtWidgets import QApplication

    app = QApplication(argv)
    desktop = QtWidgets.QApplication.desktop()
    w = FramelessWindow()  # Модуль для создания окон без рамок
    w.setWidget(Radio(w))  # Добавить свое окно
    w.resize(400, 590)
    w.show()
    exit(app.exec_())
