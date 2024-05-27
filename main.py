# import pyodbc
# import sys
# import os

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# import pyodbc
# from util import DBPropertyUtil 
# from exception import *
# from dao import *
# from entity import *

# class VirtualArtGalleryApp:
#     def __init__(self):
#         try:
#             connection_string = DBPropertyUtil.get_connection_string()
#             self.artwork_dao = ArtworkDAOImpl(connection_string)
#             self.artist_dao = ArtistDAOImpl(connection_string)
#             self.gallery_dao = GalleryDAOImpl(connection_string)
#             self.user_dao = UserDAOImpl(connection_string)
#             self.user_favorite_artwork_dao = UserFavoriteArtworkDAOImpl(connection_string)
#             self.artwork_gallery_dao = ArtworkGalleryDAOImpl(connection_string)
#             self.main_menu()
#         except Exception as e:
#             print(f"Error initializing the application: {e}")


# # -------------------------------------MAIN MENU---------------------------------------------------------------------

#     def main_menu(self):
#         try:
#             while True:
#                 print("\nVirtual Art Gallery")
#                 print("1. Artwork Management")
#                 print("2. Artist Management")
#                 print("3. Gallery Management")
#                 print("4. User Management")
#                 print("5. Exit")

#                 choice = input("Enter your choice: ")

#                 if choice == "1":
#                     self.artwork_management_menu()
#                 elif choice == "2":
#                     self.artist_management_menu()
#                 elif choice == "3":
#                     self.gallery_management_menu()
#                 elif choice == "4":
#                     self.user_management_menu()
#                 elif choice == "5":
#                     print("Exiting Virtual Art Gallery.")
#                     break
#                 else:
#                     print("Invalid choice. Please enter a valid option.")
#         except Exception as e:
#             print(f"Error in main menu: {e}")


# # -------------------------------------ARTWORK MANAGEMENT MENU---------------------------------------------------------------------

#     def artwork_management_menu(self):
#         try:
#             while True:
#                 print("\nArtwork Management")
#                 print("1. Display All Artworks")
#                 print("2. Add Artwork")
#                 print("3. Update Artwork")
#                 print("4. Remove Artwork")
#                 print("5. Search Artworks")
#                 print("6. Add Artwork to Favorite")
#                 print("7. Remove Artwork from Favorite")
#                 print("8. Add Artwork to Gallery")
#                 print("9. Get User Favorite Artworks")
#                 print("10. Remove Artwork from Gallery")
#                 print("11. View Galleries Containing Artwork")
#                 print("12. Back to Main Menu")

#                 choice = input("Enter your choice: ")

#                 if choice == "1":
#                     self.display_all_artworks()
#                 elif choice == "2":
#                     self.add_artwork()
#                 elif choice == "3":
#                     self.update_artwork()
#                 elif choice == "4":
#                     self.remove_artwork()
#                 elif choice == "5":
#                     self.search_artworks()
#                 elif choice == "6":
#                     self.add_artwork_to_favorite()
#                 elif choice == "7":
#                     self.remove_artwork_from_favorite()
#                 elif choice == '8':
#                     self.add_artwork_to_gallery()
#                 elif choice == '9':
#                     self.get_user_favorite_artworks()
#                 elif choice == '10':
#                     self.remove_artwork_from_gallery()
#                 elif choice == '11':
#                     self.get_artwork_galleries()
#                 elif choice == "12":
#                     break
#                 else:
#                     print("Invalid choice. Please enter a valid option.")
#         except Exception as e:
#             print(f"Error in artwork management menu: {e}")

#     def display_all_artworks(self):
#         try:
#             artworks = self.artwork_dao.get_all_artworks()
#             if artworks:
#                 print("\nAll Artworks:")
#                 for artwork in artworks:
#                     print(artwork)
#             else:
#                 print("No artworks found.")
#         except ArtworkNotFoundException as e:
#             print(e)
#         except Exception as e:
#             print(f"Error displaying artworks: {e}")

