import numpy as np
import matplotlib.pyplot as plt

def getBrownianMotion(noOfTimeSteps, stepSize, sigma):
    """[Include Definition]""" # TODO: Write Documentation

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
    """[Include Definition]""" # TODO: Write Documentation

    plt.figure(figsize=(8, 6))
    plt.plot(xAxisPositions, yAxisPositions, color="blue", lw=1.5)
    plt.scatter(xAxisPositions[0], yAxisPositions[0], color="red", label="Start", zorder=5)
    plt.scatter(xAxisPositions[-1], yAxisPositions[-1], color="green", label="Stop", zorder=5)

    plt.title("2D Simulation of Brownian Motion")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.legend()

    plt.savefig("./output-images/2D-brownian-motion.png") # TODO: Create Unique Names for Each run
    plt.show()


def main():
    """[Include Definition]""" # TODO: Write Documentation

    # Parameters
    noOfTimeSteps = 1000
    stepSize = 1
    sigma = 1

    xAxisPositions, yAxisPositions = getBrownianMotion(noOfTimeSteps, stepSize, sigma)
    plotBrownianMotion(xAxisPositions, yAxisPositions)

main()