import pyodbc
from abc import ABC, abstractmethod
from entity.artwork import Artwork
from exception.artwork_exceptions import ArtworkNotFoundException

class ArtworkDAO(ABC):
    @abstractmethod
    def get_all_artworks(self) -> list:
        pass

    @abstractmethod
    def add_artwork(self, artwork: Artwork) -> bool:
        pass

    @abstractmethod
    def update_artwork(self, artwork: Artwork) -> bool:
        pass

    @abstractmethod
    def remove_artwork(self, artwork_id: int) -> bool:
        pass

    @abstractmethod
    def get_artwork_by_id(self, artwork_id: int) -> Artwork:
        pass

    @abstractmethod
    def search_artworks(self, keyword: str) -> list:
        pass


class ArtworkDAOImpl(ArtworkDAO):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def get_all_artworks(self) -> list:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Artwork")
            artworks = []
            for row in cursor.fetchall():
                artwork = Artwork(row.ArtworkID, row.Title, row.Description, row.CreationDate, row.Medium, row.ImageURL)
                artworks.append(artwork)
            connection.close()
            return artworks
        except Exception as e:
            print(f"Error fetching artworks: {e}")
            return []

    def add_artwork(self, artwork: Artwork) -> bool:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Artwork (Title, Description, CreationDate, Medium, ImageURL) VALUES (?, ?, ?, ?, ?)",
                           artwork.title, artwork.description, artwork.creation_date, artwork.medium, artwork.image_url)
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(f"Error adding artwork: {e}")
            return False

    def update_artwork(self, artwork: Artwork) -> bool:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("UPDATE Artwork SET Title=?, Description=?, CreationDate=?, Medium=?, ImageURL=? WHERE ArtworkID=?",
                           artwork.title, artwork.description, artwork.creation_date, artwork.medium, artwork.image_url, artwork.artwork_id)
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(f"Error updating artwork: {e}")
            return False

    def remove_artwork(self, artwork_id: int) -> bool:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Artwork WHERE ArtworkID=?", artwork_id)
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(f"Error removing artwork: {e}")
            return False

    def get_artwork_by_id(self, artwork_id: int) -> Artwork:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Artwork WHERE ArtworkID=?", artwork_id)
            row = cursor.fetchone()
            connection.close()
            if row:
                return Artwork(row.ArtworkID, row.Title, row.Description, row.CreationDate, row.Medium, row.ImageURL)
            else:
                raise ArtworkNotFoundException(f"Artwork with ID {artwork_id} not found.")
        except Exception as e:
            print(f"Error fetching artwork by ID: {e}")
            return None

    def search_artworks(self, keyword: str) -> list:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            query = "SELECT * FROM Artwork WHERE Title LIKE ? OR Description LIKE ?"
            cursor.execute(query, ('%' + keyword + '%', '%' + keyword + '%'))
            artworks = []
            for row in cursor.fetchall():
                artwork = Artwork(row.ArtworkID, row.Title, row.Description, row.CreationDate, row.Medium, row.ImageURL)
                artworks.append(artwork)
            connection.close()
            return artworks
        except Exception as e:
            print(f"Error searching artworks: {e}")
            return []
