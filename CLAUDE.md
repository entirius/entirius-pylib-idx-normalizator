# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with the entirius-pylib-idx-normalizator codebase.

## Project Overview

This is the Entirius PyLib IDX Normalizator - a Python library for normalizing and validating identifiers in e-commerce applications. The library provides text normalization and validation utilities specifically designed for Product Information Management (PIM) systems and e-commerce applications, following Entirius platform conventions.

**Repository**: https://github.com/entirius/entirius-pylib-idx-normalizator

## Technology Stack

- **Python 3.11+** - Primary programming language
- **python-slugify** - Text slugification dependency
- **pyproject.toml** - Modern Python packaging (per ADR-009)
- **setuptools** - Build backend
- **UV** - Package manager (per ADR-007)

## Development Commands

### Environment Setup
```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode with all extras
uv pip install -e ".[dev,test]"

# Verify installation
python -c "from idx_normalizator import normalize_idx; print('OK')"
```

### Testing
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=idx_normalizator --cov-report=term-missing --cov-report=html

# Run specific test file
pytest tests/test_normalize.py

# Run specific test
pytest tests/test_normalize.py::test_basic_normalization
```

### Code Quality
```bash
# Format code
black .

# Lint and fix issues
ruff check . --fix

# Type checking
mypy .

# Run all quality checks
black . && ruff check . && mypy .
```

### Building and Publishing
```bash
# Build package
uv build

