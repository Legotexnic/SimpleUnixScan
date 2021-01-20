from utils.utils import *


class CheckLogging(Module):
    @module_logging_decorator
    @module_output_decorator
    def exec_module(self):
        out, _ = cmdcall("/usr/bin/faillog -a |head -100")
        self.out.write("The last 100 (or less) failed login attempts on the system\n")
        for line in out:
            self.out.write(line)
        self.out.write("\n")


def get_module():
    return CheckLogging()
