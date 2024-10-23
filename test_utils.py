import pytest
from unittest.mock import patch
from utils.main import getCurrentTimeInEpochSeconds, getUniqueFileName

class TestFileUtils:
    """
    Test suite for file utility functions
    """
    
    @pytest.fixture
    def mockTime(self):
        """
        Fixture to provide a consistent timestamp for testing
        """
        with patch('utils.main.getCurrentTimeInEpochSeconds', return_value=1234567890):
            yield

    def testGetCurrentTimeInEpochSecondsReturnsInteger(self):
        """
        Test that getCurrentTimeInEpochSeconds returns an integer
        """

        result = getCurrentTimeInEpochSeconds()
        assert isinstance(result, int)

    def testGetUniqueFileName(self, mockTime):
        """
        Test basic functionality of getUniqueFileName
        """

        result = getUniqueFileName("test_image")
        expected = "test_image-1234567890.png"
        assert result == expected, f"Expected {expected}, but got {result}"
    
    def testGetUniqueFileNameWithEmptyString(self, mockTime):
        """
        Test getUniqueFileName with empty string input
        """

        result = getUniqueFileName("")
        expected = "-1234567890.png"
        assert result == expected, f"Expected {expected}, but got {result}"