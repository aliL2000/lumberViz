## Hi there!

I've included some installation instructions below, feel free to contact me if there are any issues:

Run the below lines on a terminal that is located within the repository, I'd recommend doing this terminal integrated into an IDE (such as VSCode). 

These are the setup instructions to create a Python virtual environment, install pre-requisite packages/frameworks:
- `python3 -m venv .venv`/`python -m venv .venv` (**Pre-requisite**: Python 3.0+ must be installed on your system)
- `.venv\Scripts\activate` (Activates the virtual environment for development)
- `pip install -r requirements.txt` (Finds and installs all dependencies needed to run the site on the virtual environment)
- **NOTE**: If you want to deactive the virtual env (venv, for short) just type `deactivate` in the terminal. 

Nice job! To get the actual site up and running, run this line of code below in the venv terminal:
- `flask --app main.py run`/`flask --app main.py --debug run` (The debug option is useful in case you'd like to print out output and check objects)
- Navigate to this [link](http://127.0.0.1:5000/), and get started!
- Hit `Ctrl+C` to exit the website server and go back to the terminal.

Let me know if the instructions are unclear, and I can try to clarify what's happening!

The screenshot for the FE is named **fe_screenshot.jpg**, and shows you a preview of what the user will see.