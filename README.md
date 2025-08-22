# Python Hello World Project

A simple and well-structured Python project that demonstrates basic Python programming concepts including functions, type hints, docstrings, and user input handling.

## Features

- **Modular Design**: Clean separation of concerns with dedicated functions
- **Type Safety**: Full type hints for better code documentation and IDE support
- **Documentation**: Comprehensive docstrings following Python conventions
- **Interactive**: User input handling for personalized greetings
- **Best Practices**: Follows Python PEP 8 style guidelines

## Project Structure

```
ai-protocol/
├── src/
│   └── main.py          # Main Python script
├── pyproject.toml       # Project configuration and dependencies
├── requirements.txt     # Python dependencies (empty for this project)
└── README.md           # Project documentation
```

## Requirements

- Python 3.8 or higher
- No external dependencies required

## Installation

1. Clone or download this project
2. Ensure Python 3.8+ is installed on your system
3. Navigate to the project directory

### Development Setup

For development work, install the project with development dependencies:

```bash
# Install the project in editable mode with dev dependencies
pip install -e ".[dev]"

# Or install dependencies separately
pip install -e .
pip install pytest black flake8 mypy
```

## Usage

### Basic Execution

Run the project directly:

```bash
python src/main.py
```

Or make it executable and run:

```bash
chmod +x src/main.py
./src/main.py
```

### Expected Output

```
Hello, World!
Hello, Python Developer!
Enter your name (or press Enter for default):
```

## Code Structure

### `say_hello(name: str = "World") -> str`

A function that returns a personalized greeting message:

- **Parameters**: `name` (optional, defaults to "World")
- **Returns**: Formatted greeting string
- **Type Hints**: Full type annotations for clarity

### `main()`

The main execution function that:

- Demonstrates basic functionality
- Shows personalized greetings
- Handles user input interactively

## Development

This project follows Python best practices:

- **Type Safety**: Uses type hints throughout
- **Documentation**: Comprehensive docstrings
- **Modularity**: Single responsibility functions
- **Error Handling**: Graceful input validation
- **Style**: PEP 8 compliant formatting

### Development Tools

This project is configured with modern Python development tools:

#### **Code Quality Tools**

- **Black**: Automatic code formatting (PEP 8 compliant)
- **Flake8**: Linting and style checking
- **MyPy**: Static type checking
- **Pytest**: Testing framework

#### **Running Development Tools**

```bash
# Code formatting
black --check src tests          # Check formatting
black src tests                 # Auto-format code

# Linting
flake8 src tests                # Run linter

# Type checking
mypy src                        # Type check source code

# Testing
pytest                          # Run all tests
pytest -v                       # Verbose test output
pytest --cov=src               # Run tests with coverage

# Run all quality checks
pip install -e ".[dev]"        # Install dev dependencies first
black --check src tests && flake8 src tests && mypy src && pytest
```

#### **Project Configuration**

The project uses `pyproject.toml` for modern Python project configuration:

- **Build System**: Setuptools with wheel
- **Dependencies**: Managed through pyproject.toml
- **Tool Configuration**: Black, pytest, and other tools configured centrally
- **Development Dependencies**: Separate dev tools for development workflow

#### **CI/CD Ready**

The project is configured for continuous integration:

- **GitHub Actions**: Ready for `.github/workflows/ci.yml`
- **GitLab CI**: Ready for `.gitlab-ci.yml`
- **Automated Testing**: Runs on multiple Python versions
- **Quality Gates**: Linting, formatting, type checking, and testing

#### **IDE Integration**

For the best development experience:

- **VS Code**: Configure with Python extension and settings
- **PyCharm**: Native support for pyproject.toml
- **Vim/Neovim**: Use ALE or similar for real-time linting

### Development Workflow

1. **Setup**: `pip install -e ".[dev]"`
2. **Code**: Write your Python code in `src/`
3. **Format**: `black src` (auto-format)
4. **Lint**: `flake8 src` (check style)
5. **Type Check**: `mypy src` (verify types)
6. **Test**: `pytest` (run tests)
7. **Commit**: All checks should pass

## Testing

To test the project:

1. Run the script and verify output
2. Test with different input values
3. Verify type hints with a type checker like `mypy`
4. Run automated tests: `pytest`

## Future Enhancements

Potential improvements could include:

- Unit tests using `pytest`
- Command-line argument parsing with `argparse`
- Configuration file support
- Internationalization (i18n) support
- Docker containerization
- API endpoints with FastAPI
- Database integration

## License

This project is open source and available under the MIT License.
