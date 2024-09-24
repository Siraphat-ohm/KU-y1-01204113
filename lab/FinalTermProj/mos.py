def readMenu(fn="CoffeeMenu01.txt"):
    with open(fn) as fd:
        return fd.read()


class CupOfCoffee:
    def __init__(self, coffee_type, drinking_type, price):
        self.coffee_type = coffee_type
        self.drinking_type = drinking_type
        self.price = price
        self.drinking_return = None
        self.coffee_return = None
        self.price_return = 0
        self.AddOn_return = []
        self.one_add_on = []
        self.one_add_on_price = []
        self.get_AddOn = []
        self.get_AddOnPrice = []
        self.coffee_type_return = []
        self.result = {}

    def get_price(self, coffee, drinking):
        check = 0
        if drinking.lower() == "h":
            num_price = 0
            self.drinking_return = "hot"
        elif drinking.lower() == "c":
            num_price = 1
            self.drinking_return = "cold"
        else:
            num_price = 2
            self.drinking_return = "frappe"
        for key, value in self.coffee_type.items():
            if int(coffee) - 1 == key:
                self.coffee_return = value
                self.coffee_type_return.append(value)
        for key, value in self.price.items():
            if int(coffee) - 1 == key:
                check += int(value[num_price])
                pass
        return check

    def cal_total_price(self, select_coffee, select_drinking, add_on_input):
        # เมนูกาแฟ / ร้อนเย็นปั่น / ราคา / ท้อปปิ้ง / ราคาท้อปปิ้ง
        self.price_return = 0
        self.AddOn_return = []
        main_manu = []
        topping = {}
        num_price = 0
        for key, value in self.coffee_type.items():
            if int(select_coffee) - 1 == int(key):
                main_manu.append(value)
        if select_drinking.lower() == "h":
            num_price = 0
            main_manu.append("hot")
        elif select_drinking.lower() == "c":
            num_price = 1
            main_manu.append("cold")
        else:
            num_price = 2
            main_manu.append("frappe")
        for key, value in self.price.items():
            if int(select_coffee) - 1 == int(key):
                main_manu.append(value[num_price])
        if add_on_input != "":
            for item in add_on_input:
                topping[self.get_AddOn[int(item) - 1]] = self.get_AddOnPrice[
                    int(item) - 1
                ]
        else:
            add_on_input = []

        self.drinking_return = main_manu[1]
        self.coffee_return = main_manu[0]
        for key, value in topping.items():
            self.AddOn_return.append(key)
            self.price_return += int(value)
        self.price_return += int(main_manu[2])

        return main_manu, topping, self.price_return

    def check_coffee(self, coffee_type):
        dict_check = []
        typr = ["H", "C", "F"]
        for key, value in self.price.items():
            if int(coffee_type) - 1 == int(key):
                for i in range(len(value)):
                    if int(value[i]) != 0:
                        dict_check.append(typr[i])

        return dict_check

    def get_add_on(self, getAddOn, getAddOnPrice):
        self.get_AddOn = getAddOn
        self.get_AddOnPrice = getAddOnPrice

    def __repr__(self):

        if len(self.AddOn_return) == 0:
            return f" This cup is {self.drinking_return} {self.coffee_return} with no add on, {self.price_return} baht."
        elif len(self.AddOn_return) == 1:
            return f" This cup is {self.drinking_return} {self.coffee_return} with {self.AddOn_return[0]}, {self.price_return} baht."
        elif len(self.AddOn_return) == 2:
            return f" This cup is {self.drinking_return} {self.coffee_return} with {self.AddOn_return[0]} and {self.AddOn_return[1]}, {self.price_return} baht."
        elif len(self.AddOn_return) == 3:
            return f" This cup is {self.drinking_return} {self.coffee_return} with {self.AddOn_return[0]}, {self.AddOn_return[1]} and {self.AddOn_return[2]}, {self.price_return} baht."


