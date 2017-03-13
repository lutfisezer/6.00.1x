def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    trans = {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si',
             '5': 'wu', '6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu', '10': 'shi'}

    if int(us_num) < 11:
        return trans[us_num]
    elif int(us_num) > 10 and int(us_num) < 20:
        return 'shi ' + trans[us_num[1]]
    elif int(us_num) > 19 and int(us_num) < 100:
        if int(us_num) % 10 == 0:
            return trans[us_num[0]] + ' shi'
        else:
            return trans[us_num[0]] + ' shi ' + trans[us_num[1]]

convert_to_mandarin('36') #will return san shi liu
convert_to_mandarin('20') #will return er shi
convert_to_mandarin('16') #will return shi liu
