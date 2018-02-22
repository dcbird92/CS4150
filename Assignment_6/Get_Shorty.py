from collections import defaultdict
import heapq

class Graph:
    def __init__(self):
        self.vertex = set()
        self.edges = defaultdict(list)
        self.weight = {}

    def add_vertex(self, value: str):
        self.vertex.add(value)

    def add_edge(self, start: str, end: str, weight: float):
        self.vertex.add(start)
        self.vertex.add(end)

        self.edges[start].append(end)
        self.weight[(start, end)] = weight
        self.edges[end].append(start)
        self.weight[(end, start)] = weight


def dijkstra(g: Graph, start: str, n: int):
    xheappush = heapq.heappush
    xheappop = heapq.heappop
    xheapify = heapq.heapify
    end = str(n - 1)
    distance = {start: float(-1.0)}
    pq = []
    xheapify(pq)
    xheappush(pq, (-1.0, start))
 
    while pq:
        a = xheappop(pq)
        u = str(a[1])
        for v in g.edges[u]:
            w = float(g.weight[(u, v)])
            if v in distance:
                if distance[v] > distance[u] * w:
                    distance[v] = distance[u] * w
                    xheappush(pq, (distance[v], v))
            else:
                distance[v] = distance[u] * w
                xheappush(pq, (distance[v], v))

    x = format(float(distance[end])*-1, '.4f')
    print(x)


def main():
    n, m = map(int, input().split(" "))
    while 1:
        g = Graph()
        i = 0
        while i < m:
            xstart, xend, xweight = input().split(" ")
            g.add_edge(xstart, xend, xweight)
            i += 1
        dijkstra(g, '0', n)
        n, m = map(int, input().split(" "))
        if n == 0 and m == 0:
            return


if __name__ == "__main__":
    main()
