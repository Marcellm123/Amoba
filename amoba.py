def rajzol_tabla(tabla):
  """Játéktér kirajzolása"""
  for sor in tabla:
    print("┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐")
    print("│", end="")
    for cella in sor:
      print(f" {cella} │", end="")
    print("\n├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
  print("└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘")

def ellenoriz_nyertes(tabla, jatekos):
  # Vízszintes/függőleges
  for i in range(10):
    if all(tabla[i][j] == jatekos for j in range(5)):
      return True
    if all(tabla[j][i] == jatekos for j in range(5)):
      return True
  # Átló
  for i in range(6):
    if all(tabla[i+j][j] == jatekos for j in range(5)):
      return True
    if all(tabla[j][i+j] == jatekos for j in range(5)):
      return True
  return False

def main():
  tabla = [[' ' for _ in range(10)] for _ in range(10)]
  jatekosok = ['X', 'O']
  jelenlegi_jatekos = 0

  while True:
    rajzol_tabla(tabla)

    while True:
      try:
        sor, oszlop = map(int, input(f"{jatekosok[jelenlegi_jatekos]} játékos, add meg a sor és oszlop számát (pl. 1 5): ").split())
        if 1 <= sor <= 10 and 1 <= oszlop <= 10:
          if tabla[sor-1][oszlop-1] == ' ':
            break
          else:
            print("Ez a mező már foglalt. Próbáld újra!")
        else:
          print("Érvénytelen koordináták! A sor és oszlop száma 1 és 10 között lehet.")
      except ValueError:
        print("Érvénytelen bemenet! Kérlek, egész számokat adj meg.")

    tabla[sor-1][oszlop-1] = jatekosok[jelenlegi_jatekos]

    if ellenoriz_nyertes(tabla, jatekosok[jelenlegi_jatekos]):
      rajzol_tabla(tabla)
      print(f"{jatekosok[jelenlegi_jatekos]} játékos nyert!")
      break

    jelenlegi_jatekos = (jelenlegi_jatekos + 1) % 2

if __name__ == "__main__":
  main()