nums = [2,5,6,7,8,9,10]

# ----------------map way and lambda ----------------
# def mapFunction(num):
#     return num*2

print(list(map(lambda num : num*2,nums)))


# ----------------comprehension way----------------
nums =[num*2 for num in nums]
print(nums)