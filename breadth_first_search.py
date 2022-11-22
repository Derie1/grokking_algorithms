from collections import deque


def person_is_seller(name):
    return name.endswith('seller')


def bf_search(name, graph):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f"{person} is a seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    
    return False