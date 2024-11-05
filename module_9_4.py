from random import choice


"""Задача №1"""

first = 'Мама мыла раму'
second = 'Рамена мало было'

result_task1 = list(map(lambda x, y: x.lower() == y.lower(), first, second))
print(result_task1)

"""Задача №2"""

def get_advanced_writer(file_name):
    
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for elem in data_set:
                file.write(f'{str(elem)}\n')
    
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

"""Задача №3"""

class MysticBall:
    
    def __init__(self, *words):
        
        self.words = words
    
    def __call__(self):
        
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball())
print(first_ball())
print(first_ball())