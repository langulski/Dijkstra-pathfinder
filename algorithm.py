from heapq import *

grafo = {'A': [(2, 'M'), (3, 'P')],
         'M': [(2, 'A'), (2, 'N')],
         'N': [(2, 'M'), (2, 'B')],
         'P': [(3, 'A'), (4, 'B')],
         'B': [(4, 'P'), (2, 'N')]}

def dijkstra (start, goal, grafo):
    queue =[]
    heappush(queue,(0,start))
    custo_visitado = {start:0}
    visitado = {start: None}

    while queue:
        custo_atual, no_atual = heappop(queue)
        if no_atual == goal:
            break

        prox_nos = grafo[no_atual]
        for prox_no in prox_nos:
            vis_custo, vis_no = prox_no
            novo_custo = custo_visitado[no_atual] + vis_custo


            if vis_no not in custo_visitado or novo_custo < custo_visitado[vis_no]:
                heappush(queue, (novo_custo, vis_no))
                custo_visitado[vis_no] = novo_custo
                visitado[vis_no] = no_atual
        
    return visitado


start = 'A'

goal =  'B'

visitado = dijkstra(start, goal, grafo)

no_atual = goal

print(f'\npath from {goal} to { start}: \n {goal} ',end='')

while no_atual != start:
    no_atual = visitado[no_atual]
    print(f'---> {no_atual}',end='')