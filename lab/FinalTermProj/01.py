def readMenu(fn="CoffeeMenu01.txt"):
    with open(fn) as fd:
        return fd.read()


#########################################


class CupOfCoffee:
    def __init__(self, coffee_type, drinking_type, price):
        self.coffee_type = coffee_type
        self.drinking_type = drinking_type
        self.price = price
        self.add_on = []

    def set_add_on(self, one_add_on, one_add_on_price):
        self.add_on.append(one_add_on)
        self.price += one_add_on_price

    def get_addon(self):
        return self.add_on

    def get_coffee_type(self):
        return self.coffee_type

    def get_drink_type(self):
        return self.drinking_type

    def get_price(self):
        return self.price

    def __repr__(self):
        if self.add_on:
            if len(self.add_on) == 1:
                return f" This cup is {self.drinking_type.lower()} {self.coffee_type} with {", ".join(self.add_on)}, {self.price} baht."
            return f" This cup is {self.drinking_type.lower()} {self.coffee_type} with {", ".join(self.add_on[:-1])} and {self.add_on[-1]}, {self.price} baht."
        return f" This cup is {self.drinking_type.lower()} {self.coffee_type} with no add on, {self.price} baht."


class CustomerBill:
    def __init__(self, name):
        self.name = name
        self.order = []

    def add_ordered_coffee(self, aCupOfCoffeeObject: CupOfCoffee):
        self.order.append(aCupOfCoffeeObject)

    def receipt(self):
        print("++++++++++++++++++++++++++++++++")
        print("      CPE38 **StarBUG Cafe    ")
        name_leght = len(f"Kun {self.name}'s Receipt")
        bar = (32 - name_leght) // 2
        print(f"{' '*bar}Kun {self.name}'s Receipt{' '*bar}")
        print("++++++++++++++++++++++++++++++++")
        print(f"{'Description':<27}Price")
        total = 0
        for cup in self.order:
            name = f"{cup.get_drink_type()} {cup.get_coffee_type()}"
            addon = "\n".join([f" + {addon}" for addon in cup.get_addon()])
            price = cup.get_price()
            print(f"{name:<27}{price:>5}")
            total += price
            if addon:
                print(addon)
            print()
        total_f = f"{total:,}"
        print(f"{'Total':<27}{total_f:>5}")
        print("++++++++++++++++++++++++++++++++")
        print(" Thank you, please come back :) ")
        print("++++++++++++++++++++++++++++++++")
        print()


#########################################


def csv2list(csv: str):
    return [
        [value.strip() for value in row.split(",")]
        for row in csv.strip().split("\n")
        if row != ""
    ]


def printMenu(menu):
    print("+++++++++++++ MENU +++++++++++++")
    print(f"{'Coffee':<15}{'Hot':<5}{'Cold':<6}Frappe")
    for i, row in enumerate(menu):
        name, hot_p, cold_p, frappe_p = row
        # print(f"{i+1}.{row[0]:<13}{row[1]}{row[2]:>6}{row[3]:>6}")
        name = f"{i+1}.{name}"
        print(f"{name:<15}{hot_p:>3}{cold_p:>6}{frappe_p:>6}")


def printAddon(addon):
    print("++++++++++++ ADD-ON ++++++++++++")
    for i, row in enumerate(addon):
        print(f"{i+1}.{row[0]:<13}{row[1]:>9}")
    print("++++++++++++++++++++++++++++++++")


def readName():
    print()
    return input("Enter customer's name: ")


def readCup(n_c=1):
    c_map = {i + 1: row[0] for i, row in enumerate(menu)}
    while True:
        try:
            n_m = int(input(f"Cup #{n_c}, please select type of coffee: "))
            if n_m <= 0 or n_m > len(menu):
                print(" ERROR: Invalid input!")
            else:
                return c_map[n_m], n_m
        except ValueError:
            print(" ERROR: Invalid input!")


