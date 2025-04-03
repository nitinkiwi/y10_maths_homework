import time
def find_proper_factors_str(num):
    proper_factors = []
    for i in range(1, int(num) + 1):
        if num % i == 0 and i != num:
            proper_factors.append(str(round(i)))
    return proper_factors

def find_proper_factors_sum(num):
    proper_factors = []
    for i in range(1, int(num) + 1):
        if num % i == 0 and i != num:
            proper_factors.append(round(i))
    return sum(proper_factors)

def question_checker(question, answer):
    user_input = 'none given'
    while user_input not in answer:
        user_input = input(question)
        if user_input in answer:
            break
        else:
            print('\nPlease enter a provided option.')
            time.sleep(1)
    return user_input

def s(value):
    factors = []
    for i in range(1, value):
        if value % i == 0:
            factors.append(i)
    sum_factors = sum(factors)

    return sum_factors

def aliquot_sequence(starting_value, cap_of_terms):
    current_number = starting_value
    amicable_loop = 0
    if cap_of_terms == 'u':
        cap = 99999999999
    else:
        cap = int(cap_of_terms)
    sum_of_factors = 0
    number_of_terms = 0
    list_of_terms = []
    infinite_loop = False
    while current_number != 1 and number_of_terms < cap:
        print(f'\n\nThe number is {current_number}.')
        print(f'Its factors are {', '.join(find_proper_factors_str(current_number))}.')
        sum_of_factors = find_proper_factors_sum(current_number)
        print(f'The sum of its factors is {sum_of_factors}.')
        if current_number > sum_of_factors:
            print(f'{current_number} is a deficient number.')
        elif current_number < sum_of_factors:
            print(f'{current_number} is an abundant number.')
        current_number = sum_of_factors
        number_of_terms += 1
        print(f'This is term {number_of_terms}.')
        if number_of_terms == 1 and sum_of_factors == starting_value:
            infinite_loop = 'perfect number'
            list_of_terms.append(sum_of_factors)
            break
        if sum_of_factors in list_of_terms:
            infinite_loop = True
            list_of_terms.append(sum_of_factors)
            if s(int(current_number)) == int(current_number):
                infinite_loop = 'aspiring number'
            break
        list_of_terms.append(sum_of_factors)
        sum_of_factors = 0
        if cap_of_terms == 'u':
            cap += 2
        infinite_loop = False
    if infinite_loop == True:
        list_of_terms.pop()
        amicable_loop = len(list_of_terms) - list_of_terms.index(current_number)
        print(f'\n{starting_value} is an amicable number, therefore its aliquot sequence is infinite. The loop it is in has {amicable_loop} terms.')
        print('End of line.')
    elif infinite_loop == 'perfect number':
        print(f'\n{starting_value} is a perfect number, therefore its aliquot sequence will be infite and every term will be itself.')
        print('End of line.')
    elif infinite_loop == 'aspiring number':
        print(f'{starting_value} is an aspiring number. Therefore, its aliquot sequence will infinitely repeat at {current_number} becaues it is a perfect number.')
    else:
        if cap_of_terms == 'u':
            print(f'\nThere were {number_of_terms} terms in that aliquot sequence.')
        else:
            print(f'\nThose are the first {number_of_terms} terms in the aliquot sequence of {starting_value}.')
        print('End of line.')

def type_of_number(start_number, end_number):
    factors = []
    for i in range(start_number, end_number+1):
        factors = find_proper_factors_sum(i)
        if i > factors:
            print(f'{i}. Deficient')
        elif i < factors:
            print(f'{i}. Abundant')
        else:
            print(f'{i}. Perfect')
continuing = 'yes'

def num_of_terms(start_num, end_num):
    for i in range(start_num, end_num+1):
        terms = 1
        current_num = i
        beginning_value = i
        factors = []
        factors.append(current_num)
        infinite_num = ''
        while current_num != 1:
            current_num = find_proper_factors_sum(current_num)
            if current_num == beginning_value:
                terms = 'Infinite'
                infinite_num = '(perfect number)'
                break
            elif current_num in factors:
                terms = 'Infinite'
                infinite_num = '(amicable number)'
                if s(int(current_num)) == int(current_num):
                    infinite_num = '(aspiring number)'
                break
            factors.append(current_num)
            terms += 1
        print(f'{i}. {terms} terms {infinite_num}')
        factors = []
        


while True:
    mode = question_checker('''\nWhich mode do you want?\nMode 1 calculates the aliquot sequence for a specific number.\nMode 2 shows you whether numbers are perfect, abundant or deficifient.\nMode 3 shows how many terms numbers have in their aliquot sequences.
                            \n\nEnter 'Mode 1', 'Mode 2', 'Mode 3' or 'q' to quit: ''', ['Mode 1', 'Mode 2', 'Mode 3', 'q'])
    if mode == 'Mode 1':
        continuing = 'yes'
        while continuing.lower() == 'yes':
            user_number = int(input('\n\nChoose a number to begin the aliquot sequence with: '))
            term_cap = input("\nAfter how many terms would you like the program to stop running? (enter 'u' for unlimited terms) ")
            aliquot_sequence(user_number, term_cap)
            continuing = question_checker('\n\nWould you like to do another aliquot sequence calculation? (yes/no) ', ['yes', 'no'])
    elif mode == 'Mode 2':
        continuing = 'yes'
        while continuing.lower() == 'yes':
            number_one = int(input('What do you want your starting number to be? '))
            number_two = int(input('What do you want your finishing number to be? (Make sure this number is greater than your first number) '))
            assert number_one < number_two
            time.sleep(1)
            print()
            type_of_number(number_one, number_two)
            continuing = question_checker('\n\nWould you like to do another calculation? (yes/no) ', ['yes', 'no'])
    elif mode == 'Mode 3':
        continuing = 'yes'
        while continuing.lower() == 'yes':
            number_one = int(input('What do you want your starting number to be? '))
            number_two = int(input('What do you want your finishing number to be? (Make sure this number is greater than your first number) '))
            assert number_one < number_two
            time.sleep(1)
            num_of_terms(number_one, number_two)
            continuing = question_checker('\n\nWould you like to do another calculation? (yes/no) ', ['yes', 'no'])
    elif mode == 'q':
        print('\n\nEnd of program.\n\n')
        break