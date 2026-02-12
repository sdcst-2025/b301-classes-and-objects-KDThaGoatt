import os

class quadfunc:

    os.system("clear||cls")
    print("- Quadratic Equation Calculator - ")
    print("You will enter a quadratic in standard form")
    print("          ax² + bx + c")
    print("I will ask you for the coefficients")
    print("I will then tell you several things about the quadratic")
    print("I hope you are ready, this poop is about to get real!\n")

    def getCoeffs(self):
        self.vars = ['a','b','c']
        for i in range(3):
            while True:
                try:
                    coeff = int(input(f"Enter coefficient {self.vars[i]} > "))
                    self.vars[i] = coeff 
                    break
                except:
                    print("invalid! It must be an integer. Try again")

    def easyConvert(self):
        self.a = self.vars[0]
        self.b = self.vars[1] 
        self.c = self.vars[2]

    def getVertex(self):
        self.x = -(self.b)/(2*self.a)
        self.y = self.a*self.x**2 + self.b*self.x + self.c

    def getVertexForm(self):
        if self.x < 0:
            bracket = f"(x + {round(-1*self.x,2)})"
        else:
            bracket = f"(x - {round(self.x,2)})"
        if self.y < 0:
            constant = f"- {round(-1*self.y,2)}"
        else:
            constant = f" + {round(self.y)}"
        self.vertexForm = f"{round(self.a,2)}{bracket}² {constant}"

    def getDiscriminant(self):
        self.discriminant =  self.b**2 - 4*self.a*self.c

    def getXInt(self):
        self.roots = []
        if self.discriminant >= 0:
            r1 = round((-(self.b) + self.discriminant**(0.5))/(2*self.a),3)
            r2 = round((-(self.b) - self.discriminant**(0.5))/(2*self.a),3)
            self.roots.append(r1)
            self.roots.append(r2)
        else:
            self.roots.append('non real')
            self.roots.append('non real')

    def __init__(self):
        #ask user for coefficients
        self.getCoeffs()
        self.easyConvert()
        self.getDiscriminant()
        self.getVertex()
        print(f"The vertex is at x={round(self.x,2)}, y={round(self.y,2)}")
        #determine vertex form of parabola
        self.getVertexForm()
        print(f"The vertex form is {self.vertexForm}")
        #determine y-intercept
        print(f"The y-intercept is {round(self.c,2)}")
        #determine x-intercepts (if they exist)
        self.getXInt()
        print(f"The roots are {self.roots}")
        #determine directino of opening
        if self.a > 0:
            print("The parabola opens upwards")
        elif self.a < 0:
            print("The parabola opens downwards")
        else:
            print("The parabola does not exist")

calculate = quadfunc()

while True:
    question = input("Would you like to calculate another quadratic? (y or n): ")
    if question == "y" or question == "Y" or question =="yes" or question == "Yes":
        quadfunc()
    if question == "n" or question == "N" or question =="no" or question == "No":
        print("exiting...")
        break
    else:
        print("invalid input")