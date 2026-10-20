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

def search(name: str) -> bool:
    search_queue = deque()
    search_queue += graph[name]
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " продавец манго!")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False

def person_is_seller(name):
    return name[-1] == 'm'