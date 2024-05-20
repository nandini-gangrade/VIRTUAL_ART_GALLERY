

-- Inserting values into Artwork table
INSERT INTO Artwork (Title, Description, CreationDate, Medium, ImageURL) VALUES
('Starry Night', 'Oil painting of a night sky', '1889-06-01', 'Oil on canvas', 'https://example.com/starry_night.jpg'),
('Mona Lisa', 'Famous portrait painting', '1503-01-01', 'Oil on poplar', 'https://example.com/mona_lisa.jpg'),
('The Persistence of Memory', 'Surrealist painting of melting clocks', '1931-01-01', 'Oil on canvas', 'https://example.com/persistence_of_memory.jpg'),
('The Scream', 'Expressionist painting depicting a screaming figure', '1893-01-01', 'Oil, tempera, pastel on cardboard', 'https://example.com/the_scream.jpg'),
('Girl with a Pearl Earring', 'Portrait painting of a girl wearing a pearl earring', '1665-01-01', 'Oil on canvas', 'https://example.com/girl_with_pearl_earring.jpg'),
('The Starry Night', 'Landscape painting of a night sky', '1889-06-01', 'Oil on canvas', 'https://example.com/starry_night2.jpg'),
('The Last Supper', 'Famous mural painting depicting the last supper of Jesus', '1495-01-01', 'Fresco', 'https://example.com/the_last_supper.jpg'),
('Guernica', 'Cubist painting depicting the horrors of war', '1937-01-01', 'Oil on canvas', 'https://example.com/guernica.jpg'),
('The Birth of Venus', 'Famous painting depicting the birth of the goddess Venus', '1486-01-01', 'Tempera on canvas', 'https://example.com/birth_of_venus.jpg'),
('Water Lilies', 'Series of paintings depicting water lilies in a pond', '1916-01-01', 'Oil on canvas', 'https://example.com/water_lilies.jpg');

-- Inserting values into Artist table
INSERT INTO Artist (Name, Biography, BirthDate, Nationality, Website, ContactInformation) VALUES
('Vincent van Gogh', 'Dutch post-impressionist painter who is among the most famous and influential figures in the history of Western art.', '1853-03-30', 'Dutch', 'https://www.vangoghmuseum.nl/', 'info@vangoghmuseum.nl'),
('Leonardo da Vinci', 'Italian polymath of the High Renaissance who is widely considered one of the most diversely talented individuals ever to have lived.', '1452-04-15', 'Italian', 'https://www.leonardodavinci.net/', 'info@leonardodavinci.net'),
('Salvador Dal�', 'Spanish surrealist painter renowned for his eccentricity and his striking and bizarre images.', '1904-05-11', 'Spanish', 'https://www.salvador-dali.org/', 'info@salvador-dali.org'),
('Edvard Munch', 'Norwegian painter whose best-known work, The Scream, has become one of the most iconic images of world art.', '1863-12-12', 'Norwegian', 'https://www.munchmuseet.no/', 'info@munchmuseet.no'),
('Johannes Vermeer', 'Dutch Baroque Period painter who specialized in domestic interior scenes of middle-class life.', '1632-10-31', 'Dutch', 'https://www.essentialvermeer.com/', 'info@essentialvermeer.com'),
('Leonardo da Vinci', 'Italian polymath of the High Renaissance who is widely considered one of the most diversely talented individuals ever to have lived.', '1452-04-15', 'Italian', 'https://www.leonardodavinci.net/', 'info@leonardodavinci.net'),
('Leonardo da Vinci', 'Italian polymath of the High Renaissance who is widely considered one of the most diversely talented individuals ever to have lived.', '1452-04-15', 'Italian', 'https://www.leonardodavinci.net/', 'info@leonardodavinci.net'),
('Pablo Picasso', 'Spanish painter, sculptor, printmaker, ceramicist, and stage designer who is one of the most influential artists of the 20th century.', '1881-10-25', 'Spanish', 'https://www.museopicassomalaga.org/', 'info@museopicassomalaga.org'),
('Sandro Botticelli', 'Italian painter of the Early Renaissance who belonged to the Florentine School.', '1445-03-01', 'Italian', 'https://www.uffizi.it/en/botticelli', 'info@uffizi.it'),
('Claude Monet', 'French painter and founder of French Impressionist painting, and the most consistent and prolific practitioner of the movement''s philosophy of expressing one''s perceptions before nature.', '1840-11-14', 'French', 'https://www.fondation-monet.com/', 'info@fondation-monet.com');

