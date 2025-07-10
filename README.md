# Entirius PyLib IDX Normalizator

[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

A Python library for normalizing and validating identifiers in e-commerce applications, following the Entirius platform conventions.

## Overview

The IDX Normalizator provides consistent text normalization and validation utilities specifically designed for Product Information Management (PIM) systems and e-commerce applications. It ensures that all identifiers follow standardized formats for URLs, database keys, and product codes.

## Features

- **IDX Normalization**: Convert any text to URL-safe, database-friendly identifiers using slugify
- **Smart Truncation**: Automatically handles long strings with MD5 hash truncation
- **SKU Processing**: Specialized handling for Stock Keeping Unit identifiers
- **EAN Support**: European Article Number validation and normalization
- **URL Key Generation**: Create SEO-friendly URL keys for web applications
- **Comprehensive Validation**: Ensure identifiers meet business rules and format requirements
- **Type Safety**: Full type hints for better development experience

## Installation

### Production Use

```bash
# Install from PyPI (when published)
uv pip install entirius-pylib-idx-normalizator

# Install from Git repository
uv pip install git+https://github.com/entirius/entirius-pylib-idx-normalizator.git
```

### Development Setup

```bash
# Clone the repository
git clone https://github.com/entirius/entirius-pylib-idx-normalizator.git
cd entirius-pylib-idx-normalizator

# Create virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode with all extras
uv pip install -e ".[dev,test]"
```

### Integration with Entirius Projects

For Entirius platform development:

```bash
# In Django services (e.g., entirius-backend)
uv pip install -e ../../pylib/entirius-pylib-idx-normalizator

# In Django modules (e.g., entirius-pim)
uv pip install -e ../../../pylib/entirius-pylib-idx-normalizator
```

## Usage

### Basic IDX Normalization

```python
from idx_normalizator import normalize_idx, validate_idx

# Normalize product names to identifiers
product_name = "Premium Coffee Beans - Ethiopian Origin!"
idx = normalize_idx(product_name)
print(idx)  # "premium-coffee-beans-ethiopian-origin"

# Validate existing identifier
try:
    validate_idx("premium-coffee-beans")
    print("Valid identifier")
except ValueError as e:
    print(f"Invalid: {e}")
```

### SKU Management

```python
from idx_normalizator import normalize_sku, validate_sku

# Normalize SKU codes
raw_sku = "COFFEE-123-ABC DEF"
sku = normalize_sku(raw_sku)
print(sku)  # "coffee-123-abc-def"

# Validate SKU format
if validate_sku("PROD-123"):
    print("Valid SKU")
```

### EAN Code Processing

```python
from idx_normalizator import normalize_ean, validate_ean

# Normalize EAN codes
ean_input = "123 456 789 012"
ean = normalize_ean(ean_input)
print(ean)  # "123456789012"

# Validate EAN format
if validate_ean("1234567890123"):
    print("Valid EAN-13")
```

### URL Key Generation

```python
from idx_normalizator import normalize_url_key, validate_url_key

# Create SEO-friendly URL keys
category_name = "Premium Coffee & Tea Products"
url_key = normalize_url_key(category_name)
print(url_key)  # "premium-coffee-tea-products"

# Validate URL key
if validate_url_key("premium-coffee"):
    print("Valid URL key")
```

### Advanced: Long String Handling

```python
from idx_normalizator import normalize_idx

# Handle very long product names
long_name = "This is an extremely long product name that exceeds normal limits and needs truncation with hash"
short_idx = normalize_idx(long_name, max_len=50)
print(short_idx)  # "this-is-an-extremely-long-product-name-that_a1b2c3"
```

## API Reference

### Core Functions

#### `normalize_idx(text: str, max_len: int = 128) -> str`
Normalizes any text to a URL-safe identifier.

- **Parameters:**
  - `text`: Input text to normalize
  - `max_len`: Maximum length (default: 128)
- **Returns:** Normalized identifier
- **Features:** Automatic truncation with MD5 hash for long strings

#### `validate_idx(idx: str, min_len: int = 1, max_len: int = 128) -> bool`
Validates that an identifier meets format requirements.

- **Parameters:**
  - `idx`: Identifier to validate
  - `min_len`: Minimum length (default: 1)
  - `max_len`: Maximum length (default: 128)
- **Raises:** `ValueError` if validation fails

### Specialized Functions

| Function | Purpose | Example Input | Example Output |
|----------|---------|---------------|----------------|
| `normalize_sku()` | Stock Keeping Units | `"SKU-123 ABC"` | `"sku-123-abc"` |
| `validate_sku()` | SKU validation | `"PROD-123"` | `True/False` |
| `normalize_ean()` | European Article Numbers | `"123 456 789"` | `"123456789"` |
| `validate_ean()` | EAN validation | `"1234567890123"` | `True/False` |
| `normalize_url_key()` | URL-friendly keys | `"Product & Service"` | `"product-service"` |
| `validate_url_key()` | URL key validation | `"product-key"` | `True/False` |

## Configuration

The library uses sensible defaults but can be customized:

```python
# Custom maximum length
short_idx = normalize_idx("long text", max_len=50)

# Custom validation ranges
validate_idx("test", min_len=3, max_len=100)
```

## Development

### Setup Development Environment

```bash
# Install development dependencies
uv pip install -e ".[dev,test]"

# Verify installation
python -c "from idx_normalizator import normalize_idx; print('OK')"
```

### Code Quality Tools

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

### Testing

```bash
# Run test suite
pytest

# Run with coverage
pytest --cov=idx_normalizator --cov-report=html

# Run specific test
pytest tests/test_normalize.py::test_basic_normalization
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

## Integration Examples

### Django Model Integration

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

### API Serializer Integration

```python
from rest_framework import serializers
from idx_normalizator import normalize_idx, validate_idx

class ProductSerializer(serializers.ModelSerializer):
    idx = serializers.CharField(required=False)
    
    def validate_idx(self, value):
        try:
            validate_idx(value)
            return value
        except ValueError as e:
            raise serializers.ValidationError(str(e))
    
    def create(self, validated_data):
        if 'idx' not in validated_data:
            validated_data['idx'] = normalize_idx(validated_data['name'])
        return super().create(validated_data)
```

## Technical Details

### Normalization Algorithm

1. **Slugification**: Convert to lowercase, replace spaces/special chars with hyphens
2. **Character filtering**: Allow only `a-z`, `0-9`, `-`, `_`
3. **Length management**: Truncate long strings with MD5 hash suffix
4. **Uniqueness**: Hash suffix ensures uniqueness for truncated strings

### Performance Characteristics

- **Speed**: Optimized for high-throughput processing
- **Memory**: Minimal memory footprint
- **Consistency**: Deterministic output for same input
- **Scalability**: Suitable for bulk processing operations

## Requirements

- **Python**: 3.11 or higher
- **Dependencies**: 
  - `python-slugify` - Text slugification
- **Development Tools**:
  - `black` - Code formatting
  - `ruff` - Linting and code analysis
  - `mypy` - Type checking
  - `pytest` - Testing framework

## Architecture Decision Records

This library follows established Entirius platform standards:

- **[ADR-007](https://docs.entirius.com/adr/adr-007-uv-python-package-manager)**: Uses UV package manager
- **[ADR-008](https://docs.entirius.com/adr/adr-008-github-repository-naming-conventions)**: Follows `entirius-pylib-*` naming
- **[ADR-009](https://docs.entirius.com/adr/adr-009-pyproject-toml-standard)**: Uses pyproject.toml configuration

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes following the code standards
4. Run tests and quality checks
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Code Standards

- Follow PEP 8 style guide
- Use type hints for all functions
- Write comprehensive docstrings
- Maintain test coverage above 90%
- Use meaningful commit messages

## License

This project is licensed under the Mozilla Public License 2.0 (MPL-2.0) - see the [LICENSE](LICENSE) file for details.

## Links

- **Repository**: https://github.com/entirius/entirius-pylib-idx-normalizator
- **Documentation**: https://docs.entirius.com
- **Issues**: https://github.com/entirius/entirius-pylib-idx-normalizator/issues
- **Main Project**: https://github.com/entirius/entirius
- **Platform Documentation**: https://docs.entirius.com

## Support

For questions, issues, or contributions:

- **Issues**: Use GitHub Issues for bug reports and feature requests
- **Discussions**: Join GitHub Discussions for questions and community support
- **Email**: Contact the development team at dev@entirius.com

---

Part of the [Entirius](https://github.com/entirius/entirius) open-source e-commerce AI platform.