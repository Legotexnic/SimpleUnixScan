from subprocess import Popen, PIPE
from io import StringIO


def cmdcall(command):
    proc = Popen(command, stdout=PIPE, stderr=PIPE, encoding="utf-8", shell=True)
    out, err = proc.communicate()
    return out.strip(), err.strip()


def module_logging_decorator(function):
    def print_log(self):
        if self.lvl >= 1:
            print("Start module " + self.name)
        function(self)
        if self.lvl >= 1:
            print("Finish module " + self.name)
    return print_log


def module_output_decorator(function):
    def print_delimiters(self):
        self.out.write("\n" + "#" * 100 + "\n" + "\n")
        self.out.write(" " * 25 + "Output module: " + self.name + "\n")
        self.out.write("-" * 100 + "\n" + "\n")
        function(self)
    return print_delimiters


class Module:
    def __init__(self):
        self.name = self.__class__.__name__
        self.message_container = None
        self.distr = None
        self.lvl = None
        self.out = StringIO()

    def prepare_module(self, distribution, logging_level):
        self.distr = distribution
        self.lvl = logging_level

    def finish_module(self, message_container, mutex):
        with mutex:
            message_container.append(self.out)
