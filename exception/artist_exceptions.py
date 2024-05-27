class ArtistNotFoundException(Exception):
    def __init__(self, artist_id):
        self.artist_id = artist_id
        super().__init__(f"Artist with ID {artist_id} not found.")
