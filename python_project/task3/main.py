import os

def r_bk():
    cook_book = {
        dish: [{"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure}]
        for dish, quantity_portion, *ingredients in map(str.splitlines, open("recipes.txt", "r", encoding='utf-8').read().split("\n\n"))
            for ingredient_name, quantity, measure in map(lambda x: x.rsplit(" | ", 2), ingredients)
    }

    return cook_book


def r_bk2():
    cook_book = {}
    with open('recipes.txt', encoding='utf-8') as src_file:
        last_key = ''
        for line in src_file:
            line = line.strip()
            if line.isdigit():
                continue
            elif line and '|' not in line:
                cook_book[line] = []
                last_key = line
            elif line and '|' in line:
                name, qt, msure = line.split(" | ")
                cook_book.get(last_key).append(dict(ingredient_name=name, quantity=int(qt), measure=msure))
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = dict()
    for dish_name in dishes:
        if dish_name in c_b:
            for ings in c_b[dish_name]:
                meas_quan_list = dict()
                if ings['ingredient_name'] not in ingr_list:
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name']] = meas_quan_list
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] + \
                                                                     ings['quantity'] * person_count

        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingr_list


def custom_key(files_list):
    return files_list[1]


def rewrite_file(path1=None, path2=None, path3=None):
    if path1 or path2 or path3 is None:
        path1 = '1.txt'
        path2 = '2.txt'
        path3 = '3.txt'

        outout_file = "rewrite_file.txt"
        file1_path = os.path.join(os.getcwd(), path1)
        file2_path = os.path.join(os.getcwd(), path2)
        file3_path = os.path.join(os.getcwd(), path3)
        with open(file1_path, 'r', encoding='utf-8') as f1:
            file1 = f1.readlines()
        with open(file2_path, 'r', encoding='utf-8') as f2:
            file2 = f2.readlines()
        with open(file3_path, 'r', encoding='utf-8') as f3:
            file3 = f3.readlines()

        files_list = [[path1,len(file1),file1],[path2,len(file2),file2],[path3,len(file3),file3]]
        files_list.sort(key=custom_key)

        print(files_list)

        with open(outout_file, 'w', encoding='utf-8') as f_total:
            f_total.write(files_list[0][0] + '\n')
            f_total.write(str(files_list[0][1]) + '\n')
            f_total.writelines(files_list[0][2])
            # f_total.write('' + '\n')
            f_total.write(files_list[1][0] + '\n')
            f_total.write(str(files_list[1][1]) + '\n')
            f_total.writelines(files_list[2][2])
            f_total.write('' + '\n')
            f_total.write(files_list[2][0] + '\n')
            f_total.write(str(files_list[2][1]) + '\n')
            f_total.writelines(files_list[2][2])

    return


if __name__ == '__main__':
    print('Задание 1------------------------------------------------------------')
    c_b = r_bk2()
    print(c_b)

    print('Задание 2------------------------------------------------------------')
    print(get_shop_list_by_dishes(dishes=['Запеченный картофель', 'Омлет'], person_count=2))

    print('Задание 3------------------------------------------------------------')
    rewrite_file()
