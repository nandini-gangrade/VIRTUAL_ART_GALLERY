# entity/artwork.py

class Artwork:
    def __init__(self, artwork_id, title, description, creation_date, medium, image_url):
        self.artwork_id = artwork_id
        self.title = title
        self.description = description
        self.creation_date = creation_date
        self.medium = medium
        self.image_url = image_url

    def __str__(self):
        return (f"ID: {self.artwork_id}, Title: {self.title}, Description: {self.description}, "
                f"Creation Date: {self.creation_date}, Medium: {self.medium}, Image URL: {self.image_url}")

    # Getters
    @property
    def artwork_id(self):
        return self._artwork_id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def creation_date(self):
        return self._creation_date

    @property
    def medium(self):
        return self._medium

    @property
    def image_url(self):
        return self._image_url

    # Setters
    @artwork_id.setter
    def artwork_id(self, artwork_id):
        self._artwork_id = artwork_id

    @title.setter
    def title(self, title):
        self._title = title

    @description.setter
    def description(self, description):
        self._description = description

    @creation_date.setter
    def creation_date(self, creation_date):
        self._creation_date = creation_date

    @medium.setter
    def medium(self, medium):
        self._medium = medium

    @image_url.setter
    def image_url(self, image_url):
        self._image_url = image_url


    # String representation for printing
    # def __str__(self):
    #     return (f"ArtworkID: {self.artwork_id}, Title: {self.title}, Description: {self.description}, "
    #             f"CreationDate: {self.creation_date}, Medium: {self.medium}, ImageURL: {self.image_url}")
