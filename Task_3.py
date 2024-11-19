#1) find odd or even numbers
num = [10,501,22,37,100,999,87,351]
for i in num: #iterate the value using for loop
    if i % 2 == 0: #condition is which values are divide by 2 and == 0
        print(f"{i} is even") #condition meets true it will print this.
    else:
        print(f"{i} is odd") #condition meets true it will print this.

#2) find the prime number
def find_prime_number(num):
    if num > 1:
        for i in range(2, (num // 2) + 1): #i in range 2 (it mean i = 2), num divided by 2 leaves a remainder of 1
            if num % i == 0: #
                print(num,"is not prime number")
                break
        else:
            print(num,"is prime number")

lis_number = [10,501,22,37,100,999,87,351]

for i in lis_number:
    find_prime_number(i) #to call this method (find_prime_number)

# 3) find happy numbers
def happy_number_formula(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

def find_happy_number(num):
    given_lists =[]
    for i in num:
        if happy_number_formula(i):
            given_lists.append(i)
            return given_lists

lst_values = [10,501]
given_lists = find_happy_number(lst_values)

print("Happy numbers in the list:", given_lists)

# 4) find the sum of first and last digit of integer(own int)
def find_firstDigit(num):
#find the first digit
    while num >= 10:
        num = num / 10
    return int(num)
# find the last digit
def find_lastDigit(num):
    # find the last digit
    return (num % 10) # to find the reminder value

# pass the arguments to this method
num = 1008
print("First digit",find_firstDigit(num), end=" ")
print("\nLast digit", find_lastDigit(num))

#6) find duplicate values using own list

lis_one = [10, 222, 3]
lis_two = [3, 547, 85]
lis_set1 = set(lis_one) # need to convert list to set
lis_set2 = set(lis_two)

common_value = lis_set1 & lis_set2 # using & operator to get the common value
print(common_value)

#6.1) find duplicate values using own list
lis_1 = [12,24,36]
lis_2 = [110,24,316]
lis_3 = [12,204,36]

dup_values_ = []
not_dup_values = []

lis_4 = lis_2 + lis_3
#print(lis_4)

for i in lis_4:
    if i in lis_1:
        print(f'{i} is duplicate values')
    else:
        print(f'{i} is not duplicate values')

#8)find minimum element in the sorted list
list_so = [10,5,9,2,3]
sort_list = sorted(list_so)
print(sort_list)
print(min(list_so))