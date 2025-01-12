calls = 0


def count_calls():  # счетчик вызовов
    global calls  # глобальное простаранство
    calls +=1


def string_info(string):
    count_calls()  # счетчик вызовов
    return (len(string), string.upper(),
            string.lower())  # возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.


def is_contains(string, list_to_search):
    count_calls()  # счетчик вызовов
    return (string.lower () in [i.lower() for i in list_to_search])
    #return string.upper() in (i.upper() for i in list_to_search )


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

print(calls)
