# Run this in host system with python3 installed, to generate config that can be later used to get packages online
import sysconfig
import platform
import os

def generate_pip_config():
    # Get tags
    python_version = platform.python_version()
    implementation = platform.python_implementation().lower()  # 'cpython', 'pypy', etc.
    abitag = sysconfig.get_config_var("SOABI")  # like 'cpython-39-x86_64-linux-gnu'
    plat = sysconfig.get_platform()             # like 'win_amd64' or 'manylinux2014_x86_64'

    # Print to console
    print("Python version:", python_version)
    print("Implementation:", implementation)
    print("ABI:", abitag)
    print("Platform:", plat)

    # Pip options (configurable)
    config_content = f"""[global]
python-version = {python_version}
implementation = {implementation}
abi = {abitag}
platform = {plat}
"""

    # Windows user-level pip.ini location
    pip_config_path = 'pip_config.ini'

    with open(pip_config_path, "w") as f:
        f.write(config_content)

    print(f"\n✅ Config written to {pip_config_path}")

if __name__ == "__main__":
    generate_pip_config()
