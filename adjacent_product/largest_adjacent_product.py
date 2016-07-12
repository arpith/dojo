from operator import mul

def largest_product(numbers, window):
    index = 0
    largest = 0
    product = None
    while (index < len(numbers) - window + 1):
        current = numbers[index: index + window]
        if 0 in current:
            #Discard current window and skip to after the zero
            index = index + current.index(0) + 1
            product = None
        else:
            if product != None:
                #Compute product using stored value
                product = product * numbers[index + window -1] / numbers[index - 1]
            else:
                #Compute product the hard way
                product = reduce(mul, current, 1)
            if product > largest:
                largest = product
            index += 1
    return largest