class CustomerBill:
    def __init__(self, name):
        self.name = name
        self.coffee = []
        self.type_coffee = []
        self.price_all = []
        self.addon = []
        self.price_return = 0
        self.ordered_coffee = []

    def add_ordered_coffee(self, aCupOfCoffeeObject):
        self.ordered_coffee.append(aCupOfCoffeeObject)

    def get_information(self, coffee_data, add_on_data, price):
        self.coffee.append(coffee_data[0])
        self.type_coffee.append(coffee_data[1].capitalize())
        self.price_all.append(str(price))
        self.price_return += int(price)

        if len(add_on_data) != 0:
            add_on_list = list(add_on_data.keys())
            self.addon.append(add_on_list)
        else:
            self.addon.append([])

    def receipt(self):
        print("++++++++++++++++++++++++++++++++")
        print("      CPE38 **StarBUG Cafe    ")
        len_t = f"Kun {self.name}'s Receipt"
        print(
            f"{' ' * int(((32 - len(len_t)) // 2))}Kun {self.name}'s Receipt{' ' * int(((32 - len(len_t)) // 2))}"
        )
        print("++++++++++++++++++++++++++++++++")
        print("Description                Price")

        for i in range(len(self.coffee)):
            len_all = int(len(self.type_coffee[i])) + int(len(self.coffee[i]))

            print(f"{self.type_coffee[i]} {self.coffee[i]}", end=" " * (28 - len_all))
            print(f"{' ' * (3 - len(str(self.price_all[i])))}{self.price_all[i]}")

            if len(self.addon[i]) > 0:
                for item in self.addon[i]:
                    print(f" + {item}")
            print()

        total = f"{self.price_return:,}"
        print(f"Total{' ' * (27 - len(total))}{total}")
        print("++++++++++++++++++++++++++++++++")
        print(" Thank you, please come back :) ")
        print("++++++++++++++++++++++++++++++++")
        print()


############################################## นิยามเฉพาะคลาส CupOfCoffee and CustomerBill ในกล่องด้านล่างนี้
"""-----------------------------------------------------------------"""


def print_menu(coffee_type, price_coffee):

    print("Welcome to CPE38 **StarBUG Cafe!")
    print("+++++++++++++ MENU +++++++++++++")
    print("Coffee         Hot  Cold  Frappe")
    for i in range(len(coffee_type)):

        print(f"{i+1}.{coffee_type[i]}", end=" " * (10 - len(coffee_type[i])))
        prices = price_coffee[i]
        for item in prices:
            print(" " * (6 - len(item)) + f"{item}", end="")
        print()


def print_add_on(add_on_menu, add_on_price):
    print("++++++++++++ ADD-ON ++++++++++++")
    for i in range(len(add_on_menu)):
        print(f"{i+1}.{add_on_menu[i]}", end=" " * (19 - len(add_on_menu[i])))
        print(" " * (3 - len(add_on_price[i])) + f"{add_on_price[i]}")
    print("++++++++++++++++++++++++++++++++")


def good_day(coffee_menu, price, check):
    result = {}
    result_num = []
    num = 1
    price_result = sum(int(num) for num in price)
    print("++++++++++++++++++++++++++++++++")
    print("      CPE38 **StarBUG Cafe    ")
    print("  Report for Coffee sold today")
    print("++++++++++++++++++++++++++++++++")
    sorted_list = sorted(coffee_menu, key=lambda x: list(check.values()).index(x))
    for item in sorted_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    for k, v in result.items():
        if v == 1:
            x = 26 - len(k)
            print(f" {k:<24}{v} cup  ")
        else:
            print(f" {k:<24}{v} cups ")
    price_result = f"{price_result:,}"
    print()
    print(f"Total sold amount {price_result:>9} baht")
    print("++++++++++++++++++++++++++++++++")
    print("       What's a good day!     ")
    print("++++++++++++++++++++++++++++++++")


# print_menu(coffee_type, price_coffee)
# print_add_on(add_on_menu, add_on_price)


