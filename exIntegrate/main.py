from integrate import integrate
import time



if __name__ == "__main__":

    for i in range(4, 9):
        start = time.time_ns() 
        result = integrate(-100, 100, int(10**i))
        end = time.time_ns()
        print("1e+%d : %f (%fs)" % (i, result, (end-start)*1e-9))
    
