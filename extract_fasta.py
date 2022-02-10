#############################################################
# Extract fasta sequences using a list of accession numbers #
# AV                                                        #
# 10-2-2022                                                 #
#############################################################

# list of accession  numbers
with open('acc_nums.txt', 'r') as data: # CHECK file name
    acc_numbs = data.readlines() # list type
    print(acc_numbs)

# original fasta file
with open('test2_origin.fasta', 'r') as origin_fasta: # CHECK file name
    input_fasta = origin_fasta.readlines()

# final fasta file
parsed_fasta = open('fasta_parsed.txt', 'w')

ACCNUM_DICT = {}
for number in acc_numbs:
    ACCNUM_DICT[number[:-1]] = 1  # set value to 1 (can be anything)
print(ACCNUM_DICT)

skip = 0
for line in input_fasta:
    if line[0] == '>':  # should I use "^>"?
        split_header = line.split(' ')  # split header by space (CHECK HEADER FORMAT)
        acc_num_greater_than = split_header[0] # select >LongAccessionNumber
        long_acc_num_line = acc_num_greater_than.split(".") # split by "."
        long_acc_num = long_acc_num_line[0] # select >AccessionNumber
        accessionNum = long_acc_num[1:] # skip ">"
        print(accessionNum)
        if accessionNum in ACCNUM_DICT:
            parsed_fasta.write(line)
            skip = 0
        else:
            skip = 1
    else:
        if not skip:
            parsed_fasta.write(line)

parsed_fasta.close()