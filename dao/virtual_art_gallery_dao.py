# # dao/virtual_art_gallery_dao.py

# from abc import ABC, abstractmethod
# from entity import Artwork, Artist, User, Gallery

# class IVirtualArtGalleryDAO(ABC):

#     # Artwork methods
#     @abstractmethod
#     def add_artwork(self, artwork: Artwork) -> bool:
#         """
#         Add an artwork to the database.
#         Returns True if the artwork is successfully added, False otherwise.
#         """
#         pass

#     @abstractmethod
#     def update_artwork(self, artwork: Artwork) -> bool:
#         """
#         Update an existing artwork in the database.
#         Returns True if the artwork is successfully updated, False otherwise.
#         """
#         pass

#     @abstractmethod
#     def remove_artwork(self, artwork_id: int) -> bool:
#         """
#         Remove an artwork from the database.
#         Returns True if the artwork is successfully removed, False otherwise.
#         """
#         pass

#     @abstractmethod
#     def get_artwork_by_id(self, artwork_id: int) -> Artwork:
#         """
#         Retrieve an artwork from the database by its ID.
#         Returns the Artwork object if found, raises an exception otherwise.
#         """
#         pass

#     @abstractmethod
#     def search_artworks(self, keyword: str) -> list:
#         """
#         Search for artworks in the database based on a keyword.
#         Returns a list of Artwork objects matching the search criteria.
#         """
#         pass

#     @abstractmethod
#     def get_all_artworks(self) -> list:
#         """
#         Retrieve all artworks from the database.
#         Returns a list of Artwork objects.
#         """
#         pass

#     @abstractmethod
#     def add_artwork_to_favorite(self, user_id: int, artwork_id: int) -> bool:
#         """
#         Add an artwork to a user's favorites.
#         Returns True if the artwork is successfully added to the user's favorites, False otherwise.
#         """
#         pass

#     @abstractmethod
#     def remove_artwork_from_favorite(self, user_id: int, artwork_id: int) -> bool:
#         """
#         Remove an artwork from a user's favorites.
#         Returns True if the artwork is successfully removed from the user's favorites, False otherwise.
#         """
#         pass

#     @abstractmethod
#     def get_user_favorite_artworks(self, user_id: int) -> list:
#         """
#         Retrieve the favorite artworks of a user.
#         Returns a list of Artwork objects representing the user's favorite artworks.
#         """
#         pass

#     # Artist methods
#     @abstractmethod
#     def add_artist(self, artist: Artist) -> bool:
#         """
#         Add a new artist to the database.
#         Returns True if the artist is successfully added, False otherwise.
#         """
#         pass

#     @abstractmethod
#     def update_artist(self, artist: Artist) -> bool:
#         """
#         Update an existing artist in the database.
#         Returns True if the artist is successfully updated, False otherwise.
#         """
#         pass

#     @abstractmethod
#     def remove_artist(self, artist_id: int) -> bool:
#         """
#         Remove an artist from the database by their ID.
#         Returns True if the artist is successfully removed, False otherwise.
#         """
#         pass

#     @abstractmethod
#     def search_artists(self, keyword: str) -> list:
#         """
#         Search for artists in the database based on a keyword.
#         Returns a list of Artist objects matching the search criteria.
#         """
#         pass

#     @abstractmethod
#     def get_artist_by_id(self, artist_id: int) -> Artist:
#         """
#         Retrieve an artist from the database by their ID.
#         Returns the Artist object if found, raises an exception otherwise.
#         """
#         pass

#     # User methods
#     @abstractmethod
#     def add_user(self, user: User) -> bool:
#         """
#         Add a new user to the database.
#         Returns True if the user is successfully added, False otherwise.
#         """
#         pass

#     @abstractmethod
#     def update_user(self, user: User) -> bool:
#         """
#         Update an existing user in the database.
#         Returns True if the user is successfully updated, False otherwise.
#         """
#         pass

#     @abstractmethod
#     def remove_user(self, user_id: int) -> bool:
#         """
#         Remove a user from the database by their ID.
#         Returns True if the user is successfully removed, False otherwise.
#         """
#         pass

#     @abstractmethod
#     def search_users(self, keyword: str) -> list:
#         """
#         Search for users in the database based on a keyword.
#         Returns a list of User objects matching the search criteria.
#         """
#         pass

#     @abstractmethod
#     def get_user_by_id(self, user_id: int) -> User:
#         """
#         Retrieve a user from the database by their ID.
#         Returns the User object if found, raises an exception otherwise.
#         """
#         pass

#     # Gallery methods
#     @abstractmethod
#     def add_gallery(self, gallery: Gallery) -> bool:
#         """
#         Add a new gallery to the database.
#         Returns True if the gallery is successfully added, False otherwise.
#         """
#         pass

#     @abstractmethod
#     def update_gallery(self, gallery: Gallery) -> bool:
#         """
#         Update an existing gallery in the database.
#         Returns True if the gallery is successfully updated, False otherwise.
#         """
#         pass

#     @abstractmethod
#     def remove_gallery(self, gallery_id: int) -> bool:
#         """
#         Remove a gallery from the database by its ID.
#         Returns True if the gallery is successfully removed, False otherwise.
#         """
#         pass

#     @abstractmethod
#     def search_galleries(self, keyword: str) -> list:
#         """
#         Search for galleries in the database based on a keyword.
#         Returns a list of Gallery objects matching the search criteria.
#         """
#         pass

#     @abstractmethod
#     def get_gallery_by_id(self, gallery_id: int) -> Gallery:
#         """
#         Retrieve a gallery from the database by its ID.
#         Returns the Gallery object if found, raises an exception otherwise.
#         """
#         pass
