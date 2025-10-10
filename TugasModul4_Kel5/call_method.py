from TugasModul4_Kel5 import Game
print("Kelompok 05")
game = Game()

while True:
    game.mainkan()  # method dipanggil dari file lain
    ulang = input("Main lagi? (y/n): ").lower()
    if ulang != "y":
        print("Terima kasih sudah bermain!")
        break