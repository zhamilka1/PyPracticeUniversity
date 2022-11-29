import re
def parse(string):
    pattern = r"(?:^Trip) (\d+) (?:arrived|departured) (\w+) (\w+) (?:\w+) (\d+:\d+:\d+)"
    print(re.match(pattern, string))
def journal_parser(input_filename):
    file = open(input_filename, mode="r", encoding="UTF-8")
    text = file.readlines()
    for line in text:
        parse(line)


journal_parser("bad_journal.txt")