def readDrinkType(n_m, n_c=1):
    t = "HCF"[: len([p for p in menu[n_m - 1] if p != "0"]) - 1]
    t_map = {"H": "Hot", "C": "Cold", "F": "Frappe"}
    t_n_map = {"H": 1, "C": 2, "F": 3}
    while True:
        try:
            if t == "H":
                return t_map["H"], int(menu[n_m - 1][1])

            n_t = input(
                f"Cup #{n_c}, please select drinking type ({','.join(t)}): "
            ).upper()
            if not n_t in t or n_t == "":
                print(" ERROR: Invalid input!")
            else:
                return t_map[n_t], int(menu[n_m - 1][t_n_map[n_t]])
        except ValueError:
            print(" ERROR: Invalid input!")


def readNOrder():
    while True:
        try:
            n = int(input("How many cups of coffee to order? "))
            if n <= 0:
                print(" ERROR: Invalid input!")
            else:
                return n
        except ValueError:
            print(" ERROR: Invalid input!")


def printStarReceipt(order):
    menu_order = [m[0] for m in menu]
    total = 0
    print("++++++++++++++++++++++++++++++++")
    print("      CPE38 **StarBUG Cafe    ")
    print("  Report for Coffee sold today")
    print("++++++++++++++++++++++++++++++++")
    d = {}
    for cup in order:
        coffee_type = cup.get_coffee_type()
        if coffee_type in d:
            d[coffee_type] += 1
        else:
            d[coffee_type] = 1
        total += cup.get_price()
    # print(d.items())
    d = sorted(d.items(), key=lambda x: menu_order.index(x[0]))
    for c, n in d:
        print(f" {c:<24}{n}", end=" ")
        if n > 1:
            print("cups")
        else:
            print("cup")
    print()
    price_f = f"{total:,}"
    print(f"Total sold amount{price_f:>10} baht")
    print("++++++++++++++++++++++++++++++++")
    print("       What's a good day!     ")
    print("++++++++++++++++++++++++++++++++")


def runStarBUGcafe_main():
    global menu, addon
    menu = csv2list(coffee_menu_CSV)
    addon = csv2list(add_on_menu_CSV)
    a_map = {i + 1: row[0] for i, row in enumerate(addon)}
    order = []

    while True:
        print("Welcome to CPE38 **StarBUG Cafe!")
        printMenu(menu)
        printAddon(addon)
        name = readName()
        if name == "Good Day":
            printStarReceipt(order)
            break
        customer = CustomerBill(name)
        n_order = readNOrder()
        for i in range(n_order):
            c_name, n_m = readCup(i + 1)
            d_type, price = readDrinkType(n_m, i + 1)
            cup = CupOfCoffee(c_name, d_type, price)
            while True:
                try:
                    n_a = input(f"Cup #{i+1}, please select add on (enter for exit): ")
                    if n_a == "":
                        break
                    if (int(n_a) <= 0 or int(n_a) > len(addon)) and n_a != "":
                        print(" ERROR: Invalid input!")
                    else:
                        a, p = a_map[int(n_a)], int(addon[int(n_a) - 1][1])
                        if a in cup.get_addon():
                            print(" ERROR: Invalid input!")
                        else:
                            cup.set_add_on(a, p)
                    if len(cup.get_addon()) == len(addon):
                        break
                except ValueError:
                    print(" ERROR: Invalid input!")
            print(cup)
            order.append(cup)
            customer.add_ordered_coffee(cup)
        customer.receipt()


coffee_menu_filename = "./testcase/CoffeeMenu01.txt"
coffee_menu_CSV = readMenu(coffee_menu_filename)
addon_menu_filename = "./testcase/CoffeeMenuAddOn01.txt"
add_on_menu_CSV = readMenu(addon_menu_filename)

# menu = csv2list(coffee_menu_CSV)
# printMenu(menu)

runStarBUGcafe_main()
