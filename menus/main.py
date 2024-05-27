import pyodbc
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util import DBPropertyUtil 
from exception import *
from dao import *
from entity import *
from menus import *

class VirtualArtGalleryApp:
    def __init__(self):
        try:
            connection_string = DBPropertyUtil.get_connection_string()
            self.artwork_dao = ArtworkDAOImpl(connection_string)
            self.artist_dao = ArtistDAOImpl(connection_string)
            self.gallery_dao = GalleryDAOImpl(connection_string)
            self.user_dao = UserDAOImpl(connection_string)
            self.user_favorite_artwork_dao = UserFavoriteArtworkDAOImpl(connection_string)
            self.artwork_gallery_dao = ArtworkGalleryDAOImpl(connection_string)
            self.main_menu()
        except Exception as e:
            print(f"Error initializing the application: {e}")

    def main_menu(self):
        try:
            while True:
                print("\nVirtual Art Gallery")
                print("1. Artwork Management")
                print("2. Artist Management")
                print("3. Gallery Management")
                print("4. User Management")
                print("5. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    ArtworkManagementMenu(self.artwork_dao, self.user_favorite_artwork_dao, self.artwork_gallery_dao, self.gallery_dao).display_menu()
                elif choice == "2":
                    ArtistManagementMenu(self.artist_dao).display_menu()
                elif choice == "3":
                    GalleryManagementMenu(self.gallery_dao, self.artwork_gallery_dao).display_menu()
                elif choice == "4":
                    UserManagementMenu(self.user_dao, self.user_favorite_artwork_dao).display_menu()
                elif choice == "5":
                    print("Exiting Virtual Art Gallery.")
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")
        except Exception as e:
            print(f"Error in main menu: {e}")

if __name__ == "__main__":
    VirtualArtGalleryApp()
