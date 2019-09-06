#!/usr/bin/python
import urllib2 
from multiprocessing.dummy import Pool as ThreadPool 

def test( threadNum, list ):
    newList = []
    for i in list:
        newList.append(i)

    

def main():

    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    # make the Pool of workers
    pool = ThreadPool(2) 

    # open the urls in their own threads
    # and return the results
    results = pool.map(, A)

    # close the pool and wait for the work to finish 
    pool.close() 
    pool.join() 

main()