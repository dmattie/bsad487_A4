# Assignment 4 - Creating a StFX focused Chat-GPT

This assignment shows you how easy it is to use OpenAI's GPT-3 API on your own documents.  The GPT-3 language model was trained how to speak in 2021 using content in the world at that time.   It has been two years and a few things have changed at StFX.  We want to create our own GPT-3 chaptbot, but teach it about the new material at StFX.  Specifically, we want it to know about Schwartz programming.  

To begin this assignment, you will need to have the following:

* **Python 3** and pip installed on your laptop.With Python 3 and Pip installed
* **Git** software must be installed (installed already on most mac/linux machines)  [Learn more here](https://github.com/git-guides/install-git).
* A free **GitHub** account (github.com)

## Step 1: Create a python virtual environment (Optional but encouraged)

You can learn more about python virtual environments [here] (https://docs.python.org/3/library/venv.html), but basically, you are going to install some 3rd part libraries and typically wouldn't want to conflict with other projects you are working on, so you create a virtual environment (like a sandbox) where these packages will be installed:

Let's create a virtual environment in your home directory:

    mkdir -p ~/environments
    python -m venv ~/environments/bsad487Assignment4
    source ~/environments/bsad487Assignment4/bin/activate

## Step 2: Get a developer personal access token for Git.

In order to login to your Git account from the command line terminal, you will need a personal access token generated on GitHub - this is basically a time-limited password.  You can find a [tutorial here] (https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-to-create-a-GitHub-Personal-Access-Token-example).  Copy that password somewhere safe and easy to access - you will need to use it a few times.