# String Interpolation Experiment
## Overview
Literal string interpolation is a widely-used programming language construct that enables developers to embed variables, expressions, and/or functions within a string. It is consider to be more concise compared to traditional concatenation approach. The syntax of string interpolation can vary significantly between different programming languages. However, its impact on program readability and comprehension remains unexplored. Therefore, the objective of this study is to investigate the effect of literal string interpolation on program readability and comprehension.
## Tool Setup
To replicate the experiment, you can simply follow the steps below to setup the data gathering tool.
### Installation and Usage
1. **Running locally**
   - Setup the  by cloning the repository using `git clone` or download the repository.
   - It is a good practice to configure python virtual environment. Use the commands below to setup python virtual environment on `Linux/MacOS` or `Windows OS`. NB: The tool is designed using `Python 3.10` and tested on `Python 3.8` and `Python 3.9`.
   ```
   # For Linux/MacOS

   python3 -m venv venv
   source venv/bin/activate
   ```
   - For `Window OS` user, the easiest approach is to install `virtualenv` by running `pip install virtualenv`. The next step is pretty much similar to above;
   ```
   # For Window OS

   python3 -m virtualenv venv
   venv\Scripts\activate
   ```
   - Install required dependencies using `pip3 install -r requirements.txt`
   - Start the `experiment` by running `python3 app.py`. Ensure that port `5000` is open on your firewell. To interact with the experiment, go to your browser and type `localhost:5000` or `127.0.0.1:5000`.

2. **Running locally with "Docker for Desktop"**
   - Download and install `Docker fo Desktop` using the [link](https://www.docker.com/products/docker-desktop/). Once you are all set, run the commands below;
   ```
   git clone <project>
   cd /project
   docker compose up -d
   ```
  - That's all 😎!! the tool will be running on port `5000`. To interact with the experiment, go to your browser and type `localhost:5000`. You should be able to see the consent page of the experiment.