#     def add_artwork(self):
#         try:
#             title = input("Enter title: ")
#             description = input("Enter description: ")
#             creation_date = input("Enter creation date (YYYY-MM-DD): ")
#             medium = input("Enter medium: ")
#             image_url = input("Enter image URL: ")
#             artwork = Artwork(None, title, description, creation_date, medium, image_url)
#             if self.artwork_dao.add_artwork(artwork):
#                 print("Artwork added successfully.")
#             else:
#                 print("Failed to add artwork.")
#         except Exception as e:
#             print(f"Error adding artwork: {e}")

#     def update_artwork(self):
#         try:
#             matching_artworks = self.search_artworks()
#             if not matching_artworks:
#                 return 
#             artwork_id = int(input("Enter the ID of the artwork you want to update from the list above: "))
#             existing_artwork = self.artwork_dao.get_artwork_by_id(artwork_id)
#             if existing_artwork:
#                 print(f"Existing Title: {existing_artwork.title}")
#                 title = input(f"Enter new title (Leave empty to keep '{existing_artwork.title}'): ") or existing_artwork.title
#                 description = input(f"Enter new description (Leave empty to keep '{existing_artwork.description}'): ") or existing_artwork.description
#                 creation_date = input(f"Enter new creation date (Leave empty to keep '{existing_artwork.creation_date}'): ") or existing_artwork.creation_date
#                 medium = input(f"Enter new medium (Leave empty to keep '{existing_artwork.medium}'): ") or existing_artwork.medium
#                 image_url = input(f"Enter new image URL (Leave empty to keep '{existing_artwork.image_url}'): ") or existing_artwork.image_url

#                 updated_artwork = Artwork(existing_artwork.artwork_id, title, description, creation_date, medium, image_url)
#                 success = self.artwork_dao.update_artwork(updated_artwork)
#                 if success:
#                     print("Artwork updated successfully.")
#                 else:
#                     print("Failed to update artwork.")
#             else:
#                 raise ArtistNotFoundException(artwork_id)
#         except ArtworkNotFoundException as e:
#             print(e)
#         except Exception as e:
#             print(f"Error updating artwork: {e}")

#     def remove_artwork(self):
#         try:
#             matching_artworks = self.search_artworks()
#             if not matching_artworks:
#                 return 
#             artwork_id = int(input("Enter artwork ID to remove: "))
#             if not self.artwork_dao.get_artwork_by_id(artwork_id):
#                 raise ArtworkNotFoundException(artwork_id)
#             if self.artwork_dao.remove_artwork(artwork_id):
#                 print("Artwork removed successfully.")
#             else:
#                 print("Failed to remove artwork.")
#         except ArtworkNotFoundException as e:
#             print(e)
#         except Exception as e:
#             print(f"Error removing artwork: {e}")

#     def search_artworks(self):
#         try:
#             keyword = input("Enter a keyword to search for artworks: ")
#             matching_artworks = self.artwork_dao.search_artworks(keyword)
#             if matching_artworks:
#                 print("Matching artworks:")
#                 for artwork in matching_artworks:
#                     print(f"ID: {artwork.artwork_id}, Title: {artwork.title}, Description: {artwork.description}")
#                 return matching_artworks
#             else:
#                 print("No matching artworks found.")
#                 return []
#         except Exception as e:
#             print(f"Error searching artworks: {e}")
#             return []


#     def add_artwork_to_favorite(self):
#         try:
#             matching_users = self.search_users()
#             if not matching_users:
#                 return

#             user_id = int(input("Enter the ID of the user you want to add artwork to favorites from the list above: "))
#             matching_artworks = self.search_artworks()
#             if not matching_artworks:
#                 return

#             artwork_id = int(input("Enter the ID of the artwork to add to favorites from the list above: "))
#             if self.user_favorite_artwork_dao.add_favorite_artwork(user_id, artwork_id):
#                 print("Artwork added to favorites successfully.")
#             else:
#                 print("Failed to add artwork to favorites.")
#         except pyodbc.IntegrityError as e:
#             error_code = e.args[0]
#             if error_code == '23000':
#                 print("Artwork is already in the user's favorites.")
#             else:
#                 print(f"Error adding artwork to favorites: {e}")
#         except UserFavoriteArtworkNotFoundException as e:
#             print(e)
#         except Exception as e:
#             print(f"Error adding artwork to favorites: {e}")

