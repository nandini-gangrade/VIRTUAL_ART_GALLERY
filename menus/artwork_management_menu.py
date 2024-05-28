import pyodbc
from exception import *
from dao import *
from entity import *
from util import *
from datetime import datetime

class ArtworkManagementMenu:
    def __init__(self,user_dao, artwork_dao, user_favorite_artwork_dao, artwork_gallery_dao, gallery_dao):
        connection_string = DBPropertyUtil.get_connection_string()
        self.artwork_dao = ArtworkDAOImpl(connection_string)
        self.user_dao = UserDAOImpl(connection_string)
        self.user_favorite_artwork_dao = UserFavoriteArtworkDAOImpl(connection_string)
        self.artwork_gallery_dao = ArtworkGalleryDAOImpl(connection_string)
        self.gallery_dao = GalleryDAOImpl(connection_string)


    def display_menu(self):
        try:
            while True:
                print("\nArtwork Management")
                print("1. Display All Artworks")
                print("2. Add Artwork")
                print("3. Update Artwork")
                print("4. Remove Artwork")
                print("5. Search Artworks")
                print("6. Add Artwork to Favorite")
                print("7. Remove Artwork from Favorite")
                print("8. Add Artwork to Gallery")
                print("9. Get User Favorite Artworks")
                print("10. Remove Artwork from Gallery")
                print("11. View Galleries Containing Artwork")
                print("12. Back to Main Menu")

                choice = input("Enter your choice: ")

                if choice == "1":
                    self.display_all_artworks()
                elif choice == "2":
                    self.add_artwork()
                elif choice == "3":
                    self.update_artwork()
                elif choice == "4":
                    self.remove_artwork()
                elif choice == "5":
                    self.search_artworks()
                elif choice == "6":
                    self.add_artwork_to_favorite()
                elif choice == "7":
                    self.remove_artwork_from_favorite()
                elif choice == '8':
                    self.add_artwork_to_gallery()
                elif choice == '9':
                    self.get_user_favorite_artworks()
                elif choice == '10':
                    self.remove_artwork_from_gallery()
                elif choice == '11':
                    self.get_artwork_galleries()
                elif choice == "12":
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")
        except Exception as e:
            print(f"Error in artwork management menu: {e}")

    def display_all_artworks(self):
        try:
            artworks = self.artwork_dao.get_all_artworks()
            if artworks:
                print("\nAll Artworks:")
                for artwork in artworks:
                    print(artwork)
            else:
                print("No artworks found.")
        except ArtworkNotFoundException as e:
            print(e)
        except Exception as e:
            print(f"Error displaying artworks: {e}")

    def add_artwork(self):
        try:
            title = input("Enter title: ")
            description = input("Enter description: ")
            creation_date = input("Enter creation date (YYYY-MM-DD): ")
            try:
                datetime.strptime(creation_date, '%Y-%m-%d')
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                return
            medium = input("Enter medium: ")
            image_url = input("Enter image URL: ")
            artwork = Artwork(None, title, description, creation_date, medium, image_url)
            if self.artwork_dao.add_artwork(artwork):
                print("Artwork added successfully.")
            else:
                print("Failed to add artwork.")
        except pyodbc.IntegrityError as e:
            error_code = e.args[0]
            if error_code == '22007':
                print("Please enter a valid date in the format YYYY-MM-DD.")
            else:
                print(f"Database error: {e}")
        except Exception as e:
            print(f"Error adding artwork: {e}")

    def update_artwork(self):
        try:
            matching_artworks = self.search_artworks()
            if not matching_artworks:
                return 
            artwork_id = int(input("Enter the ID of the artwork you want to update from the list above: "))
            existing_artwork = self.artwork_dao.get_artwork_by_id(artwork_id)
            if existing_artwork:
                print(f"Existing Title: {existing_artwork.title}")
                title = input(f"Enter new title (Leave empty to keep '{existing_artwork.title}'): ") or existing_artwork.title
                description = input(f"Enter new description (Leave empty to keep '{existing_artwork.description}'): ") or existing_artwork.description
                creation_date = input(f"Enter new creation date (Leave empty to keep '{existing_artwork.creation_date}'): ") or existing_artwork.creation_date
                try:
                    datetime.strptime(creation_date, '%Y-%m-%d')
                except ValueError:
                    print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                    return
                medium = input(f"Enter new medium (Leave empty to keep '{existing_artwork.medium}'): ") or existing_artwork.medium
                image_url = input(f"Enter new image URL (Leave empty to keep '{existing_artwork.image_url}'): ") or existing_artwork.image_url
                updated_artwork = Artwork(existing_artwork.artwork_id, title, description, creation_date, medium, image_url)
                success = self.artwork_dao.update_artwork(updated_artwork)              
                if success:
                    print("Artwork updated successfully.")
                else:
                    print("Failed to update artwork.")
            else:
                raise ArtworkNotFoundException(artwork_id)
        except ArtworkNotFoundException as e:
            print(e)
        except pyodbc.IntegrityError as e:
            error_code = e.args[0]
            if error_code == '22007':
                print("Please enter a valid date in the format YYYY-MM-DD.")
            else:
                print(f"Database error: {e}")
        except Exception as e:
            print(f"Error updating artwork: {e}")

    def remove_artwork(self):
        try:
            matching_artworks = self.search_artworks()
            if not matching_artworks:
                return 
            artwork_id = int(input("Enter artwork ID to remove: "))
            if not self.artwork_dao.get_artwork_by_id(artwork_id):
                raise ArtworkNotFoundException(artwork_id)
            if self.artwork_dao.remove_artwork(artwork_id):
                print("Artwork removed successfully.")
            else:
                print("Failed to remove artwork.")
        except ArtworkNotFoundException as e:
            print(e)
        except Exception as e:
            print(f"Error removing artwork: {e}")

    def search_artworks(self):
        try:
            keyword = input("Enter a keyword to search for artworks: ")
            matching_artworks = self.artwork_dao.search_artworks(keyword)
            if matching_artworks:
                print("Matching artworks:")
                for artwork in matching_artworks:
                    print(f"ID: {artwork.artwork_id}, Title: {artwork.title}, Description: {artwork.description}")
                return matching_artworks
            else:
                print("No matching artworks found.")
                return []
        except Exception as e:
            print(f"Error searching artworks: {e}")
            return []

    def add_artwork_to_favorite(self):
        try:
            matching_users = self.search_users()
            if not matching_users:
                return
            user_id = int(input("Enter the ID of the user you want to add artwork to favorites from the list above: "))
            matching_artworks = self.search_artworks()
            if not matching_artworks:
                return
            artwork_id = int(input("Enter the ID of the artwork to add to favorites from the list above: "))
            if self.user_favorite_artwork_dao.add_favorite_artwork(user_id, artwork_id):
                print("Artwork added to favorites successfully.")
            else:
                print("Failed to add artwork to favorites.")
        except pyodbc.IntegrityError as e:
            error_code = e.args[0]
            if error_code == '23000':
                print("Artwork is already in the user's favorites.")
            else:
                print(f"Error adding artwork to favorites: {e}")
        except UserFavoriteArtworkNotFoundException as e:
            print(e)
        except Exception as e:
            print(f"Error adding artwork to favorites: {e}")

    def remove_artwork_from_favorite(self):
        try:
            matching_users = self.search_users()
            if not matching_users:
                return
            user_id = int(input("Enter the ID of the user you want to remove artwork from favorites from the list above: "))
            matching_artworks = self.search_artworks()
            if not matching_artworks:
                return
            artwork_id = int(input("Enter the ID of the artwork to remove from favorites from the list above: "))
            if self.user_favorite_artwork_dao.remove_favorite_artwork(user_id, artwork_id):
                print("Artwork removed from favorites successfully.")
            else:
                raise ArtworkNotFoundException(artwork_id)
        except ArtworkNotFoundException as e:
            print(e)
        except Exception as e:
            print(f"Error removing artwork from favorites: {e}")

    def get_user_favorite_artworks(self):
        try:
            matching_users = self.search_users()
            if not matching_users:
                return
            user_id = int(input("Enter the ID of the user whose favorite artworks you want to view from the list above: "))
            artworks = self.user_favorite_artwork_dao.get_user_favorite_artworks(user_id)
            print(f"\nFavorite Artworks for User ID {user_id}:")
            for artwork in artworks:
                print(artwork)
        except UserNotFoundException as e:
            print(e)
        except Exception as e:
            print(f"Error retrieving favorite artworks: {e}")

    def add_artwork_to_gallery(self):
        try:
            matching_artworks = self.search_artworks()
            if not matching_artworks:
                return
            artwork_id = int(input("Enter the ID of the artwork to add to a gallery from the list above: "))
            if not self.artwork_dao.get_artwork_by_id(artwork_id):
                raise ArtworkNotFoundException(artwork_id)
            matching_galleries = self.search_galleries()
            if not matching_galleries:
                return
            gallery_id = int(input("Enter the ID of the gallery to add the artwork to from the list above: "))
            if not self.gallery_dao.get_gallery_by_id(gallery_id):
                raise GalleryNotFoundException(gallery_id)
            if self.artwork_gallery_dao.add_artwork_to_gallery(artwork_id, gallery_id):
                print("Artwork added to gallery successfully.")
            else:
                print("Failed to add artwork to gallery.")
        except (ArtworkNotFoundException, GalleryNotFoundException, ArtworkGalleryNotFoundException) as e:
            print(e)
        except Exception as e:
            print(f"Error adding artwork to gallery: {e}")

    def remove_artwork_from_gallery(self):
        try:
            matching_artworks = self.search_artworks()
            if not matching_artworks:
                return
            artwork_id = int(input("Enter the ID of the artwork to remove from a gallery from the list above: "))
            if not self.artwork_dao.get_artwork_by_id(artwork_id):
                raise ArtworkNotFoundException(artwork_id)
            matching_galleries = self.search_galleries()
            if not matching_galleries:
                return
            gallery_id = int(input("Enter the ID of the gallery to remove the artwork from from the list above: "))
            if not self.gallery_dao.get_gallery_by_id(gallery_id):
                raise GalleryNotFoundException(gallery_id)
            if self.artwork_gallery_dao.remove_artwork_from_gallery(artwork_id, gallery_id):
                print("Artwork removed from gallery successfully.")
            else:
                print("Failed to remove artwork from gallery.")
        except (ArtworkNotFoundException, GalleryNotFoundException, ArtworkGalleryNotFoundException) as e:
            print(e)
        except Exception as e:
            print(f"Error removing artwork from gallery: {e}")

    def get_artwork_galleries(self):
        try:
            matching_artworks = self.search_artworks()
            if not matching_artworks:
                return
            artwork_id = int(input("Enter the ID of the artwork to view galleries for from the list above: "))
            if not self.artwork_dao.get_artwork_by_id(artwork_id):
                raise ArtworkNotFoundException(artwork_id)
            galleries = self.artwork_gallery_dao.get_artwork_galleries(artwork_id)
            print(f"\nGalleries containing Artwork ID {artwork_id}:")
            for gallery in galleries:
                print(gallery)
        except ArtworkGalleryNotFoundException as e:
            print(e)
        except Exception as e:
            print(f"Error retrieving galleries containing the artwork: {e}")

    def search_galleries(self):
            try:
                keyword = input("Enter a keyword to search for galleries: ")
                matching_galleries = self.gallery_dao.search_galleries(keyword)
                if matching_galleries:
                    print("Matching galleries:")
                    for gallery in matching_galleries:
                        print(f"ID: {gallery.gallery_id}, Name: {gallery.name}, Description: {gallery.description}")
                    return matching_galleries
                else:
                    print("No matching galleries found.")
                    return []
            except Exception as e:
                print(f"Error searching galleries: {e}")
                return []
            
    def search_users(self):
        try:
            keyword = input("Enter a keyword to search for users: ")
            matching_users = self.user_dao.search_users(keyword)
            if matching_users:
                print("Matching users:")
                for user in matching_users:
                    print(f"ID: {user.user_id}, Username: {user.username}, Email: {user.email}")
                return matching_users
            else:
                print("No matching users found.")
                return []
        except Exception as e:
            print(f"Error searching users: {e}")
            return []