class Laptop:
    def __init__(self,laptop_brand,laptop_prise):
        self.laptop_brand=laptop_brand
        self.laptop_prise=laptop_prise
        
    def discount(self,per):
        return (self.laptop_prise*40)/100
    
l1=Laptop('dell',24000)
l2=Laptop('hp',35000)
print(l1.discount(40))
print(f"off prise==={l2.discount(50)}")

