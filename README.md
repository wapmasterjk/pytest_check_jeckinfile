# Automation Testing Project

This project uses pytest and Selenium for UI automation testing.

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Update .env with your credentials and URL.
3. Run tests: `python cli.py` or `pytest`

## Structure

- `pages/`: Page object classes
- `locators/`: Element locators
- `tests/`: Test files
- `utils/`: Utilities like logger
- `config/`: Configuration
- `reports/`: Allure reports

## Allure Reports

After running tests, generate report: `allure serve reports/allure-results`