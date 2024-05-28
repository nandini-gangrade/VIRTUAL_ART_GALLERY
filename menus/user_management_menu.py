import pyodbc
from exception import *
from dao import *
from entity import *
from util import *
from datetime import datetime

class UserManagementMenu:
    def __init__(self, user_dao, artwork_dao, user_favorite_artwork_dao):
        connection_string = DBPropertyUtil.get_connection_string()
        self.user_dao = UserDAOImpl(connection_string)
        self.artwork_dao = ArtworkDAOImpl(connection_string)
        self.user_favorite_artwork_dao = UserFavoriteArtworkDAOImpl(connection_string)

    def display_menu(self):
        try:
            while True:
                print("\nUser Management")
                print("1. Display All Users")
                print("2. Add User")
                print("3. Update User")
                print("4. Remove User")
                print("5. Search Users")
                print("6. Add Artwork to Favorite")
                print("7. Remove Artwork from Favorite")
                print("8. Get User Favorite Artworks")
                print("9. Back to Main Menu")

                choice = input("Enter your choice: ")

                if choice == "1":
                    self.display_all_users()
                elif choice == "2":
                    self.add_user()
                elif choice == "3":
                    self.update_user()
                elif choice == "4":
                    self.remove_user()
                elif choice == "5":
                    self.search_users()
                elif choice == "6":
                    self.add_artwork_to_favorite()
                elif choice == "7":
                    self.remove_artwork_from_favorite()
                elif choice == "8":
                    self.get_user_favorite_artworks()
                elif choice == "9":
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")
        except Exception as e:
            print(f"Error in user management menu: {e}")

    def display_all_users(self):
        try:
            users = self.user_dao.get_all_users()
            if users:
                print("\nAll Users:")
                for user in users:
                    print(f"ID: {user.user_id}, Email: {user.email}, First Name: {user.first_name}, Last Name: {user.last_name}, Date of Birth: {user.date_of_birth}, Profile Picture: {user.profile_picture}")
            else:
                print("No users found.")
        except Exception as e:
            print(f"Error fetching users: {e}")

    def add_user(self):
        try:
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            email = input("Enter email: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
            profile_picture = input("Enter profile picture URL: ")
            user = User(None, username, password, email, first_name, last_name, date_of_birth, profile_picture, [])
            
            if self.user_dao.add_user(user):
                print("User added successfully.")
            else:
                print("Failed to add user.")
        except pyodbc.Error as e:
            print(f"Database error adding user: {e}")
        except Exception as e:
            print(f"Unexpected error adding user: {e}")
    
    def update_user(self):
        try:
            matching_users = self.search_users()
            if not matching_users:
                return
            user_id = int(input("Enter the ID of the user you want to update from the list above: "))
            existing_user = self.user_dao.get_user_by_id(user_id)
            if existing_user:
                email = input(f"Enter new email (Leave empty to keep '{existing_user.email}'): ") or existing_user.email
                first_name = input(f"Enter new first name (Leave empty to keep '{existing_user.first_name}'): ") or existing_user.first_name
                last_name = input(f"Enter new last name (Leave empty to keep '{existing_user.last_name}'): ") or existing_user.last_name
                date_of_birth = input(f"Enter new date of birth (Leave empty to keep '{existing_user.date_of_birth}'): ") or existing_user.date_of_birth
                profile_picture = input(f"Enter new profile picture URL (Leave empty to keep '{existing_user.profile_picture}'): ") or existing_user.profile_picture
                updated_user = User(existing_user.user_id, email, first_name, last_name, date_of_birth, profile_picture, existing_user.favorite_artworks)
                success = self.user_dao.update_user(updated_user)
                if success:
                    print("User updated successfully.")
                else:
                    print("Failed to update user.")
            else:
                raise UserNotFoundException(user_id)
        except UserNotFoundException as e:
            print(e)
        except Exception as e:
            print(f"Error updating user: {e}")

    def search_users(self):
        try:
            keyword = input("Enter a keyword to search for users: ")
            matching_users = self.user_dao.search_users(keyword)
            if matching_users:
                print("Matching users:")
                for user in matching_users:
                    print(f"ID: {user.user_id}, Email: {user.email}, First Name: {user.first_name}, Last Name: {user.last_name}")
                return matching_users
            else:
                print("No matching users found.")
                return []
        except Exception as e:
            print(f"Error searching users: {e}")
            return []

    def remove_user(self):
        try:
            matching_users = self.search_users()
            if not matching_users:
                return
            user_id = int(input("Enter user ID to remove: "))
            if not self.user_dao.get_user_by_id(user_id):
                raise UserNotFoundException(user_id)
            if self.user_dao.remove_user(user_id):
                print("User removed successfully.")
            else:
                print("Failed to remove user.")
        except UserNotFoundException as e:
            print(e)
        except Exception as e:
            print(f"Error removing user: {e}")

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
        except UserFavoriteArtworkNotFoundException as e:
            print(e)
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
                print("Failed to remove artwork from favorites.")
        except UserFavoriteArtworkNotFoundException as e:
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
                print(f"ID: {artwork.artwork_id}, Title: {artwork.title}, Description: {artwork.description}")
        except UserNotFoundException as e:
            print(e)
        except Exception as e:
            print(f"Error retrieving favorite artworks: {e}")

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
