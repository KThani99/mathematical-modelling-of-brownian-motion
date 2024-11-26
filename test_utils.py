import pytest
from unittest.mock import patch
from utils.main import getUniqueFileName

class TestFileUtils:
    """
    Test suite for file utility functions
    """
    
    @pytest.fixture
    def mockTime(self):
        """
        Fixture to provide a consistent timestamp for testing
        """
        with patch('utils.main.getUniqueId', return_value="dbe43931-e894-4675-91b3-7c7073b60b64"):
            yield

    def testGetUniqueFileName(self, mockTime):
        """
        Test basic functionality of getUniqueFileName
        """

        result = getUniqueFileName("test_image")
        expected = "test_image-dbe43931-e894-4675-91b3-7c7073b60b64.png"
        assert result == expected, f"Expected {expected}, but got {result}"
    
    def testGetUniqueFileNameWithEmptyString(self, mockTime):
        """
        Test getUniqueFileName with empty string input
        """

        result = getUniqueFileName("")
        expected = "-dbe43931-e894-4675-91b3-7c7073b60b64.png"
        assert result == expected, f"Expected {expected}, but got {result}"