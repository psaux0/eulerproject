def perm(l):  
    if(len(l)<=1):  
        return [l]  
    r=[]  
    for i in range(len(l)):  
        s=l[:i]+l[i+1:]  
        p=perm(s)  
        for x in p:  
            r.append(l[i:i+1]+x)  
    return r  
print perm([1,2,3,4])

def perm(arr, pos = 0):
    if pos == len(arr):
        yield arr
    for i in range(pos, len(arr)):
        arr[pos], arr[i] = arr[i], arr[pos]
        for _ in perm(arr, pos + 1): yield _
        arr[pos], arr[i] = arr[i], arr[pos]