# BMPCode

This repository contains multiple projects demonstrating various programming concepts and applications.

## Repository Structure

This repository is organized into the following main components:

### 1. Library Management System (C#)
Located in `AccelerateDevGitHubCopilot/`

A comprehensive console-based library management application built with .NET, featuring:
- Patron management
- Book loan operations
- Membership renewals
- JSON-based data persistence

**Technologies:**
- C# / .NET
- JSON for data storage
- Unit testing with xUnit

For detailed documentation, see [Library App README](AccelerateDevGitHubCopilot/README.md)

### 2. Rock, Paper, Scissors Game (Python)
Located in `testing/`

A simple interactive command-line game demonstrating:
- User input handling
- Random number generation
- Game logic implementation

**Technologies:**
- Python 3

## Getting Started

### Prerequisites

To work with the projects in this repository, you'll need:

- **For C# Library App:**
  - .NET SDK (version compatible with the project)
  - Visual Studio or Visual Studio Code (recommended)

- **For Python Game:**
  - Python 3.x

### Building and Running

#### Library Management System

1. Navigate to the root directory
2. Open `BMPCode.sln` in Visual Studio or your preferred IDE
3. Build the solution to restore dependencies
4. Run the `Library.Console` project
5. Follow the on-screen instructions to interact with the library system

Alternatively, using the command line:
```bash
cd AccelerateDevGitHubCopilot/src/Library.Console
dotnet run
```

#### Rock, Paper, Scissors Game

```bash
cd testing
python paper_rock_scissors.py
```

## Testing

### C# Unit Tests

The Library Management System includes comprehensive unit tests located in `AccelerateDevGitHubCopilot/tests/UnitTests/`.

To run the tests:
```bash
dotnet test
```

### Python Tests

```bash
cd testing
python test_paper_rock_scissors.py
```

## Project Components

### Library Management System Structure
- **ApplicationCore**: Business logic and domain entities
- **Infrastructure**: Data access layer with JSON repositories
- **Console**: User interface and application entry point
- **UnitTests**: Test suite for core functionality

### Files
- `BMPCode.sln` - Visual Studio solution file for the C# projects
- `.vscode/` - VS Code configuration
- `.gitattributes` - Git attributes configuration

## Contributing

When contributing to this repository:
1. Follow the existing code style and conventions
2. Write tests for new functionality
3. Update documentation as needed
4. Ensure all tests pass before submitting changes

## License

This project is licensed under the MIT License.
