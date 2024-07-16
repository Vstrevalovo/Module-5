class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            x = 1
            while x != 1+new_floor:
               print(x)
               x += 1
Domik = House('Остров', 41)
print(Domik.name, Domik.number_of_floors)
Domik.go_to(14)
Domik.go_to(-2)
Domik.go_to(57)
print(' ')
print('данные из задания')
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)



