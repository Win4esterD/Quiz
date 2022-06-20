#стр 574 Задача 9. Викторина
import random
class Question:

    def __init__(self, question, answer1, answer2, answer3, answer4):

        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4


    def __str__(self):
        return f'{self.question}\n 1){self.answer1}\n 2){self.answer2}\n 3){self.answer3}\n 4){self.answer4}'

    def __repr__(self):
        return f'{self.question}'

a = Question('На каком языке программирования написана это программа?', 'Java', 'C++', 'Python', 'HTML')
b = Question('Что такое ООП?', 'Очень опасная программа', 'Очки объективных пропорций',
 'Объектно ориентированное программирование', 'Очень опасный преступник')
c = Question('Как называется должность программиста с малым опытом?', 'Кодировщик',
'Junior разработчик', 'Нубяра', 'Тестировщик')
d = Question('Кто такой Recruter?', 'Специалист по работе с кадрами',
'Главный программист', 'Веб разработчик', 'Тот не возьмёт тебя на работу')
e = Question('Какой язык программирования самый популярный на 2021 год?', 'Javascript',
'C++', 'Python', 'Английский')
f = Question('Какая из этих операционных систем разработана компанией "Microsoft"?',
'Android', 'Windows', 'iOS', 'Linux')
g = Question('Какой из этих языков программирования является языком низкого уровня?',
'Ruby', 'C#', 'Javascript', 'Assembler')
i = Question('Сколько бит в одном байте?', '8', '16', '2', '4')
j = Question('Какая из этих фирм разрабатывает процессоры?', 'Razer', 'Logitech', 'Intel', 'ОАО "БЕЛАЗ"')
k = Question('Какая из этих фирм разрабатывает видеокарты?', 'Razer', 'Logitech', 'Intel', 'Nvidia"')

dicti = {a:3, b:3, c:2, d:1, e:1, f:2, g:4, i:1, j:3, k:4}


print('Добро пожаловать в игру \"Викторина". Игра для двоих игроков')
print('Игра для двоих игроков, Вам будут заданы вопросы, по 5 на каждого игрока.')
print('Игрок набравший большее количество очков будет объявлен победителем. Если')
print('же количество очков у обоих игроков будет равным, объявляется ничья.')
print()
player1 = input('Игрок 1, введите своё имя: ')
player2 = input('Игрок 2, введите своё имя: ')

temp = player2
count1 = 0
count2 = 0
answer = 0
print()
for i in dicti:
    if temp == player2:
        print(f'Игрок {player1}, вопрос Вам')
        print(i)
        answer = int(input())
        if answer == dicti[i]:
            count1 += 1
            print('Это правильный ответ')
            print()
        else:
            print('Это не правильный ответ')
            print()
        temp = player1
    elif temp == player1:
        print(f'Игрок {player2}, вопрос Вам')
        print(i)
        answer = int(input())
        if answer == dicti[i]:
            count2 += 1
            print('Это правильный ответ')
            print()
        else:
            print('Это не правильный ответ')
            print()
        temp = player2

if count1 == count2:
    print(f'Поздравляю, у Вас ничья, вы набрали по {count1} очков.')
elif count1 > count2:
    print(f'{player1}, поздравляем с победой. Вы набрали {count1} очков')
    print(f'{player2} набрал {count2} очков')
else:
    print(f'{player2}, поздравляем с победой. Вы набрали {count2} очков')
    print(f'{player1} набрал {count1} очков')
