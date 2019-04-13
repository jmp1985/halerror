# halerror
> The best python exception library

![GitHub](https://img.shields.io/github/license/jmp1985/halerror.svg)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
[![Travis (.org)](https://img.shields.io/travis/jmp1985/halerror.svg)](https://travis-ci.org/jmp1985/halerror)
[![Codecov](https://img.shields.io/codecov/c/github/jmp1985/halerror.svg)](https://codecov.io/gh/jmp1985/halerror)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/jmp1985/halerror.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/jmp1985/halerror/context:python)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/jmp1985/halerror.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/jmp1985/halerror/alerts/)
[![Documentation Status](https://readthedocs.org/projects/halerror/badge/?version=latest)](https://halerror.readthedocs.io/en/latest/?badge=latest)

This python library implements a sci-fi exception class!

## Installation

```sh
pip install halerror
```

## Usage example

The exception class can be used as follows.

```python
from halerror import HalError

raise HalError("Open the pod bay doors HAL")
```

This will result in the following error output, where ${NAME} is the username of the person running the software.

```sh
halerror.HalError: 

I'm sorry, ${NAME}. I'm afraid I can't do that.

Open the pod bay doors, HAL.
```

## Release History

* 0.1.0
  * The first release


