import collections
import asyncio
import csv

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

async def find_elses(lst):
    """ на вход берет лист айдишников отдает словарь
     где ключ это частотность а значение - количество уникальных
     идишников из входного листа"""
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
    finish_view = {}
    for frequency, ids in elses.items():
        finish_view[frequency] = len(ids)
    return finish_view.items()

my_list = listmaker()

async def main():
    frequency = await find_elses(my_list)
    for fr, kol in frequency:
        print(f'вот такое количество уникальных айдишников {kol} светилось в файле с частотой {fr}')

if __name__ == '__main__':
    asyncio.run(main())
