import unittest
from unittest.mock import MagicMock
from dao import VirtualArtGalleryDAOImpl
from entity import Artwork

class TestVirtualArtGalleryDAOImpl(unittest.TestCase):
    def setUp(self):
        self.dao = VirtualArtGalleryDAOImpl("your_connection_string_here")

    def test_add_artwork(self):
        artwork = Artwork(None, "Test Title", "Test Description", "2024-05-20", "Test Medium", "http://example.com/image.jpg")
        self.dao.add_artwork = MagicMock(return_value=True)
        result = self.dao.add_artwork(artwork)
        self.assertTrue(result)

    def test_get_artwork_by_id(self):
        artwork = Artwork(1, "Test Title", "Test Description", "2024-05-20", "Test Medium", "http://example.com/image.jpg")
        self.dao.get_artwork_by_id = MagicMock(return_value=artwork)
        result = self.dao.get_artwork_by_id(1)
        self.assertEqual(result.artwork_id, 1)
        self.assertEqual(result.title, "Test Title")

if __name__ == "__main__":
    unittest.main()
