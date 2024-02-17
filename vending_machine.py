from coin import Coin
from drinks import Drink

class VendingMachine:
  def __init__(self, drink1: Drink, drink2: Drink, drink3: Drink, coin: Coin):
    self.drink1 = drink1
    self.drink2 = drink2
    self.drink3 = drink3
    self.coin = coin

  def line_up(self):
    print(self.drink1.name)
    print(self.drink2.name)
    print(self.drink3.name)

  def give_drink(self):
    if self.coin.is_buyable():
      print(f'{self.coin.drink.name}を買いました')
      print(f'お釣りは{self.coin.change()}円です')
    else:
      print('お金が足りません')