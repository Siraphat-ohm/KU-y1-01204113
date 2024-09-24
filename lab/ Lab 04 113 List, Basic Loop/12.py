et = int(input("Estimated time : "))
w = et // 7
pt, wt, ft = 0, 0, 0

for i in range(w):
    print(f"Week{i+1}")
    p = int(input("Physical therapy : "))
    w = int(input("Weight training : "))
    f = int(input("Fitness training : "))
    pt += p
    wt += w
    ft += f


if pt >= et * 2.5 and wt >= et * 2.5 and ft >= et * 2.5:
    print("Buzzy has recovered in time.")
else:
    print("Buzzy has not recovered in time.")
