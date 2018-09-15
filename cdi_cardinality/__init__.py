import argparse
import csv
import itertools

parser = argparse.ArgumentParser(description="outputs the cardinality of all columns on a CSV file", prog= "cdi_cardinality")
parser.add_argument("filename")
# parser.add_argument("-s", "--separator", help="Specify the separator charcter.")
# parser.add_argument("-q", "--quote", help="Specify quote character.")
parser.add_argument("-m", "--max",  type=int, help="Specify maximum count value.")
parser.add_argument("-n", "--no-header", action='store_true',  help="Specify maximum count value.")
parser.add_argument("-v", "--valign", action='store_true',  help="Vertically align columns on the output for beter human readability")


args = parser.parse_args()

def get_col_names(csv_iterator, no_header):
    if no_header:
        csv_iter_1, csv_iter_2 = itertools.tee(csv_iterator)
        num_cols = len(next(csv_iter_1))
        del csv_iter_1
        col_names = [ "col_" + str(i) for i in range(num_cols) ]
        return col_names, csv_iter_2

    col_names = next(csv_iterator)
    col_names_stripped = [ col_name.strip() for col_name in col_names ]
    col_names_no_spaces = [ col_name.replace(" ", "_") for col_name in col_names ]

    return col_names_no_spaces, csv_iterator


def pad_col_names(col_names):
    lengths = [len(col) for col in col_names]
    max_length = max(lengths)
    padded_col_names = [ col + ' '*(max_length-len(col)) for col in col_names ]
    return padded_col_names


def output(col_names, counters, valign):
    if valign:
        col_names = pad_col_names(col_names)

    for idx, col_name in enumerate(col_names):
        print(col_name + " " + str(counters[idx]))

def main():

    max = 0
    if args.max is not None:
        max = args.max

    with open(args.filename, 'rt') as csvfile:
        csv_iter = csv.reader(csvfile)
        col_names, csv_iterator = get_col_names(csv_iter, args.no_header)
        num_cols = len(col_names)
        counters = [0] * num_cols

        found_vals = []
        for i in range(num_cols):
            found_vals.append({})

        for row in csv_iterator:

            if max != 0:
                non_maxed_counters = [x for x in counters if x < max]
                if len(non_maxed_counters) == 0:
                    output(col_names, counters, args.valign)
                    exit()

            for idx, value in enumerate(row):
                if max !=0 and counters[idx] >= max:
                    continue
                if value not in found_vals[idx]:
                    found_vals[idx][value] = 1
                    counters[idx] = counters[idx] + 1
        
        output(col_names, counters, args.valign)