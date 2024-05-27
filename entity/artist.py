# entity/artist.py
class Artist:
    def __init__(self, artist_id, name, biography, birth_date, nationality, website, contact_information):
        self.artist_id = artist_id
        self.name = name
        self.biography = biography
        self.birth_date = birth_date
        self.nationality = nationality
        self.website = website
        self.contact_information = contact_information

    def __str__(self):
        return (f"ID: {self.artist_id}, Name: {self.name}, Biography: {self.biography}, "
                f"BirthDate: {self.birth_date}, Nationality: {self.nationality}, Website: {self.website}, "
                f"ContactInformation: {self.contact_information}")

    # Getters
    @property
    def artist_id(self):
        return self._artist_id

    @property
    def name(self):
        return self._name

    @property
    def biography(self):
        return self._biography

    @property
    def birth_date(self):
        return self._birth_date

    @property
    def nationality(self):
        return self._nationality

    @property
    def website(self):
        return self._website

    @property
    def contact_information(self):
        return self._contact_information

    # Setters
    @artist_id.setter
    def artist_id(self, artist_id):
        self._artist_id = artist_id

    @name.setter
    def name(self, name):
        self._name = name

    @biography.setter
    def biography(self, biography):
        self._biography = biography

    @birth_date.setter
    def birth_date(self, birth_date):
        self._birth_date = birth_date

    @nationality.setter
    def nationality(self, nationality):
        self._nationality = nationality

    @website.setter
    def website(self, website):
        self._website = website

    @contact_information.setter
    def contact_information(self, contact_information):
        self._contact_information = contact_information
