def Vizinho(S, li, ls):
    for i in range(len(S)):
        S[i] = S[i] + random.uniform(-2, 2)
        if (S[i] < li[i]): S[i] = li[i]
        elif (S[i] > ls[i]): S[i] = ls[i]
    return S
