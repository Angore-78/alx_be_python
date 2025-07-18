pattern_size = input('Enter the of the pattern :')
output_count = 0
while output_count != int(pattern_size):
    output_count +=1
    if output_count>int(pattern_size):
        break
    print(int(pattern_size) * '*')
