import os
from Bio import SeqIO
from pathlib import Path


def parse_sequence(fasta_filename: str):
    sequence = None
    try:
        for seq in SeqIO.parse(fasta_filename, "fasta"):
            print(seq.id)
            print(repr(seq.seq))
            print(len(seq))

    except Exception as e:
        print("\nAn unexpected error occurred while reading .fasta input files:\n\n" + str(e))
    return sequence


def player1():
    pass


def player2():
    pass


def main():
    print("\n--- Welcome to the Bioinformatics Game ---")
    parse_sequence(r"../../auxiliary2023/brain.fasta")


if __name__ == "__main__":
    main()
