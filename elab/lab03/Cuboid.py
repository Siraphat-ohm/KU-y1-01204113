def compute_rectangle_area(w, l):
    return w * l


def compute_surface_area(w, l, h):
    r1 = compute_rectangle_area(w, l)
    r2 = compute_rectangle_area(w, h)
    r3 = compute_rectangle_area(l, h)
    return r1 * 2 + r2 * 2 + r3 * 2


def compute_volume(w, l, h):
    return w * l * h


def readInput():
    w = float(input("Enter width: "))
    l = float(input("Enter length: "))
    h = float(input("Enter height: "))
    return (w, l, h)


w, l, h = readInput()

print(f"For [{w:.2f} x {l:.2f} x {h:.2f}] cuboid: ")
print(f"Surface area = {compute_surface_area(w,l,h):.3f}")
print(f"Volume = {compute_volume(w,l,h):.3f}")

print()

w, l, h = w * 2, l * 2, h * 2
print("After doubling each side,")
print(f"For [{w:.2f} x {l:.2f} x {h:.2f}] cuboid: ")
print(f"Surface area = {compute_surface_area(w,l,h):.3f}")
print(f"Volume = {compute_volume(w,l,h):.3f}")
