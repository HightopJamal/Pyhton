
count = 0
s = input("Please enter a string:")
s_lower = s.lower()

for char in s_lower:
    if char in ['a', 'e', 'i', 'o', 'u']:
        count += 1

print("Number of vowels:" +str( count))
         
