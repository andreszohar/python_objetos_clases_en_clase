"""i=0
while i<10:
    i+=1
    print(i)"""


cash = float(input("ingrese el monto solicitado: "))
time = float(input("ingrese los meses del credito: "))
tax = 0.0158
base = cash / time
totalPay = 0

i=0
while i<time:
    interest = cash * (time-i) * tax
    share = (cash + interest)/(12-i)
    i+=1
    cash = cash-base
    totalPay= share + totalPay
    print("cuota # ",i ,": ", int(share))

print("Total pagado en el credito: ", int(totalPay))  