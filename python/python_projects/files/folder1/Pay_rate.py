def payment(hours,rate):
    if fh > 40:
      print("overtime")
      reg = hours * rate
      otp = (hours - 40) * (rate * 0.5)
      print(reg,otp)
      pago = reg + otp
      return pago
    else:
      pago = hours * rate
      print("regular")
      return pago

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
   fh = float(sh)
   fr = float(sr)
except:
    print("Invalid, Enter a numeric value")
    quit()

xp = payment(fh,fr)

print("Pay: ",xp)