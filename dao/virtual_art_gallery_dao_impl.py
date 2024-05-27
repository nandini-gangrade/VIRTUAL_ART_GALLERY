# import pyodbc
# from dao import IVirtualArtGalleryDAO
# from entity import Artwork, Artist, User, Gallery
# from exception import ArtworkNotFoundException, UserNotFoundException

# class VirtualArtGalleryDAOImpl(IVirtualArtGalleryDAO):
#     def __init__(self, connection_string: str):
#         self.connection_string = connection_string

#     def get_connection(self):
#         return pyodbc.connect(self.connection_string)

#     def execute_query(self, query, *params):
#         with self.get_connection() as conn:
#             with conn.cursor() as cursor:
#                 cursor.execute(query, params)
#                 return cursor.fetchall()

#     def execute_update(self, query, *params):
#         with self.get_connection() as conn:
#             with conn.cursor() as cursor:
#                 cursor.execute(query, params)
#                 conn.commit()

#     def add_artwork(self, artwork: Artwork) -> bool:
#         try:
#             query = "INSERT INTO Artwork (Title, Description, CreationDate, Medium, ImageURL) VALUES (?, ?, ?, ?, ?)"
#             self.execute_update(query, artwork.title, artwork.description, artwork.creation_date, artwork.medium, artwork.image_url)
#             return True
#         except pyodbc.Error as e:
#             print("Error occurred while adding artwork:", e)
#             return False

#     def get_all_artworks(self) -> list:
#         try:
#             query = "SELECT * FROM Artwork"
#             rows = self.execute_query(query)
#             artworks = [Artwork(*row) for row in rows]
#             return artworks
#         except pyodbc.Error as e:
#             print("Error occurred while retrieving all artworks:", e)
#             return []

#     def update_artwork(self, artwork: Artwork) -> bool:
#         try:
#             query = "UPDATE Artwork SET Title = ?, Description = ?, CreationDate = ?, Medium = ?, ImageURL = ? WHERE ArtworkID = ?"
#             self.execute_update(query, artwork.title, artwork.description, artwork.creation_date, artwork.medium, artwork.image_url, artwork.artwork_id)
#             return True
#         except pyodbc.Error as e:
#             print("Error occurred while updating artwork:", e)
#             return False

#     def remove_artwork(self, artwork_id: int) -> bool:
#         try:
#             query = "DELETE FROM Artwork WHERE ArtworkID = ?"
#             self.execute_update(query, artwork_id)
#             return True
#         except pyodbc.Error as e:
#             print("Error occurred while removing artwork:", e)
#             return False

#     def search_artworks(self, keyword: str) -> list:
#         try:
#             query = "SELECT * FROM Artwork WHERE Title LIKE ? OR Description LIKE ?"
#             rows = self.execute_query(query, f'%{keyword}%', f'%{keyword}%')
#             artworks = [Artwork(*row) for row in rows]
#             return artworks
#         except pyodbc.Error as e:
#             print("Error occurred while searching artworks:", e)
#             return []

#     def add_artwork_to_favorite(self, user_id: int, artwork_id: int) -> bool:
#         try:
#             query = "INSERT INTO User_Favorite_Artwork (UserID, ArtworkID) VALUES (?, ?)"
#             self.execute_update(query, user_id, artwork_id)
#             return True
#         except pyodbc.Error as e:
#             print("Error occurred while adding artwork to favorites:", e)
#             return False

#     def remove_artwork_from_favorite(self, user_id: int, artwork_id: int) -> bool:
#         try:
#             query = "DELETE FROM User_Favorite_Artwork WHERE UserID = ? AND ArtworkID = ?"
#             self.execute_update(query, user_id, artwork_id)
#             return True
#         except pyodbc.Error as e:
#             print("Error occurred while removing artwork from favorites:", e)
#             return False

