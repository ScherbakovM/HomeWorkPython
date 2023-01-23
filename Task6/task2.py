# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

x = [12,'sadf',5643]
digit = lambda x: True if (type(x) == int) else False
string = lambda x: True if (type(x) == str) else False
print(list(filter(string,x)), list(filter(digit,x)))
