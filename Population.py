mu_mean = (sum_ar/len(ar))

# Iterate each ar value with mu_mean and squared each of them
s = 0 
for i in ar:
    population = (i - mu_mean)**2
    s = s + population
    
print(cmath.sqrt(s/len(ar)))
