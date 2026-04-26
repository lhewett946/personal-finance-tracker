# Personal Finances Tracker

This application is used to keep track of my personal finances and my investment portfolio

# Getting Started

I am using Debian inside WSL2 for development. The below instructions assume that you have set up Git, but cover everything else needed to get up and running with the project.

## Install Python and pip
```
sudo apt install python3 python3-pip
```

## Set up a Python venv with the required dependencies
```
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Install common libraries required by PySide6
```
sudo apt install \
  libgl1 \
  libxkbcommon0 \
  libxkbcommon-x11-0 \
  libegl1 \
  libglib2.0-0 \
  libxcb-cursor0 \
  libxcb-shape0 \
  libwayland-cursor0
```

## Run the app
```
python3 app.py
```