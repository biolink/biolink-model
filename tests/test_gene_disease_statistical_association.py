"""Test gene to disease statistical association."""
import unittest
from biolink_model.datamodel.model import GeneToDiseaseStatisticalAssociation


class TestGeneDiseaseStatisticalAssociation(unittest.TestCase):
    """Test gene to disease statistical association."""

    def test_association_exists(self):
        """Test that gene to disease statistical association class exists."""
        # This test verifies that the new association class exists and can be imported
        self.assertTrue(hasattr(GeneToDiseaseStatisticalAssociation, '__name__'))
        self.assertEqual(GeneToDiseaseStatisticalAssociation.__name__, 'GeneToDiseaseStatisticalAssociation')

    def test_association_inheritance(self):
        """Test that the association inherits from gene to disease association."""
        from biolink_model.datamodel.model import GeneToDiseaseAssociation
        
        # Test inheritance relationship
        self.assertTrue(issubclass(GeneToDiseaseStatisticalAssociation, GeneToDiseaseAssociation))


if __name__ == '__main__':
    unittest.main()