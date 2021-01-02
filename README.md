# vscode-remote-snap

A **development container** is a running [Docker](https://www.docker.com) container with a well-defined tool/runtime stack and its prerequisites. The [VS Code Remote - Containers](https://aka.ms/vscode-remote/download/containers) extension allows you to clone a repository or open any folder mounted into (or already inside) a dev container and take advantage of VS Code's full development feature set.

The well-defined tool/runtime stack in this **VS Code Remote container** is:

- ESA's SNAP EO Toolbox
- SNAP snappy Python bindings
- snapista, a SNAP Python thin layer on top of snappy for creating and running SNAP GPT processing graphs
- Python development support tools such as flake8, black, mypy, etc.

## Installation

To get started, follow these steps:

1. Install and configure [Docker](https://www.docker.com/get-started) for your operating system.

    **Windows / macOS**:

    1. Install [Docker Desktop for Windows/Mac](https://www.docker.com/products/docker-desktop).

    2. Right-click on the Docker task bar item, select **Settings / Preferences** and update **Resources > File Sharing** with any locations your source code is kept. See [tips and tricks](/docs/remote/troubleshooting.md#container-tips) for troubleshooting.

    3. If you are using WSL 2 on Windows, to enable the [Windows WSL 2 back-end](https://aka.ms/vscode-remote/containers/docker-wsl2): Right-click on the Docker taskbar item and select **Settings**. Check **Use the WSL 2 based engine** and verify your distribution is enabled under **Resources > WSL Integration**.

    **Linux**:

    1. Follow the [official install instructions for Docker CE/EE for your distribution](https://docs.docker.com/install/#supported-platforms). If you are using Docker Compose, follow the [Docker Compose directions](https://docs.docker.com/compose/install/) as well.

    2. Add your user to the `docker` group by using a terminal to run: `sudo usermod -aG docker $USER`

    3. Sign out and back in again so your changes take effect.

2. On **Windows** set the environment variable `HOME`

3. Under `$HOME` create two folders: `data` and `results`

4. Install [Visual Studio Code](https://code.visualstudio.com/) 

5. Install the [Remote Development extension pack](https://aka.ms/vscode-remote/download/extension).

6. Run `Remote-Containers: Clone Repository in Container Volume...` from the Command Palette (F1)

7. Add the URL to this git repository: `https://github.com/snap-contrib/vscode-remote-snap.git`

8. Select the Volume mode 

9. Wait a few minutes for the build to complete

## Getting started with EO data

1. Download and extract the Sentinel-1 product S1A_IW_GRDH_1SDV_20201228T170552_20201228T170617_035889_0433FB_D8C7 acquisition to `$HOME/data`

2. Run the `inspect_s1.py` python script

## Interactive Python 

See https://code.visualstudio.com/docs/python/jupyter-support-py to learn about using interactive Python with Visual Studio Code
