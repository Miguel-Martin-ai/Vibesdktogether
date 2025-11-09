# Deployment Guide

> **⚠️ IMPORTANT**: This is a **Python package**. Do NOT use Node.js build tools like `npm`, `bun`, or `yarn`. Use Python tools like `pip` and `setuptools`.

This guide explains how to deploy the VibeSDK Together AI integration package.

## ⚠️ Common Mistakes to Avoid

**DON'T USE:**
- ❌ `npm run build` (this is not a Node.js project)
- ❌ `bun run build` (this is not a Bun project)
- ❌ `yarn build` (this is not a Yarn project)
- ❌ Any TypeScript/JavaScript build tools

**DO USE:**
- ✅ `python setup.py sdist bdist_wheel` (Python package build)
- ✅ `pip install .` (Python package install)
- ✅ `python -m build` (modern Python build)

## Prerequisites

1. Python 3.7 or higher
2. pip and setuptools installed
3. (Optional) PyPI account for public deployment
4. (Optional) twine for uploading to PyPI

Install required build tools:
```bash
pip install --upgrade pip setuptools wheel twine build
```

## Building the Package

### Option 1: Using pyproject.toml (Recommended - Modern Python)

```bash
# Build the distribution packages
python -m build

# This creates:
# - dist/vibesdk_together-1.0.0-py3-none-any.whl (wheel distribution)
# - dist/vibesdk-together-1.0.0.tar.gz (source distribution)
```

### Option 2: Using setup.py (Traditional)

```bash
# Build source distribution
python setup.py sdist

# Build wheel distribution
python setup.py bdist_wheel

# Or build both
python setup.py sdist bdist_wheel
```

## Local Installation

Test the package locally before deploying:

```bash
# Install from source directory
pip install .

# Or install in editable/development mode
pip install -e .

# Or install from the built wheel
pip install dist/vibesdk_together-1.0.0-py3-none-any.whl
```

## Deployment Options

### Option 1: Deploy to PyPI (Public)

1. **Create PyPI Account** (if you don't have one)
   - Go to https://pypi.org/account/register/

2. **Configure API Token**
   ```bash
   # Create a .pypirc file in your home directory
   cat > ~/.pypirc << EOF
   [pypi]
   username = __token__
   password = pypi-YOUR-API-TOKEN-HERE
   EOF
   
   chmod 600 ~/.pypirc
   ```

3. **Upload to PyPI**
   ```bash
   # Upload using twine
   python -m twine upload dist/*
   
   # Or upload to Test PyPI first (recommended)
   python -m twine upload --repository testpypi dist/*
   ```

4. **Install from PyPI**
   ```bash
   pip install vibesdk-together
   ```

### Option 2: Deploy to GitHub Releases

1. **Create a GitHub Release**
   ```bash
   # Tag the release
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```

2. **Upload Distribution Files**
   - Go to your repository on GitHub
   - Click "Releases" → "Create a new release"
   - Select the tag v1.0.0
   - Upload the files from `dist/` directory
   - Add release notes

3. **Install from GitHub**
   ```bash
   pip install https://github.com/Miguel-Martin-ai/Vibesdktogether/releases/download/v1.0.0/vibesdk_together-1.0.0-py3-none-any.whl
   ```

### Option 3: Deploy as Git Package

Users can install directly from the GitHub repository:

```bash
# Install from main branch
pip install git+https://github.com/Miguel-Martin-ai/Vibesdktogether.git

# Install from specific branch
pip install git+https://github.com/Miguel-Martin-ai/Vibesdktogether.git@copilot/adjust-vibesdk-for-together

# Install from specific tag
pip install git+https://github.com/Miguel-Martin-ai/Vibesdktogether.git@v1.0.0
```

### Option 4: Private Package Repository

For private deployment, you can use:

- **GitHub Packages**: Configure as a Python package repository
- **GitLab Package Registry**: Similar to GitHub Packages
- **AWS CodeArtifact**: Enterprise package management
- **JFrog Artifactory**: Enterprise artifact repository
- **Azure Artifacts**: Azure DevOps package management

## Verification After Deployment

```bash
# Install the package
pip install vibesdk-together

# Test the installation
python -c "from vibesdk_together import TogetherAIProvider; print('✓ Installation successful')"

# Run the examples (requires API key)
export TOGETHER_API_KEY="your-api-key"
python -c "from vibesdk_together import TogetherAIProvider; p = TogetherAIProvider(); print(p.test_connection())"
```

## Quick Deployment Checklist

- [ ] Version updated in `setup.py` and `pyproject.toml`
- [ ] CHANGELOG.md updated (if you create one)
- [ ] All tests passing: `python -m unittest test_vibesdk_together.py -v`
- [ ] Documentation updated
- [ ] Built distributions: `python -m build`
- [ ] Tested local installation: `pip install dist/*.whl`
- [ ] Tagged release: `git tag v1.0.0`
- [ ] Uploaded to PyPI or alternative

## Updating the Package

When releasing a new version:

1. Update version in `setup.py` and `pyproject.toml`
2. Update documentation
3. Run tests
4. Build new distributions
5. Create new git tag
6. Upload to PyPI/your chosen platform

```bash
# Example for version 1.0.1
# 1. Update version numbers in setup.py and pyproject.toml
# 2. Build
python -m build
# 3. Tag
git tag -a v1.0.1 -m "Release version 1.0.1"
git push origin v1.0.1
# 4. Upload
python -m twine upload dist/*
```

## Troubleshooting

### "Package already exists"
If uploading to PyPI and package already exists:
- Increment the version number
- Use a different package name
- Delete old distributions from `dist/` before building

### "Invalid distribution file"
- Make sure you're using `python -m build` or latest setuptools
- Check that MANIFEST.in is properly formatted
- Verify all files referenced exist

### "Import errors after installation"
- Check that `py_modules` in setup.py matches your module name
- Ensure all dependencies are listed in `install_requires`
- Verify Python version compatibility

## Best Practices

1. **Always test locally first** before deploying
2. **Use Test PyPI** before deploying to production PyPI
3. **Version your releases** using semantic versioning (MAJOR.MINOR.PATCH)
4. **Tag your releases** in git for traceability
5. **Keep CHANGELOG** documenting changes between versions
6. **Sign your releases** for security (optional but recommended)

## Additional Resources

- [Python Packaging Guide](https://packaging.python.org/)
- [PyPI Documentation](https://pypi.org/help/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [Semantic Versioning](https://semver.org/)
