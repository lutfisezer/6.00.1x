s = 'dznppkioymrpglddozz'

sub = ""
maxsub = ""

for letter in range(len(s)):
    sub += s[letter]
    if len(sub) > len(maxsub):
        maxsub = sub
    while letter != len(s) - 1:
        if s[letter] > s[letter + 1]:
            sub = ""
        break
print("Longest substring in alphabetical order is:", maxsub)
