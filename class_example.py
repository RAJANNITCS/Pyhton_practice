class Person:
    count_instance=0#class variable/class attribute
    
    def __init__(self,first_name,last_name):
        Person.count_instance += 1
        self.first_name=first_name
        self.last_name=last_name
    @classmethod
    def from_string(cls,string):
        first_name,last_name=string.split(",")
        return cls(first_name,last_name)
    @classmethod
    def count_instances(cls):
        return f"you have created {cls.count_instance} instan {cls.__name__} class"
    @staticmethod
    def hello():
        print("hello static method called")


# p1=Person('rajan','singh')
# p2=Person('rohit','singh')
# print(Person.count_instance)
# print(Person.count_instances())
# p1=Person.from_string('rajan,singh')
# print(p1.first_name)
Person.hello()