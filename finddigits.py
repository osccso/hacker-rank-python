def findDigits(n):
    #convert number to string and split the numbers
    list_numbers = list(str(n))
    print(list_numbers)
    #count how many numbers are divisors of the number n
    count = 0
    for number in list_numbers:
        if int(number) == 0:
          continue
        if n % int(number) == 0:
            count += 1
    return count

result = findDigits(1012)
print(result)