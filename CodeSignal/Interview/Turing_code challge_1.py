nums=[1,2,2]
a=0
res=[]
bien=[i for i in range(1,len(nums)+1)]


for i in nums:
    a = nums.count(i)
    if a > 1:
        res.append(i)
        break

for i in bien:
   b = nums.count(i)
   if b == 0:
       res.append(i)
       break

print(res)

#open AI code: 
"""
create a python program that recives a list with a ordered list but one numer of the list is repeted. the function should return the number that is repeted and the number that is missing. 

for expample it recives [1,2,3,4,3]
it needs to return [3, 5]

"""

def find_duplicate_and_missing(numbers):
  # Calculate the sum of the numbers and the sum of the squares
  sum_of_numbers = sum(numbers)
  sum_of_squares = sum([x ** 2 for x in numbers])

  # Calculate the expected sum of the numbers and the expected sum of the squares
  expected_sum = len(numbers) * (len(numbers) + 1) // 2
  expected_squares_sum = (2 * len(numbers) + 1) * \
      (len(numbers) + 1) * (len(numbers)) // 6

  # Calculate the difference between the expected and actual sums
  difference = sum_of_numbers - expected_sum
  squares_difference = sum_of_squares - expected_squares_sum

  # Calculate the duplicate and missing numbers
  duplicate = (difference + squares_difference // difference) // 2
  missing = duplicate - difference

  return [duplicate, missing]


# Test the function
print(find_duplicate_and_missing(nums))

