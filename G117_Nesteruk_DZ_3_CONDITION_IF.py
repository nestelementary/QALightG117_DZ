"""Необходимо создать код, в котором будет фигурировать три элемента,
которые Вы как пользователь программы будете вводить после запуска кода.
Данный код буде проверять эти элементы по следующей логике:
Если А больше Б, тогда вывести в консоль "Свершилось!"
Если Б больше А, тогда вывести в консоль "Да ну!"
Если А и Б равны, тогда вывести в консоль "А если так?" и прибавить к А В, а от Б отнять В и заново сравнить."""
print('Завдання "Порівняння А і B"')
print('Будь ласка, задайте число A:')
A = float(input())
print('Будь ласка, задайте число B:')
B = float(input())
print('Будь ласка, задайте число C:')
C = float(input())
if A > B:
    print('Задане Вами А =', A, 'є більшим за В =', B, '. Наше завдання виконане!')
elif A < B:
    print('Задане Вами А =', A, 'є меншим за В =', B, '. На жаль, це не те, що нам було потрібно((')
else:
    print('Задані Вами А =', A, 'і В =', B, 'дорівнюють одне одному. Спробуємо збільшити A на В, а В зменшити на С.')
    A = A + B
    B = B - C
    if A > B:
        print('Наші дії виявились успішними: А =', A, 'і стало більшим за В =', B, '. Завдання виконано!')
    elif A < B:
        print('Нас спіткала невдача, А =', A, 'стало меншим за В =', B, 'і, на жаль, це не те, що нам було потрібно((')
    else:
        print('Дивно, нове значення А =', A, 'дорівнює новому значенню В =', B, '. Цікаво, як таке могло статись?')