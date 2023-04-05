def fitness1(chromozome, param):
    cost = 0
    for i in range(0, len(chromozome.repres)-1):
        added = 100000
        for j in range(0, len(param['adjList'][chromozome.repres[i]])):
            if param['adjList'][chromozome.repres[i]][j][0] == chromozome.repres[i+1]:
                added = param['adjList'][chromozome.repres[i]][j][1]
                break
        cost += added

    return cost

#FITNESS MAI MARE => SOLUTIE MAI SLABA
