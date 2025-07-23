from functools import reduce

numbers = list(range(1, 101))
multiples_of_3 = list(filter(lambda x: x % 3 == 0, numbers))
mapped_result = list(map(lambda x: x, multiples_of_3))
sum_of_multiples = reduce(lambda x, y: x + y, multiples_of_3)

print("Multiples of 3 from 1 to 100:", mapped_result)
print("Sum of all multiples of 3:", sum_of_multiples)
print("hi my name is adarsh")
print("myself adarsh")