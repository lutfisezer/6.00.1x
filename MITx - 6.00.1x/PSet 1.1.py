s = 'azcbobobegghakl'

vowels = 0
for i in str(s):
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowels += 1
print('Number of vowels: ' + str(vowels))