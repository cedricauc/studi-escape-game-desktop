from datetime import datetime


class Util:
    @staticmethod
    def day_beginning(dt=None):
        """
        Retourne le début de la journée
        """
        if not dt:
            dt = datetime.today()

        return dt.replace(hour=0, minute=0, second=0, microsecond=0)

    @staticmethod
    def day_end(dt=None):
        """
        Retourne la fin de la journée
        """
        if not dt:
            dt = datetime.today()

        return dt.replace(hour=23, minute=59, second=0, microsecond=0)

    @staticmethod
    def time_diff(start, end):
        start_dt = datetime.strptime(start, '%H:%M')
        end_dt = datetime.strptime(end, '%H:%M')
        diff = (end_dt - start_dt)
        return diff.seconds / 3600
