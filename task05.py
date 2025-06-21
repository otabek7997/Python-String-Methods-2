template = '{num_1} + {num_2} = {result}'

num_1 = int(input())
num_2 = int(input())
result = num_1  + num_2

print(template.format(num_1 = num_1, num_2 = num_2, result = result))