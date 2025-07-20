pattern_size = input('Enter the size of the pattern: ')
output_count = 0
while int(pattern_size) > output_count:
    output_count += 1
    for size in pattern_size:
        print(f'*' * int(pattern_size))
