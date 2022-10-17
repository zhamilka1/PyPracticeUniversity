def parse(string):
    data = string.split()
    number = int(data[1])
    departure = str(data[6])
    status = str(data[3])
    from_to = str(data[4])
    return[number, status, from_to, departure]

def journal_parser(input_filename, output_filename):
    bad_journal = open(input_filename, 'r')
    good_journal = open(output_filename, 'w')
    for line in bad_journal:
        data = parse(line)
        good_journal.writelines(f"[{data[3]}] - Train № {data[0]} {data[1]} {data[2]}\n")