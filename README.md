# Calculator using PLY (Python Lex-Yacc)

This project contains a simple calculator implemented in Python using the **PLY** (Python Lex-Yacc) library. Follow the steps below to set up a Python environment, install the required dependencies, and run the program.

## Prerequisites

- **Python 3.x** installed on your machine. You can download Python [here](https://www.python.org/downloads/).

## Step 1: Set Up a Python Virtual Environment

It's recommended to create a virtual environment to manage dependencies for this project. Here's how you can set one up:

1. **Open a terminal (or command prompt)** and navigate to the directory where the project is located.

2. **Create a virtual environment** by running the following command:

    ```bash
    python -m venv myenv
    ```

    This will create a new directory named `myenv` which will contain your virtual environment.

3. **Activate the virtual environment**:

    - On **Windows**:

        ```bash
        myenv\Scripts\activate
        ```

    - On **macOS/Linux**:

        ```bash
        source myenv/bin/activate
        ```

    Once activated, your terminal should show the name of the environment, indicating that the virtual environment is active.
	You can also run the file EnvironmentTest.py to check if you are operating within a Python environment. If the output is True, it confirms that you are in a Python environment.

## Step 2: Install PLY Library

With the virtual environment activated, you can install the **PLY** library, which is required for this project.

1. Run the following command to install PLY:

    ```bash
    pip install ply
    ```

    This will install the **PLY** library into your virtual environment.

## Step 3: Run the Python File

After setting up the environment and installing the dependencies, you can run the `CalculatorPLY.py` file.

1. **Make sure your virtual environment is activated**. If it's not activated, follow the steps in **Step 1** to activate it again.

2. Run the `CalculatorPLY.py` file using the Python interpreter:

    ```bash
    python CalculatorPLY.py
    ```

    This will execute the program and output the results of the calculator.

## Deactivating the Virtual Environment

Once you're done, you can deactivate the virtual environment by running:

```bash
deactivate
