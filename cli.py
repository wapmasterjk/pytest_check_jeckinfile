import click
import os
from dotenv import load_dotenv

load_dotenv()

@click.command()
@click.option('--username', prompt='Username', help='Username for login')
@click.option('--password', prompt=True, hide_input=True, help='Password for login')
@click.option('--headless', is_flag=True, help='Run in headless mode')
@click.option('--browser', default='chrome', help='Browser to use')
def run_tests(username, password, headless, browser):
    # Set environment variables
    os.environ['USERNAME'] = username
    os.environ['PASSWORD'] = password
    os.environ['HEADLESS'] = str(headless)
    os.environ['BROWSER'] = browser

    # Run pytest
    import subprocess
    subprocess.run(['pytest'])

if __name__ == '__main__':
    run_tests()