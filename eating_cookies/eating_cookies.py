'''
Input: an integer
Returns: an integer
'''
from itertools import permutations 

perm = permutations([1, 2, 3]) 
  
# Print the obtained permutations 
print(perm)

for i in list(perm): 
    print(i)
# def eating_cookies(n):
#     # Your code here

#     pass

# if __name__ == "__main__":
#     # Use the main function here to test out your implementation
#     num_cookies = 5

#     print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
