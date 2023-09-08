nums = [1,2,3,4,5,6,7,8,9,10]

# ----------------filter way and lambda----------------
# def even(num):
#     return (num%2) == 0

print(list(filter(lambda num: (num%2) == 0,nums)))


# ----------------comprehension way----------------
nums = [num for num in nums if (num%2) == 0]
print(nums)


# ----------------loop way----------------
evenNum = []
for num in nums:
    if num%2 == 0 :
        evenNum.append(num)
print(evenNum)