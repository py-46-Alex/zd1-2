import collections
import asyncio
import csv
from datetime import datetime


def listmaker():
    """создаст лист из айдишников
    на основе файла с кучей айдишников и их месейджей"""
    all_id = []
    with open("table.csv") as f:
        reader = csv.reader(f)
        new_list = list(reader)
        pop_exp = new_list.pop(0)
    for row in new_list:
        message = row[0]
        id = row[1]
        all_id.append(id)
    return all_id

async def find_duplicates(lst):
    """на вход принимает лист из наших идишников.
    На выход отдаст только те айдишники  которые повторялись в списке 3 раза
    асинхронна. чтобы видеть глазами нужо евейтить"""
    counter = collections.Counter(lst)
    # print(type(counter))
    duplicates = [id for id in counter if counter[id] == 3]
    return duplicates

async def find_elses(lst):
    counter = collections.Counter(lst)
    elses = {}
    todict = dict(counter)
    for id, frequency in todict.items():
        if frequency != 3:
            if frequency not in elses:
                elses.setdefault(frequency, [])
                elses[frequency].append(id)
            elif frequency in elses:
                elses[frequency].append(id)
    # return elses.items()
    finish_view = {}
    for frequency, ids in elses.items():
        finish_view[frequency] = len(ids)
    return finish_view.items()


my_list = listmaker()

async def main():
    duplicates = await find_duplicates(my_list)
    print("Айдишники, повторяющиеся три раза: ", len(duplicates))
    frequency = await find_elses(my_list)
    for fr, kol in frequency:
        print(f'вот такое количество уникальных айдишников {kol} светилось в файле с частотой {fr}')

    print('________________________________________________________________________________________________________')

if __name__ == '__main__':
    # start = datetime.now()
    asyncio.run(main())
    # print('текущее время работы программы')
    # print(datetime.now() - start)
    print('________________________________________________________________________________________________________')
