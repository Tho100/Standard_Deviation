import cmath

value = [4,5,6]
# Find mean value of of value array
sum_value = 0
for k in range(len(value)):
    sum_value = sum_value + value[k]
value_mean = (sum_value/len(value))

sum = 0
for j in value:
    sample = (j - value_mean)**2
    sum = sum + sample
    
print(cmath.sqrt(sum/len(value)-1))
