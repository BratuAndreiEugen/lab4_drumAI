from random import randint, choice


def generateARandomPermutation(n, start=-1, end=-1):
    perm = [i for i in range(n)]
    pos1 = randint(0, n - 1)
    pos2 = randint(0, n - 1)
    perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
    loc_start = 0
    loc_end = 0
    if start >= 0 and end >=0:
        for i in range(n):
            if perm[i] == start:
                loc_start = i
            if perm[i] == end:
                loc_end = i
    perm[0], perm[loc_start] = perm[loc_start], perm[0]
    perm[n-1], perm[loc_end] = perm[loc_end], perm[n-1]

    return perm

def generatePerm(n):
    perm = [i for i in range(n)]
    pos1 = randint(0, n - 1)
    pos2 = randint(0, n - 1)
    perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
    return perm

def generateRestOfPerm(perm,n):
    v = []
    for i in range(0, n):
        if perm.count(i) == 0:
            v.append(i)
    for i in range(len(perm), n):
        a = choice(v)
        v.remove(a)
        perm.append(a)
    return perm

def matrix_to_adjacency(dict):
    adj_list = []
    for i in range(0, len(dict['matrix'])):
        adj_list.append([])
        for j in range(0, len(dict['matrix'][i])):
            if dict['matrix'][i][j] != 0:
                adj_list[i].append([j, dict['matrix'][i][j]])

    new_dict = {}
    new_dict['adjList'] = adj_list
    new_dict['noNodes'] = dict['noNodes']
    new_dict['start'] = dict['start']
    new_dict['end'] = dict['end']
    return new_dict

def tryGenerate(dict, start):

    neigbours = {}
    maxim = 0
    for i in range(0, dict['noNodes']):
        neigbours[i] = []
        for j  in range(0, len(dict['adjList'][i])):
            neigbours[i].append(dict['adjList'][i][j][0])
        if len(neigbours[i]) > maxim:
            maxim = len(neigbours[i])

    covered = dict['noNodes']
    path = [[start] for i in range(0, maxim)]
    curent = [start for i in range(0, maxim)]

    while covered > 0:
        found = 0
        for k in range(0, maxim):
            v = choice(neigbours[curent[k]])
            if path[k].count(v) == 0:
                path[k].append(v)
                curent[k] = v
                found = 1
        for p in path:
            if len(p) == dict['noNodes']:
                return p
        covered-=1

    minp = []
    lenm = maxim + 1
    for p in path:
        if len(p) == dict['noNodes']:
            return p
        if len(p) < lenm:
            lenm = len(p)
            minp = p
    print("N-am gasit")
    return generateRestOfPerm(minp, dict['noNodes'])

def bfsGenerate(dict, start):
    q = []
    path = [start]
    q.append([start, path])  # node #path it was found on
    visited = [0 for i in range(0, dict['noNodes'])]
    visited[start] = 1
    while len(q) != 0:
        c = q.pop(0)
        path = c[1]
        for k in range(0, len(dict['adjList'][c[0]])):
            if path.count(dict['adjList'][c[0]][k][0]) == 0:
                q.append([dict['adjList'][c[0]][k][0], path + [dict['adjList'][c[0]][k][0]]])
                #visited[dict['adjList'][c[0]][k][0]] = 1
                print(len(path + [dict['adjList'][c[0]][k][0]]) )
                if len(path + [dict['adjList'][c[0]][k][0]]) == dict['noNodes']:
                    return path + [dict['adjList'][c[0]][k][0]]

    return generatePerm(dict['noNodes'])


def bfs(dict):
    start = 1
    q = []
    q.append(start)
    visited = [0 for i in range(0, dict['noNodes'])]
    visited[start] = 1
    cnt = 0
    while len(q)!= 0:
        c = q.pop(0)
        print(c)
        cnt += 1
        for k in range(0, len(dict['adjList'][c])):
            if visited[dict['adjList'][c][k][0]] == 0:
                q.append(dict['adjList'][c][k][0])
                visited[dict['adjList'][c][k][0]] = 1
    print(cnt)

def generatePath(dict, visited):
    start = dict['start']
    end = dict['end']
    neigbours = {}
    for i in range(0, dict['noNodes']):
        neigbours[i] = []
        for j  in range(0, len(dict['adjList'][i])):
            neigbours[i].append(dict['adjList'][i][j][0])

    r = [start]
    curent = start
    pas = 0
    vispath = [0 for i in range(0,dict['noNodes'])]
    vispath[start] = 1
    while curent != end:
       for i in range(0, len(neigbours[curent])):
           c = neigbours[curent][i]
           if visited[pas][c] == 0 and vispath[c] == 0:
                r.append(c)
                visited[pas][c] = 1
                vispath[c] = 1
                curent = c
                break
       if pas < len(visited):
        pas += 1
       else:
           print(r)
    print(r)
    return r

def justGenerate(dict):
    path = [dict['start']]
    length = randint(2, dict['noNodes'])
    visit = [0 for i in range(0,dict['noNodes'])]
    visit[dict['start']]
    crrL = 1
    curent = dict['start']
    while crrL < length:
        if crrL + 1 == length:
            path.append(dict['end'])
            return path
        visitnot = []
        for i in range(0, len(visit)):
            if visit[i] == 0:
                visitnot.append(i)
        next = choice(visitnot)
        path.append(next)
        visit[next] = 1
        crrL += 1

