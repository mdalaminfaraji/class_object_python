class Student:
    def __init__(self, name, current_class, id):
        self.name=name
        self.current_class=current_class
        self.id=id
    def __repr__(self) -> str:
        return f'student name: {self.name} , class: {self.current_class} , Id: {self.id}'

alamin=Student('Alia Torkari', 4, 3)
print(alamin)