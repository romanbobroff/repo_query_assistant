# Contributing to Repo Query Assistant

We welcome contributions to the Repo Query Assistant project and are grateful for every pull request or suggestion. This document provides guidelines for contributing to the project.

## Code of Conduct

Participation in this project is governed by a Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to [ValentinBugakov@gmail.com].

## Getting Started

1. **Fork the repository** on GitHub.
2. **Clone the forked repository** to your local machine.
3. **Create a new branch** for your changes.
4. **Make your changes** and commit them to your branch.

## Development Setup

Follow these steps to set up your development environment for the `repo_query_assistant` project:

1. Ensure you have `poetry` installed on your system. If you don't have `poetry`, install it by following the instructions on the [Poetry website](https://python-poetry.org/docs/#installation).
2. Clone the project repository and navigate to the project directory.
3. Run `poetry install` to install all project dependencies, including the `ruff` linter, as specified in the `pyproject.toml` file.
4. Write tests for new code and run them using `poetry run pytest` to ensure everything works as expected.

## Using Linters in the Project

### Purpose of Linters

Linters are used in the `repo_query_assistant` project to maintain high code quality, ensure adherence to coding standards, and prevent potential errors. They help in keeping the code clean and improving its readability.

### Linter Used

In this project, we use [ruff](https://ruff.rs/) as our primary linting tool for Python code. `Ruff` is integrated into our development environment via `poetry`, so it gets installed automatically when you run `poetry install`.

### Running the Linter

To lint your code with `ruff`, you can run the following command in the root of your project directory:

```bash
poetry run ruff .
```

## Submitting Changes

1. Push your changes to your fork on GitHub.
2. Submit a pull request to the `dev` branch of the `romanbobroff/repo_query_assistant` repository.
3. In the pull request, describe the changes and reference any related issues.

## Reporting Issues

- Use the [GitHub Issues](https://github.com/romanbobroff/repo_query_assistant/issues) page to report issues.
- Describe the issue in detail, including steps to reproduce the issue.
- Include information about your environment, such as operating system, Python version, and any other relevant details.

## Code Review Process

- The project maintainers will review your pull request.
- Changes may be requested to conform to our style and standards.
- Once approved, one of the maintainers will merge the pull request.

## Community and Communication

- If you have questions or want to discuss the project, use [GitHub Discussions](https://github.com/romanbobroff/repo_query_assistant/discussions).

Thank you for your interest in contributing to the Repo Query Assistant!