import pyodbc
from abc import ABC, abstractmethod
from entity.artist import Artist
from exception.artist_exceptions import ArtistNotFoundException

class ArtistDAO(ABC):
    @abstractmethod
    def get_all_artists(self) -> list:
        pass

    @abstractmethod
    def add_artist(self, artist: Artist) -> bool:
        pass

    @abstractmethod
    def update_artist(self, artist: Artist) -> bool:
        pass

    @abstractmethod
    def remove_artist(self, artist_id: int) -> bool:
        pass

    @abstractmethod
    def get_artist_by_id(self, artist_id: int) -> Artist:
        pass

    @abstractmethod
    def search_artists(self, keyword: str) -> list:
        pass


class ArtistDAOImpl(ArtistDAO):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def get_all_artists(self) -> list:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Artist")
            artists = []
            for row in cursor.fetchall():
                artist = Artist(row.ArtistID, row.Name, row.Biography, row.BirthDate, row.Nationality, row.Website, row.ContactInformation)
                artists.append(artist)
            connection.close()
            return artists
        except Exception as e:
            print(f"Error fetching artists: {e}")
            return []

    def add_artist(self, artist: Artist) -> bool:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Artist (Name, Biography, BirthDate, Nationality, Website, ContactInformation) VALUES (?, ?, ?, ?, ?, ?)",
                           artist.name, artist.biography, artist.birth_date, artist.nationality, artist.website, artist.contact_information)
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(f"Error adding artist: {e}")
            return False

    def update_artist(self, artist: Artist) -> bool:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("UPDATE Artist SET Name=?, Biography=?, BirthDate=?, Nationality=?, Website=?, ContactInformation=? WHERE ArtistID=?",
                           artist.name, artist.biography, artist.birth_date, artist.nationality, artist.website, artist.contact_information, artist.artist_id)
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(f"Error updating artist: {e}")
            return False

    def remove_artist(self, artist_id: int) -> bool:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Artist WHERE ArtistID=?", artist_id)
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(f"Error removing artist: {e}")
            return False

    def get_artist_by_id(self, artist_id: int) -> Artist:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Artist WHERE ArtistID=?", artist_id)
            row = cursor.fetchone()
            connection.close()
            if row:
                return Artist(row.ArtistID, row.Name, row.Biography, row.BirthDate, row.Nationality, row.Website, row.ContactInformation)
            else:
                raise ArtistNotFoundException(f"Artist with ID {artist_id} not found.")
        except Exception as e:
            print(f"Error fetching artist by ID: {e}")
            return None

    def search_artists(self, keyword: str) -> list:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            query = "SELECT * FROM Artist WHERE Name LIKE ? OR Biography LIKE ?"
            cursor.execute(query, ('%' + keyword + '%', '%' + keyword + '%'))
            artists = []
            for row in cursor.fetchall():
                artist = Artist(row.ArtistID, row.Name, row.Biography, row.BirthDate, row.Nationality, row.Website, row.ContactInformation)
                artists.append(artist)
            connection.close()
            return artists
        except Exception as e:
            print(f"Error searching artists: {e}")
            return []
