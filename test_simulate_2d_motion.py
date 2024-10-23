import pytest
import numpy as np
from unittest.mock import patch, Mock
import matplotlib.pyplot as plt
from simulate_2d_motion import getBrownianMotion, plotBrownianMotion, main

class Test2DSimulation:
    """
    Test suite for 2D Brownian motion simulation
    """
    
    @pytest.fixture
    def mockRandom(self):
        """
        Fixture to provide consistent random numbers for testing
        """

        with patch('numpy.random.normal', return_value=0.5):
            yield

    @pytest.fixture
    def mockPlot(self):
        """
        Fixture to mock plotting functions
        """

        with patch('matplotlib.pyplot.figure'), \
             patch('matplotlib.pyplot.plot'), \
             patch('matplotlib.pyplot.scatter'), \
             patch('matplotlib.pyplot.savefig'), \
             patch('matplotlib.pyplot.show'):
            yield

    def testGetBrownianMotionShape(self):
        """
        Test if getBrownianMotion returns correct array shapes
        """

        noOfTimeSteps = 10
        xAxisPositions, yAxisPositions = getBrownianMotion(noOfTimeSteps, 1, 1)
        
        assert len(xAxisPositions) == noOfTimeSteps, f"Expected xAxisPositions to be of length {noOfTimeSteps} but got {len(xAxisPositions)}"
        assert len(yAxisPositions) == noOfTimeSteps, f"Expected yAxisPositions to be of length {noOfTimeSteps} but got {len(yAxisPositions)}"

    def testGetBrownianMotionStartPosition(self):
        """
        Test if particle starts at origin [0,0]
        """

        xAxisPositions, yAxisPositions = getBrownianMotion(10, 1, 1)
        
        assert xAxisPositions[0] == 0, f"Expected x origin to be 0 but got {xAxisPositions[0]}"
        assert yAxisPositions[0] == 0, f"Expected y origin to be 0 but got {yAxisPositions[0]}"

    def testPlotBrownianMotion(self, mockPlot):
        """
        Test if plotting functions are called
        """

        xAxisPositions = np.array([0, 1, 2])
        yAxisPositions = np.array([0, 1, 2])
        
        plotBrownianMotion(xAxisPositions, yAxisPositions)
        
        plt.figure.assert_called_once()
        plt.plot.assert_called_once()
        plt.savefig.assert_called_once()