# Задание 2 - Импортируй нужные классы
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from urllib.request import urlopen

class Question:

    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    # Задание 1 - Создай геттер для получения текста вопроса
    @property #Декоратор, позволяющий вызвать метод по имени без скобок и добавляет в метод поле setter
    def text(self):
        return self.__text
    
    def gen_markup(self):
    
        markup = InlineKeyboardMarkup() # Клавиатура, привязанная к сообщению
        markup.row_width = len(self.options)
        #print(markup)
        for i,option in enumerate(self.options):
            if i == self.__answer_id:
                markup.add(InlineKeyboardButton(option, callback_data="correct",switch_inline_query_current_chat="links"))
                
            else:
                markup.add(InlineKeyboardButton(option, callback_data="wrong",switch_inline_query_current_chat="links"))    
       # Задание 3 - Создай метод для генерации Inline клавиатуры
        return markup

# Задание 4 - заполни список своими вопросами


#url = "./1.jpg"
url1 = "Пишут мемы "+"https://yaustal.com/uploads/posts/2025-06/5fede51a6e_bolshoj-sbornik-smeshnyh-memov-i-kartinok-0.jpg"
url2 = ""
url3 = ""
url4 = ""
quiz_questions = [
    Question("Что котики делают, когда никто их не видит?", 1, "Спят", url1),
    Question("Как котики выражают свою любовь?", 0, "Громким мурлыканием", "Отправляют фото на Instagram", "Гавкают"),
    Question("Какие книги котики любят читать?", 3, "Обретение вашего внутреннего урр-мирения", "Тайм-менеджмент или как выделить 18 часов в день для сна", "101 способ уснуть на 5 минут раньше, чем хозяин", "Пособие по управлению людьми"),
    Question("Какие блюда готовят котики?", 2, "Сар-р-р-рдельки в собственном соку", "Скумбрия с хвостом", "Мышки в кошке")
]

