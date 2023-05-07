class Menu:
    def __init__(self):
        print("\n\t\t\t--- Welcome to the Bioinformatics Game ---")
        print("Two players play the following game with two sequences of length n and m nucleotides.\n"
              "At every turn a player must delete two nucleotides from one sequence (either the first\n"
              "or the second) and one nucleotide from the other. The player who cannot move loses. Who\n"
              "will win ? Describe the winning strategy for all values of n and m.")

    @staticmethod
    def user_selected_sequence_files():
        user_choice = input("\nWhich two nucleotide sequences do you want to import ?\n"
                            "Separate them with a comma e.g. 1,3\n"
                            "0) Brain\n1) Liver\n2) Muscle\n\n").lower()
        if len(user_choice) == 3:
            while not (user_choice[0].isdigit() or user_choice[2].isdigit()) or user_choice[0] == user_choice[2]:
                user_choice = input("\nPlease enter a valid choice:\n0) Brain\n1) Liver\n2) Muscle\n\n")

        return user_choice[0], user_choice[2]
