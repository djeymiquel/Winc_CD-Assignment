# Continuous Deployment

Continuous Deployment is a software development practice where code changes are automatically built, tested, and deployed to production. With GitHub Actions, you can automate the deployment process of your Flask application by defining a workflow in a YAML file. The workflow can include steps to build and test your application, and then deploy it to a server or hosting platform. This way, every time you push changes to your GitHub repository, the workflow will run, and your application will be updated automatically, allowing for a faster and more efficient deployment process.

## Digital ocean Virtual Private Server

*Create a Droplet:* Create a virtual server (Droplet) on DigitalOcean to host the Flask application. Choose the operating system and resources needed, such as the amount of memory and CPU.

*Install required software:* Connect to the Droplet via SSH and install all the necessary software to run the Flask application, such as Python, pip, and any required packages.

*Deploy your Flask app:* Copy the files of the Flask application to the Droplet, by transferring the files directly to the server.

```bash:
scp -r (dir) root@(SERVER_IP):/home/
```

*Set up a Web Server:* To serve the Flask application over the internet, we need to set up a web server such as Nginx or Apache. Configure the web server to forward incoming requests to the Flask application *"reverse proxy"*.

*Start the Flask app:* Finally start the Flask application, by using a process manager like Gunicorn (WSGI).

## GitHub Actions

### Run this workflow whenever something new is pushed

```yaml:
name: Run tests
on: push
jobs:
  run-tests:
    runs-on: ubuntu-20.04
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8.10'
      - name: Install Dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest

      - name: Login to Remote Server
        run: |
          echo "$ASSIGNMENT"
        env:
          ASSIGNMENT: ${{secrets.ASSIGNMENT}}
```

This is a **YAML** file, a human-readable data serialization format commonly used for configuration files. The code above sets up a **Github Actions** workflow named *"run tests"*. The workflow is triggered whenever there is a new push to the repository.

The workflow consists of a single job named *"run-tests"* that runs on an Ubuntu 20.04 virtual environment.

**The job contains the following steps:**

*"Checkout repository":* This step uses the "actions/checkout@v2" Github Actions step to checkout the code in the repository.

*"Setup Python":* This step uses the "actions/setup-python@v2" Github Actions step to setup the specified version of Python (3.8.10) on the virtual environment.

*"Install Dependencies":* This step uses a shell command to run "pip install -r requirements.txt", which installs all the dependencies listed in the requirements.txt file.

```txt
attrs==22.2.0
click==8.1.3
exceptiongroup==1.1.0
Flask==2.2.2
importlib-metadata==6.0.0
iniconfig==2.0.0
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.2
packaging==23.0
pluggy==1.0.0
pytest==7.2.1
tomli==2.0.1
Werkzeug==2.2.2
zipp==3.12.0
```
When working in a python env we install all necessary moduls for our project.
when we use pip freeze we can see all the modules in our envirement.
to have this modules we can use pip freeze requirements.txt to save all the modules in this text file.

*"Run tests":* This step uses a shell command to run "pytest", which runs the tests in the repository.

*"Login to Remote Server (if tests passes)":* This step uses a shell command to print out the value of the "ASSIGNMENT" environment variable. The value of this variable is set from the "secrets.ASSIGNMENT" Github Actions secret, which allows me to store sensitive information, such as passwords or API keys, securely within my Github Actions workflow.

This workflow is set up to perform a basic continuous deployment pipeline: it checks out the code, sets up the environment, installs dependencies, runs tests, and logs into a remote server if the tests pass and updates the code with a pull request from a **.sh** file.

## Generating SSH key and adding it to the ssh-agent

To login to github without login in manually entering a passprase
we need to generate a **SSH** key and add it to the ssh-agent

### **generate ssh key github in .ssh folder root dir**

```bash:
ssh-keygen -t ed25519 -C "email@example.com
```

### **Start ssh-agent**

```bash:
eval "$(ssh-agent -s)"
```

### **add ssh key to ssh agent**

```bash:
ssh-add ~/.ssh/id_ed25519
```
