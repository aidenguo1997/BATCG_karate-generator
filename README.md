
# Karate Automation Framework

This project demonstrates the use of a Karate-based framework for testing REST APIs using Gherkin syntax. The framework is designed to parse Gherkin feature files and Swagger/OpenAPI definitions, generate Karate test scripts, and execute them.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Features](#features)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Overview

The `Karate Automation Framework` is a Java-based testing framework that integrates with Gherkin and Swagger/OpenAPI specifications to generate and run API tests. It supports converting Gherkin scenarios into Karate scripts that can be executed against API endpoints defined in the Swagger/OpenAPI documentation.

## Project Structure

- `Main.java`: The entry point of the application that orchestrates the conversion process from Gherkin to Karate.
- `KarateFileGenerator.java`: Responsible for reading Gherkin files, parsing Swagger/OpenAPI definitions, generating Karate scripts, and writing them to files.
- `KarateElementGenerator.java`: Handles the generation of Karate scripts for both background and scenario sections based on the provided Gherkin content and Swagger/OpenAPI paths.
- `RequestDataHandler.java`: Manages the mapping between request data and API paths/methods.
- `ParametersHandler.java`: Processes and formats request parameters (JSON or Form URL-encoded) into Karate-compatible scripts.
- `DataTablesHandler.java`: Generates the data tables required for parameterized testing in Karate.
- `OperationHandler.java`: Handles the core operations for transforming Gherkin and Swagger data into executable Karate scripts.
- `GherkinTag.java`: Manages the tagging and session handling within Gherkin scripts.

## Usage

To use the framework:

1. Ensure that the Gherkin feature files, Swagger/OpenAPI specifications, and request data files are available at the specified paths.
2. Run the `Main.java` class, which triggers the conversion process.
3. The generated Karate scripts will be saved in the specified output directory, ready for execution.

### Example Command:

```sh
java -cp your-jar-file.jar com.ntousoselab.karate.Main
```

## Features

- **Gherkin to Karate Conversion**: Automatically converts Gherkin feature files into executable Karate scripts.
- **Swagger/OpenAPI Integration**: Parses Swagger/OpenAPI definitions to validate and generate accurate API test cases.
- **Dynamic Request Handling**: Supports both JSON and Form URL-encoded request formats.
- **Data-Driven Testing**: Facilitates data-driven testing by generating data tables for multiple test scenarios.

## Requirements

- Java 8 or higher
- Maven or Gradle for dependency management
- Gherkin feature files
- Swagger/OpenAPI specifications

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
