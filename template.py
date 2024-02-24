import os  # Importing the OS module to interact with the operating system.
from pathlib import Path  # Importing Path from pathlib for easy path manipulations.
import logging  # Importing the logging module for logging functionality.


list_of_files = [  # Creating a list of file and directory paths relevant to the MLOps project.
    ".github/workfiles/.gitkeep",  # GitHub Actions or workflows directory for CI/CD automation.
    "src/__init__.py",  # Marks the src directory as a Python package.
    "src/components/__init__.py",  # Marks the components directory as a Python package.
    "src/components/data_ingestion.py",  # Script for data ingestion processes.
    "src/components/data_transformation.py",  # Script for data transformation or preprocessing.
    "src/components/model_trainer.py",  # Script for training the machine learning model.
    "src/components/model_evaluation.py",  # Script for evaluating the trained model's performance.
    "src/pipeline/__init__.py",  # Marks the pipeline directory as a Python package.
    "src/pipeline/training_pipeline.py",  # Script for defining the training pipeline.
    "src/pipeline/prediction_pipeline.py",  # Script for defining the prediction or inference pipeline.
    "src/utils/utils.py",  # Utilities or helper functions used across the project.
    "src/logger/logging.py",
    "src/exception/exception",
    "tests/unit/__init__.py",  # Marks the unit tests directory as a Python package.
    "tests/integration/__init__.py",  # Marks the integration tests directory as a Python package.
    "init_setup.sh",  # Shell script for initial project setup (e.g., environment setup).
    "requirements.txt",  # Specifies the Python dependencies for production.
    "requirements_dev.txt",  # Specifies the Python dependencies for development (includes testing libraries, etc.).
    "setup.py",  # Setup script for installing the project package.
    "setup.cfg",  # Configuration file for the setup.py script.
    "pyproject.toml",  # Specifies build system requirements for the Python project.
    "tox.ini",  # Configuration file for Tox, a tool for automating testing in multiple environments.
    "experiment/experiments.ipynb"  # Jupyter notebook for experimental code, data analysis, and exploration.
]

for filepath in list_of_files:
    filepath = Path(filepath)  # Convert the filepath to a Path object for easier manipulation.
    filedir, filename = os.path.split(filepath)  # Split the filepath into directory and filename.
    
    if filedir != "":  # If the directory is not empty.
        os.makedirs(filedir, exist_ok=True)  # Create the directory if it doesn't exist.
        logging.info(f"Creating directory: {filedir} for file: {filename}")  # Log the creation of the directory.
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):  # If the file doesn't exist or is empty.
        with open(filepath, "w") as f:  # Open the file in write mode.
            pass  # Do nothing, effectively creating an empty file.
