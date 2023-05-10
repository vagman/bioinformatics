from user import Menu
from Bio import SeqIO
import pandas as pd
from tqdm import trange


def parse_sequence(file_name: str):
    for sequence_record in SeqIO.parse(file_name, "fasta"):
        sequence = sequence_record.seq
    return sequence


# Fill the first two columns and row of the matrix which we already know
def fill_first_2rows2cols_matrix(n: int, m: int, solution_matrix: list):
    for i in range(m + 1):
        solution_matrix[i][0] = "W"
    for j in range(n + 1):
        solution_matrix[0][j] = "W"
    if n > 0 and m > 0:
        solution_matrix[1][1] = "W"
    if m >= 2 and n >= 2:
        for i in range(2, m + 1):
            solution_matrix[i][1] = "L"
    if n >= 2 and m >= 2:
        for j in range(2, n + 1):
            solution_matrix[1][j] = "L"
    return solution_matrix


# Calculate the rest of the results based on the algorithm
def calculate_results_matrix(n: int, m: int):
    results = []

    for i in trange(len(str(m)) + 1):
        results.append([i] * (len(str(n)) + 1))
    results = fill_first_2rows2cols_matrix(len(str(n)), len(str(m)), results)

    if len(str(n)) >= 2 and len(str(m)) >= 2:
        for i in trange(2, len(str(m)) + 1):
            for j in range(2, len(str(n)) + 1):
                # The two possible moves every player has in their turn
                if results[i - 2][j - 1] == "W" and results[i - 1][j - 2] == "W":
                    results[i][j] = "L"
                else:
                    results[i][j] = "W"
    pretty_print(n, m, results)
    return results[-1][-1]


def pretty_print(n: int, m: int, solution_array: list):
    print("\nPrinting result's matrix of the game..")
    df = pd.DataFrame(solution_array,
                      columns=[j for j in trange(len(str(n)) + 1)],
                      index=[i for i in trange(len(str(m)) + 1)])
    print("\nBook's example representation [11 rows x 11 columns] array :\n", df[[j for j in range(11)]].head(11), "\n")
    print("The whole thing:\n", df)


def announce_winner(n: str, m: str, result: str):
    if result == "W":
        print(f"\nWith given sequences, an array of n={len(m)}, m={len(n)} was created. Bob won!\n")
    else:
        print(f"\nWith given sequences, an array of n={len(m)}, m={len(n)} was created. Alice won!\n")


def main():
    menu = Menu()
    user_choices = menu.user_selected_sequence_files()

    sequence_a = parse_sequence(r"../../auxiliary2023/" + user_choices[0] + ".fasta")
    sequence_b = parse_sequence(r"../../auxiliary2023/" + user_choices[1] + ".fasta")

    # Print all possible outcomes for every value of n, m given from the user input sequence
    result_matrix = calculate_results_matrix(sequence_a, sequence_b)

    # Print who is the winner for n, m given
    announce_winner(sequence_a, sequence_b, result_matrix)


if __name__ == "__main__":
    main()
