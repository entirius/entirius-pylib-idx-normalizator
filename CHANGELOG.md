# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-10

### Added
- Initial release of `entirius-pylib-idx-normalizator`
- Core normalization functions:
  - `normalize_idx()` - General text to URL-safe identifier conversion
  - `normalize_sku()` - Stock Keeping Unit processing with validation
  - `normalize_ean()` - European Article Number normalization
  - `normalize_url_key()` - SEO-friendly URL key generation
- Validation functions for all normalization types:
  - `validate_idx()` - IDX format validation with customizable length constraints
  - `validate_sku()` - SKU format validation with forbidden character checks
  - `validate_ean()` - EAN format validation with length constraints
  - `validate_url_key()` - URL key format validation
- Smart truncation with MD5 hash for long strings to maintain uniqueness
- Comprehensive error handling with descriptive error messages
- Full type hints support for better developer experience
- Python 3.11+ compatibility with modern language features

### Technical Features
- **Packaging**: Modern `pyproject.toml` configuration following Python packaging standards
- **License**: Mozilla Public License 2.0 (MPL-2.0) for open-source distribution
- **Dependencies**: Minimal dependencies with only `python-slugify` required
- **Code Quality**: Integrated `ruff` for formatting, linting, and code analysis
- **Testing**: `pytest` framework with comprehensive test coverage
- **CI/CD**: GitHub Actions workflow for automated testing and building
- **Documentation**: Complete README with installation, usage examples, and API reference
- **Architecture**: Follows Entirius platform standards and ADR guidelines

### Performance Characteristics
- **Speed**: Optimized for high-throughput processing in e-commerce applications
- **Memory**: Minimal memory footprint suitable for bulk operations
- **Consistency**: Deterministic output for same input across different environments
- **Scalability**: Designed for PIM systems handling large product catalogs

### Development Environment
- **Package Manager**: UV integration for fast Python package management
- **Code Style**: Ruff-based formatting and linting (replaced Black)
- **Build System**: Setuptools with modern pyproject.toml configuration
- **Type Safety**: Runtime validation approach (mypy removed for simplicity)
- **Testing**: Simple pytest setup without coverage complexity
- **Documentation**: Comprehensive examples for Django integration

### Integration Support
- **Django**: Ready-to-use model integration examples
- **REST APIs**: Serializer validation examples with Django REST Framework
- **Database**: Database-friendly output formats for storage
- **URLs**: SEO-optimized URL generation for web applications
- **E-commerce**: Specialized functions for product catalogs and PIM systems

## [0.1.0] - Initial Development

### Added
- Project structure and basic functionality
- Initial implementation of core normalization logic
- Basic test coverage and validation

### Changed
- Migrated from Black to Ruff for code formatting
- Updated license format to modern SPDX standard
- Removed pytest-cov dependency for simplified testing
- Removed mypy for lighter development workflow

### Technical Improvements
- Fixed setuptools deprecation warnings
- Updated GitHub Actions workflow for UV package manager
- Improved error messages and validation logic
- Enhanced documentation with practical examples

---

## Development Notes

### Version 1.0.0 Release
This is the first stable release of the IDX Normalizator library for the Entirius platform. The library provides robust text normalization utilities specifically designed for e-commerce applications, with particular focus on Product Information Management (PIM) systems.

**Key Design Decisions:**
- **Simplicity over complexity**: Removed mypy and coverage tools for easier maintenance
- **Modern tooling**: Uses UV package manager and Ruff for all code quality needs
- **E-commerce focus**: Specialized functions for SKU, EAN, and URL handling
- **Platform integration**: Designed for seamless integration with Entirius ecosystem

**Breaking Changes from Pre-release:**
- None (this is the initial stable release)

**Migration Guide:**
- This is the first public release, no migration needed

**Known Limitations:**
- Limited to basic text normalization patterns
- No advanced Unicode handling beyond python-slugify
- No plugin system for custom normalization rules

**Future Roadmap:**
- Enhanced Unicode support for international products
- Plugin architecture for custom normalization rules
- Performance optimizations for very large datasets
- Additional e-commerce specific validators (GTIN, UPC, etc.)

### Links
- **Repository**: https://github.com/entirius/entirius-pylib-idx-normalizator
- **Documentation**: https://docs.entirius.com
- **Issues**: https://github.com/entirius/entirius-pylib-idx-normalizator/issues
- **Main Project**: https://github.com/entirius/entirius
