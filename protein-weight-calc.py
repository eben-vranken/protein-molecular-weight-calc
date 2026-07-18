from argparse import ArgumentParser

from src import parser

def parse_args():
    parser = ArgumentParser()

    parser.add_argument("-f", "--file", help="Filepath to the FASTA file to be parsed.")
    parser.add_argument("-s", "--sequence", help="Protein sequence to be parsed")
    
    args = parser.parse_args()

    if not args.file and not args.sequence:
        print("Either file or sequence flags are required.")
        exit(1)

    if args.file and args.sequence:
        print("Only 1 flag can be chosen between file and sequence.")
        exit(1)

    return args

if __name__ == "__main__":
    args = parse_args()

    if args.file:
        sequence = parser.parse_fasta(args.file)
    else:
        sequence = args.sequence