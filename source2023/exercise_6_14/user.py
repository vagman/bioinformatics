import json


class Menu:
    def __init__(self):
        print("\n\t\t\t--- Welcome to the Bioinformatics Game ---")
        print("Two players, Bob and Alice, play the following game with two sequences of length n and m nucleotides.\n"
              "At every turn a player must delete two nucleotides from one sequence (either the first\n"
              "or the second) and one nucleotide from the other. The player who cannot move loses. Who\n"
              "will win ? Describe the winning strategy for all values of n and m.")

    @staticmethod
    def user_selected_sequence_files():
        user_choice = input("\nWhich two nucleotide sequences do you want to import ?\n"
                            "Separate them with a comma e.g. 0,2\n"
                            "0) Brain\n1) Liver\n2) Muscle\n\n").lower()
        if len(user_choice) == 3:
            while not (user_choice[0].isdigit() or user_choice[2].isdigit()) or user_choice[0] == user_choice[2]:
                user_choice = input("\nPlease enter a valid choice:\n0) Brain\n1) Liver\n2) Muscle\n\n")
            with open(r"../../auxiliary2023/fasta.json", "r") as json_fasta:
                data = json.load(json_fasta)
                seq_a_name = data['sequences'][0][user_choice[0]][0]['name']
                seq_b_name = data['sequences'][0][user_choice[2]][0]['name']
            print(f"You chose nucleotide sequences of {seq_a_name} and {seq_b_name}.")

            # Some rough estimates on how long it will take to print the result
            if (seq_a_name == "liver" and seq_b_name == "muscle") or (seq_a_name == "muscle" and seq_b_name == "liver"):
                print("You will have to wait for at least 4' for the results.\n")
            if (seq_a_name == "brain" and seq_b_name == "muscle") or (seq_a_name == "muscle" and seq_b_name == "brain"):
                print("You will have to wait for at least 8' for the results.\n")
            if (seq_a_name == "brain" and seq_b_name == "liver") or (seq_a_name == "liver" and seq_b_name == "brain"):
                print("You will have to wait for at least 10' for the results.\n")

        return seq_a_name, seq_b_name
