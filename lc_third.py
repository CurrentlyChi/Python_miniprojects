# <!-- You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

 

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0]. -->




class Solution:
    def plusOne(self, digits:list[int]):
        str_list = [str(digit) for digit in digits]
        joint_str = ''.join(str_list)
        int_nums = int(joint_str)
        int_nums_plus_one = int_nums + 1
        str_again = str(int_nums_plus_one)
        final_list = [nums for nums in str_again]
        return final_list
    
digits = [4,3,2,1]
so = Solution()
print(so.plusOne(digits))



# second solution with the same approach
class Solution:
    def plusOne(self, digits:list[int]):

        number = ""
        for i in digits:
            number = number + str(i)
        intnum = int(number)
        intnum = intnum + 1
        output=[]
        for i in str(intnum):
            output.append(int(i))
        return output

# third solution with the same approach

class Solution:
    def plusOne(self, digits:list[int]):
        nums = int("".join(str(i) for i in digits))
        nums += 1
        return [int(x) for x in str(nums)]
    
#fourth solution with the math-based approach

class Solution:
    def plusOne(self, digits:list[int]):
        for i in reversed(range(len(digits))):  
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits

