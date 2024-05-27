class GalleryNotFoundException(Exception):
    def __init__(self, gallery_id):
        super().__init__(f"Gallery with ID {gallery_id} not found.")
