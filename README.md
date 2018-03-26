# IPC 7251-7351 component name generator

A small app to create component name IPC-7251-7351 compliant.
The app uses wx library for graphics and django as a stand-alone app.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Install virtualenv and git for your OS.
create a virtual environment

```
virtualenv venv
```

clone the repo with git:

```
git clone https://github.com/bancaldo/ipcnaming ipcnaming
```

activate the virtualenvironment
#### linux:
```
source ven\bin\activate
```
#### windows:
```
ven\Scripts\activate
```

## Installing

Install the given requirements (django, wx)
```
cd djangosite
pip install -r requirements.txt
```

## Quick start


## Running test

Some tests for ipcnaming app are written in names/tests.py
To run test the command is:
```
python manage.py test --verbosity=2
```

## Running the app
To run the app, launch the scipt ipcnaming/main.py:
```
python main.py
```

### Generate a new component name IPC compliant
Select the type of component. Choices are: 'SMT' or PTH.
Select the description of component in the combobox.
A child frame will open and you can insert the thousand of inches values required.
When all the field are filled, click on Generate button to create the IPC compliant name.

## Licenses

Copyright (c) 2018 Bancaldo
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice,
       this list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright
       notice, this list of conditions and the following disclaimer in the
       documentation and/or other materials provided with the distribution.

    3. Neither the name of Django nor the names of its contributors may be used
       to endorse or promote products derived from this software without
       specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.