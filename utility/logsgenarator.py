import inspect
import logging


class Loggen:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        file = logging.FileHandler(r'C:\Users\Dell\PycharmProjects\demoblaze\logs\demoblazelog.log')
        formatter = logging.Formatter('%(message)s : %(asctime)s  : %(lineno)s : %(funcName)s')
        logger.addHandler(file)
        file.setFormatter(formatter)
        return logger
