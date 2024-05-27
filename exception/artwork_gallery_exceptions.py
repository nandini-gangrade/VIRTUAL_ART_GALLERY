class ArtworkGalleryNotFoundException(Exception):
    def __init__(self, artwork_id, gallery_id):
        super().__init__(f"Artwork-Gallery relationship not found for Artwork ID {artwork_id} and Gallery ID {gallery_id}.")
