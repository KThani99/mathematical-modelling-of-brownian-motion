import numpy as np
import matplotlib.pyplot as plt
from utils.main import getUniqueFileName

def getBrownianMotion(noOfTimeSteps, stepSize, sigma):
    """
    Generates a Brownian motion for a particle with the given paremeters.
    
    Parameters:
        noOfTimeSteps (int): 
            The number of time steps the particle takes in the simulation.
        
        stepSize (int): 
            The time interval between each step in the simulation.
        
        sigma (int): 
            The standard deviation.
    
    Returns:
        tuple: 
            A tuple containing two elements:
            - xAxisPositions (array): A 1D array representing the x coordinates of the particle.
            - yAxisPositions (array): A 1D array representing the y coordinates of the particle.
    """

    startPosition = [0, 0]

    xAxisPositions = np.zeros(noOfTimeSteps)
    yAxisPositions = np.zeros(noOfTimeSteps)
    xAxisPositions[0], yAxisPositions[0] = startPosition

    for i in range(1, noOfTimeSteps):
        dx = np.random.normal(0, sigma * np.sqrt(stepSize))
        dy = np.random.normal(0, sigma * np.sqrt(stepSize))

        xAxisPositions[i] = xAxisPositions[i - 1] + dx
        yAxisPositions[i] = yAxisPositions[i - 1] + dy
    
    return xAxisPositions, yAxisPositions


def plotBrownianMotion(xAxisPositions, yAxisPositions):
    """
    Plots the Brownian motion of the particle in 2D.

    Parameters:
        xAxisPositions (array):
            A 1D array representing the x coordinates of the particle.
            
        yAxisPositions (array):
            A 1D array representing the y coordinates of the particle.

    Outputs:
        Plots the Brownian Motion of the particle in 2DB and saves the image to disk.
    """

    plt.figure(figsize=(8, 6))
    plt.plot(xAxisPositions, yAxisPositions, color="blue", lw=1.5)
    plt.scatter(xAxisPositions[0], yAxisPositions[0], color="red", label="Start", zorder=5)
    plt.scatter(xAxisPositions[-1], yAxisPositions[-1], color="green", label="Stop", zorder=5)

    plt.title("2D Simulation of Brownian Motion")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.legend()

    uniqueFileName = getUniqueFileName("2D-brownian-motion")
    plt.savefig(f"./output-images/{uniqueFileName}")
    plt.show()


def main():
    """
    Main function that generates and plots Brownian motion of 1 particle in 2 Dimensions.

    It defines:
        - The number of time steps taken by the particle (`noOfTimeSteps`).
        - The individual step size of the particle (`stepSize`).
        - The standard deviation (`sigma`).
    """

    # Parameters
    noOfTimeSteps = 1000
    stepSize = 1
    sigma = 1

    xAxisPositions, yAxisPositions = getBrownianMotion(noOfTimeSteps, stepSize, sigma)
    plotBrownianMotion(xAxisPositions, yAxisPositions)

main()