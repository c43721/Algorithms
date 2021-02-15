queue = []
visited = []

def bfs(visited, graph, start, target):
    visited.append(start)
    queue.append(start)

    while queue:
        cur = queue.pop(0)
        if cur == target:
            break

        for child in graph[cur]:
            if child not in visited:
                visited.append(child)
                queue.append(child)
    else:
         return None

    return visited

if __name__ == "__main__":
    #       A
    #     B   C
    #   D  E F  G
    graph = {
        'A' : ['B','C'],
        'B' : ['D', 'E'],
        'C' : ['F', 'G'],
        'D' : [],
        'E' : ['F'],
        'F' : [],
        'G' : []
    }

    find = "Q"
    start = "A"
    res = bfs(visited, graph, start, find)
    if res == None:
        print(f"Can't find node {find} in graph...")
    else:
        print(f"Found node {find}, visited: {res}")
        