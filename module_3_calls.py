calls = 0
def count_calls():   #подсчитывающая вызовы остальных функций
    calls =+ 1          #Эта функция должна вызываться в остальных двух функциях.
    print(calls)

def string_info(string, a=None):
    a = []
    a.append(len(string))
    a.append(string.upper())
    a.append(string.lower())
    tuple(a)
    print(a)
    print(count_calls())

def is_contains(s, list=[]):
    string = s.lower()
    list_to_search = [i.lower() for i in list]
    if any(string in i for i in list_to_search):
        print(True)
    else:
        print(False)
    print(count_calls())

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)