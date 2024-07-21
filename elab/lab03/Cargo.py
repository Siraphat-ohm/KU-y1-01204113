from math import ceil


def travel_time(s, d):
    """calculate total days to travel distance d using speed s.
    A fraction of day is roundup to full day"""
    hours = d / s
    day = ceil(hours / 24)
    return day


def travel_speed(w):
    """calculate traveling speed using a formular that is given in the problem"""
    return 90 / (30 + w) + 5


def cal_sub_profit(d, n_w, s_w, p_c, p_s):
    """calculate profit that is received when travel from a town to a next town"""
    speed = travel_speed(n_w)
    cargo_price = s_w * p_c
    supply_price = travel_time(speed, d) * p_s
    return cargo_price - supply_price


def readInput():
    w_a = float(input("weight of cargo to A: "))
    w_b = float(input("weight of cargo to B: "))
    w_c = float(input("weight of cargo to C: "))
    w_o = float(input("weight of cargo to O: "))

    p_a = float(input("price of cargo to A: "))
    p_b = float(input("price of cargo to B: "))
    p_c = float(input("price of cargo to C: "))
    p_o = float(input("price of cargo to O: "))
    p_s = float(input("price of supply: "))

    d_oa = float(input("distance O to A: "))
    d_ab = float(input("distance A to B: "))
    d_bc = float(input("distance B to C: "))
    d_co = float(input("distance C to O: "))

    return (
        (w_a, w_b, w_c, w_o),
        (p_a, p_b, p_c, p_o, p_s),
        (d_oa, d_ab, d_bc, d_co),
    )


def calculate_profit(n):
    n_w = sum(n[0])
    profit = 0
    for i in range(4):
        w = n[0][i]
        p = n[1][i]
        d = n[2][i]
        p_s = n[1][-1]
        profit += cal_sub_profit(d, n_w, w, p, p_s)
        n_w -= w
    return profit


profit = calculate_profit(readInput())
print(f"result profit is {profit:.3f}")
