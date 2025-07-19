pattern_size = int(input('Enter the of the pattern :'))
output_count = 0
while output_count != (pattern_size):
    output_count +=1
    if output_count>(pattern_size):
        break
    print((pattern_size) * '*')
