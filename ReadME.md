# Voter Sync App

## Overview
The Voter Sync App is a Python application designed to synchronize voter data between different databases. It ensures that voter information is up-to-date and consistent across multiple platforms.

## Features
- Synchronize voter data between multiple databases
- Ensure data consistency and integrity
- Easy to configure and use

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/voter_sync_app.git
    ```
2. Navigate to the project directory:
    ```bash
    cd voter_sync_app
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

The application uses a configuration file (`config.py`) to manage settings for different environments (development, testing, production). The configuration settings are defined in the `Config` class and its subclasses.

### Configuration Classes

- **Config**: Base configuration class with common settings.
  -`SECRET_KEY`: Secret key for session management and security. Default is `'you-will-never-guess'`.
  - `SQLALCHEMY_DATABASE_URI`: Database URI. Default is `'sqlite:///app.db'`.
  - `SQLALCHEMY_TRACK_MODIFICATIONS`: Disable SQLAlchemy track modifications. Default is `False`.

- **DevelopmentConfig**: Configuration for development environment.
  - Inherits from `Config`.
  - `DEBUG`: Enable debug mode. Default is `True`.

- **TestingConfig**: Configuration for testing environment.
  - Inherits from `Config`.
  - `TESTING`: Enable testing mode. Default is `True`.
  - `SQLALCHEMY_DATABASE_URI`: Database URI for testing. Default is `'sqlite:///test.db'`.

- **ProductionConfig**: Configuration for production environment.
  - Inherits from `Config`.
  - `DEBUG`: Disable debug mode. Default is `False`.

### Environment Variables

You can override the default configuration settings by setting environment variables:

- `SECRET_KEY`: Set the secret key for session management and security.
- `DATABASE_URL`: Set the database URI.

### Usage

To use a specific configuration, set the `FLASK_ENV` environment variable:

```bash
export FLASK_ENV=development  # For development environment
export FLASK_ENV=testing      # For testing environment
export FLASK_ENV=production   # For production environment
```

## Usage
1. Configure the application by editing the `config.json` file with your database credentials and settings.
2. Run the application:
    ```bash
    python voter_sync_app.py
    ```

## Contributing
We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more details.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact
For any questions or feedback, please contact [your email address].
