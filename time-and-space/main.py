import numpy as np
import matplotlib.pyplot as plt

def getBrownianMotion(noOfSamplePoints, noOfBrownianMotions, timeStep):
    """
    Generates a Brownian motion for a given number of sample points and a specified time step.
    
    Parameters:
        noOfSamplePoints (int): 
            The number of time intervals (sample points) over which the Brownian motion is generated. 
        
        noOfBrownianMotions (int): 
            The number of independent Brownian motions (paths) to simulate. 
        
        timeStep (float): 
            The time difference between each consecutive sample point. 
    
    Returns:
        tuple: 
            A tuple containing two elements:
            - np.ndarray: A 1D array representing the time intervals (sample points) from 0 to the specified time step.
            - np.ndarray: A 2D array representing the generated Brownian motion paths..
    """

    samplePointsAcrossTime = np.linspace(0., timeStep, noOfSamplePoints)
    stepDifference = samplePointsAcrossTime[1] - samplePointsAcrossTime[0]

    differenceBetweenMotion = np.sqrt(stepDifference) * np.random.normal(size=(noOfSamplePoints - 1, noOfBrownianMotions))

    firstStep = np.zeros(shape=(1, noOfBrownianMotions))
    brownianMotion = np.concatenate((firstStep, np.cumsum(differenceBetweenMotion, axis=0)), axis=0)

    return samplePointsAcrossTime, brownianMotion

def plotBrownianMotion(samplePointsAcrossTime, brownianMotion):
    """
    """ # TODO: Write Documentation

    plt.plot(samplePointsAcrossTime, brownianMotion)

    plt.xlabel("Time")
    plt.ylabel("Displacement")

    plt.savefig("./output-images/brownian-motion-time-and-space.png") # TODO: Create Unique Names for Each run
    plt.show()


def main():
    """[Include Definition]""" # TODO: Write Documentation

    noOfSamplePoints = 10000
    noOfBrownianMotions = 1
    timeStep = 1.

    samplePointsAcrossTime, brownianMotion = getBrownianMotion(noOfSamplePoints, noOfBrownianMotions, timeStep)
    plotBrownianMotion(samplePointsAcrossTime, brownianMotion)

main()