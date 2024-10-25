import pytest
import numpy as np
from unittest.mock import patch, Mock
import matplotlib.pyplot as plt
from simulate_time_and_space_motion import getBrownianMotion, plotBrownianMotion

class TestTimeAndSpaceSimulation:
    """
    Test suite for Time and Space Brownian motion simulation
    """

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

        samplePointsAcrossTime, motion = getBrownianMotion(1000, 1, 1.0)
        
        assert len(samplePointsAcrossTime) == 1000, f"Expected samplePointsAcrossTime length to be 1000, but got {len(samplePointsAcrossTime)}"
        assert motion.shape == (1000, 1), f"Expected brownianMotion shape to be (1000, 1), but got {motion.shape}"
    
    def testIfInvalidInputsAreRejected(self):
        """
        Test to see if invalid values to getBrownianMotion is being rejected
        """

        with pytest.raises(ValueError):
            getBrownianMotion(0, 1, 1.)

        with pytest.raises(ValueError):
            getBrownianMotion(1000, 0, 1.)

        with pytest.raises(ValueError):
            getBrownianMotion(1000, 1, 0)

    def testPlotBrownianMotion(self, mockPlot):
        """
        Test if plotting functions are called
        """

        samplePointsAcrossTime, brownianMotion = getBrownianMotion(1000, 1, 1.)
        plotBrownianMotion(samplePointsAcrossTime, brownianMotion)

        plt.plot.assert_called_once()
        plt.savefig.assert_called_once()