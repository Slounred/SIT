import random
import time

def get_matrix(length):
    mat = [[0 for i in range(length)] for j in range(length)]
    for i in range(length):
        for j in range(i + 1, length):
            if j == i + 1:
                mat[i][j] = 1
                mat[j][i] = 1
            else:
                s = round(100 * random.random())
                if s > 50:
                    mat[i][j] = 0
                    mat[j][i] = 0
                else:
                    mat[i][j] = 1
                    mat[j][i] = 1
    mat[length - 1][0] = 1
    mat[0][length - 1] = 1    
    return mat


def get_list(mat):
    l = []
    for i in mat:
        ll = []
        for ind, j in enumerate(i):
            if j > 0:
                ll.append(ind);
        l.append(ll)
    return l


def get_cicle(Graf):
    for i in range(1, len(Graf)):
        l = get_cicle_rec(i, Graf)
        if l:
            return l
    return [];
    
    
def get_cicle_rec(v, Graf):
    querry = []
    cicle = []
    parents = [0 for i in range(len(Graf))]
    branches = [0 for i in range(len(Graf))]
    parents[v] = -1
    for u in Graf[v]:
        parents[u] = v
        branches[u] = u
        querry.append(u)
    for i in querry:
        flag = False
        for u in Graf[i]:
            if parents[u] == 0:
                parents[u] = i
                branches[u] = branches[i]
                querry.append(u)
            elif parents[i] != u and branches[i] != branches[u]:
                while i != v:
                    cicle.append(i)
                    i = parents[i]
                while u != v:
                    cicle.insert(0,u)
                    u = parents[u] 
                cicle.insert(0,v)
                flag = True
                break
        if flag:
            break
    return(cicle)

def get_chains(cicle, Graf):
    chains = []
    chains.extend([cicle])
    chains[0].append(cicle[0])
    L = [0 for i in Graf]
    for i in cicle:
        L[i] = 1
    for p in range(1, len(cicle)):
        for u in Graf[p]:
            if L[u] == 0:
                new_chains = get_chains_rec(p, u, L, Graf)
                if new_chains[0]:
                    new_chains[0].insert(0, p)
                    chains.extend(new_chains)
    return chains


def get_chains_rec(p, v, L, Graf):
    L[v] = 2
    chains = [[]]
    for u in Graf[v]:
        if L[u] == 0:
            if chains[0]:
                new_chains = get_chains_rec(v, u, L, Graf)
                if new_chains[0]:
                    new_chains[0].insert(0, v)
                    chains.extend(new_chains)                
            else:
                new_chains = get_chains_rec(p, u, L, Graf)
                if new_chains[0]:
                    L[v] = 1
                    new_chains[0].insert(0, v)
                    chains = list(new_chains) 
        elif L[u] == 1 and u != p and L[v] != 1:
            L[v] = 1
            return [[v, u]]
    if chains[0] == []:
        L[v] = 0
    return chains

def get_trees(chains):
    trees = []
    tree = []
    for i1 in chains:
        for i2 in range(len(i1) - 2):
            tree.append([i1[i2], i1[i2+1]])
    trees.append(tree)
    tree = []
    for i1 in chains:
        for i2 in range(len(i1) - 1, 1, -1):
            tree.append([i1[i2], i1[i2-1]])
    trees.append(tree)
    return trees

def main():
    v = int(input('Enter the number of vertices: '))
    t = time.time()
    m = get_matrix(v)
    Graf = get_list(m)    
    cicle = get_cicle(Graf)
    chains = get_chains(cicle, Graf)
    k = get_trees(chains)
    t = time.time() - t
    s = 0
    for i in Graf:
        for j in i:
            s = s + 1
    s = s // 2
    print("Vertices - ", v, "Edges - ", s, "Time - ", t, 'Status: OK')
    

if __name__ == "__main__":
    main()
            
