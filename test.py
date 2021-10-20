values=[1,2,3,2,3,1,4]
values_cnt={}
for value in values:
   values_cnt[value]=values_cnt.get(value,0)+1
print(values_cnt)