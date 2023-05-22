p=int(input("enter the amount: "))
r=float(input("enter the rate of interest: "))
t=float(input("enter the time of loan(in years): "))

compound_interest=p*(1+r/100)**t-p
print (f" the C.I is: {compound_interest}")
