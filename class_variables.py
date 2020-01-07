class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def calc_circumference(self):
        return 2*self.radius*self.pi
    
# Circle.pi=7.4 
c=Circle(2)
c.pi=23
print(c.calc_circumference())
print(c.__dict__)