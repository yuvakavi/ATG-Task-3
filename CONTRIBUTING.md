# Contributing to Avatar System

We welcome contributions! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone <your-fork-url>`
3. Create a branch: `git checkout -b feature/your-feature`
4. Install dev dependencies: `pip install -r requirements-dev.txt`

## Development Workflow

### Code Style

- Follow PEP 8 guidelines
- Use type hints where applicable
- Add docstrings to all functions and classes
- Run linting: `flake8 .`
- Format code: `black .`

### Testing

Before submitting a PR:

```bash
# Run workspace tests
python test_workspace.py

# Run unit tests (when available)
pytest tests/

# Check code coverage
pytest --cov=. tests/
```

### Commit Messages

Use clear, descriptive commit messages:
```
feat: Add new speech encoder model
fix: Resolve audio loading issue
docs: Update installation guide
refactor: Simplify pipeline initialization
```

## Contribution Guidelines

### Reporting Bugs

When reporting bugs, include:
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages and logs

### Requesting Features

For feature requests:
- Describe the feature clearly
- Explain the use case
- Suggest implementation approach (if applicable)

### Pull Requests

1. Update documentation for any new features
2. Add tests for new functionality
3. Ensure all tests pass
4. Update CHANGELOG.md
5. Request review from maintainers

## Code Review Process

- PRs require at least one approval
- Address all reviewer comments
- Keep PRs focused and manageable in size
- Rebase on main before merging

## Areas for Contribution

- **Models**: Improve neural network architectures
- **Optimization**: Better quantization and acceleration
- **Documentation**: Tutorials, examples, guides
- **Testing**: Unit tests, integration tests, benchmarks
- **Features**: New capabilities and improvements

## Questions?

Open an issue or start a discussion in the repository.

Thank you for contributing! 🎉
