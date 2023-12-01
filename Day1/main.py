import re

input = open('input.txt').read()
numberLines = [re.findall('[0-9]', line) for line in input.split('\n')]
print('Part 1: {}'.format(sum([int(numbers[0] + numbers[-1]) if len(numbers) else 0 for numbers in numberLines])))  # 56465

replaceMap = {
    'one'   : 'o1ne',
    'two'   : 't2wo',
    'three' : 't3hree',
    'four'  : 'f4our',
    'five'  : 'f5ive',
    'six'   : 's6ix',
    'seven' : 's7even',
    'eight' : 'e8ight',
    'nine'  : 'n9ine',
}

for key, value in replaceMap.items():
    input = input.replace(key, value)

numberLines = [re.findall('[0-9]', line) for line in input.split('\n')]
print('Part 2: {}'.format(sum([int(numbers[0] + numbers[-1]) if len(numbers) else 0 for numbers in numberLines])))  # 55902