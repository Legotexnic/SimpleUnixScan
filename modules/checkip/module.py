from utils.utils import *


class CheckIP(Module):
    @module_logging_decorator
    @module_output_decorator
    def exec_module(self):
        out, _ = cmdcall("which ip")
        if len(out) == 0:
            self.out.write("'ip' not found in system")
        else:
            out, _ = cmdcall("ip -s link")
            self.out.write("Output from ip showing Kernel interface statistics\n")
            for line in out:
                self.out.write(line)

        self.out.write("\n")
        self.out.write("-" * 100 + "\n")
        self.out.write("\n")

        out, _ = cmdcall("which nmap")
        if len(out) == 0:
            self.out.write("'nmap' not found in system")
        else:
            out, _ = cmdcall("nmap - v - T insane ` / sbin / ifconfig | grep inet | grep - v 127.0.0.1 | awk \
- F\" \" 'length($2) > 0 {print $2}' |awk -F\":\" 'length($2) >0 {print $2}' |xargs`")
            self.out.write("Output from nmap run on local IP(s)\nCheck these services to see if they are \
critical.\nDisable services you do not need.\n")
            for line in out:
                self.out.write(line)
        self.out.write("\n")

        self.out.write("\n")
        self.out.write("-" * 100 + "\n")
        self.out.write("\n")

        out, _ = cmdcall("which arp")
        if len(out) == 0:
            self.out.write("'arp' not found in system")
        else:
            out, _ = cmdcall("arp -a |awk '{print $4}' |uniq -cd")
            self.out.write("Output from arp -a. \nIf you have arp poisoning, you would see a MAC address here.\n")
            for line in out:
                self.out.write(line)

        self.out.write("\n")
        self.out.write("-" * 100 + "\n")
        self.out.write("\n")

        out, _ = cmdcall("which netstat")
        if len(out) == 0:
            self.out.write("'netstat' not found in system")
        else:
            out, _ = cmdcall("netstat -rn")
            self.out.write("Output from netstat -rn showing current routing\n")
            for line in out:
                self.out.write(line)

        self.out.write("\n")


def get_module():
    return CheckIP()