def runStarBUGcafe_main():
    def menu_coffee(coffee_menu_CSV):
        a = coffee_menu_CSV.strip().split("\n")
        z = []
        coffee_type = {}
        price_coffee = {}
        for item in a:
            if item != "":
                x = item.strip().split(",")
                z.append(x)

        for i in range(len(z)):
            coffee_type[i] = z[i][0]
            price_coffee[i] = z[i][1:]
        drink_type = ["h", "c", "f"]
        return coffee_type, drink_type, price_coffee

    def add_on(add_on):
        a = add_on.strip().split("\n")
        z = []
        add_on_type = []
        price_add_on = []
        for item in a:
            if item != "":
                x = item.split(",")
                z.append(x)
        for i in range(len(z)):
            add_on_type.append(z[i][0])
            price_add_on.append(z[i][1])
        return add_on_type, price_add_on

    all_manu = []
    all_price = []

    coffee_type, drink_type, price_coffee = menu_coffee(coffee_menu_CSV)
    add_on_menu, add_on_price = add_on(add_on_menu_CSV)

    coffee = CupOfCoffee(coffee_type, drink_type, price_coffee)
    coffee.get_add_on(add_on_menu, add_on_price)
    add_on_ = add_on_menu
    range_add_on = len(add_on_)
    name = 0
    drink_type_letters = ["h", "c", "f"]

    while name != "Good Day":
        print_menu(coffee_type, price_coffee)
        print_add_on(add_on_menu, add_on_price)
        print()
        name = str(input("Enter customer's name: "))
        bill = CustomerBill(name)

        if name == "Good Day":
            good_day(all_manu, all_price, coffee_type)
            break

        num_order = input("How many cups of coffee to order? ")
        while not num_order.isdigit() or int(num_order) <= 0:
            print(" ERROR: Invalid input!")
            num_order = input("How many cups of coffee to order? ")

        for i in range(int(num_order)):

            select_coffee = input(f"Cup #{i + 1}, please select type of coffee: ")
            while (
                not select_coffee.isdigit()
                or int(select_coffee) <= 0
                or int(select_coffee) > len(coffee_type)
            ):
                print(" ERROR: Invalid input!")
                select_coffee = input(f"Cup #{i + 1}, please select type of coffee: ")

            cc = coffee.check_coffee(select_coffee)
            select_drinking = 0

            if len(cc) != 1:
                ff = f"Cup #{i + 1}, please select drinking type ({','.join(cc)}): "
                select_drinking = input(ff)
                while (
                    select_drinking.lower() not in drink_type_letters
                    or select_drinking.upper() not in cc
                ):
                    print(" ERROR: Invalid input!")
                    select_drinking = input(ff)
            else:
                select_drinking = cc[0]

            add_on_num = []

            check_add_on = coffee.get_price(select_coffee, select_drinking)

            if int(check_add_on) != 0:
                while True:
                    add_on_input = input(
                        f"Cup #{i + 1}, please select add on (enter for exit): "
                    )
                    if add_on_input != "":
                        if (
                            not add_on_input.isdigit()
                            or int(add_on_input) > range_add_on
                            or int(add_on_input) <= 0
                            or add_on_input in add_on_num
                        ):
                            print(" ERROR: Invalid input!")
                        else:
                            add_on_num.append(add_on_input)
                            if len(add_on_num) == range_add_on:
                                break
                    else:
                        break

            a, b, c = coffee.cal_total_price(select_coffee, select_drinking, add_on_num)
            bill.add_ordered_coffee(repr(coffee))
            all_manu.append(a[0])
            all_price.append(c)

            print(coffee)

            # Store order information in the bill
            bill.get_information(a, b, c)  # Properly handle add-ons in the bill.

        # Print receipt for the customer
        bill.receipt()

    else:
        good_day(all_manu, all_price, coffee_type)


coffee_menu_filename = "./testcase/CoffeeMenu02.txt"
coffee_menu_CSV = readMenu(coffee_menu_filename)
addon_menu_filename = "./testcase/CoffeeMenuAddOn02.txt"
add_on_menu_CSV = readMenu(addon_menu_filename)
runStarBUGcafe_main()
