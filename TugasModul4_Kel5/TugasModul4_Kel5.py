import random

def hasil_permainan(player, komputer):
    if player == komputer:
        return "Seri"
    elif (player == "batu" and komputer == "gunting") or \
         (player == "gunting" and komputer == "kertas") or \
         (player == "kertas" and komputer == "batu"):
        return "Menang"
    else:
        return "Kalah"

def tampilkan(player, komputer, hasil):
    print(f"\nKamu: {player}")
    print(f"Komputer: {komputer}")
    print(f"Hasil: {hasil}\n")

class Game:
    def mainkan(self):
        pilihan = ["batu", "gunting", "kertas"]
        player = input("Pilih (batu/gunting/kertas): ").lower()

        if player not in pilihan:
            print("Pilihan tidak valid!\n")
            return

        komputer = random.choice(pilihan)
        hasil = hasil_permainan(player, komputer)
        tampilkan(player, komputer, hasil)