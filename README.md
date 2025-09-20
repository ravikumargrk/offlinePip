# offlinePip
Download pip packages offline by platform-config to install later

Note: This is WIP

1. In host, copy this file and run using python3 to generate config: github.com/ravikumargrk/offlinePip/generateHostConfig.py
2. You can download complete binary wheels using this command for host in remote system with internet access
```shell
set PIP_CONFIG_FILE=%cd%\pip_config.ini
pip download ollama --only-binary=:all:
```
Or you may download with no dependencies (Not really useful)
```shell
set PIP_CONFIG_FILE=%cd%\pip_config.ini
pip download ollama --no-deps
```
3. Copy wheels to host system and install using this command:
```shell
pip install --no-index --find-links=. ollama
```
4. Try to get numpy/pandas like this. Note: fix versions for better success:
```shell
pip install --no-index --find-links=. ollama==0.6.3
```
This did not work for chromadb as their dependencies could not all be in binaries
So we need a method to download binaries or pure python modules, building from source is to be avoided completely because that does not work

