# dao/virtual_art_gallery_dao.py

from abc import ABC, abstractmethod
from entity import Artwork

class IVirtualArtGalleryDAO(ABC):
    @abstractmethod
    def add_artwork(self, artwork: Artwork) -> bool:
        """
        Add an artwork to the database.
        Returns True if the artwork is successfully added, False otherwise.
        """
        pass
    
    @abstractmethod
    def update_artwork(self, artwork: Artwork) -> bool:
        """
        Update an existing artwork in the database.
        Returns True if the artwork is successfully updated, False otherwise.
        """
        pass
    
    @abstractmethod
    def remove_artwork(self, artwork_id: int) -> bool:
        """
        Remove an artwork from the database.
        Returns True if the artwork is successfully removed, False otherwise.
        """
        pass
    
    @abstractmethod
    def get_artwork_by_id(self, artwork_id: int) -> Artwork:
        """
        Retrieve an artwork from the database by its ID.
        Returns the Artwork object if found, raises an exception otherwise.
        """
        pass
    
    @abstractmethod
    def search_artworks(self, keyword: str) -> list:
        """
        Search for artworks in the database based on a keyword.
        Returns a list of Artwork objects matching the search criteria.
        """
        pass
    
    @abstractmethod
    def add_artwork_to_favorite(self, user_id: int, artwork_id: int) -> bool:
        """
        Add an artwork to a user's favorites.
        Returns True if the artwork is successfully added to the user's favorites, False otherwise.
        """
        pass
    
    @abstractmethod
    def remove_artwork_from_favorite(self, user_id: int, artwork_id: int) -> bool:
        """
        Remove an artwork from a user's favorites.
        Returns True if the artwork is successfully removed from the user's favorites, False otherwise.
        """
        pass
    
    @abstractmethod
    def get_user_favorite_artworks(self, user_id: int) -> list:
        """
        Retrieve the favorite artworks of a user.
        Returns a list of Artwork objects representing the user's favorite artworks.
        """
        pass
    
    @abstractmethod
    def get_all_artworks(self) -> list:
        """
        Retrieve all artworks from the database.
        Returns a list of Artwork objects.
        """
        pass
    