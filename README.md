<p align="center">
  <img src="https://user-images.githubusercontent.com/76184559/108545275-99ce1900-72b5-11eb-913f-baa768335c07.png"/>
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

## Example
```python
from PyEmail import Email, Server

email = Email(subject="My email title.", text="Hello!")
with Server("user@email.com", "password", "domain.org") as server:
    server.send(email, to=["guest@email.com", "vistor@email.com"])
```

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/SFL09/PyEmail/blob/main/LICENSE) file for details
