from collections import deque


graph = {}
graph["you"] = ["Alice", "Bob", "Claire"]
graph["Bob"] = ["Anuj", "Peggy"]
graph["Alice"] = ["Peggy"]
graph["Claire"] = ["Tom", "Johnny"]
graph["Anuj"] = []
graph["Peggy"] = []
graph["Tom"] = []
graph["Johnny"] = []

search_queue = deque()
search_queue += graph["you"]

def search_seller():
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(person + " продавец манго!")
            return True
        else:
            search_queue += graph[person]

def person_is_seller(name):
    return name[-1] == 'm'