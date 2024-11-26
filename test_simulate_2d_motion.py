import pytest
import numpy as np
from simulate_2d_motion import getBrownianMotion

class Test2DSimulation:
    """
    Test suite for 2D Brownian motion simulation
    """

    def testGetBrownianMotionShape(self):
        """
        Test if getBrownianMotion returns correct array shapes
        """

        noOfTimeSteps = 10
        xAxisPositions, yAxisPositions = getBrownianMotion(noOfTimeSteps, 1, 1)
        
        assert len(xAxisPositions) == noOfTimeSteps, f"Expected xAxisPositions to be of length {noOfTimeSteps}, but got {len(xAxisPositions)}"
        assert len(yAxisPositions) == noOfTimeSteps, f"Expected yAxisPositions to be of length {noOfTimeSteps}, but got {len(yAxisPositions)}"

    def testGetBrownianMotionStartPosition(self):
        """
        Test if particle starts at origin [0,0]
        """

        xAxisPositions, yAxisPositions = getBrownianMotion(10, 1, 1)
        
        assert xAxisPositions[0] == 0, f"Expected x origin to be 0 but got {xAxisPositions[0]}"
        assert yAxisPositions[0] == 0, f"Expected y origin to be 0 but got {yAxisPositions[0]}"
    
    def testIfInvalidInputsAreRejected(self):
        """
        Test to see if invalid values to getBrownianMotion are being rejected
        """

        with pytest.raises(ValueError, match="noOfTimeSteps must be positive"):
            getBrownianMotion(0, 1, 1)
        
        with pytest.raises(ValueError, match="stepSize must be positive"):
            getBrownianMotion(10, 0, 1)
            
        with pytest.raises(ValueError, match="sigma must be positive"):
            getBrownianMotion(10, 1, 0)
    
    def testRandomBehavior(self):
        """
        Test to check that the random increments behave as expected.
        """

        noOfTimeSteps = 10
        stepSize = 1
        sigma = 1

        xAxisPositions, yAxisPositions = getBrownianMotion(noOfTimeSteps, stepSize, sigma)

        dx = np.diff(xAxisPositions)
        dy = np.diff(yAxisPositions)

        assert dx.std() > 0, "dx standard deviation should be greater than 0."
        assert dy.std() > 0, "dy standard deviation should be greater than 0."
    
    def testLargeNoOfTimeSteps(self):
        """
        Test the function with a very large number of time steps.
        """

        noOfTimeSteps = 10**6
        stepSize = 1
        sigma = 1

        xAxisPositions, yAxisPositions = getBrownianMotion(noOfTimeSteps, stepSize, sigma)

        assert len(xAxisPositions) == noOfTimeSteps, "Length mismatch for large noOfTimeSteps in xAxisPositions."
        assert len(yAxisPositions) == noOfTimeSteps, "Length mismatch for large noOfTimeSteps in yAxisPositions."
    
    def testMinimalInput(self):
        """
        Test the function with the smallest valid number of time steps.
        """

        noOfTimeSteps = 1
        stepSize = 1
        sigma = 1

        xAxisPositions, yAxisPositions = getBrownianMotion(noOfTimeSteps, stepSize, sigma)

        assert len(xAxisPositions) == 1, "Expected single value for xAxisPositions, but got more."
        assert len(yAxisPositions) == 1, "Expected single value for yAxisPositions, but got more."
        assert xAxisPositions[0] == 0, "Expected xAxisPositions[0] to be 0 for minimal input."
        assert yAxisPositions[0] == 0, "Expected yAxisPositions[0] to be 0 for minimal input."
    
    def testBehaviorWithFixedSeed(self):
        """
        Test to check deterministic output with a fixed random seed.
        """

        noOfTimeSteps = 1
        stepSize = 1
        sigma = 1

        np.random.seed(42)
        x1, y1 = getBrownianMotion(noOfTimeSteps, stepSize, sigma)
        np.random.seed(42)
        x2, y2 = getBrownianMotion(noOfTimeSteps, stepSize, sigma)

        assert np.allclose(x1, x2), "Outputs differ despite using the same seed for xAxisPositions."
        assert np.allclose(y1, y2), "Outputs differ despite using the same seed for yAxisPositions."