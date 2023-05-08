from Bio import SeqIO
from user import Menu

fasta_files = {'0': 'brain',
               '1': 'liver',
               '2': 'muscle'}


def parse_sequence(fasta_filename: str):
    sequence = None
    try:
        for seq in SeqIO.parse(fasta_filename, "fasta"):
            pass
            print(f"The length of {(fasta_filename.split('/')[3]).split('.fasta')[0]} nucleotide sequence is: {len(seq)} characters.")

    except Exception as e:
        print("\nAn unexpected error occurred while reading .fasta input files:\n\n" + str(e))
    return sequence


def announce_winner(n, m):
    pass


def main():
    menu = Menu()
    user_choices = menu.user_selected_sequence_files()

    parse_sequence(r"../../auxiliary2023/" + fasta_files[user_choices[0]] + ".fasta")
    parse_sequence(r"../../auxiliary2023/" + fasta_files[user_choices[1]] + ".fasta")


if __name__ == "__main__":
    main()
