from multiprocessing import Process, Value, Array

def f(a):
    for x in range(len(a)):
        a[x] = x*x

if __name__ == '__main__':
    arr = Array('i', range(10))


    p = Process(target=f, args=(arr, ))
    p.start()
    p.join()

    asd = []
    for i in range (len(arr)):
        asd.append(arr[i])

    print asd