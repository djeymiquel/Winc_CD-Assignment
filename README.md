# Continuous Deployment

Continuous Deployment is a software development practice where code changes are automatically built, tested, and deployed to production. With GitHub Actions, you can automate the deployment process of your Flask application by defining a workflow in a YAML file. The workflow can include steps to build and test your application, and then deploy it to a server or hosting platform. This way, every time you push changes to your GitHub repository, the workflow will run, and your application will be updated automatically, allowing for a faster and more efficient deployment process.

## Digital ocean Virtual Private Server

Create a Droplet: I started by creating a virtual server (Droplet) on DigitalOcean to host my Flask application. Choose the operating system and resources i needed, such as the amount of memory and CPU.

Then i connected to the Droplet via SSH and install all the necessary software to run my Flask application, such as Python, pip, and any required packages.

Then i Copied the files of my Flask application to the Droplet, by using transferring the files directly to the server.

```{
scp -r (dir) root@(SERVER_IP):/home/
```

Set up a Web Server: To serve my Flask application over the internet, i need to set up a web server such as Nginx or Apache. Configure the web server to forward incoming requests to my Flask application.

Start the Flask app: Finally, start my Flask application, by using a process manager like Gunicorn (WSGI).
