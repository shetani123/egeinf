def f(s,s1,m):
    if s + s1 >= 154:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s+4,s1,m-1), f(s,s1+4,m-1), f(s*3,s1,m-1), f(s,s1*3,m-1)]
    return any(h) if m % 2 != 0 else all(h)

print('19',[s for s in range(1,143) if f(11,s,2) and not(f(11,s,1))])
print('20',[s for s in range(1,143) if not(f(11,s,1)) and f(11,s,3)])