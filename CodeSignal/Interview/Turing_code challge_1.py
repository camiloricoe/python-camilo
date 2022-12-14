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
