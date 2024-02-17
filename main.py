
#Задача
#Создайте базовый класс "Школьный предмет" с общими характеристиками (например, название, уровень сложности).
# Затем создайте подклассы для различных предметов, таких как "Математика" и "Литература", добавляя уникальные свойства и методы для каждого предмета.
# Реализуйте методы для вычисления средней оценки по предмету.







class Subject:
    def __init__(self, name, level):
        self.name = name
        self.level = level


    def show_name(self):
        print(self.name)

    def show_level(self):
        print(self.level)



class Literature(Subject):
    grade2 = 0
    def __init__(self, Subname1, subject_level1):
        Subject.__init__(self, Subname1, subject_level1)



class Math(Subject):
    grade = 0
    def __init__(self, Subname, subject_level):
        Subject.__init__(self, Subname, subject_level )


def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum




    def about_grade(self):
        return self.grade


math_grade1 = 4545545
math_grade2 = 4555


sub1 = Math('Математика', '10')
print('Название предмета:')
sub1.show_name()
print('Уровень сложности предмета:')
sub1.show_level()
print('Средний балл по предмету математика:')
print(sum_of_digits(math_grade1)/len(str(math_grade1)))


sub2 = Literature('Литература', '8')
print('Название предмета:')
sub2.show_name()
print('Уровень сложности предмета:')
sub2.show_level()
print('Средний балл по предмету литература:')
print(sum_of_digits(math_grade2)/len(str(math_grade2)))