#     def remove_artwork_from_favorite(self):
#         try:
#             matching_users = self.search_users()
#             if not matching_users:
#                 return

#             user_id = int(input("Enter the ID of the user you want to remove artwork from favorites from the list above: "))
#             matching_artworks = self.search_artworks()
#             if not matching_artworks:
#                 return

#             artwork_id = int(input("Enter the ID of the artwork to remove from favorites from the list above: "))
#             if self.user_favorite_artwork_dao.remove_favorite_artwork(user_id, artwork_id):
#                 print("Artwork removed from favorites successfully.")
#             else:
#                 raise ArtworkNotFoundException(artwork_id)
#         except ArtworkNotFoundException as e:
#             print(e)
#         except Exception as e:
#             print(f"Error removing artwork from favorites: {e}")

#     def get_user_favorite_artworks(self):
#         try:
#             matching_users = self.search_users()
#             if not matching_users:
#                 return

#             user_id = int(input("Enter the ID of the user whose favorite artworks you want to view from the list above: "))
#             artworks = self.user_favorite_artwork_dao.get_user_favorite_artworks(user_id)
#             print(f"\nFavorite Artworks for User ID {user_id}:")
#             for artwork in artworks:
#                 print(artwork)
#         except UserNotFoundException as e:
#             print(e)
#         except Exception as e:
#             print(f"Error retrieving favorite artworks: {e}")

#     def add_artwork_to_gallery(self):
#         try:
#             matching_artworks = self.search_artworks()
#             if not matching_artworks:
#                 return
#             artwork_id = int(input("Enter the ID of the artwork to add to a gallery from the list above: "))
#             if not self.artwork_dao.get_artwork_by_id(artwork_id):
#                 raise ArtworkNotFoundException(artwork_id)
#             matching_galleries = self.search_galleries()
#             if not matching_galleries:
#                 return
#             gallery_id = int(input("Enter the ID of the gallery to add the artwork to from the list above: "))
#             if not self.gallery_dao.get_gallery_by_id(gallery_id):
#                 raise GalleryNotFoundException(gallery_id)
#             if self.artwork_gallery_dao.add_artwork_to_gallery(artwork_id, gallery_id):
#                 print("Artwork added to gallery successfully.")
#             else:
#                 print("Failed to add artwork to gallery.")
#         except (ArtworkNotFoundException, GalleryNotFoundException, ArtworkGalleryNotFoundException) as e:
#             print(e)
#         except Exception as e:
#             print(f"Error adding artwork to gallery: {e}")

#     def remove_artwork_from_gallery(self):
#         try:
#             matching_artworks = self.search_artworks()
#             if not matching_artworks:
#                 return
#             artwork_id = int(input("Enter the ID of the artwork to remove from a gallery from the list above: "))
#             if not self.artwork_dao.get_artwork_by_id(artwork_id):
#                 raise ArtworkNotFoundException(artwork_id)
#             matching_galleries = self.search_galleries()
#             if not matching_galleries:
#                 return
#             gallery_id = int(input("Enter the ID of the gallery to remove the artwork from from the list above: "))
#             if not self.gallery_dao.get_gallery_by_id(gallery_id):
#                 raise GalleryNotFoundException(gallery_id)
#             if self.artwork_gallery_dao.remove_artwork_from_gallery(artwork_id, gallery_id):
#                 print("Artwork removed from gallery successfully.")
#             else:
#                 print("Failed to remove artwork from gallery.")
#         except (ArtworkNotFoundException, GalleryNotFoundException, ArtworkGalleryNotFoundException) as e:
#             print(e)
#         except Exception as e:
#             print(f"Error removing artwork from gallery: {e}")

