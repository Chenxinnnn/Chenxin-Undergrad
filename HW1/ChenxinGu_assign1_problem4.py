#ChenxinGu, YuxuanDu, Sep 17th, Section 003, ChenxinGu_assign1_problem4.py
#Use space and dashes to print the title
print("--------------------------------------------------------------")
print("                mL to US Fluid Volume Units")
print("--------------------------------------------------------------")

#Define each varialbe and use float function to save each variable as a float.
ml = float(250.0)
tsp = float(0.202884 * ml)
tbsp = float(tsp / 3)
cup = float(tbsp / 16)
pint = float(cup /2)
quart = float(pint / 2)
gallon = float(quart / 4)
floz = float(ml / 29.5735)

#Print out all the results of math calculation above.
print("	mL:		", ml)
print("	tsp:		", tsp)
print("	tbsp:		", tbsp)
print("	cup(s):		", cup)
print("	pint(s):	", pint)
print("	quart(s):	", quart)
print("	gallon(s):	", gallon)
print("	fl oz:		", floz)

#End with dashes.
print("--------------------------------------------------------------")


