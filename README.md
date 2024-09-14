# yijia_ids706_miniProj2

## Python Template

This project provides a Python-based framework designed to generate descriptive statistics and visualizations from datasets, with integrated CI/CD capabilities using GitHub Actions.


## File Structure

- **`.devcontainer/`**: Contains the development container configuration (`devcontainer.json` and a Dockerfile) to ensure a consistent development environment.
- **`Makefile`**: Provides commands for setup, testing, linting, and formatting the project.
- **`.github/workflows/`**: Contains CI/CD workflows for GitHub, which trigger actions like setup, linting, and testing when code is pushed to the repository.

## Setup

### 1. Clone the Repository

```bash
git clone git@github.com:nogibjj/yijia_ids706_miniProj2.git
```

### 2. Open the Repository in Visual Studio Code

- Reopen in the container using the .devcontainer configuration.
- Rebuild the container if necessary, ensuring Docker is running on your computer.

### 3. Install dependencies
Run the following command to install all required dependencies:

```bash
make install
```

## Usage
- make install: Installs dependencies specified in requirements.txt.
- make format: Formats Python files using Black.
- make lint: Lints Python files using Pylint, ignoring specific patterns.
- make test: Runs tests using pytest and generates a coverage report.
- make clean: Removes pytest cache.
- make generate_profile_report: Generates a profiling report in HTML and Markdown formats.

## CI/CD Setup
- Location: .github/workflows/
- Description: Contains GitHub Actions workflows for CI/CD, which automatically run setup, lint, and test actions on pushes to the GitHub repository.

## CI/CD Badge
[![CI](https://github.com/nogibjj/yijia_ids706_miniProj1/actions/workflows/hello.yml/badge.svg)](https://github.com/nogibjj/yijia_ids706_miniProj1/actions/workflows/hello.yml)

## Summary Report Generation
The CI/CD pipeline generates a Markdown report during its runtime using the profiling capabilities of ydata_profiling and Pandas. The generated report includes descriptive statistics and visualizations, which are committed and pushed back to the repository.
