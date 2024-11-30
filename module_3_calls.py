calls = 0

def count_calls():
    global calls
    calls = calls + 1
    return calls

def string_info(string, a=None):
    global calls
    calls = calls + 1
    a = []
    a.append(len(string))
    a.append(string.upper())
    a.append(string.lower())
    return a
#count_calls()

def is_contains(s, list):
    global calls
    calls = calls + 1
    string = s.lower()
    list_to_search = [i.lower() for i in list]
    if any(string in i for i in list_to_search):
        m = True
    else:
        m = False
    return m
#count_calls()

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
