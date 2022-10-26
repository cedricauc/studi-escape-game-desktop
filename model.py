from config import Config
from utils import Util


class Model(Config):
    def __init__(self):
        super().__init__()
        self.connect()

    def getData(self, day=None):
        params = [Util.day_beginning(day), Util.day_end(day)]

        statement = "SELECT " \
                    "s.title, " \
                    "b.participant, " \
                    "g.start_time, " \
                    "g.end_time, " \
                    "s.duration, " \
                    "b.start_hour, " \
                    "b.start_minutes, " \
                    "b.end_hour, " \
                    "b.end_minutes, " \
                    "b.in_progress, " \
                    "b.is_complete " \
                    "FROM booking as b " \
                    "INNER JOIN game as g ON b.game_id = g.id " \
                    "INNER JOIN scenario as s ON g.scenario_id = s.id " \
                    "WHERE g.start_time> %s AND g.end_time< %s "

        return self.prepare(statement, params)