#     def get_artwork_galleries(self):
#         try:
#             matching_artworks = self.search_artworks()
#             if not matching_artworks:
#                 return
#             artwork_id = int(input("Enter the ID of the artwork to view galleries for from the list above: "))
#             if not self.artwork_dao.get_artwork_by_id(artwork_id):
#                 raise ArtworkNotFoundException(artwork_id)
#             galleries = self.artwork_gallery_dao.get_artwork_galleries(artwork_id)
#             print(f"\nGalleries containing Artwork ID {artwork_id}:")
#             for gallery in galleries:
#                 print(gallery)
#         except ArtworkGalleryNotFoundException as e:
#             print(e)
#         except Exception as e:
#             print(f"Error retrieving galleries containing the artwork: {e}")


# # -------------------------------------ARTIST MANAGEMENT MENU---------------------------------------------------------------------

#     def artist_management_menu(self):
#         try:
#             while True:
#                 print("\nArtist Management")
#                 print("1. Display All Artists")
#                 print("2. Add Artist")
#                 print("3. Update Artist")
#                 print("4. Remove Artist")
#                 print("5. Search Artists")
#                 print("6. Back to Main Menu")

#                 choice = input("Enter your choice: ")

#                 if choice == "1":
#                     self.display_all_artists()
#                 elif choice == "2":
#                     self.add_artist()
#                 elif choice == "3":
#                     self.update_artist()
#                 elif choice == "4":
#                     self.remove_artist()
#                 elif choice == "5":
#                     self.search_artists()
#                 elif choice == "6":
#                     break
#                 else:
#                     print("Invalid choice. Please enter a valid option.")
#         except Exception as e:
#             print(f"Error in artist management menu: {e}")

#     def display_all_artists(self):
#         try:
#             artists = self.artist_dao.get_all_artists()
#             if artists:
#                 print("\nAll Artists:")
#                 for artist in artists:
#                     print(artist)
#             else:
#                 print("No artists found.")
#         except Exception as e:
#             print(f"Error fetching artists: {e}")

#     def add_artist(self):
#         try:
#             name = input("Enter name: ")
#             bio = input("Enter bio: ")
#             birth_date = input("Enter birth date (YYYY-MM-DD): ")
#             death_date = input("Enter death date (YYYY-MM-DD): ")
#             website = input("Enter Website: ")
#             contact_information = input("Enter Contact Information: ")
#             artist = Artist(None, name, bio, birth_date, death_date, website, contact_information)
#             if self.artist_dao.add_artist(artist):
#                 print("Artist added successfully.")
#             else:
#                 print("Failed to add artist.")
#         except Exception as e:
#             print(f"Error adding artist: {e}")

#     def update_artist(self):
#         try:
#             matching_artists = self.search_artists()
#             if not matching_artists:
#                 return

#             artist_id = int(input("Enter the ID of the artist you want to update from the list above: "))
#             existing_artist = self.artist_dao.get_artist_by_id(artist_id)
#             if existing_artist:
#                 print(f"Existing Name: {existing_artist.name}")
#                 name = input(f"Enter new name (Leave empty to keep '{existing_artist.name}'): ") or existing_artist.name
#                 bio = input(f"Enter new bio (Leave empty to keep '{existing_artist.biography}'): ") or existing_artist.biography
#                 birth_date = input(f"Enter new birth date (Leave empty to keep '{existing_artist.birth_date}'): ") or existing_artist.birth_date
#                 nationality = input(f"Enter new nationality (Leave empty to keep '{existing_artist.nationality}'): ") or existing_artist.nationality
#                 website = input(f"Enter new website (Leave empty to keep '{existing_artist.website}'): ") or existing_artist.website
#                 contact_info = input(f"Enter new contact information (Leave empty to keep '{existing_artist.contact_information}'): ") or existing_artist.contact_information

#                 updated_artist = Artist(existing_artist.artist_id, name, bio, birth_date, nationality, website, contact_info)
#                 success = self.artist_dao.update_artist(updated_artist)
#                 if success:
#                     print("Artist updated successfully.")
#                 else:
#                     print("Failed to update artist.")
#             else:
#                 raise ArtistNotFoundException(artist_id) 
#         except ArtistNotFoundException as e:
#             print(e)
#         except Exception as e:
#             print(f"Error updating artist: {e}")

#     def remove_artist(self):
#         try:
#             matching_artists = self.search_artists()
#             if not matching_artists:
#                 return 
            
