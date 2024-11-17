#Задача "Рассылка писем"
def send_email(message, recipient, sender = 'university.help@gmail.com'):
    rashir = ['.com', '.ru', '.net']
    rec = str(recipient.endswith)
    for i in rashir:
        if (recipient.endswith, sender.endswith) != i:
    #if not any(item in str(recipient.endswith) for item in rashir):
    #if not recipient.endswith('.com') and recipient.endswith('.ru') and recipient.endswith('.net') and sender.endswith('.com') and sender.endswith('.ru') and sender.endswith('.net'):
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
            print(recipient.endswith)
    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')