class UserFavoriteArtworkNotFoundException(Exception):
    def __init__(self, user_id, artwork_id):
        super().__init__(f"Favorite artwork for User ID {user_id} and Artwork ID {artwork_id} not found.")
