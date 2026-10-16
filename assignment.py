def classify(value):
    if value < 198:
        return 'Below range'
    elif 198 <= value <= 202:
        return 'In range'
    else:
        return 'Above range'
def calculate_average(total, count):
    return total / count
num_strips = int(input('Enter the number of strips: '))
total_length = 0
below_count = 0
in_range_count = 0
above_count = 0
for i in range(num_strips):
    strip_length = int(input('Enter the strip length: '))
    result = classify(strip_length)
    print(result)
    if result == 'Below range':
        below_count += 1
    elif result == 'In range':
        in_range_count += 1
    else:
        above_count += 1
    total_length += strip_length
average_length = calculate_average(total_length, num_strips)
print(f'Total length: {total_length} mm')
print(f'Average length: {average_length:.1f} mm')
print(f'Below range: {below_count}')
print(f'In range: {in_range_count}')
print(f'Above range: {above_count}')





