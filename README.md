# mini-devops-project

A small demonstration to show the implementation of the DevOps concepts and tech taught in our DevOps class.

## Steps to use

- Create a conda environment for the project:
  `conda env create -f environment.yml`

- Activate the environment:
  `conda activate mini-devops-project`

- To run the tests (from project root):
  `pytest tests.py`


## Heroku

In order to deploy to Heroku, you'll need a Heroku account and you'll need to install the Heroku-cli on your workstation. 

### Install Heroku client

To do this on Ubuntu, follow these steps (for other OS, check the Heroku documentation):

```bash
curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
heroku --version
```

### Link your heroku-cli to your heroku account

```bash
heroku login
```

### Create a token using the heroku-cli

You'll need to add this to your Github secrets.

```bash
heroku auth:token
```
