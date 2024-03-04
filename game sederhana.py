import random

welcome_message = "WELCOME TO MY GAMES"

print("**********************")
print(f"* {welcome_message} *")
print("**********************")

nama = input("Masukkan nama anda: ")

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Draw"
    elif (player_choice == "batu" and computer_choice == "gunting") or \
         (player_choice == "gunting" and computer_choice == "kertas") or \
         (player_choice == "kertas" and computer_choice == "batu"):
        return "Player wins!"
    else:
        return "Computer wins!"

def main():
    choices = ["batu", "gunting", "kertas"]

    print(f"Selamat datang {nama} di permainan Batu Gunting Kertas!")
    player_choice = input("Pilih batu, gunting, atau kertas: ").lower()

    if player_choice not in choices:
        print("Pilihan tidak valid. Silakan pilih antara batu, gunting, atau kertas.")
        return

    computer_choice = random.choice(choices)
    print(f"Komputer memilih: {computer_choice}")

    result = determine_winner(player_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
