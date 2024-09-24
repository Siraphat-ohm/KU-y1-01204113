class Radio:
    def __init__(self, mode="FM", frequency=87.5):

        self.mode = mode
        self.frequency = frequency

    def _is_in_fm(self, f):
        return f >= 87.5 and f <= 108

    def _is_in_am(self, f):
        return f >= 150 and f <= 280

    def set_mode(self, mode):
        if mode == "AM":
            self.frequency = 150
            self.mode = mode
        else:
            self.frequency = 87.5
            self.mode = mode

    def set_frequency(self, frequency):
        if self.mode == "AM" and self._is_in_am(frequency):
            self.frequency = frequency
        elif self.mode == "FM" and self._is_in_fm(frequency):
            self.frequency = frequency

    def get_mode(self):
        return self.mode

    def get_frequency(self):
        return self.frequency

    def adjust_frequency(self, x):
        n_f = self.frequency + x
        if (self.mode == "AM" and self._is_in_am(n_f)) or (
            self.mode == "FM" and self._is_in_fm(n_f)
        ):
            self.frequency = n_f
            return True
        else:
            return False

    def __str__(self):
        unit = "MHz"
        if self.mode == "AM":
            unit = "kHz"
        return f"{self.mode} Radio: {self.frequency:.1f} {unit}"


############## test case for Radio class
def print_des(a):
    print("mode:", a.get_mode())
    print("freq:", a.get_frequency())
    print("str:", a)
    print("")


def do_set_freq(a, fre):
    a.set_frequency(fre)
    print(f"set_frequency({fre})")
    print_des(a)


def do_set_mode(a, mode):
    a.set_mode(mode)
    print(f"set_mode({mode})")
    print_des(a)


def do_adjust(a, adjust):
    b = a.adjust_frequency(adjust)
    print(f"adjust({adjust})")
    print(f"return: {b}")
    print_des(a)
    return b


a = Radio()
b = False
print("Init")
print_des(a)
a.set_mode("AM")
print("a.set_mode(AM)")
print_des(a)
do_set_freq(a, 149.9)
do_set_freq(a, 270)
do_set_freq(a, 280.0001)
do_set_freq(a, 280)
do_set_mode(a, "FM")
do_set_freq(a, 10)
do_set_freq(a, 107.9)
do_set_freq(a, 108.1)
do_set_freq(a, 108)
do_set_freq(a, 87.5)
do_adjust(a, 0.5)
do_adjust(a, -5)
do_adjust(a, 19.9)
do_adjust(a, 0.1)
do_adjust(a, 1)
do_adjust(a, -20.5)
do_adjust(a, 0.0001)
do_set_mode(a, "AM")
do_adjust(a, -0.001)
do_adjust(a, 100.51)
do_adjust(a, -0.51)
do_adjust(a, 30)
do_adjust(a, 20.5)
do_adjust(a, -2000)
do_adjust(a, -130)
