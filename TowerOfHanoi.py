def TowerOfHanoi(n,s,a,d):
    if n==1:
        print(s+" => "+d)
    else:
        TowerOfHanoi(n-1,s,d,a)
        TowerOfHanoi(1,s,a,d)
        TowerOfHanoi(n-1,a,s,d)

TowerOfHanoi(4,'source','auxiliary','destination')
