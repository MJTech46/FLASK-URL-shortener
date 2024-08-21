# Flask URL Shortener
A simple project purely aimed for testing/interacting with Python's Flask framework.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Screenshots](#screenshots)
  - [Home Page](#home-page)
  - [URL Shortening Process](#url-shortening-process)
  - [Short URL Created](#short-url-created)
  - [Redirection Preview](#redirection-preview)
- [Installation and Setup](#installation-and-setup)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

This is a URL Shortener application built using the Flask framework in Python. It allows users to input a long URL and get a shortened version of it, which can then be shared or used elsewhere. The shortened URLs redirect to the original URLs when accessed.

## Features

- **URL Shortening:** Converts long URLs into short, manageable links.
- **Redirect Functionality:** Shortened URLs redirect users to the original long URLs.
- **Custom Short URLs:** Option to create custom short links ( Reroll ).
- **Analytics Dashboard:** Track clicks and provide analytics for shortened URLs.
- **Persistent Storage:** Stores the original and shortened URLs in a database for easy retrieval.
- **Error Handling:** Includes basic error handling for invalid URLs and duplicate entries.


## Tech Stack

- **Python:** Core programming language used for developing the backend.
- **Flask:** Lightweight web framework used for building the application.
- **HTML/CSS:** Frontend structure and styling.
- **SQLite:** Database for storing URL mappings.
- **Jinja2:** Template engine used in Flask for rendering dynamic content.
- **Bootstrap:** Used for responsive design and UI components.

## Screenshots

### Home Page
![Home Page](https://github.com/user-attachments/assets/da03ab97-a2cb-4ca6-8c05-69280727efd3)

### URL Shortening Process
![URL Shortening Process](https://github.com/user-attachments/assets/b7a8965f-3a8a-402b-8870-1e57861c245a)

### Short URL Created
![Short URL Created](https://github.com/user-attachments/assets/27d58b54-d6c5-4b59-a28c-754104040d5b)

### Redirection Preview
![Redirection in Action](https://github.com/user-attachments/assets/3977bf98-2546-42bc-9ff4-9c5f873bc865)

## Installation and Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/your-repository.git
    cd your-repository
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```bash
    flask shell
    >>> from app import db
    >>> db.create_all()
    >>> exit()
    ```

5. **Run the application:**
    ```bash
    python3 app.py  # On Windows use `python app.py`
    ```

6. **Access the application:**
    Open a web browser and go to `http://localhost/`.


## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any feature enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the Flask community and all the developers who contribute to open-source software.

