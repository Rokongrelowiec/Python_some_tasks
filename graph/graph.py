
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
  }

def search(graph, source):
    print(source)
    for neighbor in graph[source]:
        search(graph, neighbor)
    
search(graph, 'a')
