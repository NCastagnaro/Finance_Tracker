class Person:
    population = 0  # Class-level variable

    def __init__(self, first_name,last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Person.population += 1  # Modify the class-level variable
        
    #method used to help format the first and last name of the employees    
    def fullname(self):
        return '{} {}'.format(self.first_name,self.last_name)

    @classmethod
    def get_population(cls):
        print(f"Current population: {cls.population}")

# Creating instances of the Person class
#"person1" and "person2" are going to be passed in as "self" to the __init__ method
person1 = Person("Alice", "Z", 30)
person2 = Person("Bob", "L", 40)

# Calling a class method on the class
Person.get_population()  # Output: Current population: 2

#Prints out fullname of person1
print(person1.fullname())
print(Person.fullname(person1)) #This is how you would retrieve the full name if you were to start with calling the class



