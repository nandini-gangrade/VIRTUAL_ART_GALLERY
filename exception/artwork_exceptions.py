# In myexceptions/artwork_exceptions.py

class ArtworkNotFoundException(Exception):
    def __init__(self, artwork_id):
        super().__init__(f"Artwork with ID {artwork_id} not found.")