-- Inserting values into User table
INSERT INTO [User] (Username, Password, Email, FirstName, LastName, DateOfBirth, ProfilePicture, FavoriteArtworks) VALUES
('user1', 'password1', 'user1@example.com', 'John', 'Doe', '1990-05-15', 'https://example.com/profile1.jpg', '1,3,5'),
('user2', 'password2', 'user2@example.com', 'Jane', 'Smith', '1985-10-20', 'https://example.com/profile2.jpg', '2,4,6'),
('user3', 'password3', 'user3@example.com', 'Alice', 'Johnson', '1995-03-25', 'https://example.com/profile3.jpg', '7,8,9'),
('user4', 'password4', 'user4@example.com', 'Bob', 'Brown', '1988-12-10', 'https://example.com/profile4.jpg', '10,1,2'),
('user5', 'password5', 'user5@example.com', 'Emily', 'Wilson', '1992-08-05', 'https://example.com/profile5.jpg', '3,6,9'),
('user6', 'password6', 'user6@example.com', 'Michael', 'Taylor', '1983-06-30', 'https://example.com/profile6.jpg', '4,7,10'),
('user7', 'password7', 'user7@example.com', 'Sarah', 'Clark', '1998-01-03', 'https://example.com/profile7.jpg', '2,5,8'),
('user8', 'password8', 'user8@example.com', 'David', 'Anderson', '1975-09-18', 'https://example.com/profile8.jpg', '1,3,6'),
('user9', 'password9', 'user9@example.com', 'Jessica', 'Lee', '1980-04-12', 'https://example.com/profile9.jpg', '4,7,9'),
('user10', 'password10', 'user10@example.com', 'Matthew', 'White', '1991-11-28', 'https://example.com/profile10.jpg', '2,5,8');

-- Inserting values into Gallery table
INSERT INTO Gallery (Name, Description, Location, Curator, OpeningHours) VALUES
('Louvre Museum', 'The world''s largest art museum and a historic monument in Paris, France.', 'Rue de Rivoli, 75001 Paris, France', 2, '9:00 AM - 6:00 PM'),
('Museum of Modern Art (MoMA)', 'Art museum located in Midtown Manhattan, New York City.', '11 W 53rd St, New York, NY 10019, United States', 7, '10:30 AM - 5:30 PM'),
('Rijksmuseum', 'Dutch national museum dedicated to arts and history in Amsterdam.', 'Museumstraat 1, 1071 XX Amsterdam, Netherlands', 9, '9:00 AM - 5:00 PM'),
('British Museum', 'Public institution dedicated to human history, art, and culture in London.', 'Great Russell St, Bloomsbury, London WC1B 3DG, United Kingdom', 5, '10:00 AM - 5:30 PM'),
('Museo Nacional del Prado', 'Spanish national art museum located in Madrid.', 'Paseo del Prado, s/n, 28014 Madrid, Spain', 8, '10:00 AM - 8:00 PM'),
('National Gallery', 'Art museum in Trafalgar Square in the City of Westminster, in Central London.', 'Trafalgar Square, Charing Cross, London WC2N 5DN, United Kingdom', 10, '10:00 AM - 6:00 PM'),
('State Hermitage Museum', 'Museum of art and culture in Saint Petersburg, Russia.', 'Palace Square, 2, St Petersburg, Russia, 190000', 3, '10:30 AM - 6:00 PM'),
('Uffizi Gallery', 'Prominent art museum located adjacent to the Piazza della Signoria in the Historic Centre of Florence in the region of Tuscany, Italy.', 'Piazzale degli Uffizi, 6, 50122 Firenze FI, Italy', 1, '8:15 AM - 6:50 PM'),
('Mus�e d''Orsay', 'Art museum located on the Left Bank of the Seine in Paris, France.', '1 Rue de la L�gion d''Honneur, 75007 Paris, France', 6, '9:30 AM - 6:00 PM'),
('Tate Modern', 'Art museum located in London, England.', 'Bankside, London SE1 9TG, United Kingdom', 4, '10:00 AM - 6:00 PM');

-- Inserting values into User_Favorite_Artwork junction table
INSERT INTO User_Favorite_Artwork (UserID, ArtworkID) VALUES
(1, 1), (1, 3), (1, 5), (2, 2), (2, 4), (2, 6), (3, 7), (3, 8), (3, 9), (4, 10);

-- Inserting values into Artwork_Gallery junction table
INSERT INTO Artwork_Gallery (ArtworkID, GalleryID) VALUES
(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 1), (7, 2), (8, 3), (9, 4), (10, 5);