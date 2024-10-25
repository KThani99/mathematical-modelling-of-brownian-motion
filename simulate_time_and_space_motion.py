import numpy as np
import matplotlib.pyplot as plt
from utils.main import getUniqueFileName

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

    if noOfSamplePoints <= 0:
        raise ValueError("noOfSamplePoints must be positive")
    if noOfBrownianMotions <= 0:
        raise ValueError("noOfBrownianMotions must be positive")
    if timeStep <= 0:
        raise ValueError("timeStep must be positive")

    samplePointsAcrossTime = np.linspace(0., timeStep, noOfSamplePoints)
    stepDifference = samplePointsAcrossTime[1] - samplePointsAcrossTime[0]

    differenceBetweenMotion = np.sqrt(stepDifference) * np.random.normal(size=(noOfSamplePoints - 1, noOfBrownianMotions))

    firstStep = np.zeros(shape=(1, noOfBrownianMotions))
    brownianMotion = np.concatenate((firstStep, np.cumsum(differenceBetweenMotion, axis=0)), axis=0)

    return samplePointsAcrossTime, brownianMotion


def plotBrownianMotion(samplePointsAcrossTime, brownianMotion):
    """
    Plots the Brownian motion(s) over time and space.

    Parameters:
        samplePointsAcrossTime (array):
            A 1D array representing the time points at which the Brownian motion was sampled.
            
        brownianMotion (array):
            A 2D array where each row corresponds to a different time point and each column corresponds to 
            an independent Brownian motion path.

    Outputs:
        Plots the Brownian Motion across Time and Space and saves the image to disk.
    """

    plt.plot(samplePointsAcrossTime, brownianMotion)

    plt.title("Brownian Motion across Time and Space")
    plt.xlabel("Time")
    plt.ylabel("Displacement")

    uniqueFileName = getUniqueFileName("brownian-motion-time-and-space")
    plt.savefig(f"./output-images/{uniqueFileName}")
    plt.show()


def main():
    """
    Main function that generates and plots Brownian motion across Time and Space.

    It defines:
        - The number of sample points (`noOfSamplePoints`) to represent time intervals.
        - The number of independent Brownian motion paths (`noOfBrownianMotions`) to simulate.
        - The time step (`timeStep`) representing the time interval for the simulation.
    """

    # Parameters
    noOfSamplePoints = 10000
    noOfBrownianMotions = 1
    timeStep = 1.

    samplePointsAcrossTime, brownianMotion = getBrownianMotion(noOfSamplePoints, noOfBrownianMotions, timeStep)
    plotBrownianMotion(samplePointsAcrossTime, brownianMotion)

main()