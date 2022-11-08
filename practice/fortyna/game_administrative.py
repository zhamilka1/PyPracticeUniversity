def read_words(filename="fortyna/words.txt"):
    file = open(filename, mode="r", encoding="utf-8")
    words = []
    for line in file:
        buffer = line.replace('\n', '')
        words.append(buffer)
    file.close()
    return words

def get_record(filename="fortyna/record.txt"):
    file = open(filename, mode="r", encoding="windows-1251")
    record = int(file.readline())
    file.close()
    return record
def update_record(record_new, filename="fortyna/record.txt"):
    file = open(filename, mode="r", encoding="windows-1251")
    record_old = get_record()
    file.close()
    if  record_old < record_new:
        file = open(filename, 'w')
        file.write(str(record_new))
def read_lives(filename="fortyna/lives.txt"):
    file = open(filename, "r")
    lives = int(file.readline())
    file.close()
    return lives
