""" # Исходный список
myList = [
    "lion",     # 0
    "tiger",    # 1
    "elephant", # 2
    "giraffe",  # 3
    "zebra",    # 4
    "panda",    # 5
    "wolf",     # 6
    "kangaroo", # 7
    "fox",      # 8
    "bear",     # 9
]

# 1. extend() добавляет элементы из другого списка или итерации в конец текущего списка
myList.extend(["koala", "leopard"])
print(myList)
# ['lion', 'tiger', 'elephant', 'giraffe', 'zebra', 'panda', 'wolf', 'kangaroo', 'fox', 'bear', 'koala', 'leopard']

# 2. sort() сортирует список в алфавитном порядке (по умолчанию) или по ключу
myList.sort()
print(myList)
# ['bear', 'elephant', 'fox', 'giraffe', 'kangaroo', 'koala', 'leopard', 'lion', 'panda', 'tiger', 'wolf', 'zebra']

# 3. reverse() меняет порядок элементов на обратный
myList.reverse()
print(myList)
# ['zebra', 'wolf', 'tiger', 'panda', 'lion', 'leopard', 'koala', 'kangaroo', 'giraffe', 'fox', 'elephant', 'bear']

# 4. insert() вставляет элемент в указанную позицию
myList.insert(2, "dolphin")
print(myList)
# ['zebra', 'wolf', 'dolphin', 'tiger', 'panda', 'lion', 'leopard', 'koala', 'kangaroo', 'giraffe', 'fox', 'elephant', 'bear']

# 5. pop() удаляет элемент по индексу и возвращает его
removed_item = myList.pop(2)  # Удаляем элемент с индексом 2
print(removed_item)           # dolphin
print(myList)
# ['zebra', 'wolf', 'tiger', 'panda', 'lion', 'leopard', 'koala', 'kangaroo', 'giraffe', 'fox', 'elephant', 'bear']

# 6. clear() удаляет все элементы из списка
myList.clear()
print(myList)
# []

# Восстанавливаем список для дальнейших примеров
myList = [
    "lion", "tiger", "elephant", "giraffe", "zebra", 
    "panda", "wolf", "kangaroo", "fox", "bear"
]

# 7. copy() создает копию списка
copied_list = myList.copy()
print(copied_list)
# ['lion', 'tiger', 'elephant', 'giraffe', 'zebra', 'panda', 'wolf', 'kangaroo', 'fox', 'bear']

# 8. index() возвращает индекс первого вхождения указанного элемента
index_of_zebra = myList.index("zebra")
print(index_of_zebra)
# 4

# 9. remove() удаляет первое вхождение указанного элемента
myList.remove("zebra")
print(myList)
# ['lion', 'tiger', 'elephant', 'giraffe', 'panda', 'wolf', 'kangaroo', 'fox', 'bear']
 """

""" 
1.Создание списка и вывод
Создай список с элементами "Python", "JavaScript" и "C++". Выведи этот список на экран.
"""
""" myList = ["Python", "JavaScript", "C++"]
print(myList) """

""" 
2.Длина списка
У тебя есть список: 
Напиши код, который выводит количество элементов в этом списке.
"""

""" languages = ["Python", "JavaScript", "C++", "Java", "C#"]
print(len(languages)) """

""" 
3.Обращение по индексу
Используй список из второго задания. Напиши код, который выводит:

Первый элемент списка.
Последний элемент списка. 
"""

""" languages = ["Python", "JavaScript", "C++", "Java", "C#"]
print(languages[0]) #Первый элемент
print(languages[-1]) #Последний элемент
print(languages[len(languages) - 1]) #Последний элемент """

""" 
4.Замена элемента
В списке:
Замени "banana" на "kiwi" и выведи обновлённый список.
"""
""" fruits = ["apple", "banana", "cherry"]
fruits[1] = "kiwi"
print(fruits) """


"""
5.Проверка на существование
В списке:
Проверь, есть ли число 30 в этом списке. Если да, выведи "Found", иначе "Not Found". 
"""

""" numbers = [10, 20, 30, 40, 50]

if 30 in numbers:
    print("Found")
else:
    print("Not Found") """

"""
6.Добавление элемента
В список:
Добавь "hamster" и выведи обновлённый список.
"""

""" animals = ["cat", "dog", "rabbit"]
animals.append("hamster")
print(animals) """

"""
7.Удаление элемента
В списке из шестого задания удали "dog" и выведи результат.
"""

""" animals = ["cat", "dog", "rabbit"]
animals.remove("dog") # variant
animals.pop(1) # variant
del animals[1] # variant """


# Задачи:
"""
1.Список с разными типами данных
Создай список, который содержит следующие элементы: строку "hello", число 42, и булево значение True. 
Выведи этот список и тип его элементов.
"""

""" myList = ["hello", 42, True]
print(myList)

# Типы данных
print(type(myList[0]))
print(type(myList[1]))
print(type(myList[2]))

# Типы данных
print(*(type(elm) for elm in myList)) """


"""
2.Использование list() конструктора
Создай список из строки "banana" с помощью конструктора list(). Выведи результат.
"""

""" myList = list("banana")
myList2 = list(elm for elm in "banana")
print(myList)
 """
"""
3.Дубликаты в списке
У тебя есть список:
Напиши код, который выводит все уникальные элементы списка, сохраняя их порядок.
"""

""" fruits = ["apple", "banana", "apple", "cherry", "cherry"]
fruits_unique = []
for fruit in fruits:
    if fruit not in fruits_unique:
        fruits_unique.append(fruit)
print(fruits_unique) """


"""
4.Добавление нескольких элементов
Есть список:
Добавь в него элементы "yellow" и "purple" за одну операцию. Выведи результат.
"""

""" colors = ["red", "green", "blue"]
colors += ["yellow", "purple"]
colors.extend(["yellow", "purple"])
print(colors) """

"""
5.Удаление всех элементов
Удали все элементы из списка:
И выведи пустой список.
"""

""" numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)
 """


""" 
6.Копирование списка
Создай копию списка:
Убедись, что изменения в копии не влияют на оригинал.
"""

""" names = ["John", "Jane", "Joe"]
names_copy = names.copy()
 """
