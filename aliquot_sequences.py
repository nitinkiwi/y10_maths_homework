
def find_proper_factors(num):
    proper_factors = []
    for i in range(1, int(num) + 1):
        if num % i == 0 and i != num:
            proper_factors.append(str(round(i)))
    return proper_factors

def aliquot_sequence(starting_value):
    current_number = starting_value
    sum_of_factors = 0
    number_of_terms = 0
    list_of_terms = []
    infinite_loop = False
    while current_number != 1:
        print(f'\n\nThe number is {current_number}.')
        print(f'Its factors are {', '.join(find_proper_factors(current_number))}.')
        for i in range(0,len(find_proper_factors(current_number))):
            sum_of_factors += int(find_proper_factors(current_number)[i])
        print(f'The sum of its factors is {sum_of_factors}.')
        if current_number > sum_of_factors:
            print(f'{current_number} is a deficient number.')
        elif current_number < sum_of_factors:
            print(f'{current_number} is an abundant number.')
        current_number = sum_of_factors
        number_of_terms += 1
        if number_of_terms == 1 and sum_of_factors == starting_value:
            infinite_loop = 'perfect number'
            break
        if sum_of_factors in list_of_terms:
            infinite_loop = True
            break
        list_of_terms.append(sum_of_factors)
        sum_of_factors = 0
        infinite_loop = False
    if infinite_loop == True:
        print(f'\n{starting_value} is an amicable number, therefore its aliquot sequence is infinite. The loop it is in has {len(list_of_terms)} terms.')
        print('End of line.')
    elif infinite_loop == 'perfect number':
        print(f'\n{starting_value} is a perfect number, therefore its aliquot sequence will be infite and every term will be itself.')
        print('End of line.')
    else:
        print(f'\nThere were {number_of_terms} terms in that aliquot sequence.')
        print('End of line.')

continuing = 'yes'

while continuing.lower() == 'yes':
    question_answer = 'invalid'
    user_number = int(input('\n\nChoose a number to begin the aliquot sequence with: '))
    aliquot_sequence(user_number)
    while question_answer == 'invalid':
        continuing = input('\n\nWould you like to do another aliquot sequence calculation? (yes/no) ')
        if continuing != 'yes' and continuing != 'no':
            print("\n\nPlease type either 'yes' or 'no'.")
        else:
            question_answer = 'valid'


print('\n\nEnd of program.\n\n')