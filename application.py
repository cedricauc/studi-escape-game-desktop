from datetime import datetime

from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QMainWindow, QTreeWidgetItem, QHeaderView
from PyQt5.QtCore import QDate
from pui.interface import Ui_MainWindow
from model import Model
from utils import Util


class AppWindow(Ui_MainWindow, QMainWindow):
    model = Model()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_app()
        self.setup_links()
        self.load_items()

    def setup_app(self):
        self.setWindowTitle("Paradox Escape Game")

        self.dateEdit.setDate(QDate.currentDate())

        header = self.booking.header()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

    def setup_links(self):
        self.dateEdit.dateChanged.connect(self.change_date)

    def load_items(self, dt=None):

        self.booking.clear()

        rows = self.model.getData(dt)

        for title, participant, start_time, end_time, duration, start_hour, start_minutes, end_hour, end_minutes, \
                in_progress, is_complete in rows:
            scenario = QTreeWidgetItem()
            scenario.setText(0, title)
            scenario.setText(1, str(participant))
            scenario.setText(2, "{:d}:{:02d}".format(start_time.hour, start_time.minute))
            scenario.setText(3, "{:d}:{:02d}".format(end_time.hour, end_time.minute))

            try:
                current_duration = Util.time_diff("{}:{}".format(start_hour, start_minutes),
                                                  "{}:{}".format(end_hour, end_minutes))
            except ValueError:
                current_duration = 0

            item_duration = QTreeWidgetItem()
            item_duration.setText(0, "Durée séance: {}h".format(duration))

            item_time_exceed = QTreeWidgetItem()
            exceed_time = current_duration - float(duration) if current_duration - float(duration) > 0 else 0
            item_time_exceed.setText(0, "Temps supplémentaire: {}h".format(exceed_time))

            for i in range(4):
                if current_duration > duration:
                    scenario.setBackground(i, QBrush(QColor(236, 78, 32)))
                elif is_complete:
                    scenario.setBackground(i, QBrush(QColor(1, 111, 185)))
                else:
                    scenario.setBackground(i, QBrush(QColor(109, 211, 206)))

            scenario.addChild(item_duration)
            scenario.addChild(item_time_exceed)
            self.booking.addTopLevelItem(scenario)

    def change_date(self, item: QDate):
        dt = item.toPyDate()
        dt_time = datetime.combine(dt, datetime.min.time())
        self.load_items(dt_time)
