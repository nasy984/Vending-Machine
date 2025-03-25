class DFAVendingMachine:
    def __init__(self, dfa_file):
        self.states = {}  # Menyimpan aturan transisi DFA
        self.start_state = "S0" #start state 
        self.accept_states = set()
        self.current_state = self.start_state
        self.prices = {"A": 3000, "B": 4000, "C": 6000}  # Harga minuman
        self.balance = 0  # Saldo pengguna
        self.transition_history = [self.start_state]  # Menyimpan lintasan DFA
        self.load_dfa(dfa_file)  # Memuat aturan DFA dari file

    def load_dfa(self, dfa_file):
        with open(dfa_file, 'r') as file:
            lines = file.readlines()
            transitions_start = False
            for line in lines:
                line = line.strip()
                if line.startswith("States:"):
                    continue
                elif line.startswith("Alphabet:"):
                    continue
                elif line.startswith("Start:"):
                    self.start_state = line.split(": ")[1]
                    self.current_state = self.start_state
                elif line.startswith("Accept:"):
                    self.accept_states = set(line.split(": ")[1].split(", "))
                elif line.startswith("Transitions:"):
                    transitions_start = True
                elif transitions_start and line:
                    parts = line.split()
                    if len(parts) == 3:
                        state_from, input_symbol, state_to = parts
                        if state_from not in self.states:
                            self.states[state_from] = {}
                        self.states[state_from][input_symbol] = state_to

    def process_input(self, user_input):
        user_input = user_input.upper().strip()  

        if user_input.isdigit():  # Jika input adalah uang
            if self.current_state in self.states and user_input in self.states[self.current_state]:
                self.balance += int(user_input)
                print(f"Saldo saat ini: {self.balance}")
                self.current_state = self.states[self.current_state][user_input]
                self.transition_history.append(self.current_state)

                available_drinks = [drink for drink, price in self.prices.items() if self.balance >= price]
                if available_drinks:
                    print(f"ON: Minuman {' '.join(available_drinks)}")
                return True
            else:
                return "Uang tidak bisa diterima. Status: REJECTED."

        elif user_input in self.prices:  # Jika input adalah minuman
            price = self.prices[user_input]

            print("\nLintasan DFA:", " → ".join(self.transition_history))

            if self.balance == price:  # Hanya bisa beli jika saldo pas
                print(f"Minuman {user_input} dapat dibeli. Status: ACCEPTED.")

                # Reset saldo dan DFA setelah transaksi
                self.balance = 0
                self.current_state = self.start_state
                self.transition_history = [self.start_state]
                return True
            elif self.balance > price:
                return f"Uang lebih dari harga minuman. Status: REJECTED."
            else:
                return "Uang tidak cukup. Status: REJECTED."

        return "Input tidak valid. Status: REJECTED."

    def reset(self):
        """Reset mesin setelah transaksi selesai"""
        self.balance = 0
        self.current_state = self.start_state
        self.transition_history = [self.start_state]


def main():
    dfa = DFAVendingMachine("vending_dfa.txt")

    print("Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C). Ketik 'exit' untuk keluar.")
    while True:
        user_input = input("Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C) : ").strip()
        if user_input.lower() == "exit":
            break

        result = dfa.process_input(user_input)
        if isinstance(result, str):  # Jika ada pesan error
            print(result)
        elif not result:
            print("Input tidak valid. Status: REJECTED.")


if __name__ == "__main__":
    main()
