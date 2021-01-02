# vscode-remote-snap

A **development container** is a running [Docker](https://www.docker.com) container with a well-defined tool/runtime stack and its prerequisites. The [VS Code Remote - Containers](https://aka.ms/vscode-remote/download/containers) extension allows you to clone a repository or open any folder mounted into (or already inside) a dev container and take advantage of VS Code's full development feature set.

The well-defined tool/runtime stack in this **VS Code Remote container** is:

- ESA's SNAP EO Toolbox
- SNAP snappy Python bindings
- snapista, a SNAP Python thin layer on top of snappy for creating and running SNAP GPT processing graphs
- Python development support tools such as flake8, black, mypy, etc.
