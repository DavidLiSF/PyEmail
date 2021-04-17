<p align="center">
  <img src="https://user-images.githubusercontent.com/76184559/108545275-99ce1900-72b5-11eb-913f-baa768335c07.png"/>
</p>

<p align="center">
![Version: v0.1.0](https://img.shields.io/badge/version-v0.1.0-orange)
[![GitHub license](https://img.shields.io/github/license/SFL09/PyEmail)](https://github.com/SFL09/PyEmail/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
</p>

PyEmail is a fast, powerful, and easy-to-use open-source Email tool.

* Integrated [standard libraries](https://docs.python.org/3/library/) to provide a powerfully, user-friendly, and programmatically mail user agent;
* All in a single file with no dependencies other than the [Python Standard Library](https://docs.python.org/3/library/).

## Features
- The defined Email class allows users to set HTML or plain text and reuse the information;
- The defined Server class can automatically manage the connection and send an email.

## Installation
```bash
$ python -m pip install .
```

```bash
$ python setup.py install
```

## Example
```python
from PyEmail import Email, Server

email = Email(subject="My email title.", text="Hello!")
with Server("user@email.com", "password", "domain.org") as server:
    server.send(email, to=["guest@email.com", "vistor@email.com"])
```

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/SFL09/PyEmail/blob/main/LICENSE) file for details.
