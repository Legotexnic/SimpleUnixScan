from utils.utils import *


class CheckNet(Module):
    @module_logging_decorator
    @module_output_decorator
    def exec_module(self):
        out, _ = cmdcall("ss -anp |grep -v \"* 0\" |grep -v WAIT")
        self.out.write("Check these ports in /etc/services to see what they are.\nClose all ports you do not \
need.\n\nPorts listening on this system:\nProtocol\tPort\n")
        for line in out:
            self.out.write(line)
        self.out.write("\n")


def get_module():
    return CheckNet()