#             artist_id = int(input("Enter artist ID to remove: "))
#             if self.artist_dao.remove_artist(artist_id):
#                 print("Artist removed successfully.")
#             else:
#                 print("Failed to remove artist.")
#         except ArtistNotFoundException as e:
#             print(e)
#         except Exception as e:
#             print(f"Error removing artist: {e}")

#     def search_artists(self):
#         try:
#             keyword = input("Enter a keyword to search for artists: ")
#             matching_artists = self.artist_dao.search_artists(keyword)
#             if matching_artists:
#                 print("Matching artists:")
#                 for artist in matching_artists:
#                     print(f"ID: {artist.artist_id}, Name: {artist.name}, Bio: {artist.biography}")
#                 return matching_artists
#             else:
#                 print("No matching artists found.")
#                 return []
#         except ArtistNotFoundException as e:
#             print(e)
#         except Exception as e:
#             print(f"Error searching artists: {e}")
#             return []


# # -------------------------------------GALLERY MANAGEMENT MENU---------------------------------------------------------------------

#     def gallery_management_menu(self):
#         try:
#             while True:
#                 print("\nGallery Management")
#                 print("1. Display All Galleries")
#                 print("2. Add Gallery")
#                 print("3. Update Gallery")
#                 print("4. Remove Gallery")
#                 print("5. Search Galleries")
#                 print("6. Add Artwork to Gallery")
#                 print("7. Remove Artwork from Gallery")
#                 print("8. View Galleries Containing Artwork")
#                 print("9. Back to Main Menu")

#                 choice = input("Enter your choice: ")

#                 if choice == "1":
#                     self.display_all_galleries()
#                 elif choice == "2":
#                     self.add_gallery()
#                 elif choice == "3":
#                     self.update_gallery()
#                 elif choice == "4":
#                     self.remove_gallery()
#                 elif choice == "5":
#                     self.search_galleries()
#                 elif choice == '6':
#                     self.add_artwork_to_gallery()
#                 elif choice == '7':
#                     self.remove_artwork_from_gallery()
#                 elif choice == '8':
#                     self.get_artwork_galleries()
#                 elif choice == "9":
#                     break
#                 else:
#                     print("Invalid choice. Please enter a valid option.")
#         except Exception as e:
#             print(f"Error in gallery management menu: {e}")

#     def display_all_galleries(self):
#         try:
#             galleries = self.gallery_dao.get_all_galleries()
#             if galleries:
#                 print("\nAll Galleries:")
#                 for gallery in galleries:
#                     print(gallery)
#             else:
#                 print("No galleries found.")
#         except Exception as e:
#             print(f"Error fetching galleries: {e}")

#     def add_gallery(self):
#         try:
#             name = input("Enter name: ")
#             location = input("Enter location: ")
#             curator = input("Enter curator: ")
#             opening_hours = input("Enter opening hours: ")
#             gallery = Gallery(None, name, location, curator, opening_hours)
#             if self.gallery_dao.add_gallery(gallery):
#                 print("Gallery added successfully.")
#             else:
#                 print("Failed to add gallery.")
#         except Exception as e:
#             print(f"Error adding gallery: {e}")

#     def update_gallery(self):
#         try:
#             matching_galleries = self.search_galleries()
#             if not matching_galleries:
#                 return

#             gallery_id = int(input("Enter the ID of the gallery you want to update from the list above: "))
#             existing_gallery = self.gallery_dao.get_gallery_by_id(gallery_id)
#             if existing_gallery:
#                 print(f"Existing Name: {existing_gallery.name}")
#                 name = input(f"Enter new name (Leave empty to keep '{existing_gallery.name}'): ") or existing_gallery.name
#                 description = input(f"Enter new description (Leave empty to keep '{existing_gallery.description}'): ") or existing_gallery.description
#                 location = input(f"Enter new location (Leave empty to keep '{existing_gallery.location}'): ") or existing_gallery.location
#                 curator = input(f"Enter new curator ID (Leave empty to keep '{existing_gallery.curator}'): ") or existing_gallery.curator
#                 opening_hours = input(f"Enter new opening hours (Leave empty to keep '{existing_gallery.opening_hours}'): ") or existing_gallery.opening_hours

