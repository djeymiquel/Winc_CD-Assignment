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
# Run this workflow whenever something new is pushed.
on: push
jobs:
  run-tests:
    runs-on: ubuntu-20.04
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2
      - name: Install Dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest

      - name: Log in to remote server via SSH
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.HOSTNAME }}
          username: ${{ secrets.USERNAME }}
          key: ${{ secrets.PASS }}
          port: ${{ secrets.PORT }}
          script: |
            echo "Logged in via SSH"
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
to save this modules ina a text file, we can use pip freeze requirements.txt from this file all depenidies can be installed.

*"Run tests":* This step uses a shell command to run "pytest", which runs the tests in the repository.

*"Login to Remote Server via SSH":* appleboy/ssh-action is a GitHub Action that allows you to run SSH commands on a remote server from a GitHub Actions workflow

## Generating SSH key and adding it to the ssh-agent

To login to the remote server without manually entering a passphrase
we need to generate a **SSH** key and add it to the ssh-agent the command for this is in the example below:

### **generate ssh key github in .ssh folder root dir**

```bash:
ssh-keygen -t ed25519 -C "email@example.com"
```

After generating the key we need to copy it to the remote directory
by using this command:

```bash:
ssh-copy-id user@<remote server>
```

the remote server will save this file in the .ssh folder under the name authorized_keys

### **Start ssh-agent**

SSH agent is a program that runs in the background and manages SSH private keys used for authentication when logging into remote servers.

```bash:
eval "$(ssh-agent -s)"
```

### **add ssh key to ssh agent**

this command will add a key to the ssh agent.

```bash:
ssh-add ~/.ssh/id_ed25519 
```

In this assignment i didn't came across alot of difficult issues.
the steps where good to follow for this basic application.
I've learned about yaml config files, generating a ssh key and how to use github repository secrets.
The only part that was a little challenging was the part where i needed to figure out what the correct way was to copy the ssh key into the remote server.
First i tryed to do a normal copy of the ssh key and pasted that into the remote server, it did not work.
So i googled for a solution and came across a video explaining how to copy ssh to the server and it worked !!
