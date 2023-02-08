
def get_steps_lst(in_data: str) -> list: # Переводим строку в лист с разделение по операндам
    res = ''

    for el in in_data:
        if el.isdigit():
            res += el

        else:
            res += f' {el} '

    res = res.split()

    for i in range(len(res)):
        if res[i].isdigit():
            res[i] = int(res[i])

    return res

def process_step(lst_in: list):  # Для рассчетов 
    lst_work = lst_in[:] # lst_in.copy()
    if ('/' in lst_work) or ('*' in lst_work):
        for i in range(len(lst_work)):
            if lst_work[i] == '/':
                temp = lst_work[i - 1] / lst_work[i + 1]
                del lst_work[i-1 : i+2]
                lst_work.insert(i - 1, temp)
                break

            elif lst_work[i] == '*':
                temp = lst_work[i - 1] * lst_work[i + 1]
                del lst_work[i-1 : i+2]
                lst_work.insert(i - 1, temp)
                break
    else:
        for i in range(len(lst_work)):
            if lst_work[i] == '+':
                temp = lst_work[i - 1] + lst_work[i + 1]
                del lst_work[i-1 : i+2]
                lst_work.insert(i - 1, temp)
                break

            elif lst_work[i] == '-':
                temp = lst_work[i - 1] - lst_work[i + 1]
                del lst_work[i-1 : i+2]
                lst_work.insert(i - 1, temp)
                break

    return lst_work

def CheckR(arg): # Зацикливаем пока длина не равна 1
    if len(arg) > 1:
        Checked = process_step(arg)
        return CheckR(Checked)
    else: return arg


def logger(log):
    with open('loggers.csv', 'a', encoding='utf-8') as f:
        f.write(f"{log}")

if __name__ == '__main__':
    print('models')
    




    

