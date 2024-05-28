import pyodbc
from abc import ABC, abstractmethod
from entity.user import User
from exception.user_exceptions import UserNotFoundException

class UserDAO(ABC):
    @abstractmethod
    def get_all_users(self) -> list:
        pass

    @abstractmethod
    def add_user(self, user: User) -> bool:
        pass

    @abstractmethod
    def update_user(self, user: User) -> bool:
        pass

    @abstractmethod
    def remove_user(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def search_users(self, keyword: str) -> list:
        pass


class UserDAOImpl(UserDAO):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def get_all_users(self) -> list:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM [User]")
            users = []
            for row in cursor.fetchall():
                user = User(row.UserID, row.Username, row.Password, row.Email, row.FirstName, row.LastName, row.DateOfBirth, row.ProfilePicture, row.FavoriteArtworks)
                users.append(user)
            connection.close()
            return users
        except Exception as e:
            print(f"Error fetching users: {e}")
            return []

    def add_user(connection_string, user):
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO [User] (Username, Password, Email, FirstName, LastName, DateOfBirth, ProfilePicture, FavoriteArtworks) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        user.username, user.password, user.email, user.first_name, user.last_name, user.date_of_birth, user.profile_picture, ','.join(user.favorite_artworks))
            connection.commit()
            connection.close()
            return True
        except pyodbc.Error as e:
            print(f"Database error adding user: {e}")
        except Exception as e:
            print(f"Unexpected error adding user: {e}")
        return False


    def update_user(self, user: User) -> bool:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("UPDATE [User] SET Username=?, Password=?, Email=?, FirstName=?, LastName=?, DateOfBirth=?, ProfilePicture=?, FavoriteArtworks=? WHERE UserID=?",
                           user.username, user.password, user.email, user.first_name, user.last_name, user.date_of_birth, user.profile_picture, user.favorite_artworks, user.user_id)
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(f"Error updating user: {e}")
            return False

    def remove_user(self, user_id: int) -> bool:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("DELETE FROM [User] WHERE UserID=?", user_id)
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(f"Error removing user: {e}")
            return False

    def get_user_by_id(self, user_id: int) -> User:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM [User] WHERE UserID=?", user_id)
            row = cursor.fetchone()
            connection.close()
            if row:
                return User(row.UserID, row.Username, row.Password, row.Email, row.FirstName, row.LastName, row.DateOfBirth, row.ProfilePicture, row.FavoriteArtworks)
            else:
                raise UserNotFoundException(f"User with ID {user_id} not found.")
        except Exception as e:
            print(f"Error fetching user by ID: {e}")
            return None

    def search_users(self, keyword: str) -> list:
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            query = "SELECT * FROM [User] WHERE Username LIKE ? OR Email LIKE ? OR FirstName LIKE ? OR LastName LIKE ?"
            cursor.execute(query, ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
            users = []
            for row in cursor.fetchall():
                user = User(row.UserID, row.Username, row.Password, row.Email, row.FirstName, row.LastName, row.DateOfBirth, row.ProfilePicture, row.FavoriteArtworks)
                users.append(user)
            connection.close()
            return users
        except Exception as e:
            print(f"Error searching users: {e}")
            return []
