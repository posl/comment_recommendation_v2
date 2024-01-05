def test():
    print('test')

def test2():
    return ('test2')

def test3():
    t = 'nums, l, a, target'
    t = t.replace(' ', '')
    l = t.split(',')
    l = list(filter(None, l))
    print(l)

def test4():
    l = [1,2,3,4,5]
    ll = [[],[],[]]
    ll[0].append(l[0:2])
    ll[1].append(l[2:4])
    ll[2].append(l[4:6])
    print(l)
    print(ll)

if __name__ == '__main__':
    a = test()
    print(a)
    b = test2()
    print(b)
    test3()
    test4()