# Cтворити функцію generator_numbers, яка буде аналізувати текст, ідентифікувати 
# всі дійсні числа, що вважаються частинами доходів, і повертати їх як генератор. 
# Реалізувати функцію sum_profit, яка буде використовувати generator_numbers
# для підсумовування цих чисел і обчислення загального прибутку.

import re

def generator_numbers(text):
    pattern = r'\b\d+\.\d+\b|\b\d+\b'       # шаблон для дійсних чисел
    matches = re.findall(pattern, text)     # знаходимо всі числа
    for i in matches:
        yield float(i)

def sum_profit(text, func):
    total_profit = sum(func(text))
    return total_profit

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: \
1000.01 як основний дохід,доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

