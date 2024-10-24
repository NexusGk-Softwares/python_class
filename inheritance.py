#dealing with python inheritance

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass
    
    def eat(self):
        pass
    
    def sleep(self):
        pass
    
    def introduce(self):
        print(f"I am {self.name} and I am {self.age} years old.")
        
    