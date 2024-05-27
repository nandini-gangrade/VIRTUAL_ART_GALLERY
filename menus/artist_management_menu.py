import pyodbc
from exception import *
from dao import *
from entity import *
from util import *
from datetime import datetime

class ArtistManagementMenu:
    def __init__(self, artist_dao):
        connection_string = DBPropertyUtil.get_connection_string()
        self.artist_dao = ArtistDAOImpl(connection_string)

    def display_menu(self):
        try:
            while True:
                print("\nArtist Management")
                print("1. Display All Artists")
                print("2. Add Artist")
                print("3. Update Artist")
                print("4. Remove Artist")
                print("5. Search Artists")
                print("6. Back to Main Menu")

                choice = input("Enter your choice: ")

                if choice == "1":
                    self.display_all_artists()
                elif choice == "2":
                    self.add_artist()
                elif choice == "3":
                    self.update_artist()
                elif choice == "4":
                    self.remove_artist()
                elif choice == "5":
                    self.search_artists()
                elif choice == "6":
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")
        except Exception as e:
            print(f"Error in artist management menu: {e}")

    def display_all_artists(self):
        try:
            artists = self.artist_dao.get_all_artists()
            if artists:
                print("\nAll Artists:")
                for artist in artists:
                    print(f"ID: {artist.artist_id}, Name: {artist.name}, Bio: {artist.biography}, Birth Date: {artist.birth_date}, Death Date: {artist.death_date}, Website: {artist.website}, Contact Info: {artist.contact_information}")
            else:
                print("No artists found.")
        except Exception as e:
            print(f"Error fetching artists: {e}")

    def add_artist(self):
        try:
            name = input("Enter name: ")
            bio = input("Enter bio: ")
            birth_date = input("Enter birth date (YYYY-MM-DD): ")
            if birth_date:
                try:
                    datetime.strptime(birth_date, '%Y-%m-%d')
                except ValueError:
                    print("Invalid birth date format. Please enter the date in YYYY-MM-DD format.")
                    return
            death_date = input("Enter death date (YYYY-MM-DD): ")
            if death_date:
                try:
                    datetime.strptime(death_date, '%Y-%m-%d')
                except ValueError:
                    print("Invalid death date format. Please enter the date in YYYY-MM-DD format.")
                    return
            website = input("Enter website: ")
            contact_information = input("Enter contact information: ")
            artist = Artist(None, name, bio, birth_date, death_date, website, contact_information)
            if self.artist_dao.add_artist(artist):
                print("Artist added successfully.")
            else:
                print("Failed to add artist.")
        except Exception as e:
            print(f"Error adding artist: {e}")

    def update_artist(self):
        try:
            matching_artists = self.search_artists()
            if not matching_artists:
                return
            artist_id = int(input("Enter the ID of the artist you want to update from the list above: "))
            existing_artist = self.artist_dao.get_artist_by_id(artist_id)
            if existing_artist:
                print(f"Existing Name: {existing_artist.name}")
                name = input(f"Enter new name (Leave empty to keep '{existing_artist.name}'): ") or existing_artist.name
                bio = input(f"Enter new bio (Leave empty to keep '{existing_artist.biography}'): ") or existing_artist.biography
                birth_date = input(f"Enter new birth date (Leave empty to keep '{existing_artist.birth_date}'): ") or existing_artist.birth_date
                if birth_date != existing_artist.birth_date:
                    try:
                        datetime.strptime(birth_date, '%Y-%m-%d')
                    except ValueError:
                        print("Invalid birth date format. Please enter the date in YYYY-MM-DD format.")
                        return
                death_date = input(f"Enter new death date (Leave empty to keep '{existing_artist.death_date}'): ") or existing_artist.death_date
                if death_date != existing_artist.death_date:
                    try:
                        datetime.strptime(death_date, '%Y-%m-%d')
                    except ValueError:
                        print("Invalid death date format. Please enter the date in YYYY-MM-DD format.")
                        return
                website = input(f"Enter new website (Leave empty to keep '{existing_artist.website}'): ") or existing_artist.website
                contact_info = input(f"Enter new contact information (Leave empty to keep '{existing_artist.contact_information}'): ") or existing_artist.contact_information
                updated_artist = Artist(existing_artist.artist_id, name, bio, birth_date, death_date, website, contact_info)
                success = self.artist_dao.update_artist(updated_artist)
                if success:
                    print("Artist updated successfully.")
                else:
                    print("Failed to update artist.")
            else:
                raise ArtistNotFoundException(artist_id)
        except ArtistNotFoundException as e:
            print(e)
        except Exception as e:
            print(f"Error updating artist: {e}")

    def remove_artist(self):
        try:
            matching_artists = self.search_artists()
            if not matching_artists:
                return

            artist_id = int(input("Enter artist ID to remove: "))
            if self.artist_dao.remove_artist(artist_id):
                print("Artist removed successfully.")
            else:
                print("Failed to remove artist.")
        except ArtistNotFoundException as e:
            print(e)
        except Exception as e:
            print(f"Error removing artist: {e}")

    def search_artists(self):
        try:
            keyword = input("Enter a keyword to search for artists: ")
            matching_artists = self.artist_dao.search_artists(keyword)
            if matching_artists:
                print("Matching artists:")
                for artist in matching_artists:
                    print(f"ID: {artist.artist_id}, Name: {artist.name}, Bio: {artist.biography}")
                return matching_artists
            else:
                print("No matching artists found.")
                return []
        except ArtistNotFoundException as e:
            print(e)
        except Exception as e:
            print(f"Error searching artists: {e}")
            return []
