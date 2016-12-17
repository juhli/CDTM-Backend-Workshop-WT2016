class Person:
    def __init__(self, name, age, study_subject):
        self.name = name
        self.age = age
        self.study_subject = study_subject
        self.car = None

    def growing_older(self):
        self.age = self.age+1

class Car:
    def __init__(self, color, age, wheels):
        self.color = color
        self.age = age
        self.wheels = wheels

if __name__ == "__main__":
    person1= Person("Juli", 25, "World dominance")
    person1.growing_older()
    print person1.name, person1.age, person1.study_subject
    print vars(person1)
    car1= Car("gold", "11m", 4)
    print vars(car1)