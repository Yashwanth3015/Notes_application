# UI + API Hybrid Automation – ExpandTesting Notes App

## Project Overview

This project is a Hybrid Test Automation Framework developed for the ExpandTesting Notes Application.  
The framework combines:

* UI Automation using Selenium WebDriver
* API Automation using Python Requests
* Hybrid End-to-End Validation
* Parallel Execution using Pytest-xdist
* Reporting using Allure Reports
* CI/CD Integration using Jenkins

The framework follows the Page Object Model (POM) design pattern for better maintainability and scalability.

\---

# Objectives

* Automate UI functionalities of Notes Application
* Validate API endpoints and responses
* Perform Hybrid UI + API synchronization testing
* Improve execution speed using parallel testing
* Generate professional reports using Allure
* Integrate automation with Jenkins CI/CD pipeline

\---

# Tech Stack

|Technology|Purpose|
|-|-|
|Python|Programming Language|
|Selenium WebDriver|UI Automation|
|Pytest|Test Framework|
|Requests|API Testing|
|Allure Reports|Reporting|
|Jenkins|CI/CD Integration|
|Pytest-xdist|Parallel Execution|
|WebDriver Manager|Browser Driver Management|

\---

# Framework Architecture

```text
Project Root

│

├── api/

│   └── api\_client.py

│

├── pages/

│   ├── base\_page.py

│   ├── home\_page.py

│   ├── login\_page.py

│   └── notes\_page.py

│

├── tests/

│   ├── api/

│   ├── hybrid/

│   ├── negative/

│   └── ui/

│

├── utils/

│   ├── config.py

│   ├── logger.py

│   └── retry.py

│

├── reports/

├── screenshots/

├── logs/

├── README.md

├── docker-compose.yml

├── Jenkinsfile

├── requirements.txt

└── pytest.ini

\---

# Features Covered

## UI Testing

* Valid Login
* Invalid Login
* Create Note
* Empty Title Validation
* Duplicate Note Validation
* Instant Note Visibility
* Logout Functionality

## API Testing

* GET Notes API
* DELETE Notes API
* Invalid Token Validation
* Missing Fields Validation
* Invalid Endpoint Validation
* API Response Time Validation

## Hybrid Testing

* UI to API Consistency
* API to UI Synchronization
* End-to-End Full Cycle Validation

\---

# Page Object Model (POM)

The framework follows the Page Object Model design pattern.

# BasePage

`BasePage` contains reusable Selenium methods:

* click()
* enter\_text()
* get\_text()
* is\_visible()

All page classes inherit from BasePage.

\---

# API Client

`APIClient` centralizes reusable API methods:

* Token generation
* GET notes
* Create note
* Delete note

Authentication token is generated automatically using constructor.

\---

# Parallel Execution

Framework uses:

```bash
pytest -n 2
```

Benefits:

* Faster execution
* Reduced execution time
* Better resource utilization

\---

# Reporting

Allure Reports are used for:

* Test execution visualization
* Failure analysis
* Screenshots
* Logs
* Execution trends

Generate report:

```bash
allure serve allure-results
```

\---

# Jenkins Integration

The project is integrated with Jenkins CI/CD pipeline.

## Jenkins Stages

1. Checkout Source Code
2. Install Dependencies
3. Execute Tests
4. Generate Allure Report
5. Archive Reports

\---

# Docker Integration

Docker is used to containerize the automation framework for consistent execution across environments.

## Docker Benefits

* Environment consistency
* Easy dependency management
* Portable execution
* Simplified setup process
* CI/CD friendly execution

\---

# Test Execution

Run all tests:

```bash
pytest -v
```

Run parallel execution:

```bash
pytest -n 2
```

Run with Allure:

```bash
pytest --alluredir=allure-results
```

\---

# Assertions Used

Assertions are used to validate:

* Successful login
* Note creation
* API responses
* Synchronization
* Error handling

\---

# Logging

Logging is implemented for:

* Click actions
* Text entry
* Debugging
* Failure analysis



