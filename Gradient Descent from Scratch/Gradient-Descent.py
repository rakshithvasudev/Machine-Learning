from numpy import *

def run():
    points = genfromtxt('data.csv', delimiter=",")    
    
    # hyper-parameters
    learning_rate = 0.0001

    # y = mx + b -> slope of a line
    initial_b = 0
    initial_m = 0
    num_iterations = 1000
    

if __name__ =='__main__':
    run()