def read_input(filename):
    graph = {}
    heuristic = {}
    start = goal = ""

    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    i = 0
    while i < len(lines):
        line = lines[i]

        if line.startswith("START"):
            start = line.split()[1]

        elif line.startswith("GOAL"):
            goal = line.split()[1]

        elif line == "HEURISTIC":
            i += 1
            while lines[i] != "END":
                node, h = lines[i].split()
                heuristic[node] = int(h)
                i += 1

        elif line == "EDGES":
            i += 1
            while lines[i] != "END":
                u, v, cost = lines[i].split()
                cost = int(cost)
                if u not in graph:
                    graph[u] = []
                graph[u].append((v, cost))
                i += 1
        i += 1

    return start, goal, graph, heuristic

def write_output(filename, path, cost):
    with open(filename, 'w', encoding='utf-8') as f:
        if path:
            f.write("E:\\Documents\\Python\\TTNT\\input.txt" + " ".join(path) + "\n")
        f.write("COST " + str(cost) + "\n")     
        
def Best_First_Search(start, goal, graph, heuristic):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))
    parent = {}
    closed_set = set()
    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path, sum(graph[parent[node]][node] for node in path[1:])
        closed_set.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor in closed_set:
                continue
            if all(neighbor != item[1] for item in open_list):
                parent[neighbor] = current
                heapq.heappush(open_list, (heuristic[neighbor], neighbor))
start, goal, graph, heuristic = read_input("E:\\Documents\\Python\\TTNT\\input.txt")
write_output("E:\\Documents\\Python\\TTNT\\output.txt", *Best_First_Search(start, goal, graph, heuristic))