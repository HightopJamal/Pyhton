
count = 0
s = input("Please enter a string:")
s_lower = s.lower()

for i in range(len(s_lower)):
    if s_lower[i:i+3] == "bob":
        count += 1
    

print("Number of bobs:" +str( count))
