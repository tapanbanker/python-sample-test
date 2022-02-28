
# Pre-Requisite
(1) Install Python Verion 3 

- Download and install on your OS https://docs.brew.sh/Homebrew-and-Python

(2) Install Pipenv

```
brew install pyenv
brew install pipenv # if you have brew installed
```
# Python Project Template

Using Python 3.9 version 

## Installation

```
pipenv install --dev
```

## Tests (Run the test)

```
pipenv run test
```

## TO start the application 

Go to the root directory of the project. THen run the followning commands
```
pipenv run hard_math
```

# For example

Run the command PIPENV Install Dev
```
pipenv install --dev
```

Sample Output 
```
Creating a virtualenv for this project...
Pipfile: /Users/mathplus/sourcecode/python-sourcecode/Pipfile
Using /Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9 (3.9.7) to create virtualenv...
⠹ Creating virtual environment...created virtual environment CPython3.9.7.final.0-64 in 816ms
  creator CPython3Posix(dest=/Users/mathplus/.local/share/virtualenvs/python-sourcecode-Wcv-FHDW, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/mathplus/Library/Application Support/virtualenv)
    added seed packages: pip==21.3.1, setuptools==60.2.0, wheel==0.37.1
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

✔ Successfully created virtual environment! 
Virtualenv location: /Users/mathplus/.local/share/virtualenvs/python-sourcecode-Wcv-FHDW
Installing dependencies from Pipfile.lock (cb4e84)...
Looking in indexes: https://pypi.python.org/simple00:00
Ignoring atomicwrites: markers 'sys_platform == "win32"' don't match your environment
Looking in indexes: https://pypi.python.org/simple
Ignoring colorama: markers 'sys_platform == "win32"' don't match your environment
Looking in indexes: https://pypi.python.org/simple:00:04
Ignoring pywin32: markers 'sys_platform == "win32" and platform_python_implementation != "PyPy"' don't match your environment
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 47/47 — 00:00:14
Looking in indexes: https://pypi.python.org/simple
Ignoring typing-extensions: markers 'python_version >= "3.10"' don't match your environment
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```
Run the test command

```
pipenv run test
```
Sample Output
```
pipenv run test 
=================================================================== test session starts ====================================================================
platform darwin -- Python 3.9.7, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /Users/mathplus/sourcecode/python-sourcecode
collected 3 items                                                                                                                                          

test/test_bar.py .                                                                                                                                   [ 33%]
test/test_foo.py ..                                                                                                                                  [100%]

==================================================================== 3 passed in 0.08s =====================================================================
 
```
Building from source
Get a local copy of the repository and navigate to the project directory.

Inside the project directory, run the command below. This will build the image.
```
docker buildx build --platform=linux/amd64 --progress=plain . -t pytest:v1
docker images
```

Tag the Image

 ```
docker tag pytest:v1 tapanbanker/pytest:v1
docker images
 ```
