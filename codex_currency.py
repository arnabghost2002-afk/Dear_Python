pesos= float(input("Enter pesos: "))
soles= float(input("Enter soles: "))
reais= float(input("Enter reais: "))
 

usd = (pesos * 0.000306) + (soles * 0.298) + (reais * 0.195)
print("TOTAL $: ",usd)
