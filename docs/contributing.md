# Contributing to Renesis AI Assistant

Thank you for your interest in contributing to the Renesis AI Assistant! This guide will help you get started with contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contributing Guidelines](#contributing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)
- [Issue Reporting](#issue-reporting)
- [Feature Requests](#feature-requests)
- [Community](#community)

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct:

- **Be respectful**: Treat all contributors with respect and kindness
- **Be inclusive**: Welcome newcomers and help them get started
- **Be constructive**: Provide helpful feedback and suggestions
- **Be professional**: Maintain a professional tone in all communications
- **Be patient**: Remember that everyone has different skill levels and backgrounds

## Getting Started

### Prerequisites

Before contributing, ensure you have:

- Python 3.8 or higher
- Git installed and configured
- A GitHub account
- Basic knowledge of Python, Slack APIs, and AI/ML concepts
- Familiarity with the project architecture (see [Architecture Guide](architecture.md))

### First Steps

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/gutless-ai-assistant.git
   cd gutless-ai-assistant
   ```
3. **Add the upstream remote**:
   ```bash
   git remote add upstream https://github.com/ORIGINAL_OWNER/gutless-ai-assistant.git
   ```
4. **Set up the development environment** (see [Development Setup](#development-setup))

## Development Setup

### Environment Setup

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Development dependencies
   ```

3. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Install pre-commit hooks**:
   ```bash
   pre-commit install
   ```

### Development Dependencies

The project uses additional development tools:

```bash
# Code formatting and linting
pip install black flake8 isort mypy

# Testing
pip install pytest pytest-cov pytest-mock

# Documentation
pip install -r docs/requirements.txt

# Pre-commit hooks
pip install pre-commit
```

### Running the Application

1. **Start the development server**:
   ```bash
   python src/bot.py
   ```

2. **Run tests**:
   ```bash
   pytest
   ```

3. **Check code quality**:
   ```bash
   # Format code
   black .
   isort .
   
   # Lint code
   flake8 .
   mypy .
   ```

## Contributing Guidelines

### Types of Contributions

We welcome various types of contributions:

- **Bug fixes**: Fix issues and improve stability
- **Feature development**: Add new functionality
- **Documentation**: Improve or add documentation
- **Testing**: Add or improve test coverage
- **Performance**: Optimize code performance
- **Refactoring**: Improve code structure and maintainability

### Contribution Workflow

1. **Check existing issues** to see if your contribution is already being worked on
2. **Create an issue** if one doesn't exist for your contribution
3. **Discuss your approach** in the issue before starting work
4. **Create a feature branch** from the main branch
5. **Make your changes** following our coding standards
6. **Write tests** for your changes
7. **Update documentation** as needed
8. **Submit a pull request**

### Branch Naming Convention

Use descriptive branch names:

- `feature/add-user-authentication`
- `bugfix/fix-slack-connection-timeout`
- `docs/update-installation-guide`
- `refactor/improve-embedding-service`
- `test/add-core-logic-tests`

## Pull Request Process

### Before Submitting

Ensure your pull request:

- [ ] Follows the coding standards
- [ ] Includes appropriate tests
- [ ] Updates relevant documentation
- [ ] Passes all existing tests
- [ ] Has a clear, descriptive title
- [ ] Includes a detailed description

### Pull Request Template

Use this template for your pull requests:

```markdown
## Description

Brief description of the changes made.

## Type of Change

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing

- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] I have tested the changes manually

## Documentation

- [ ] I have updated the documentation accordingly
- [ ] I have added docstrings to new functions/classes
- [ ] I have updated the API reference if needed

## Checklist

- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
```

### Review Process

1. **Automated checks**: CI/CD pipeline runs tests and quality checks
2. **Code review**: Maintainers review your code for quality and correctness
3. **Feedback**: Address any feedback or requested changes
4. **Approval**: Once approved, your PR will be merged

## Coding Standards

### Python Style Guide

We follow PEP 8 with some modifications:

- **Line length**: 88 characters (Black default)
- **Imports**: Use isort for import organization
- **Type hints**: Use type hints for all public functions
- **Docstrings**: Use Google-style docstrings

### Code Formatting

We use automated tools for consistent formatting:

```bash
# Format code
black .

# Sort imports
isort .

# Check formatting
black --check .
isort --check-only .
```

### Linting

We use flake8 for linting:

```bash
# Run linter
flake8 .

# Configuration in setup.cfg
[flake8]
max-line-length = 88
extend-ignore = E203, W503
exclude = venv, .git, __pycache__
```

### Type Checking

We use mypy for static type checking:

```bash
# Run type checker
mypy .

# Configuration in mypy.ini
[mypy]
python_version = 3.8
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
```

### Documentation Standards

#### Docstring Format

Use Google-style docstrings:

```python
def process_query(query: str, user_id: str) -> QueryResponse:
    """Process a user query and return a response.
    
    Args:
        query: The user's question or request.
        user_id: Unique identifier for the user.
        
    Returns:
        QueryResponse object containing the answer and metadata.
        
    Raises:
        ValueError: If query is empty or invalid.
        APIError: If external API calls fail.
        
    Example:
        >>> response = process_query("What foods are eliminated?", "user123")
        >>> print(response.answer)
        "In Week 1, the following foods are eliminated..."
    """
```

#### Code Comments

- Use comments sparingly for complex logic
- Prefer self-documenting code
- Explain "why" not "what"
- Keep comments up-to-date with code changes

## Testing

### Testing Framework

We use pytest for testing:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_core_logic.py

# Run with verbose output
pytest -v
```

### Test Structure

Organize tests to mirror the source structure:

```
tests/
├── conftest.py              # Shared fixtures
├── test_bot.py              # Tests for src/bot.py
├── test_core_logic.py       # Tests for src/core_logic.py
├── test_embedding_service.py # Tests for src/embedding_service.py
└── integration/             # Integration tests
    ├── test_slack_integration.py
    └── test_api_integration.py
```

### Writing Tests

#### Unit Tests

```python
import pytest
from unittest.mock import Mock, patch
from src.core_logic import QueryProcessor

class TestQueryProcessor:
    def test_process_query_success(self):
        """Test successful query processing."""
        processor = QueryProcessor()
        result = processor.process_query("test query", "user123")
        
        assert result.answer is not None
        assert result.confidence > 0.5
        assert len(result.sources) > 0
    
    @patch('src.core_logic.openai_client')
    def test_process_query_api_error(self, mock_client):
        """Test handling of API errors."""
        mock_client.side_effect = Exception("API Error")
        processor = QueryProcessor()
        
        with pytest.raises(APIError):
            processor.process_query("test query", "user123")
```

#### Integration Tests

```python
import pytest
from src.bot import SlackBot

@pytest.mark.integration
class TestSlackIntegration:
    def test_bot_responds_to_mention(self, slack_client):
        """Test bot responds when mentioned."""
        bot = SlackBot()
        response = bot.handle_mention("@bot what is Week 1?")
        
        assert response is not None
        assert "Week 1" in response
```

### Test Coverage

Maintain high test coverage:

- **Minimum**: 80% overall coverage
- **Target**: 90%+ for core modules
- **Critical paths**: 100% coverage for error handling

```bash
# Generate coverage report
pytest --cov=src --cov-report=html

# View coverage report
open htmlcov/index.html
```

### Mocking External Services

Mock external API calls in tests:

```python
@patch('src.services.openai_client')
@patch('src.services.pinecone_client')
def test_query_processing(mock_pinecone, mock_openai):
    # Mock responses
    mock_pinecone.query.return_value = mock_search_results
    mock_openai.chat.completions.create.return_value = mock_completion
    
    # Test your code
    result = process_query("test query")
    assert result.answer == "expected answer"
```

## Documentation

### Documentation Types

1. **Code documentation**: Docstrings and comments
2. **User documentation**: Usage guides and tutorials
3. **Developer documentation**: Architecture and API reference
4. **Process documentation**: Contributing and deployment guides

### Writing Documentation

#### Markdown Guidelines

- Use clear, concise language
- Include code examples
- Add table of contents for long documents
- Use consistent formatting
- Include links to related documentation

#### Code Examples

Include working code examples:

```python
# Good: Complete, runnable example
from src.core_logic import QueryProcessor

processor = QueryProcessor()
response = processor.process_query(
    query="What foods should I avoid in Week 1?",
    user_id="user123"
)
print(f"Answer: {response.answer}")
print(f"Sources: {[s.title for s in response.sources]}")
```

#### API Documentation

Document all public APIs:

```python
class QueryProcessor:
    """Processes user queries and generates responses.
    
    This class handles the core logic for processing user questions,
    including embedding generation, vector search, and response generation.
    
    Attributes:
        embedding_service: Service for generating text embeddings.
        pinecone_service: Service for vector database operations.
        llm_service: Service for language model interactions.
    
    Example:
        >>> processor = QueryProcessor()
        >>> response = processor.process_query("What is Week 1?", "user123")
        >>> print(response.answer)
    """
```

### Building Documentation

We use a modern documentation framework:

```bash
# Install documentation dependencies
pip install -r docs/requirements.txt

# Serve documentation locally
python -m http.server 8000 --directory site

# Build documentation
npm run build
```

## Issue Reporting

### Bug Reports

When reporting bugs, include:

1. **Clear title**: Descriptive summary of the issue
2. **Environment**: Python version, OS, dependencies
3. **Steps to reproduce**: Detailed steps to recreate the bug
4. **Expected behavior**: What should happen
5. **Actual behavior**: What actually happens
6. **Error messages**: Full error messages and stack traces
7. **Additional context**: Screenshots, logs, or other relevant information

### Bug Report Template

```markdown
**Bug Description**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected Behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Environment:**
 - OS: [e.g. Windows 10, macOS 12.0, Ubuntu 20.04]
 - Python Version: [e.g. 3.9.7]
 - Project Version: [e.g. 1.0.0]

**Additional Context**
Add any other context about the problem here.
```

## Feature Requests

### Proposing Features

Before proposing a feature:

1. **Check existing issues** to avoid duplicates
2. **Consider the scope**: Does it fit the project goals?
3. **Think about implementation**: Is it technically feasible?
4. **Consider maintenance**: Will it require ongoing support?

### Feature Request Template

```markdown
**Feature Description**
A clear and concise description of the feature you'd like to see.

**Problem Statement**
Describe the problem this feature would solve.

**Proposed Solution**
Describe the solution you'd like to see implemented.

**Alternatives Considered**
Describe any alternative solutions or features you've considered.

**Use Cases**
Provide specific examples of how this feature would be used.

**Implementation Notes**
Any technical considerations or implementation ideas.

**Additional Context**
Add any other context, mockups, or examples about the feature request.
```

## Community

### Communication Channels

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and discussions
- **Slack Workspace**: Real-time communication (if available)
- **Email**: Direct contact with maintainers

### Getting Help

1. **Check documentation**: Start with existing docs
2. **Search issues**: Look for similar problems
3. **Ask questions**: Use GitHub Discussions
4. **Be specific**: Provide context and details
5. **Be patient**: Maintainers are volunteers

### Helping Others

- Answer questions in discussions
- Review pull requests
- Improve documentation
- Share your experience
- Mentor newcomers

## Release Process

### Versioning

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Checklist

- [ ] Update version numbers
- [ ] Update CHANGELOG.md
- [ ] Run full test suite
- [ ] Update documentation
- [ ] Create release notes
- [ ] Tag release in Git
- [ ] Deploy to production

## Recognition

We appreciate all contributions! Contributors will be:

- Listed in the project's contributors file
- Mentioned in release notes for significant contributions
- Invited to join the maintainers team for sustained contributions

## Questions?

If you have questions about contributing:

1. Check this guide first
2. Search existing issues and discussions
3. Create a new discussion with your question
4. Contact maintainers directly if needed

Thank you for contributing to the Renesis AI Assistant! 🚀