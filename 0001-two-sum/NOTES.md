Step-by-Step Walkthrough
Class and Method Definition:
​
A class Solution is defined.
The method twoSum takes two parameters: nums, a list of integers, and target, an integer. It returns a list of two integers.
Initialize prevMap:
​
prevMap is initialized as an empty dictionary. This dictionary will store the values of the numbers as keys and their corresponding indices as values.
Comment: # val : index indicates the structure of prevMap.
Loop Through nums:
​
A for loop starts, iterating over the enumerated nums. This gives us both the index i and the value n at each iteration.
Calculate diff:
​
For each number n in nums, the difference diff is calculated as target - n.
Check for diff in prevMap:
​
If diff is found in prevMap, it means we have found two numbers (n and the number corresponding to diff) that add up to the target.
The method returns a list containing the indices of these two numbers: [prevMap[diff], i].
Update prevMap:
​
If diff is not found in prevMap, the current number n and its index i are added to prevMap.
​
Example Debugging
Let's debug the code with an example:
​
Input
nums = [2, 7, 11, 15]
target = 9
​
Execution
Initialization:
​
prevMap = {}
First Iteration (i = 0, n = 2):
​
diff = 9 - 2 = 7
7 is not in prevMap
Update prevMap: {2: 0}
Second Iteration (i = 1, n = 7):
​
diff = 9 - 7 = 2
2 is in prevMap (it maps to index 0)
Return [prevMap[2], 1], which is [0, 1]
The method returns [0, 1], which are the indices of the numbers 2 and 7 that add up to 9.