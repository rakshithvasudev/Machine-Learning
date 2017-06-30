from numpy import *


def compute_error_for_given_points(b,m, points, learning_rate):
    ''' Computes the sum of squares distance from the line to the point '''
    
    totalError = 0
    for i in range(len(points)):
        x = points[i,0]
        y = points[0,1]
        totalError += (y -(m*x+b)) ** 2
    return totalError/len(points)

def step_gradient(b,m, points, learning_rate):
    ''' Perform gradient descent'''



def radient_descent_runner(points, starting_b, starting_m, learning_rate,num_iterations):
    b = starting_b
    m = starting_m

    for in in range(num_iterations):
        b,m = step_gradient(b,m, array(points), learning_rate)
    return [b,m]    


def run():
    points = genfromtxt('data.csv', delimiter=",")    
    
    # hyper-parameters
    learning_rate = 0.0001

    # y = mx + b -> slope of a line
    initial_b = 0
    initial_m = 0
    num_iterations = 1000
    [b,m] = gradient_descent_runner(points,initial_b,initial_m,learning_rate,num_iterations)
    print(b)
    print(m)

if __name__ =='__main__':
    run()