from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMenu=Menu()
coffeeMaker= CoffeeMaker()
moneyMachine= MoneyMachine()


coffeeMaker.report()
moneyMachine.report()

while(1):
  while(1):
    choice=input(("what would you Like? ("+coffeeMenu.get_items()+"):"))
    drink=coffeeMenu.find_drink(choice)
    if(drink!=False):
      break
  if(coffeeMaker.is_resource_sufficient(drink)):
    if(moneyMachine.make_payment(drink.cost)):
      coffeeMaker.make_coffee(drink)

  
  

  