#                 updated_gallery = Gallery(existing_gallery.gallery_id, name, description, location, curator, opening_hours)
#                 success = self.gallery_dao.update_gallery(updated_gallery)
#                 if success:
#                     print("Gallery updated successfully.")
#                 else:
#                     print("Failed to update gallery.")
#             else:
#                 raise GalleryNotFoundException(gallery_id)
#         except GalleryNotFoundException as e:
#             print(e)
#         except Exception as e:
#             print(f"Error updating gallery: {e}")

#     def search_galleries(self):
#         try:
#             keyword = input("Enter a keyword to search for galleries: ")
#             matching_galleries = self.gallery_dao.search_galleries(keyword)
#             if matching_galleries:
#                 print("Matching galleries:")
#                 for gallery in matching_galleries:
#                     print(f"ID: {gallery.gallery_id}, Name: {gallery.name}, Description: {gallery.description}")
#                 return matching_galleries
#             else:
#                 print("No matching galleries found.")
#                 return []
#         except Exception as e:
#             print(f"Error searching galleries: {e}")
#             return []

#     def remove_gallery(self):
#         try:
#             matching_galleries = self.search_galleries()
#             if not matching_galleries:
#                 return            
#             gallery_id = int(input("Enter gallery ID to remove: "))
#             if not self.gallery_dao.get_gallery_by_id(gallery_id):
#                 raise GalleryNotFoundException(gallery_id)
#             if self.gallery_dao.remove_gallery(gallery_id):
#                 print("Gallery removed successfully.")
#             else:
#                 print("Failed to remove gallery.")
#         except GalleryNotFoundException as e:
#             print(e)
#         except Exception as e:
#             print(f"Error removing gallery: {e}")

#     def add_artwork_to_gallery(self):
#         try:
#             matching_artworks = self.search_artworks()
#             if not matching_artworks:
#                 return
#             artwork_id = int(input("Enter the ID of the artwork to add to a gallery from the list above: "))
#             if not self.artwork_dao.get_artwork_by_id(artwork_id):
#                 raise ArtworkNotFoundException(artwork_id)
#             matching_galleries = self.search_galleries()
#             if not matching_galleries:
#                 return
#             gallery_id = int(input("Enter the ID of the gallery to add the artwork to from the list above: "))
#             if not self.gallery_dao.get_gallery_by_id(gallery_id):
#                 raise GalleryNotFoundException(gallery_id)
#             if self.artwork_gallery_dao.add_artwork_to_gallery(artwork_id, gallery_id):
#                 print("Artwork added to gallery successfully.")
#             else:
#                 print("Failed to add artwork to gallery.")
#         except (ArtworkNotFoundException, GalleryNotFoundException, ArtworkGalleryNotFoundException) as e:
#             print(e)
#         except Exception as e:
#             print(f"Error adding artwork to gallery: {e}")

#     def remove_artwork_from_gallery(self):
#         try:
#             matching_artworks = self.search_artworks()
#             if not matching_artworks:
#                 return
#             artwork_id = int(input("Enter the ID of the artwork to remove from a gallery from the list above: "))
#             if not self.artwork_dao.get_artwork_by_id(artwork_id):
#                 raise ArtworkNotFoundException(artwork_id)
#             matching_galleries = self.search_galleries()
#             if not matching_galleries:
#                 return
#             gallery_id = int(input("Enter the ID of the gallery to remove the artwork from from the list above: "))
#             if not self.gallery_dao.get_gallery_by_id(gallery_id):
#                 raise GalleryNotFoundException(gallery_id)
#             if self.artwork_gallery_dao.remove_artwork_from_gallery(artwork_id, gallery_id):
#                 print("Artwork removed from gallery successfully.")
#             else:
#                 print("Failed to remove artwork from gallery.")
#         except (ArtworkNotFoundException, GalleryNotFoundException, ArtworkGalleryNotFoundException) as e:
#             print(e)
#         except Exception as e:
#             print(f"Error removing artwork from gallery: {e}")

