import pytest
import numpy as np
from unittest.mock import patch, Mock
import matplotlib.pyplot as plt
from simulate_time_and_space_motion import getBrownianMotion, plotBrownianMotion

class TestTimeAndSpaceSimulation:
    """
    Test suite for Time and Space Brownian motion simulation
    """
    
    def testGetBrownianMotionShape(self):
        """
        Test if getBrownianMotion returns correct array shapes
        """

        samplePointsAcrossTime, motion = getBrownianMotion(1000, 1, 1.0)
        
        assert len(samplePointsAcrossTime) == 1000, f"Expected samplePointsAcrossTime length to be 1000, but got {len(samplePointsAcrossTime)}"
        assert motion.shape == (1000, 1), f"Expected brownianMotion shape to be (1000, 1), but got {motion.shape}"
    
    def testGetBrownianMotionStartPosition(self):
        """
        Ensure the Brownian motion starts at the origin (0) for all motions.
        """

        noOfSamplePoints = 500
        noOfBrownianMotions = 5
        timeStep = 1.0

        _, brownianMotion = getBrownianMotion(noOfSamplePoints, noOfBrownianMotions, timeStep)

        assert np.all(brownianMotion[0, :] == 0), "Expected all motions to start at 0, but found non-zero values."
    
    def testIfInvalidInputsAreRejected(self):
        """
        Test to see if invalid values to getBrownianMotion are being rejected
        """

        with pytest.raises(ValueError):
            getBrownianMotion(0, 1, 1.)

        with pytest.raises(ValueError):
            getBrownianMotion(1000, 0, 1.)

        with pytest.raises(ValueError):
            getBrownianMotion(1000, 1, 0)
    
    def testRandomBehavior(self):
        """
        Test to check that the random increments behave as expected.
        """

        noOfSamplePoints = 1000
        noOfBrownianMotions = 3
        timeStep = 1.0

        _, brownianMotion = getBrownianMotion(noOfSamplePoints, noOfBrownianMotions, timeStep)

        increments = np.diff(brownianMotion, axis=0)

        assert np.allclose(np.mean(increments, axis=0), 0, atol=0.1), "Expected increments to have a mean near 0."

        expected_std = np.sqrt(timeStep / (noOfSamplePoints - 1))
        assert np.allclose(np.std(increments, axis=0), expected_std, atol=0.1), (
            f"Expected increment standard deviation to be {expected_std}, but got {np.std(increments, axis=0)}"
        )
    
    def testMinimalInput(self):
        """
        Test the function with the smallest valid inputs.
        """

        noOfSamplePoints = 2
        noOfBrownianMotions = 1
        timeStep = 0.1

        samplePointsAcrossTime, brownianMotion = getBrownianMotion(noOfSamplePoints, noOfBrownianMotions, timeStep)

        assert len(samplePointsAcrossTime) == 2, "Expected samplePointsAcrossTime to have length 1."
        assert brownianMotion.shape == (2, 1), "Expected brownianMotion shape to be (2, 1)."
        assert np.isclose(samplePointsAcrossTime[0], 0), "Expected first time point to be 0."
        assert brownianMotion[0, 0] == 0, "Expected Brownian motion to start at 0."

    def testLargeNoOfSamplePoints(self):
        """
        Test the function with a very large number of time steps.
        """

        noOfSamplePoints = 10**6
        noOfBrownianMotions = 1
        timeStep = 0.1

        samplePointsAcrossTime, _ = getBrownianMotion(noOfSamplePoints, noOfBrownianMotions, timeStep)
        assert len(samplePointsAcrossTime) == noOfSamplePoints, f"Expected samplePointsAcrossTime to have length {noOfSamplePoints}."

    def testBehaviorWithFixedSeed(self):
        """
        Test to check deterministic output with a fixed random seed.
        """

        noOfSamplePoints = 1000
        noOfBrownianMotions = 2
        timeStep = 1.0

        np.random.seed(42)
        sp1, bm1 = getBrownianMotion(noOfSamplePoints, noOfBrownianMotions, timeStep)
        np.random.seed(42)
        sp2, bm2 = getBrownianMotion(noOfSamplePoints, noOfBrownianMotions, timeStep)

        assert np.allclose(sp1, sp2), "Sample points differ despite using the same random seed."
        assert np.allclose(bm1, bm2), "Brownian motions differ despite using the same random seed."