## Contributing to SerpentScribe

First off, thank you for considering contributing to serpentscribe! It's people like you that make the open source community such a great place to learn, inspire, and create. Here are some guidelines we'd like you to follow so we can keep the project as effective as possible.

## Getting Started

Before you begin:
- Ensure you have installed the latest version of Python.
- Check if an issue already exists for your question/bug/feature request.

## Making Changes

Here's a quick guide to contributing:
1. Fork the repository.
2. Clone your fork to your local machine.
3. Create a new branch for your changes.
4. Make your changes.
5. Run the tests to ensure your changes don't break existing functionality.
6. Commit your changes with a clear and detailed commit message.
7. Push your changes to your fork.
8. Submit a pull request to the `serpentscribe` repository.

## Pull Request Guidelines

- **Title**: Use a descriptive title that indicates the purpose of your pull request.
- **Description**: Provide a detailed description of your changes. Include any relevant issue numbers.
- **Commits**: Each commit should add a clear change or fix. Large changes should be broken into smaller commits.

Commit messages should be similar in description to the following:
```text
Enhance logging functionality and update package…

DESCRIPTION

This commit extends the functionality of the SerpentScribe decorator to include flexible configuration of log level, optional logging to a specified file path, and expanded documentation on usage. Detailed descriptions for each supported log level have been added to the README.

This also modifies the project's version number in setup.py from '0.1' to '0.2' and refines the package's short description text.

Notable changes:
- The decorator now requires a log level ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL").
- File logging can be optionally enabled by providing a file path.
- Each function invocation will continue to output logs to stdout.
- Readme has been enriched with explanatory information about features and usage.
```

- **Testing**: Add any new tests necessary to cover the changes made.

## Reporting Bugs

When reporting bugs, include as much information as possible, such as:
- The version of Python you're using
- Any relevant error messages or logs
- Steps to reproduce the issue

## Feature Requests

We love to hear about new features! But first, check if it's already been suggested or planned. If not, provide as much detail as possible about the feature and how it would benefit the project.

## Code of Conduct

We expect all contributors to adhere to our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it before participating.

## Questions?

If you have any questions, feel free to create an issue in the repository with your question.

Thank you for contributing to `SerpentScribe`!
