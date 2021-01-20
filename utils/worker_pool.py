from concurrent.futures import ThreadPoolExecutor, as_completed
import importlib
import time


def thread_func(module, message_container, mutex, distribution, logging_level):
    try:
        m = importlib.import_module("modules." + module + ".module")
        m = m.get_module()
        m.prepare_module(distribution, logging_level)
        m.exec_module()
        m.finish_module(message_container, mutex)
    except Exception:
        print("Fail in module: '" + module + "'" + "with exception", Exception)


def thread_pool_controller(message_container, mutex, modules, distribution, logging_level, worker_count):
    print("Start process pool...")
    thread_count = min(worker_count, len(modules))
    print("Work thread count = ", thread_count)
    with ThreadPoolExecutor(thread_count) as tp:
        for module in modules:
            tp.submit(thread_func, module, message_container, mutex, distribution, logging_level)

    print("Finish process pool")
