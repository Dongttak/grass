def solution(info, edges):
    n = len(info)
    children = [[] for _ in range(n)]
    for a, b in edges:
        children[a].append(b)

    best = 0
    
    def dfs(wolf, sheep, candidate):
        nonlocal best
        
        for nxt in candidate:
            newcandi=[]
            ns=sheep+(info[nxt]==0)
            nw=wolf+(info[nxt]==1)
            
            if nw>=ns:
                continue
            best=max(best, ns)
            
            for x in candidate:
                if nxt!=x:
                    newcandi.append(x)
            newcandi.extend(children[nxt])
            
            dfs(nw, ns, newcandi)

    print(dfs(0,0, [0]))
    return best