#     def get_artwork_by_id(self, artwork_id: int) -> Artwork:
#         try:
#             query = "SELECT * FROM Artwork WHERE ArtworkID = ?"
#             row = self.execute_query(query, artwork_id)
#             if not row:
#                 raise ArtworkNotFoundException(f"Artwork with ID {artwork_id} not found.")
#             return Artwork(*row[0])
#         except pyodbc.Error as e:
#             print(f"Error occurred while getting artwork by ID: {e}")
#             return None

#     def get_user_favorite_artworks(self, user_id: int) -> list:
#         try:
#             query = """
#                 SELECT Artwork.ArtworkID, Artwork.Title, Artwork.Description, Artwork.CreationDate, Artwork.Medium, Artwork.ImageURL
#                 FROM Artwork
#                 JOIN User_Favorite_Artwork ON Artwork.ArtworkID = User_Favorite_Artwork.ArtworkID
#                 WHERE User_Favorite_Artwork.UserID = ?
#             """
#             rows = self.execute_query(query, user_id)
#             favorite_artworks = [Artwork(*row) for row in rows]
#             if not favorite_artworks:
#                 raise UserNotFoundException(f"User with ID {user_id} not found.")
#             return favorite_artworks
#         except pyodbc.Error as e:
#             print("Error occurred while getting user's favorite artworks:", e)
#             return []
        
#     def search_artists(self, keyword):
#             artists = []
#             try:
#                 conn = pyodbc.connect(self.connection_string)
#                 cursor = conn.cursor()
#                 query = "SELECT artist_id, name, bio, birth_date, death_date FROM Artists WHERE name LIKE ? OR bio LIKE ?"
#                 cursor.execute(query, ('%' + keyword + '%', '%' + keyword + '%'))
#                 for row in cursor.fetchall():
#                     artist = Artist(row.artist_id, row.name, row.bio, row.birth_date, row.death_date)
#                     artists.append(artist)
#                 cursor.close()
#                 conn.close()
#             except pyodbc.Error as e:
#                 print(f"Error searching artists: {e}")
#             return artists
        
#     def add_artist(self, artist):
#         try:
#             conn = pyodbc.connect(self.connection_string)
#             cursor = conn.cursor()
#             query = "INSERT INTO Artists (name, bio, birth_date, death_date) VALUES (?, ?, ?, ?)"
#             cursor.execute(query, (artist.name, artist.bio, artist.birth_date, artist.death_date))
#             conn.commit()
#             cursor.close()
#             conn.close()
#             return True
#         except pyodbc.Error as e:
#             print(f"Error adding artist: {e}")
#             return False

#     def update_artist(self, artist):
#         try:
#             conn = pyodbc.connect(self.connection_string)
#             cursor = conn.cursor()
#             query = "UPDATE Artists SET name = ?, bio = ?, birth_date = ?, death_date = ? WHERE artist_id = ?"
#             cursor.execute(query, (artist.name, artist.bio, artist.birth_date, artist.death_date, artist.artist_id))
#             conn.commit()
#             cursor.close()
#             conn.close()
#             return True
#         except pyodbc.Error as e:
#             print(f"Error updating artist: {e}")
#             return False

#     def remove_artist(self, artist_id):
#         try:
#             conn = pyodbc.connect(self.connection_string)
#             cursor = conn.cursor()
#             query = "DELETE FROM Artists WHERE artist_id = ?"
#             cursor.execute(query, (artist_id,))
#             conn.commit()
#             cursor.close()
#             conn.close()
#             return True
#         except pyodbc.Error as e:
#             print(f"Error removing artist: {e}")
#             return False

#     def search_artists(self, keyword):
#         artists = []
#         try:
#             conn = pyodbc.connect(self.connection_string)
#             cursor = conn.cursor()
#             query = "SELECT artist_id, name, bio, birth_date, death_date FROM Artists WHERE name LIKE ? OR bio LIKE ?"
#             cursor.execute(query, ('%' + keyword + '%', '%' + keyword + '%'))
#             for row in cursor.fetchall():
#                 artist = Artist(row.artist_id, row.name, row.bio, row.birth_date, row.death_date)
#                 artists.append(artist)
#             cursor.close()
#             conn.close()
#         except pyodbc.Error as e:
#             print(f"Error searching artists: {e}")
#         return artists

