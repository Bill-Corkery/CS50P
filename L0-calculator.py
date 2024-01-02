x = float(input('Whats x? '))
y = float(input('Whats y? '))
# z = x+y better to not introduce extra variables. 
# would need to handle errors and non-integers.

z = round(x+y)
# Z = round(x/y,2) # rounds to 2

print(f"{z:,}") #this changes the results to add commas.     
# print(f"{z:.2f}") # this rounds it to 2 digits. 