#     def get_artwork_galleries(self):
#         try:
#             matching_artworks = self.search_artworks()
#             if not matching_artworks:
#                 return
#             artwork_id = int(input("Enter the ID of the artwork to view galleries for from the list above: "))
#             if not self.artwork_dao.get_artwork_by_id(artwork_id):
#                 raise ArtworkNotFoundException(artwork_id)
#             galleries = self.artwork_gallery_dao.get_artwork_galleries(artwork_id)
#             print(f"\nGalleries containing Artwork ID {artwork_id}:")
#             for gallery in galleries:
#                 print(gallery)
#         except ArtworkGalleryNotFoundException as e:
#             print(e)
#         except Exception as e:
#             print(f"Error retrieving galleries containing the artwork: {e}")


# # -------------------------------------USER MANAGEMENT MENU---------------------------------------------------------------------

#     def user_management_menu(self):
#         try:
#             while True:
#                 print("\nUser Management")
#                 print("1. Display All Users")
#                 print("2. Add User")
#                 print("3. Update User")
#                 print("4. Remove User")
#                 print("5. Search Users")
#                 print("6. Add Artwork to Favorite")
#                 print("7. Remove Artwork from Favorite")
#                 print("8. Get User Favorite Artworks")
#                 print("9. Back to Main Menu")

#                 choice = input("Enter your choice: ")

#                 if choice == "1":
#                     self.display_all_users()
#                 elif choice == "2":
#                     self.add_user()
#                 elif choice == "3":
#                     self.update_user()
#                 elif choice == "4":
#                     self.remove_user()
#                 elif choice == "5":
#                     self.search_users()
#                 elif choice == "6":
#                     self.add_artwork_to_favorite()
#                 elif choice == "7":
#                     self.remove_artwork_from_favorite()
#                 elif choice == "8":
#                     self.get_user_favorite_artworks()
#                 elif choice == "9":
#                     break
#                 else:
#                     print("Invalid choice. Please enter a valid option.")
#         except Exception as e:
#             print(f"Error in user management menu: {e}")

#     def display_all_users(self):
#         try:
#             users = self.user_dao.get_all_users()
#             if users:
#                 print("\nAll Users:")
#                 for user in users:
#                     print(user)
#             else:
#                 print("No users found.")                
#         except Exception as e:
#             print(f"Error fetching users: {e}")

#     def add_user(self):
#         try:
#             email = input("Enter email: ")
#             first_name = input("Enter first name: ")
#             last_name = input("Enter last name: ")
#             date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
#             profile_picture = input("Enter profile picture URL: ")
#             user = User(None, email, first_name, last_name, date_of_birth, profile_picture, [])
#             if self.user_dao.add_user(user):
#                 print("User added successfully.")
#             else:
#                 print("Failed to add user.")
#         except Exception as e:
#             print(f"Error adding user: {e}")

#     def update_user(self):
#         try:
#             matching_users = self.search_users()
#             if not matching_users:
#                 return  
#             user_id = int(input("Enter the ID of the user you want to update from the list above: "))
#             existing_user = self.user_dao.get_user_by_id(user_id)
#             if existing_user:
#                 print(f"Existing Username: {existing_user.username}")
#                 username = input(f"Enter new username (Leave empty to keep '{existing_user.username}'): ") or existing_user.username
#                 password = input(f"Enter new password (Leave empty to keep '{existing_user.password}'): ") or existing_user.password
#                 email = input(f"Enter new email (Leave empty to keep '{existing_user.email}'): ") or existing_user.email
#                 first_name = input(f"Enter new first name (Leave empty to keep '{existing_user.first_name}'): ") or existing_user.first_name
#                 last_name = input(f"Enter new last name (Leave empty to keep '{existing_user.last_name}'): ") or existing_user.last_name
#                 date_of_birth = input(f"Enter new date of birth (Leave empty to keep '{existing_user.date_of_birth}'): ") or existing_user.date_of_birth
#                 profile_picture = input(f"Enter new profile picture URL (Leave empty to keep '{existing_user.profile_picture}'): ") or existing_user.profile_picture
#                 favorite_artworks = input(f"Enter new favorite artworks (Leave empty to keep '{existing_user.favorite_artworks}'): ") or existing_user.favorite_artworks
#                 updated_user = User(existing_user.user_id, username, password, email, first_name, last_name, date_of_birth, profile_picture, favorite_artworks)
#                 success = self.user_dao.update_user(updated_user)
#                 if success:
#                     print("User updated successfully.")
#                 else:
#                     print("Failed to update user.")
#             else:
#                 raise UserNotFoundException(user_id)
#         except UserNotFoundException as e:
#             print(e)
#         except Exception as e:
#             print(f"Error updating user: {e}")