#     def get_artist_by_id(self, artist_id):
#         try:
#             conn = pyodbc.connect(self.connection_string)
#             cursor = conn.cursor()
#             query = "SELECT artist_id, name, bio, birth_date, death_date FROM Artists WHERE artist_id = ?"
#             cursor.execute(query, (artist_id,))
#             row = cursor.fetchone()
#             if row:
#                 return Artist(row.artist_id, row.name, row.bio, row.birth_date, row.death_date)
#             cursor.close()
#             conn.close()
#             return None
#         except pyodbc.Error as e:
#             print(f"Error retrieving artist: {e}")
#             return None
 
#     def add_artist(self):
#         name = input("Enter artist name: ")
#         bio = input("Enter artist biography: ")
#         birth_date = input("Enter birth date (YYYY-MM-DD): ")
#         death_date = input("Enter death date (YYYY-MM-DD), leave blank if still alive: ")
#         death_date = death_date if death_date else None
#         artist = Artist(None, name, bio, birth_date, death_date)
#         if self.dao.add_artist(artist):
#             print("Artist added successfully.")
#         else:
#             print("Failed to add artist.")

#     def update_artist(self):
#         artist_id = int(input("Enter artist ID to update: "))
#         existing_artist = self.dao.get_artist_by_id(artist_id)
#         if existing_artist:
#             print(f"Existing Name: {existing_artist.name}")
#             name = input(f"Enter new name (Leave empty to keep '{existing_artist.name}'): ") or existing_artist.name
#             bio = input(f"Enter new biography (Leave empty to keep '{existing_artist.bio}'): ") or existing_artist.bio
#             birth_date = input(f"Enter new birth date (Leave empty to keep '{existing_artist.birth_date}'): ") or existing_artist.birth_date
#             death_date = input(f"Enter new death date (Leave empty to keep '{existing_artist.death_date}'): ") or existing_artist.death_date

#             updated_artist = Artist(artist_id, name, bio, birth_date, death_date)
#             success = self.dao.update_artist(updated_artist)
#             if success:
#                 print("Artist updated successfully.")
#             else:
#                 print("Failed to update artist.")
#         else:
#             print(f"Artist with ID {artist_id} not found.")

#     def remove_artist(self):
#         try:
#             artist_id = int(input("Enter artist ID to remove: "))
#             if self.dao.remove_artist(artist_id):
#                 print("Artist removed successfully.")
#             else:
#                 print("Failed to remove artist.")
#         except Exception as e:
#             print(f"Error removing artist: {e}")

#     def add_user(self, user):
#         try:
#             conn = pyodbc.connect(self.connection_string)
#             cursor = conn.cursor()
#             query = "INSERT INTO Users (username, email, password, created_at) VALUES (?, ?, ?, ?)"
#             cursor.execute(query, (user.username, user.email, user.password, user.created_at))
#             conn.commit()
#             cursor.close()
#             conn.close()
#             return True
#         except pyodbc.Error as e:
#             print(f"Error adding user: {e}")
#             return False

#     def update_user(self, user):
#         try:
#             conn = pyodbc.connect(self.connection_string)
#             cursor = conn.cursor()
#             query = "UPDATE Users SET username = ?, email = ?, password = ? WHERE user_id = ?"
#             cursor.execute(query, (user.username, user.email, user.password, user.user_id))
#             conn.commit()
#             cursor.close()
#             conn.close()
#             return True
#         except pyodbc.Error as e:
#             print(f"Error updating user: {e}")
#             return False

#     def remove_user(self, user_id):
#         try:
#             conn = pyodbc.connect(self.connection_string)
#             cursor = conn.cursor()
#             query = "DELETE FROM Users WHERE user_id = ?"
#             cursor.execute(query, (user_id,))
#             conn.commit()
#             cursor.close()
#             conn.close()
#             return True
#         except pyodbc.Error as e:
#             print(f"Error removing user: {e}")
#             return False

