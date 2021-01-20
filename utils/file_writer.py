def write_function(filename, message_container, mutex, event):
    print("Start write thread...")
    file = open(filename, "w+")
    file.write("-" * 100 + "\n")
    file.write("-" * 40 + "Start  Unix  Scanner" + "-" * 40 + "\n")
    file.write("-" * 100 + "\n" + "\n")
    flag = True
    while flag:
        with mutex:
            if len(message_container) > 0:
                print("Write message")
                record = message_container.pop()
                file.write(record.getvalue())
            else:
                if event.is_set():
                    flag = False

    file.write("\n" + "-" * 100 + "\n")
    file.write("-" * 40 + "Finish  Unix  Scanner" + "-" * 39 + "\n")
    file.write("-" * 100 + "\n")
    file.close()
    print("Finish write thread")
