def f(s,s1,m):
    if s * s1 >= 255:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s+2,s1,m-1), f(s*2,s1,m-1), f(s,s1+2,m-1),f(s,s1*2,m-1)]
    return any(h) if m % 2 != 0 else all(h)
print('19',[s for s in range(1,51) if f(5,s,2)])
print('20',[s for s in range(1,51) if not(f(5,s,1)) and f(5,s,3)])
print('21',[s for s in range(1,51) if not(f(5,s,2)) and f(5,s,4)])