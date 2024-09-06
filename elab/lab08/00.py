import random
import time

# import turtle


class Card:
    # """Card(): create a card object. To create a deck, try \Card.test_Card()\!"""

    symbols = {"D": "♦", "C": "♣", "H": "♥", "S": "♠"}

    def __init__(self, name, suit):
        self.name = name
        self.suit = suit

    def get_name(self):
        return self.name

    def get_suit(self):
        return self.suit

    def __repr__(self):
        return f"{self.name}{Card.symbols[self.suit]}"

    def test_Card(self):
        Names = ["A", 2, 3, 4, 5, 6, 7, 8, 9, "T", "J", "Q", "K"]
        Suits = ["D", "C", "H", "S"]
        deck = [Card(str(n), s) for s in Suits for n in Names]
        random.shuffle(deck)
        res = [str(card) for card in deck]
        return " ".join(res)


class Deck:
    """Deck(): สร้างสำรับไพ่"""

    Names = ["A", 2, 3, 4, 5, 6, 7, 8, 9, "T", "J", "Q", "K"]
    Suits = ["D", "C", "H", "S"]

    def __init__(self):
        Names, Suits = Deck.Names, Deck.Suits
        self.cards = [Card(str(n), s) for s in Suits for n in Names]

    def shuffle(self):
        random.shuffle(self.cards)

    def get_card(self):
        return self.cards.pop()

    def set_cards(self, cards):
        self.cards = cards

    def reset(self, n=1):
        Names, Suits = Deck.Names, Deck.Suits
        self.cards = [Card(str(n), s) for s in Suits for n in Names]
        for i in range(n):
            self.shuffle()

    def __repr__(self):
        res = [str(x) for x in self.cards]
        return " ".join(res)


def createVirtualDeck(s="K♣ Q♠ A♣ 3♥ 2♠ 6♥ 8♥ 9♥ J♠ 4♦ 2♥ 9♠"):
    dd = s.split()
    res = []
    suit = {"♦": "D", "♣": "C", "♥": "H", "♠": "S"}
    for d in dd:
        card = Card(d[0], suit[d[1]])
        res.append(card)
    deck = Deck()
    deck.set_cards(res)
    return deck


class Player:
    def __init__(self, name="Player", deck=Deck()):
        self.cards = [deck.get_card()]
        self.name = name
        self.deck = deck
        self.is_blak_jack = False

    def get_cards(self):
        return "".join([f"{c} " for c in self.cards])

    def hit(self):
        self.cards.append(self.deck.get_card())

    def get_num_cards(self):
        return len(self.cards)

    def _calculate_points(self, cards):
        points = 0
        aces = 0

        for card in cards:
            if card.name.isdigit():
                points += int(card.name)
            elif card.name == "A":
                aces += 1
            else:
                points += 10

        points += aces * 11

        while points > 21 and aces > 0:
            points -= 10
            aces -= 1

        return points

    def get_point(self, i):
        return self._calculate_points([self.cards[i]])

    def get_points(self):
        return self._calculate_points(self.cards)

    def get_is_black_jack(self):
        num_cards = self.get_num_cards()
        if self.get_point(0) + self.get_point(1) == 21 and num_cards == 2:
            return True
        elif num_cards == 5 and self.get_points() <= 21:
            return True
        return False

    def __str__(self):
        return f"{self.name:>9}: {self.get_cards():<16}-> {self.get_points()}"


class Computer(Player):
    def __init__(self, name="Computer", deck=Deck()):
        self.hidden = True
        Player.__init__(self, name, deck)

    def switch_hidden(self):
        self.hidden = not self.hidden

    def get_cards(self):
        if self.hidden:
            return f"O{self.cards[0].__repr__()[1]} " + "".join(
                [f"{c} " for c in self.cards[1:]]
            )
        else:
            return "".join([f"{c} " for c in self.cards])

    def get_points(self):
        if self.hidden:
            return self._calculate_points(self.cards[1:])
        else:
            return self._calculate_points(self.cards)


def play(player1="Computer", player2="Player", d=None, RENDER=False):
    print("Welcome to MikeLab BlackJack Casino.")
    # preamble(RENDER)
    # create a deck of cards
    if d == None:
        deck = Deck()
        deck.reset()
    else:
        # ----------------------------- virtual deck
        # d = 'A♦ A♥ 3♥ 4♣ 4♥ 7♣ 5♣ 6♦ A♠'
        deck = createVirtualDeck(d)
    # ----------------------
    # print(deck)  # for DEBUG
    # ----------------------
    ###-------------- student code begins here --------------###

    com = Computer(player1, deck)
    p = Player(player2, deck)

    com.hit()
    p.hit()

    com_points = com.get_points()
    p_points = p.get_points()

    print(com)
    print(p)

    while True:
        if p.get_num_cards() >= 5 or p_points >= 21:
            break
        q = input("Draw another card (y/n): ").lower()
        if q == "y":
            p.hit()
            p_points = p.get_points()
            print(p)
            continue
        break

    com.switch_hidden()
    com_points = com.get_points()

    while True:
        if p_points > 21:
            if com_points <= 16 and com_points < 21 and com.get_num_cards() < 5:
                com.hit()
                com_points = com.get_points()
            else:
                break
        else:
            if (
                (com_points <= 16 or com_points < p_points or p.get_is_black_jack())
                and com_points < 21
                and com.get_num_cards() < 5
            ):
                com.hit()
                com_points = com.get_points()
            else:
                break

    print("+++++++++++++++++++++++++++++++++")
    print(com)
    print(p)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")
    if (
        (p.get_is_black_jack() and com.get_is_black_jack())
        or (com_points == p_points)
        or (com_points > 21 and p_points > 21)
    ):
        print("Draw!")
    elif (
        (p.get_is_black_jack() or p_points > com_points or com_points > 21)
        and p_points <= 21
        and not com.get_is_black_jack()
    ):
        print(f"{p.name} wins.")
    else:
        print(f"{com.name} wins.")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")


## main begins here
def testcase01():
    random.seed(2)
    play()


def testcase02():
    random.seed(16)
    play()


def testcase03():
    random.seed(30)
    play()


def testcase04():
    s = "K♣ Q♠ A♣ 3♥ 2♠ 6♥ 8♥ 9♥ J♠ 4♦ 2♥ 9♠"
    play("Toto", "Tutu", d=s)


def testcase05():
    s = "A♣ 3♥ 2♠ T♥ 8♥ A♠ A♦ 2♥ 3♠"
    play(d=s)


def testcase06():
    s = "4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ 2♥ 3♠"
    play(d=s)


def testcase07():
    s = "4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ 2♥ T♠"
    play(d=s)


def testcase08():
    s = "4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ Q♥ 3♠"
    play(d=s)


def testcase09():
    s = "5♠ A♥ A♣ 8♥ J♠ 4♥ 5♥ A♠ A♦ 2♥ 3♠"
    play(d=s)


# ------------------------------------------
q = int(input())
if q == 1:
    testcase01()
elif q == 2:  # Ex3
    testcase02()
elif q == 3:  # Ex4
    testcase03()
elif q == 4:  # Ex5
    testcase04()
elif q == 5:  # Ex8
    testcase05()
elif q == 6:  # Ex9
    testcase06()
elif q == 7:
    testcase07()
elif q == 8:
    testcase08()
elif q == 9:
    testcase09()
