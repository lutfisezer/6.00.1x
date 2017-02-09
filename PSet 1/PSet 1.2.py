s = 'azcbobobegghakl'

len = len(s)
bobs = 0
for i in range(len - 2):
    if s[i:i+3] == "bob":
        bobs += 1
print("Number of times bob occurs is:", str(bobs))