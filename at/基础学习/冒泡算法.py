nums = [12,456,4564,4,4654,16,49,749,37498,41,5541,987,46497,78941,446,1744,9,85461]
lenth = len(nums)
# count=0
# swap=0
# print(lenth)
print((lenth))
for i in range(lenth):
    # flag = True
    for j in range(lenth-1-i):
        # count += 1
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
            # swap += 1
            # flag = False
    # if flag:
    #     break

print(nums)
# print(count)
# print(swap)