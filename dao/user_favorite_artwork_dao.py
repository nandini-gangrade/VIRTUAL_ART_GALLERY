# user_favorite_artwork_dao.py
import pyodbc
from abc import ABC, abstractmethod
from entity import *
from exception.user_favorite_artwork_exceptions import UserFavoriteArtworkNotFoundException

class UserFavoriteArtworkDAO(ABC):
    @abstractmethod
    def add_favorite_artwork(self, user_id: int, artwork_id: int) -> bool:
        pass

    @abstractmethod
    def remove_favorite_artwork(self, user_id: int, artwork_id: int) -> bool:
        pass

    @abstractmethod
    def get_user_favorite_artworks(self, user_id: int) -> list:
        pass


class UserFavoriteArtworkDAOImpl(UserFavoriteArtworkDAO):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def add_favorite_artwork(self, user_id: int, artwork_id: int) -> bool:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO User_Favorite_Artwork (UserID, ArtworkID) VALUES (?, ?)", user_id, artwork_id)
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(f"Error adding favorite artwork: {e}")
            return False

    def remove_favorite_artwork(self, user_id: int, artwork_id: int) -> bool:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("DELETE FROM User_Favorite_Artwork WHERE UserID=? AND ArtworkID=?", user_id, artwork_id)
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(f"Error removing favorite artwork: {e}")
            return False

    def get_user_favorite_artworks(self, user_id: int) -> list:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("SELECT ArtworkID, Title FROM User_Favorite_Artwork JOIN Artwork ON User_Favorite_Artwork.ArtworkID = Artwork.ArtworkID WHERE UserID=?", user_id)
            favorite_artworks = [(row.ArtworkID, row.Title) for row in cursor.fetchall()]
            connection.close()
            return favorite_artworks
        except Exception as e:
            print(f"Error fetching user's favorite artworks: {e}")
            return []