#     def search_users(self, keyword):
#         users = []
#         try:
#             conn = pyodbc.connect(self.connection_string)
#             cursor = conn.cursor()
#             query = "SELECT user_id, username, email, password, created_at FROM Users WHERE username LIKE ? OR email LIKE ?"
#             cursor.execute(query, ('%' + keyword + '%', '%' + keyword + '%'))
#             for row in cursor.fetchall():
#                 user = User(row.user_id, row.username, row.email, row.password, row.created_at)
#                 users.append(user)
#             cursor.close()
#             conn.close()
#         except pyodbc.Error as e:
#             print(f"Error searching users: {e}")
#         return users

#     def get_user_by_id(self, user_id):
#         try:
#             conn = pyodbc.connect(self.connection_string)
#             cursor = conn.cursor()
#             query = "SELECT user_id, username, email, password, created_at FROM Users WHERE user_id = ?"
#             cursor.execute(query, (user_id,))
#             row = cursor.fetchone()
#             if row:
#                 return User(row.user_id, row.username, row.email, row.password, row.created_at)
#             cursor.close()
#             conn.close()
#             return None
#         except pyodbc.Error as e:
#             print(f"Error retrieving user: {e}")
#             return None

#     def add_gallery(self, gallery):
#         try:
#             conn = pyodbc.connect(self.connection_string)
#             cursor = conn.cursor()
#             query = "INSERT INTO Galleries (name, location, description) VALUES (?, ?, ?)"
#             cursor.execute(query, (gallery.name, gallery.location, gallery.description))
#             conn.commit()
#             cursor.close()
#             conn.close()
#             return True
#         except pyodbc.Error as e:
#             print(f"Error adding gallery: {e}")
#             return False

#     def update_gallery(self, gallery):
#         try:
#             conn = pyodbc.connect(self.connection_string)
#             cursor = conn.cursor()
#             query = "UPDATE Galleries SET name = ?, location = ?, description = ? WHERE gallery_id = ?"
#             cursor.execute(query, (gallery.name, gallery.location, gallery.description, gallery.gallery_id))
#             conn.commit()
#             cursor.close()
#             conn.close()
#             return True
#         except pyodbc.Error as e:
#             print(f"Error updating gallery: {e}")
#             return False

#     def remove_gallery(self, gallery_id):
#         try:
#             conn = pyodbc.connect(self.connection_string)
#             cursor = conn.cursor()
#             query = "DELETE FROM Galleries WHERE gallery_id = ?"
#             cursor.execute(query, (gallery_id,))
#             conn.commit()
#             cursor.close()
#             conn.close()
#             return True
#         except pyodbc.Error as e:
#             print(f"Error removing gallery: {e}")
#             return False

#     def search_galleries(self, keyword):
#         galleries = []
#         try:
#             conn = pyodbc.connect(self.connection_string)
#             cursor = conn.cursor()
#             query = "SELECT gallery_id, name, location, description FROM Galleries WHERE name LIKE ? OR location LIKE ? OR description LIKE ?"
#             cursor.execute(query, ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
#             for row in cursor.fetchall():
#                 gallery = Gallery(row.gallery_id, row.name, row.location, row.description)
#                 galleries.append(gallery)
#             cursor.close()
#             conn.close()
#         except pyodbc.Error as e:
#             print(f"Error searching galleries: {e}")
#         return galleries

#     def get_gallery_by_id(self, gallery_id):
#         try:
#             conn = pyodbc.connect(self.connection_string)
#             cursor = conn.cursor()
#             query = "SELECT gallery_id, name, location, description FROM Galleries WHERE gallery_id = ?"
#             cursor.execute(query, (gallery_id,))
#             row = cursor.fetchone()
#             if row:
#                 return Gallery(row.gallery_id, row.name, row.location, row.description)
#             cursor.close()
#             conn.close()
#             return None
#         except pyodbc.Error as e:
#             print(f"Error retrieving gallery: {e}")
#             return None
