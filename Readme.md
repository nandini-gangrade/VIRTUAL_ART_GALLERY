# [Virtual Art Gallery](https://github.com/nandini-gangrade/VIRTUAL_ART_GALLERY/blob/main/VirtualArtGallery.pdf)

Virtual Art Gallery is a Python project aimed at simulating the functionalities of a virtual art gallery. 
The Virtual Art Gallery project is designed to offer a platform where users can view, add, update, and remove artworks. It also provides features for users to mark artworks as favorites and explore various artworks based on different criteria.


## Features

- **Artwork Management**: Add, update, and remove artworks from the gallery.
- **User Interaction**: Users can mark artworks as favorites and explore their favorite artworks.
- **Search Functionality**: Search for artworks based on title or description.
- **Data Persistence**: Utilizes a database backend for storing and retrieving artwork and user information.
- **User Authentication**: Provides authentication mechanisms to ensure secure access to user-specific functionalities.


## Installation

To install and set up the Virtual Art Gallery project, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/nandini-gangrade/Virtual-Art-Gallery.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Virtual-Art-Gallery
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv myenv
    ```

4. Activate the virtual environment:
    - On Windows (PowerShell):

        ```powershell
        Set-ExecutionPolicy -Scope Process Bypass
        .\myenv\Scripts\Activate.ps1
        ```

    - On Unix or MacOS:

        ```bash
        source myenv/bin/activate
        ```

5. Install the `pyodbc` package for SQL Server connectivity:

    ```bash
    pip install pyodbc
    ```

## Directory Structure
```
Virtual Art Gallery/
│
├── main.py
│
├── tests/
│   └── test_main.py
│
├── db/
│   ├── ERD
│   ├── schema.sql
│   └── seed.sql
│
├── dao/
│   ├── __init__.py
│   ├── virtual_art_gallery_dao.py
│   └── virtual_art_gallery_dao_impl.py   
│
├── entity/
│   ├── __init__.py
│   ├── artwork.py
│   ├── artist.py
│   ├── user.py
│   └── gallery.py
│
├── exception/
│   ├── __init__.py
│   ├── artwork_exceptions.py
│   └── user_exceptions.py
│
└── util/
    ├── __init__.py
    ├── db_conn_util.py
    └── db_property_util.py
```

## Usage

To run the Virtual Art Gallery application, execute the `main.py` script:

```bash
python main.py
```

Follow the on-screen instructions to navigate through the application and explore its functionalities.

## Testing

Unit tests for the project are located in the `tests` directory. To run the tests, use the following command:

```bash
python -m unittest discover -s tests
```

## Contributing

Contributions to the Virtual Art Gallery project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
