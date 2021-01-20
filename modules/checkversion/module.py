from utils.utils import *
import os


class CheckVersion(Module):
    @module_logging_decorator
    @module_output_decorator
    def exec_module(self):
        out = os.uname()
        self.out.write("Имя ядра: " + out.sysname + "\n")
        self.out.write("Имя хоста: " + out.nodename + "\n")
        self.out.write("Выпуск ядра: " + out.release + "\n")
        self.out.write("Версия ядра: " + out.version + "\n")
        self.out.write("Название архитектуры машины: " + out.machine + "\n")


def get_module():
    return CheckVersion()
