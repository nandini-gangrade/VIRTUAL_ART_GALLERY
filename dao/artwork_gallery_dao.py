# artwork_gallery_dao.py
import pyodbc
from abc import ABC, abstractmethod
from entity import *
from exception.artwork_gallery_exceptions import ArtworkGalleryNotFoundException

class ArtworkGalleryDAO(ABC):
    @abstractmethod
    def add_artwork_to_gallery(self, artwork_id: int, gallery_id: int) -> bool:
        pass

    @abstractmethod
    def remove_artwork_from_gallery(self, artwork_id: int, gallery_id: int) -> bool:
        pass

    @abstractmethod
    def get_artwork_galleries(self, artwork_id: int) -> list:
        pass


class ArtworkGalleryDAOImpl(ArtworkGalleryDAO):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def add_artwork_to_gallery(self, artwork_id: int, gallery_id: int) -> bool:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Artwork_Gallery (ArtworkID, GalleryID) VALUES (?, ?)", artwork_id, gallery_id)
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(f"Error adding artwork to gallery: {e}")
            return False

    def remove_artwork_from_gallery(self, artwork_id: int, gallery_id: int) -> bool:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Artwork_Gallery WHERE ArtworkID=? AND GalleryID=?", artwork_id, gallery_id)
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(f"Error removing artwork from gallery: {e}")
            return False

    def get_artwork_galleries(self, artwork_id: int) -> list:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("SELECT GalleryID FROM Artwork_Gallery WHERE ArtworkID=?", artwork_id)
            galleries = [(row.GalleryID, row.Name) for row in cursor.fetchall()]
            connection.close()
            return galleries
        except Exception as e:
            print(f"Error fetching artwork's galleries: {e}")
            return []