# Check build
twine check dist/*

# Upload to PyPI (maintainers only)
twine upload dist/*
```

## Project Structure

```
entirius-pylib-idx-normalizator/
├── src/
│   └── idx_normalizator/
│       ├── __init__.py         # Public API exports
│       └── idx_normalizator.py # Core implementation
├── tests/                      # Test suite (when created)
├── pyproject.toml             # Project configuration (ADR-009)
├── README.md                  # Main documentation
├── LICENSE                    # MPL-2.0 license
└── CLAUDE.md                  # This file
```

## Core Functions

The library provides the following main functions:

1. **normalize_idx(text, max_len=128)** - Core identifier normalization
2. **validate_idx(idx, min_len=1, max_len=128)** - Identifier validation
3. **normalize_sku(text)** - Stock Keeping Unit normalization
4. **validate_sku(sku)** - SKU validation
5. **normalize_ean(text)** - European Article Number normalization
6. **validate_ean(ean)** - EAN validation
7. **normalize_url_key(text)** - URL key normalization
8. **validate_url_key(key)** - URL key validation

## Configuration

The project uses pyproject.toml for configuration (per ADR-009):

- **Build system**: setuptools with modern configuration
- **Dependencies**: Minimal runtime dependencies (python-slugify)
- **Development tools**: black, ruff, mypy, pytest
- **Python requirement**: >=3.11
- **License**: MPL-2.0

## Development Guidelines

### Code Standards
- Follow PEP 8 style guide
- Use type hints for all functions
- Write comprehensive docstrings
- Maintain test coverage above 90%
- Use meaningful commit messages

### Library Design Principles
- **Simplicity**: Clear, simple API with minimal dependencies
- **Performance**: Optimized for high-throughput processing
- **Consistency**: Deterministic output for same input
- **Reliability**: Comprehensive validation and error handling
- **Compatibility**: Works with Django, FastAPI, and other frameworks

### Function Implementation Guidelines
- All functions should have type hints
- Handle edge cases gracefully
- Raise ValueError for invalid inputs with clear messages
- Use consistent parameter naming across functions
- Maintain backward compatibility when possible

## Testing Strategy

- **Unit tests**: Test each function individually
- **Edge cases**: Test with empty strings, None values, very long strings
- **Performance tests**: Ensure acceptable performance for bulk operations
- **Integration tests**: Test with real-world e-commerce data
- **Coverage**: Maintain above 90% test coverage

## Architecture Decision Records

This library follows established Entirius platform standards:

- **ADR-007**: UV Python Package Manager - use `uv` for all package operations
- **ADR-008**: GitHub Repository Naming Conventions - follows `entirius-pylib-*` naming
- **ADR-009**: pyproject.toml Standard - uses modern Python packaging

## Integration with Entirius Platform

### Django Services Integration
```bash
# Install in Django services (e.g., entirius-backend)
uv pip install -e ../../pylib/entirius-pylib-idx-normalizator
```

### Django Modules Integration
```bash
# Install in Django modules (e.g., entirius-pim)
uv pip install -e ../../../pylib/entirius-pylib-idx-normalizator
```

### Usage in Django Models
```python
from django.db import models
from idx_normalizator import normalize_idx

class Product(models.Model):
    name = models.CharField(max_length=255)
    idx = models.SlugField(max_length=128, unique=True)
    
    def save(self, *args, **kwargs):
        if not self.idx:
            self.idx = normalize_idx(self.name)
        super().save(*args, **kwargs)
```

## Important Notes for Claude Code

### Development Workflow
- **Always run tests** after making code changes: `pytest`
- **Use proper linting commands**: `ruff check .`, `black .`, `mypy .`
- **Follow library design principles** and maintain API consistency
- **Ensure backward compatibility** when modifying existing functions
- **Update version** in pyproject.toml when making changes
- **IMPORTANT: Follow all Architecture Decision Records (ADRs)** - all decisions must align with established ADRs

### Package Management
- **Use UV exclusively** per ADR-007: `uv pip install` instead of `pip install`, `uv venv` instead of `python -m venv`
- **Use pyproject.toml** per ADR-009: all configuration in pyproject.toml, no setup.py or setup.cfg
- **Follow naming convention** per ADR-008: `entirius-pylib-*` pattern

### Quality Standards
- **Type hints required** for all public functions
- **Comprehensive docstrings** following Google or NumPy style
- **Error handling** with clear, actionable error messages
- **Performance considerations** for bulk processing scenarios
- **No breaking changes** without major version bump

### Security Considerations
- **Input validation** for all public functions
- **No eval() or exec()** usage
- **Safe string handling** to prevent injection attacks
- **Minimal dependencies** to reduce attack surface

## Common Operations

### Adding New Normalization Function
1. Add function to `src/idx_normalizator/idx_normalizator.py`
2. Add function to exports in `src/idx_normalizator/__init__.py`
3. Add comprehensive tests
4. Update README.md with usage examples
5. Run full test suite and quality checks

### Updating Dependencies
1. Update `pyproject.toml` dependencies section
2. Test with new dependency versions
3. Update README.md if needed
4. Ensure compatibility with Entirius platform

### Making Releases
1. Update version in `pyproject.toml`
2. Run full test suite: `pytest`
3. Run quality checks: `black . && ruff check . && mypy .`
4. Build package: `uv build`
5. Tag release and create GitHub release

## Related Documentation

- Main project documentation: `/home/zolv/desktop/entirius-nexus/docs/entirius-docs/`
- Architecture Decision Records: `/home/zolv/desktop/entirius-nexus/docs/entirius-docs/docs/adr/`
- Entirius Backend integration: `/home/zolv/desktop/entirius/services/entirius-backend/`
- Library README: `/home/zolv/desktop/entirius/pylib/entirius-pylib-idx-normalizator/README.md`

## Troubleshooting

### Common Issues
- **Import errors**: Ensure library is installed in development mode: `uv pip install -e .`
- **Type checking errors**: Run `mypy .` to check type annotations
- **Test failures**: Run `pytest -v` for detailed test output
- **Build issues**: Ensure pyproject.toml is valid and dependencies are correct

### Performance Optimization
- **Bulk processing**: Consider caching for repeated operations
- **Memory usage**: Monitor memory usage for large string processing
- **Regex compilation**: Regex patterns are compiled once at module level

## Support

For questions, issues, or contributions related to this library:

- **Issues**: Use GitHub Issues for bug reports and feature requests
- **Main project**: Reference main Entirius project documentation
- **Architecture**: Follow established ADRs for all architectural decisions