#     def search_users(self):
#         try:
#             keyword = input("Enter a keyword to search for users: ")
#             matching_users = self.user_dao.search_users(keyword)
#             if matching_users:
#                 print("Matching users:")
#                 for user in matching_users:
#                     print(f"ID: {user.user_id}, Username: {user.username}, Email: {user.email}")
#                 return matching_users
#             else:
#                 print("No matching users found.")
#                 return []
#         except Exception as e:
#             print(f"Error searching users: {e}")
#             return []

#     def remove_user(self):
#         try:
#             matching_users = self.search_users()
#             if not matching_users:
#                 return  
#             user_id = int(input("Enter user ID to remove: "))
#             if not self.user_dao.get_user_by_id(user_id):
#                 raise UserNotFoundException(user_id)
#             if self.user_dao.remove_user(user_id):
#                 print("User removed successfully.")
#             else:
#                 print("Failed to remove user.")
#         except UserNotFoundException as e:
#             print(e)
#         except Exception as e:
#             print(f"Error removing user: {e}")
            
#     def add_artwork_to_favorite(self):
#         try:
#             matching_users = self.search_users()
#             if not matching_users:
#                 return
#             user_id = int(input("Enter the ID of the user you want to add artwork to favorites from the list above: "))
#             matching_artworks = self.search_artworks()
#             if not matching_artworks:
#                 return
#             artwork_id = int(input("Enter the ID of the artwork to add to favorites from the list above: "))
#             if self.user_favorite_artwork_dao.add_favorite_artwork(user_id, artwork_id):
#                 print("Artwork added to favorites successfully.")
#             else:
#                 print("Failed to add artwork to favorites.")
#         except UserFavoriteArtworkNotFoundException as e:
#             print(e)
#         except pyodbc.IntegrityError as e:
#             error_code = e.args[0]
#             if error_code == '23000':
#                 print("Artwork is already in the user's favorites.")
#             else:
#                 print(f"Error adding artwork to favorites: {e}")
#         except Exception as e:
#             print(f"Error adding artwork to favorites: {e}")

#     def remove_artwork_from_favorite(self):
#         try:
#             matching_users = self.search_users()
#             if not matching_users:
#                 return

#             user_id = int(input("Enter the ID of the user you want to remove artwork from favorites from the list above: "))
#             matching_artworks = self.search_artworks()
#             if not matching_artworks:
#                 return

#             artwork_id = int(input("Enter the ID of the artwork to remove from favorites from the list above: "))
#             if self.user_favorite_artwork_dao.remove_favorite_artwork(user_id, artwork_id):
#                 print("Artwork removed from favorites successfully.")
#             else:
#                 print("Failed to remove artwork from favorites.")
#         except UserFavoriteArtworkNotFoundException as e:
#             print(e)
#         except Exception as e:
#             print(f"Error removing artwork from favorites: {e}")

#     def get_user_favorite_artworks(self):
#         try:
#             matching_users = self.search_users()
#             if not matching_users:
#                 return

#             user_id = int(input("Enter the ID of the user whose favorite artworks you want to view from the list above: "))
#             artworks = self.user_favorite_artwork_dao.get_user_favorite_artworks(user_id)
#             print(f"\nFavorite Artworks for User ID {user_id}:")
#             for artwork in artworks:
#                 print(artwork)
#         except UserNotFoundException as e:
#             print(e)
#         except Exception as e:
#             print(f"Error retrieving favorite artworks: {e}")
    

# if __name__ == "__main__":
#     app = VirtualArtGalleryApp()