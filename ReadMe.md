# Foundation Watering

An app for calculating how much time to water a foundation in The Colony, Texas

# Basic Setup

1. If on Windows, set up WSL and open an Ubuntu terminal

2. Create virtual environment
   ```shell
   python3 -m venv venv
   ```
3. Enter virtual environment
   ```shell
   source venv/bin/activate
   ```
4. Install requirements
    ```shell
    pip install -r requirements.txt
    ```

# Gather Data (Ubuntu running venv)

1. Run 
   ```shell
   python3 collect/src/main/app.py
   ```

# Setup - Back End (Ubuntu running venv)

1. Set flask source
   ```shell
   export FLASK_APP=analyze/src/main/app.py
   ```
## Run

2. Run the back end
   ```shell
   flask run --port=8000
   ```

# Setup - Front End

1. Open new Ubuntu terminal and enter venv
	```shell
	source venv/bin/activate
	```
2. Set flask source
	```shell
	export FLASK_APP=src/main/app.py
	```
## Run

3. Run the front end
	```shell
	flask run
	```