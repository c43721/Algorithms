queue = []
visited = []

def bfs(visited, graph, start, target):
    visited.append(start)
    queue.append(start)

    while queue:
        cur = queue.pop()
        print(cur)

        if cur == target:
            break

        for child in graph[cur]:
            if child not in visited:
                visited.append(child)
                queue.append(child)

    return visited

if __name__ == "__main__":
    #       A
    #     B   C
    #   D  E    F
    graph = {
        'A' : ['B','C'],
        'B' : ['D', 'E'],
        'C' : ['F'],
        'D' : [],
        'E' : ['F'],
        'F' : []
    }

    res = bfs(visited, graph, "A", "E")
    print(res)