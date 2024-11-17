class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, u):
        while self.parent[u] != u:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            self.components -= 1


with open('input.txt', 'r') as file:
    with open('output.txt', 'w') as output_file:
        n, q = map(int, file.readline().split())
        uf = UnionFind(n)
        for _ in range(q):
            u, v = map(int, file.readline().split())
            uf.union(u - 1, v - 1)
            print(uf.components)
            output_file.write(str(uf.components)+'\n')
