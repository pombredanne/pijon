# pijon :bird:

A json migration tool available through both a Python library and tool script.


## Getting started

### Requirements

* Python >= 3.5

### Installation

```bash
pip install pijon
```


## Usage

### Script tool

The client gives you access to a powerful set of commands aimed to handle your migrations.

Here is a simple example:
```bash
pijon migrate input.json output.json
```

Basic commands are:
* `new` to generate a new migration file with a simple template.
* `list` to fetch the list of available migrations.
* `migrate` to perform the migrations.

See `pijon --help` for more details (for instance, how to select a specific migration target).

### Library API

Here is the same example as above using the Python API:
```python
import pijon
pijon.migrate({'my key': 'my value'})
```
