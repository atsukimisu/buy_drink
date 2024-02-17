from drinks import Drink

class Coin:
  def __init__(self, money: int, drink: Drink) -> None:
    self.money = money
    self.drink = drink

  def change(self) -> int:
    change_coins = self.money - self.drink.price
    return change_coins
  
  def is_buyable(self) -> bool:
    if self.change() < 0:
      return False
    else:
      return True
