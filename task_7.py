def digit_root(num):
    if num >=10:
        num_str = str(num)
        summary = 0
        for i in num_str:
            summary +=int(i)
            num = summary
    return num


print(digit_root(1012))

print(digit_root(89755))