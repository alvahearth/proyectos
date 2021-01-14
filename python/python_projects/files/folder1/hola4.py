def computepay(xh, xr):
    if xh > 40:
        regularpay = xh * xr
        overtimepay = (xh - 40) * (xr * 0.5)
        pay = regularpay + overtimepay
        return pay
    else:
        normalpay = xh * xr
        return normalpay


hours = input("Enter Hours: ")
rate = input("Enter Rate:")

xh = float(hours)
xr = float(rate)

finalpay = computepay(xh, xr)
print("Pay", finalpay)
