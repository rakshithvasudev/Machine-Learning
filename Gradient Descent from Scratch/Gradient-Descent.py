from numpy import *

def run():
    points = genfromtxt('data.csv', delimiter=",")    
    print(points)

if __name__ =='__main__':
    run()