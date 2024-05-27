import pyodbc
from abc import ABC, abstractmethod
from entity.gallery import Gallery
from exception.gallery_exceptions import GalleryNotFoundException

class GalleryDAO(ABC):
    @abstractmethod
    def get_all_galleries(self) -> list:
        pass

    @abstractmethod
    def add_gallery(self, gallery: Gallery) -> bool:
        pass

    @abstractmethod
    def update_gallery(self, gallery: Gallery) -> bool:
        pass

    @abstractmethod
    def remove_gallery(self, gallery_id: int) -> bool:
        pass

    @abstractmethod
    def get_gallery_by_id(self, gallery_id: int) -> Gallery:
        pass

    @abstractmethod
    def search_galleries(self, keyword: str) -> list:
        pass


class GalleryDAOImpl(GalleryDAO):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def get_all_galleries(self) -> list:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Gallery")
            galleries = []
            for row in cursor.fetchall():
                gallery = Gallery(row.GalleryID, row.Name, row.Description, row.Location, row.Curator, row.OpeningHours)
                galleries.append(gallery)
            connection.close()
            return galleries
        except Exception as e:
            print(f"Error fetching galleries: {e}")
            return []

    def add_gallery(self, gallery: Gallery) -> bool:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Gallery (Name, Description, Location, Curator, OpeningHours) VALUES (?, ?, ?, ?, ?)",
                           gallery.name, gallery.description, gallery.location, gallery.curator, gallery.opening_hours)
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(f"Error adding gallery: {e}")
            return False

    def update_gallery(self, gallery: Gallery) -> bool:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("UPDATE Gallery SET Name=?, Description=?, Location=?, Curator=?, OpeningHours=? WHERE GalleryID=?",
                           gallery.name, gallery.description, gallery.location, gallery.curator, gallery.opening_hours, gallery.gallery_id)
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(f"Error updating gallery: {e}")
            return False

    def remove_gallery(self, gallery_id: int) -> bool:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Gallery WHERE GalleryID=?", gallery_id)
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(f"Error removing gallery: {e}")
            return False

    def get_gallery_by_id(self, gallery_id: int) -> Gallery:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Gallery WHERE GalleryID=?", gallery_id)
            row = cursor.fetchone()
            connection.close()
            if row:
                return Gallery(row.GalleryID, row.Name, row.Description, row.Location, row.Curator, row.OpeningHours)
            else:
                raise GalleryNotFoundException(f"Gallery with ID {gallery_id} not found.")
        except Exception as e:
            print(f"Error fetching gallery by ID: {e}")
            return None

    def search_galleries(self, keyword: str) -> list:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            query = "SELECT * FROM Gallery WHERE Name LIKE ? OR Description LIKE ?"
            cursor.execute(query, ('%' + keyword + '%', '%' + keyword + '%'))
            galleries = []
            for row in cursor.fetchall():
                gallery = Gallery(row.GalleryID, row.Name, row.Description, row.Location, row.Curator, row.OpeningHours)
                galleries.append(gallery)
            connection.close()
            return galleries
        except Exception as e:
            print(f"Error searching galleries: {e}")
            return []
