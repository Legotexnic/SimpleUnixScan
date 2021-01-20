import argparse
import os.path
import threading
import time
from multiprocessing import Queue, Manager
from utils.file_writer import *
from utils.worker_pool import *


def check_distribution():
    distribution_list = ["debian", "redhat", "ubuntu"]
    out = os.uname().version
    for distr in distribution_list:
        if distr in out.lower():
            return distr

    return "ubuntu"


def process_modules(distribution, filename, logging_level, worker_count):
    modules = os.listdir("modules")
    modules_count = len(modules)
    if modules_count > 0:
        message_container = []
        mutex = threading.Lock()
        event = threading.Event()
        print("Registered " + str(modules_count) + " modules")

        write_thread = threading.Thread(target=write_function, args=(filename, message_container, mutex, event))
        write_thread.start()

        thread_pool_controller(message_container, mutex, modules, distribution, logging_level, worker_count)

        event.set()
        write_thread.join()

    else:
        print("No modules found.")


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
    group.add_argument("-q", "--quiet", action="store_true", help="mutes output")
    parser.add_argument("-d", "--distribution", action="store", help="Force a specific distribution, "
                                                                     "valid distro names are: "
                                                                     "debian, "
                                                                     "redhat, "
                                                                     "ubuntu")
    parser.add_argument("-o", "--output", action="store", help="path to output file")
    parser.add_argument("-j", "--jobs",  action="store", help="count worker thread", type=int, default=6)
    args = parser.parse_args()
    logging_level = 1
    if args.verbose:
        logging_level = 2
    if args.quiet:
        logging_level = 0
    if args.distribution:
        distribution = args.distribution
    else:
        distribution = check_distribution()
    filename = "out.txt"
    if args.output:
        filename = args.output

    start_time = time.time()
    print("Start program... ")

    process_modules(distribution, filename, logging_level, args.jobs)

    print("Finish program ")

    print(time.time()-start_time)


if __name__ == "__main__":
    main()
