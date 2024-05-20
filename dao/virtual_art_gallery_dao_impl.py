import pyodbc
from dao import IVirtualArtGalleryDAO
from entity import Artwork
from exception import ArtworkNotFoundException, UserNotFoundException

class VirtualArtGalleryDAOImpl(IVirtualArtGalleryDAO):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def get_connection(self):
        return pyodbc.connect(self.connection_string)

    def execute_query(self, query, *params):
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()

    def execute_update(self, query, *params):
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                conn.commit()

    def add_artwork(self, artwork: Artwork) -> bool:
        try:
            query = "INSERT INTO Artwork (Title, Description, CreationDate, Medium, ImageURL) VALUES (?, ?, ?, ?, ?)"
            self.execute_update(query, artwork.title, artwork.description, artwork.creation_date, artwork.medium, artwork.image_url)
            return True
        except pyodbc.Error as e:
            print("Error occurred while adding artwork:", e)
            return False

    def get_all_artworks(self) -> list:
        try:
            query = "SELECT * FROM Artwork"
            rows = self.execute_query(query)
            artworks = [Artwork(*row) for row in rows]
            return artworks
        except pyodbc.Error as e:
            print("Error occurred while retrieving all artworks:", e)
            return []

    def update_artwork(self, artwork: Artwork) -> bool:
        try:
            query = "UPDATE Artwork SET Title = ?, Description = ?, CreationDate = ?, Medium = ?, ImageURL = ? WHERE ArtworkID = ?"
            self.execute_update(query, artwork.title, artwork.description, artwork.creation_date, artwork.medium, artwork.image_url, artwork.artwork_id)
            return True
        except pyodbc.Error as e:
            print("Error occurred while updating artwork:", e)
            return False

    def remove_artwork(self, artwork_id: int) -> bool:
        try:
            query = "DELETE FROM Artwork WHERE ArtworkID = ?"
            self.execute_update(query, artwork_id)
            return True
        except pyodbc.Error as e:
            print("Error occurred while removing artwork:", e)
            return False

    def search_artworks(self, keyword: str) -> list:
        try:
            query = "SELECT * FROM Artwork WHERE Title LIKE ? OR Description LIKE ?"
            rows = self.execute_query(query, f'%{keyword}%', f'%{keyword}%')
            artworks = [Artwork(*row) for row in rows]
            return artworks
        except pyodbc.Error as e:
            print("Error occurred while searching artworks:", e)
            return []

    def add_artwork_to_favorite(self, user_id: int, artwork_id: int) -> bool:
        try:
            query = "INSERT INTO User_Favorite_Artwork (UserID, ArtworkID) VALUES (?, ?)"
            self.execute_update(query, user_id, artwork_id)
            return True
        except pyodbc.Error as e:
            print("Error occurred while adding artwork to favorites:", e)
            return False

    def remove_artwork_from_favorite(self, user_id: int, artwork_id: int) -> bool:
        try:
            query = "DELETE FROM User_Favorite_Artwork WHERE UserID = ? AND ArtworkID = ?"
            self.execute_update(query, user_id, artwork_id)
            return True
        except pyodbc.Error as e:
            print("Error occurred while removing artwork from favorites:", e)
            return False

    def get_artwork_by_id(self, artwork_id: int) -> Artwork:
        try:
            query = "SELECT * FROM Artwork WHERE ArtworkID = ?"
            row = self.execute_query(query, artwork_id)
            if not row:
                raise ArtworkNotFoundException(f"Artwork with ID {artwork_id} not found.")
            return Artwork(*row[0])
        except pyodbc.Error as e:
            print(f"Error occurred while getting artwork by ID: {e}")
            return None

    def get_user_favorite_artworks(self, user_id: int) -> list:
        try:
            query = """
                SELECT Artwork.ArtworkID, Artwork.Title, Artwork.Description, Artwork.CreationDate, Artwork.Medium, Artwork.ImageURL
                FROM Artwork
                JOIN User_Favorite_Artwork ON Artwork.ArtworkID = User_Favorite_Artwork.ArtworkID
                WHERE User_Favorite_Artwork.UserID = ?
            """
            rows = self.execute_query(query, user_id)
            favorite_artworks = [Artwork(*row) for row in rows]
            if not favorite_artworks:
                raise UserNotFoundException(f"User with ID {user_id} not found.")
            return favorite_artworks
        except pyodbc.Error as e:
            print("Error occurred while getting user's favorite artworks:", e)
            return []
