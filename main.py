import random

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
           'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
           'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
           'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
           'Перспективы не очень хорошие', 'Весьма сомнительно']
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Как Вас зовут?')
name = input()
print('Приветствую Вас,', name, '!')
again = 'д'
while again.lower() == 'д':
    question = input('Задай мне свой вопрос: ')
    print(random.choice(answers))
    again = input('Задать еще один вопрос? (д = да, н = нет): ')

    if not again.lower() == 'д':
        print('Возвращайся если возникнут вопросы!')

