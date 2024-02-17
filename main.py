from drinks import Drink
from coin import Coin
from vending_machine import VendingMachine
  
def main():
  cola = Drink('コーラ', 150)
  water = Drink('水', 100)
  tea = Drink('お茶', 130)
  coin = Coin(200, cola)
  boss = VendingMachine(cola, water, tea, coin)

  boss.line_up()
  boss.give_drink()

if __name__ == '__main__':
  main()

