def count_substring(string, sub_string):
    cnt = 0
    charcnt = 0
    for i in string:
        charcnt = charcnt  +1
        if i == sub_string[0]:
            tmp = string[charcnt-1:]
            if tmp[0:len(sub_string)] == sub_string:
                cnt = cnt + 1
    return(cnt)


string = input().strip()
sub_string = input().strip()
    
count = count_substring(string, sub_string)
print(count)
