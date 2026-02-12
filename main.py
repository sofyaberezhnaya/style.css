from flask import Flask
import random

app = Flask(__name__)
facts_list = {
    "Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства."
    "зучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время."
    "Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение."
}

@app.route("/")
def home():
    return "<h1>Добро пожаловать на сайт ! </h1>"
     
@app.route("/randomfacts")
def random_fact():
    return f'<p>{random.choice(facts_list)}</p>'
@app.route("/secret")
def secret():
    return "<h1>Ты нашёл тайную страницу!" 
from random import randint
print("Привет. Можем поиграть в одну игру")
ans = int(input("Я загадываю число от 1 до 100, а ты угадываешь. Начинай"))
my_num = randint(0, 100)

while True:
    if ans > my_num:
        print("Меньше")
        ans = int(input("Я загадал другое число"))
    if ans < my_num:
        print("Больше")
        ans = int(input("Пробуй другие варианты"))
    if ans == my_num:
        print("Молодец ты угадал!")
        my_num = randint(0, 100)
        ans = int(input("Я загадал другое число попробуй угадать его"))
app.run(debug=True)
  

