from dao import VirtualArtGalleryDAOImpl
from entity import Artwork
from exception import UserNotFoundException
from util import DBPropertyUtil  
import pyodbc

class VirtualArtGalleryApp:
    def __init__(self):
        connection_string = DBPropertyUtil.get_connection_string()
        self.dao = VirtualArtGalleryDAOImpl(connection_string)
        self.main_menu()

    def main_menu(self):
        while True:
            print("\nVirtual Art Gallery")
            print("1. Add Artwork")
            print("2. Update Artwork")
            print("3. Remove Artwork")
            print("4. Search Artworks")
            print("5. Add Artwork to Favorite")
            print("6. Remove Artwork from Favorite")
            print("7. Get User Favorite Artworks")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_artwork()
            elif choice == "2":
                self.update_artwork()
            elif choice == "3":
                self.remove_artwork()
            elif choice == "4":
                self.search_artworks()
            elif choice == "5":
                self.add_artwork_to_favorite()
            elif choice == "6":
                self.remove_artwork_from_favorite()
            elif choice == "7":
                self.get_user_favorite_artworks()
            elif choice == "8":
                print("Exiting Virtual Art Gallery.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def add_artwork(self):
        title = input("Enter title: ")
        description = input("Enter description: ")
        creation_date = input("Enter creation date (YYYY-MM-DD): ")
        medium = input("Enter medium: ")
        image_url = input("Enter image URL: ")
        artwork = Artwork(None, title, description, creation_date, medium, image_url)
        if self.dao.add_artwork(artwork):
            print("Artwork added successfully.")
        else:
            print("Failed to add artwork.")

    def update_artwork(self):
        artwork_id = int(input("Enter artwork ID to update: "))
        existing_artwork = self.dao.get_artwork_by_id(artwork_id)
        if existing_artwork:
            print(f"Existing Title: {existing_artwork.title}")
            title = input(f"Enter new title (Leave empty to keep '{existing_artwork.title}'): ") or existing_artwork.title
            description = input(f"Enter new description (Leave empty to keep '{existing_artwork.description}'): ") or existing_artwork.description
            creation_date = input(f"Enter new creation date (Leave empty to keep '{existing_artwork.creation_date}'): ") or existing_artwork.creation_date
            medium = input(f"Enter new medium (Leave empty to keep '{existing_artwork.medium}'): ") or existing_artwork.medium
            image_url = input(f"Enter new image URL (Leave empty to keep '{existing_artwork.image_url}'): ") or existing_artwork.image_url

            updated_artwork = Artwork(artwork_id, title, description, creation_date, medium, image_url)
            success = self.dao.update_artwork(updated_artwork)
            if success:
                print("Artwork updated successfully.")
            else:
                print("Failed to update artwork.")
        else:
            print(f"Artwork with ID {artwork_id} not found.")


    def remove_artwork(self):
        try:
            artwork_id = int(input("Enter artwork ID to remove: "))
            if self.dao.remove_artwork(artwork_id):
                print("Artwork removed successfully.")
            else:
                print("Failed to remove artwork.")
        except Exception as e:
            print(f"Error removing artwork: {e}")

    def search_artworks(self):
        keyword = input("Enter keyword to search: ")
        artworks = self.dao.search_artworks(keyword)
        print("\nSearch Results:")
        for artwork in artworks:
            print(artwork)

    def add_artwork_to_favorite(self):
        try:
            user_id = int(input("Enter user ID: "))
            artwork_id = int(input("Enter artwork ID to add to favorites: "))
            if self.dao.add_artwork_to_favorite(user_id, artwork_id):
                print("Artwork added to favorites successfully.")
            else:
                print("Failed to add artwork to favorites.")
        except pyodbc.IntegrityError as e:
            error_code = e.args[0]
            if error_code == '23000':
                print("Artwork is already in the user's favorites.")
            else:
                print(f"Error adding artwork to favorites: {e}")
        except Exception as e:
            print(f"Error adding artwork to favorites: {e}")

    def remove_artwork_from_favorite(self):
        try:
            user_id = int(input("Enter user ID: "))
            artwork_id = int(input("Enter artwork ID to remove from favorites: "))
            if self.dao.remove_artwork_from_favorite(user_id, artwork_id):
                print("Artwork removed from favorites successfully.")
            else:
                print("Failed to remove artwork from favorites.")
        except Exception as e:
            print(f"Error removing artwork from favorites: {e}")

    def get_user_favorite_artworks(self):
        try:
            user_id = int(input("Enter user ID: "))
            artworks = self.dao.get_user_favorite_artworks(user_id)
            print(f"\nFavorite Artworks for User ID {user_id}:")
            for artwork in artworks:
                print(artwork)
        except UserNotFoundException as e:
            print(e)
        except Exception as e:
            print(f"Error retrieving favorite artworks: {e}")

if __name__ == "__main__":
    VirtualArtGalleryApp()
