def Vizinho(S, li, ls, passo):
    Si = S + random.uniform(-passo, passo)
    if(Si < li): 
        Si = li
    elif( Si > ls): 
        Si = ls
    return Si
