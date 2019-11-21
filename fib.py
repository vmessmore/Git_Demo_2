#Tori Messmore
#CSCI 101-Section C
#Python Lab 1B

nums=[1,1]

def Fib(nums):
    new_num = nums[-1] + nums[-2]
    nums.append(new_num)
    print(new_num)

print('1 \n1')
for i in range(98):
    Fib(nums)
