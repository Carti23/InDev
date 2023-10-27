# InDev

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running with Docker](#running-with-docker)
- [Contributing](#contributing)
- [License](#license)
- [Swagger Documentation](#swagger-documentation)

## Getting Started

Instructions for setting up and using your project locally.

### Prerequisites

- Python 3.9 or later
- Docker (optional, for containerization)
- Postgres
- Redis

### Installation

1. Clone this repository to your local machine:

    ```bash
    https://github.com/Carti23/wht_testove.git
    cd wht_testove
    ```


## Usage

Explain how to use your project and interact with the AI assistant.

### Running with Docker

1. Build the Docker image from the project directory:

    ```bash
    docker-compose build 
    ```

2. Run the Docker container:

    ```bash
     docker-compose up
    ```
3. Make Migrations

   ```bash
     docker-compose run --rm server sh -c "python manage.py makemigrations"
    ```


## Contributing

Contributions to this project are welcome. Follow these steps to contribute:

1. Fork the repository and clone your fork:

    ```bash
    git clone https://github.com/your-username/your-project.git
    cd your-project
    ```

2. Create a new branch for your changes:

    ```bash
    git checkout -b feature/new-feature
    ```

3. Make your changes, commit, and push to your fork:

    ```bash
    git add .
    git commit -m "Add new feature"
    git push origin feature/new-feature
    ```

4. Create a pull request describing your changes.

## License

This project is licensed under the [Your License Name] - see the [LICENSE](LICENSE) file for details.

## Swagger Documentation

Access the Swagger API documentation at [http://localhost:8000/swagger/](http://127.0.0.1/swagger) for more details on the API endpoints and usage.
