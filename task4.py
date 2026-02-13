#!python3
"""
Compound Interest Calculator
Create a class object that accepts paramters for Principal, Annual Interest Rate, Number of compounding periods.  
Create a class method that calculates the amount of compound interest for a given length of time.

Extension: accept time given in different measurements, but convert them to years for use in your class template.
"""


class Calc:
    principal = 0
    rate = 0
    nPeriods = 0

    def __init__(self, P, r, n):
        #more input parameters needed
        self.principal = P
        self.rate = r/100
        self.nPeriods = n
        return
    
    def timeconvert(self):
        measure = input("Which time measurement would you like to use? (Years, Months, Days): ")
        if measure == "months" or measure == "Months":
            self.adjtime = self.time / 12
        elif measure == "days" or measure == "Days":
            self.adjtime = self.time / 365
        elif measure == "years" or measure == "Years":
            self.adjtime = self.time
        else:
            print("invalid input")
        return self.adjtime

    def interest(self,t):
        self.time = t
        newtime = self.timeconvert()
        interest = self.principal * ((1 + (self.rate/self.nPeriods)) ** (self.nPeriods * newtime))
        gained = interest - self.principal
        print(gained)
        return round(gained,2)
    
    def amount(self,t):
        self.time = t
        newtime = self.timeconvert()
        interest = self.principal * (1 + (self.rate/self.nPeriods)) ** (self.nPeriods * newtime)
        print(interest)
        return round(interest,2)

daytest = Calc(P=1000, r=4, n=2) #Use day option for this assertion
assert daytest.interest(365) == 40.40
assert daytest.amount(365) == 1040.40

monthtest = Calc(P=1000, r=4, n=2) #Use month option for this assertion
assert daytest.interest(12) == 40.40
assert daytest.amount(12) == 1040.40

#Use years for the next ones

a = Calc(P=1000,r=4,n=2)
assert a.interest(3) == 126.16
assert a.amount(5) == 1218.99

b = Calc(P=5000,r=5.25,n=12)
assert b.interest(10) == 3442.62

