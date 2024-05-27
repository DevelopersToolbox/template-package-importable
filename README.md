<!-- markdownlint-disable -->
<p align="center">
    <a href="https://github.com/DevelopersToolbox/">
        <img src="https://cdn.wolfsoftware.com/assets/images/github/organisations/developerstoolbox/black-and-white-circle-256.png" alt="DevelopersToolbox logo" />
    </a>
    <br />
    <a href="https://github.com/DevelopersToolbox/template-package-importable/actions/workflows/cicd.yml">
        <img src="https://img.shields.io/github/actions/workflow/status/DevelopersToolbox/template-package-importable/cicd.yml?branch=master&label=build%20status&style=for-the-badge" alt="Github Build Status" />
    </a>
    <a href="https://github.com/DevelopersToolbox/template-package-importable/blob/master/LICENSE.md">
        <img src="https://img.shields.io/github/license/DevelopersToolbox/template-package-importable?color=blue&label=License&style=for-the-badge" alt="License">
    </a>
    <a href="https://github.com/DevelopersToolbox/template-package-importable">
        <img src="https://img.shields.io/github/created-at/DevelopersToolbox/template-package-importable?color=blue&label=Created&style=for-the-badge" alt="Created">
    </a>
    <br />
    <a href="https://github.com/DevelopersToolbox/template-package-importable/releases/latest">
        <img src="https://img.shields.io/github/v/release/DevelopersToolbox/template-package-importable?color=blue&label=Latest%20Release&style=for-the-badge" alt="Release">
    </a>
    <a href="https://github.com/DevelopersToolbox/template-package-importable/releases/latest">
        <img src="https://img.shields.io/github/release-date/DevelopersToolbox/template-package-importable?color=blue&label=Released&style=for-the-badge" alt="Released">
    </a>
    <a href="https://github.com/DevelopersToolbox/template-package-importable/releases/latest">
        <img src="https://img.shields.io/github/commits-since/DevelopersToolbox/template-package-importable/latest.svg?color=blue&style=for-the-badge" alt="Commits since release">
    </a>
    <br />
    <a href="https://github.com/DevelopersToolbox/template-package-importable/blob/master/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Code%20of%20Conduct-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/DevelopersToolbox/template-package-importable/blob/master/.github/CONTRIBUTING.md">
        <img src="https://img.shields.io/badge/Contributing-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/DevelopersToolbox/template-package-importable/blob/master/.github/SECURITY.md">
        <img src="https://img.shields.io/badge/Report%20Security%20Concern-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/DevelopersToolbox/template-package-importable/issues">
        <img src="https://img.shields.io/badge/Get%20Support-blue?style=for-the-badge" />
    </a>
</p>

## Overview

This is the package template that we use internally when creating new python based importable packages. It has all of the basic functionality and workflows needed to create,
build and publish new package to [PyPI](https://pypi.org/).

This package template does NOT provide any cli functionality but instead is designed for creating importable packages.

We decided to make this available along with our other tools to allow people to use a well engineered starting point when creating their own tools.

We also provide 2 other templates which we use.

- [template python project](https://github.com/DevelopersToolbox/template-python-project)
- [template package cli](https://github.com/DevelopersToolbox/template-package-cli)

## Features

- **Modular Architecture**: Organize your code into modules for better maintainability.
- **Custom Exceptions**: BAsic examples for implementing custom exceptions for specific error handling.
- **Testing Examples**: Basic examples for writing pytest tests for your package.

## Installation

To install the importable package, clone the repository and navigate to the project directory:

```bash
git clone https://github.com/DevelopersToolbox/template-package-importable.git
cd template-package-importable
```

It is recommended to use a virtual environment to manage dependencies. You can create and activate a virtual environment using the following commands:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Project Structure

The project is organized as follows:

```sh
template-package-importable/
├── wolfsoftware/
│   └── template_package_importable/
│       ├── __init__.py
│       ├── exceptions.py
│       └── functions.py
├── tests/
│   ├── __init__.py
│   └── test_template_package_importable.py
├── README.md
├── setup.py
└── requirements.txt
```

- `wolfsoftware/template_package_importable`: Contains the core modules of the application.
  - `exceptions.py`: Handles custom exceptions.
  - `functions.py`: Defines some example functions (for testing).
- `tests`: Where the pytest tests are located.
  - `test_template_package_importable.py`: The specific tests to run.
- `setup.py`: The package configuration.
- `requirements.txt`: Lists the dependencies required for the project.
- `README.md`: The file you are currently reading.

<br />
<p align="right"><a href="https://wolfsoftware.com/"><img src="https://img.shields.io/badge/Created%20by%20Wolf%20on%20behalf%20of%20Wolf%20Software-blue?style=for-the-badge" /></a></p>
