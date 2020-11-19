class CoffeeMachine:
    # The machine's initial values are: 400 ml. of water, 540 ml. of milk, 120 g. of coffee beans, 9 disposable cups and $550 in cash
    def __init__(self, water=400, milk=540, beans=120, cups=9, money=550):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    # Main menu
    def menu(self):
        while True:
            action = input("What do you want? Type 'buy', 'fill', 'take', 'remaining' or 'exit'\n")
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.status()
            elif action == "exit":
                break
                
    def buy(self):
        type_coffee = input("\nWhat do you want to buy?\n1 -- Espresso\n2 -- Latte\n3 -- Cappuccino\nback -- To main menu:\n")
        if type_coffee == "1":
            self.make_coffee(250, 16, 4)
        elif type_coffee == "2":
            self.make_coffee(350, 20, 7, 75)
        elif type_coffee == "3":
            self.make_coffee(200, 12, 6, 100)
        elif type_coffee == "back" or type_coffee == "Back":
            return
            
    def make_coffee(self, water, beans, money, milk=0):
        # `if` to determine the quantity of resources, printing a message accordingly
        if self.water >= water and self.beans >= beans and self.cups > 0 and self.milk >= milk:
            self.water -= water
            self.milk -= milk
            self.beans -= beans
            self.cups -= 1
            self.money += money
            print("I have enough resources, making you a coffee!")
        elif self.water < water:
            print("Sorry, not enough water!")
        elif self.milk < milk:
            print("Sorry, not enough milk!")
        elif self.beans < beans:
            print("Sorry, not enough coffee beans!")
        elif self.cups == 0:
            print("Sorry, not enough disposable cups!")
            
    def fill(self):
        # User input is added to the available resources right away
        self.water += int(input("Write how many ml. of water do you want to add:\n"))
        self.milk += int(input("Write how many ml. of milk do you want to add:\n"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def status(self):
        # The values are updated and displayed every time the user types `remaining`
        print(f"""The coffee machine has:
        {self.water} ml. of water
        {self.milk} ml. of milk
        {self.beans} g. of coffee beans
        {self.cups} disposable cups
        ${self.money} in cash""")

coffee_machine = CoffeeMachine()
coffee_machine.menu()
