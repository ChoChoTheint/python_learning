# prices = [2000,1000,3000,4000]

# double_price = []
# for price in prices:
#     double_price.append(price*2)
# print(double_price)


# double_price = [price*2 for price in prices]
# print(double_price)


nums = [1,2,3,4,5,6,7,8,9,10]
# even_double_nums = []
# for num in nums:
#     if(num%2)  == 0:
#         event_double_nums.append(num*2)
# print(even_double_nums)

even_double_nums = [num*2 for num in nums if (num%2) == 0]
print(even_double_nums)