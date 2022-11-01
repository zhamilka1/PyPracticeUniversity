def read_logs(filename="game_log.py"):
    file = open(filename, "r")
    record = int(file.readline())
    iterations = int(file.readline())
    words = []
    for i in range(0, iterations):
        words.append(file.readline())
    result = [record, words]
    file.close()
    return result

def get_record(filename="game_log.py"):
    file = open(filename, "r")
    record = int(file.readline())
    file.close()
    return record

def update_logs(record_new, filename="game_log.py"):
    record_old = get_record()
    if  record_old < record_new:

        file = open(filename, 'w')
        file.write()
    else:
        return "Nothing to update"

