from bs4 import BeautifulSoup
import re
import os
from collections import deque


# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_tree(start, end, path):
    link_re = re.compile(r"(?<=/wiki/)[\w()]+")  # Искать ссылки можно как угодно, не обязательно через re
    files = dict.fromkeys(os.listdir(path))  # Словарь вида {"filename1": None, "filename2": None, ...}
    # TODO Проставить всем ключам в files правильного родителя в значение, начиная от start
    links_dict = {}
    for file in files:
        links = []
        with open('./wiki/' + file, 'r') as f:
            for link in re.findall(link_re, f.read()):
                if link != start and link in files and link not in links and link != file:
                    links.append(link)

        links_dict[file] = links

    for file, links in links_dict.items():
        # parents = []
        for link in links:
            if link in files:
                # parents.append()
                if files[link] is None:
                    files[link] = [file]
                else:
                    files[link].append(file)

    # files = fill_tree(start, end, files)

    # children = []
    # parents = [start]
    # with open('./wiki/' + start, 'r') as f:
    #     for child in re.findall(link_re, f.read()):
    #         if child in files and child not in children:
    #             children.append(child)
    #             files[child] = parents
    #
    # for child in children:
    #     fill_tree(child, end, files)

    # files[start] = links
    # for link in links:
    #     if link == end:
    #         break
    #     else:
    #         build_tree(link, end, path)

    return files


def bfs(start, end, files):
    if start == end:
        return [start]
    visited = {start}
    queue = deque([(start, [])])

    while queue:
        current, path = queue.popleft()
        visited.add(current)
        for neighbor in files[current]:
            if neighbor == end:
                return path + [current, neighbor]
            if neighbor in visited:
                continue
            queue.append((neighbor, path + [current]))
            visited.add(neighbor)
    return None


# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_bridge(start, end, path):
    files = build_tree(start, end, path)

    bridge = bfs(end, start, files)
    return bridge[::-1]


def parse(start, end, path):
    """
    Если не получается найти список страниц bridge, через ссылки на которых можно добраться от start до end, то,
    по крайней мере, известны сами start и end, и можно распарсить хотя бы их: bridge = [end, start]. Оценка за тест,
    в этом случае, будет сильно снижена, но на минимальный проходной балл наберется, и тест будет пройден.
    Чтобы получить максимальный балл, придется искать все страницы. Удачи!
    """

    bridge = build_bridge(start, end, path)  # Искать список страниц можно как угодно, даже так: bridge = [end, start]
    # bridge = [end, start]

    # Когда есть список страниц, из них нужно вытащить данные и вернуть их
    out = {}
    for file in bridge:
        with open("{}{}".format(path, file)) as data:
            soup = BeautifulSoup(data, "lxml")

        body = soup.find(id="bodyContent")

        # TODO посчитать реальные значения
        imgs = 0  # Количество картинок (img) с шириной (width) не меньше 200
        for img in body.find_all('img', width=True):
            if int(img['width']) >= 200:
                imgs += 1

        headers = 0  # Количество заголовков, первая буква текста внутри которого: E, T или C
        for a in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            for head in body.find_all(a):
                if re.match(r'^[E,T,C]', head.text) is not None:
                    headers += 1

        linkslen = 0  # Длина максимальной последовательности ссылок, между которыми нет других тегов
        for a in body.find_all('a'):
            siblings = a.find_next_siblings()
            len = 1
            for sibling in siblings:
                if sibling.name == 'a':
                    len += 1
                else:
                    break
            if len > linkslen:
                linkslen = len

        lists = 0  # Количество списков, не вложенных в другие списки
        ulol_list = body.find_all(['ol', 'ul'])
        for list_ in ulol_list:
            if not list_.find_parent(['ol', 'ul']):
                lists += 1

        out[file] = [imgs, headers, linkslen, lists]

    return out
