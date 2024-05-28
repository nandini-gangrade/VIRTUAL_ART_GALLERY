import pyodbc
from exception import *
from dao import *
from entity import *
from util import *
from datetime import datetime

class GalleryManagementMenu:
    def __init__(self, gallery_dao, artwork_dao, artwork_gallery_dao):
        connection_string = DBPropertyUtil.get_connection_string()
        self.gallery_dao = GalleryDAOImpl(connection_string)
        self.artwork_dao = ArtworkDAOImpl(connection_string)
        self.artwork_gallery_dao = ArtworkGalleryDAOImpl(connection_string)

    def display_menu(self):
        try:
            while True:
                print("\nGallery Management")
                print("1. Display All Galleries")
                print("2. Add Gallery")
                print("3. Update Gallery")
                print("4. Remove Gallery")
                print("5. Search Galleries")
                print("6. Add Artwork to Gallery")
                print("7. Remove Artwork from Gallery")
                print("8. View Galleries Containing Artwork")
                print("9. Back to Main Menu")

                choice = input("Enter your choice: ")

                if choice == "1":
                    self.display_all_galleries()
                elif choice == "2":
                    self.add_gallery()
                elif choice == "3":
                    self.update_gallery()
                elif choice == "4":
                    self.remove_gallery()
                elif choice == "5":
                    self.search_galleries()
                elif choice == '6':
                    self.add_artwork_to_gallery()
                elif choice == '7':
                    self.remove_artwork_from_gallery()
                elif choice == '8':
                    self.get_artwork_galleries()
                elif choice == "9":
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")
        except Exception as e:
            print(f"Error in gallery management menu: {e}")

    def display_all_galleries(self):
        try:
            galleries = self.gallery_dao.get_all_galleries()
            if galleries:
                print("\nAll Galleries:")
                for gallery in galleries:
                    print(f"ID: {gallery.gallery_id}, Name: {gallery.name}, Location: {gallery.location}, Curator: {gallery.curator}, Opening Hours: {gallery.opening_hours}")
            else:
                print("No galleries found.")
        except Exception as e:
            print(f"Error fetching galleries: {e}")

    def add_gallery(self):
        try:
            name = input("Enter name: ")
            description = input("Enter description: ")
            location = input("Enter location: ")
            curator = input("Enter curator (INT): ")
            opening_hours = input("Enter opening hours [(HH:MM) AM - HH:MM) PM]: ")
            gallery = Gallery(None, name, description, location, curator, opening_hours)
            if self.gallery_dao.add_gallery(gallery):
                print("Gallery added successfully.")
            else:
                print("Failed to add gallery.")
        except Exception as e:
            print(f"Error adding gallery: {e}")

    def update_gallery(self):
        try:
            matching_galleries = self.search_galleries()
            if not matching_galleries:
                return
            gallery_id = int(input("Enter the ID of the gallery you want to update from the list above: "))
            existing_gallery = self.gallery_dao.get_gallery_by_id(gallery_id)
            if existing_gallery:
                print(f"Existing Name: {existing_gallery.name}")
                name = input(f"Enter new name (Leave empty to keep '{existing_gallery.name}'): ") or existing_gallery.name
                description = input(f"Enter new description (Leave empty to keep '{existing_gallery.description}'): ") or existing_gallery.description
                location = input(f"Enter new location (Leave empty to keep '{existing_gallery.location}'): ") or existing_gallery.location
                curator = input(f"Enter new curator (Leave empty to keep '{existing_gallery.curator}'): ") or existing_gallery.curator
                opening_hours = input(f"Enter new opening hours (Leave empty to keep '{existing_gallery.opening_hours}'): ") or existing_gallery.opening_hours
                updated_gallery = Gallery(existing_gallery.gallery_id, name, description, location, curator, opening_hours)
                success = self.gallery_dao.update_gallery(updated_gallery)
                if success:
                    print("Gallery updated successfully.")
                else:
                    print("Failed to update gallery.")
            else:
                raise GalleryNotFoundException(gallery_id)
        except GalleryNotFoundException as e:
            print(e)
        except Exception as e:
            print(f"Error updating gallery: {e}")

    def search_galleries(self):
        try:
            keyword = input("Enter a keyword to search for galleries: ")
            matching_galleries = self.gallery_dao.search_galleries(keyword)
            if matching_galleries:
                print("Matching galleries:")
                for gallery in matching_galleries:
                    print(f"ID: {gallery.gallery_id}, Name: {gallery.name}, Description: {gallery.description}, Location: {gallery.location}, Curator: {gallery.curator}, Opening Hours: {gallery.opening_hours}")
                return matching_galleries
            else:
                print("No matching galleries found.")
                return []
        except Exception as e:
            print(f"Error searching galleries: {e}")
            return []

    def remove_gallery(self):
        try:
            matching_galleries = self.search_galleries()
            if not matching_galleries:
                return
            gallery_id = int(input("Enter gallery ID to remove: "))
            if not self.gallery_dao.get_gallery_by_id(gallery_id):
                raise GalleryNotFoundException(gallery_id)
            if self.gallery_dao.remove_gallery(gallery_id):
                print("Gallery removed successfully.")
            else:
                print("Failed to remove gallery.")
        except GalleryNotFoundException as e:
            print(e)
        except Exception as e:
            print(f"Error removing gallery: {e}")

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
        except (ArtworkNotFoundException, GalleryNotFoundException) as e:
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
        except (ArtworkNotFoundException, GalleryNotFoundException) as e:
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
                print(f"ID: {gallery.gallery_id}, Name: {gallery.name}, Location: {gallery.location}, Curator: {gallery.curator}, Opening Hours: {gallery.opening_hours}")
        except ArtworkNotFoundException as e:
            print(e)
        except Exception as e:
            print(f"Error retrieving galleries containing the artwork: {e}")

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
