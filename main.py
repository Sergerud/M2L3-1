
import telebot
from config import token
# Задание 7 - испортируй команду defaultdict
from collections import defaultdict
from logic import quiz_questions

user_responses = {} 
# Задание 8 - создай словарь points для сохранения количества очков пользователя
points = defaultdict(int) #словарь с дефолтным значением для любого нового ключа
bot = telebot.TeleBot(token)
count_quest=0

def send_question(chat_id):
    
    bot.send_message(chat_id, quiz_questions[user_responses[chat_id]].text, 
                     reply_markup=quiz_questions[user_responses[chat_id]].gen_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global count_quest, points

    if call.data == "correct":
        points[call.message.chat.id] += 1
        bot.answer_callback_query(call.id, "Answer is correct")
        
        # Задание 9 - добавь очки пользователю за правильный ответ
    elif call.data == "wrong":
        bot.answer_callback_query(call.id,  "Answer is wrong")
    
    # Задание 5 - реализуй счетчик вопросов
    user_responses[call.message.chat.id]+=1  
    # Задание 6 - отправь пользователю сообщение с количеством его набранных очков, если он ответил на все вопросы, а иначе отправь следующий вопрос
    
    if user_responses[call.message.chat.id]>=len(quiz_questions):
        bot.send_message(call.message.chat.id, "The end")
        bot.send_message(call.message.chat.id, "Правильных ответов "+str(points[call.message.chat.id]))
    else:
        send_question(call.message.chat.id)

@bot.message_handler(commands=['start'])  #Обработчик команды start
def start(message):
    if message.chat.id not in user_responses.keys():
        user_responses[message.chat.id] = 0
        send_question(message.chat.id)
    else:    
        points.clear
        count_quest=0
        user_responses[message.chat.id] = 0
        send_question(message.chat.id)
        #print(count_quest)
        

bot.infinity_polling()
