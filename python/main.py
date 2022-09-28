import data
import json
import threading
import time


def example_1():
    start = time.time()
    for progress_exam in data.progress_exam_list:
        # filter map `id` on progress_section_list
        progress_exam_filter = filter(
            lambda progress_section: progress_section['progress_exam_id'] == progress_exam['id'], data.progress_section_list)

        # set variable `progress_section_list` data filter `progress_exam_filter`
        progress_exam['progress_section_list'] = list(progress_exam_filter)

        time.sleep(0.5)
        # print pretty log ^^
        # print(json.dumps(data.progress_exam_list, indent=2))
    end = time.time()
    print('Time example_1 : ', end - start)


# map new object
def newMap(iterables):
    return dict({
        'book_id': iterables['book_id'],
        'author_list': iterables['author_list']
    })


def newAuthor(iterables):
    return dict({
        'id': iterables['author_list']['id'],
        'name': iterables['author_list']['name']
    })


def example_2():
    start = time.time()
    for author_book in data.author_book_map:
        # filter map `id` on author_list
        author = filter(
            lambda author: author['id'] == author_book['author_id'], data.author_list)

        # set variable `author_list` data filter `author`
        author_book['author_list'] = list(author)[0]

    # set variable `new_book_list` list
    new_book_list = list()
    for book in data.book_list:

        # map new object`author_book_map`
        new_map = map(newMap, data.author_book_map)

        # filter map new `id` on `new_map`
        author = filter(
            lambda author_map: author_map['book_id'] == book['id'], new_map)

        # map new object `author`
        new_author = map(newAuthor, author)

        # append new book list on `new_book_list`
        new_book_list.append({
            'id': book['id'],
            'name': book['name'],
            'author_list': list(new_author)
        })

    time.sleep(1)
    # print(json.dumps(new_book_list, indent=2))
    end = time.time()

    print('Time example_2 : ', end - start)


# Multi threading

example_task_1 = threading.Thread(target=example_1)
example_task_2 = threading.Thread(target=example_2)

example_task_1.start()
example_task_2.start()

example_task_1.join()
example_task_2.join()

# example_1()
# example_2()

