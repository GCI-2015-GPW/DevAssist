# DevAssist

[![Join the chat at https://gitter.im/GCI-2015-GPW/DevAssist](https://badges.gitter.im/GCI-2015-GPW/DevAssist.svg)](https://gitter.im/GCI-2015-GPW/DevAssist?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

![Build Status](https://travis-ci.org/DarkmatterVale/DevAssist.svg?branch=master)
[![Code Climate](https://codeclimate.com/github/DarkmatterVale/regex4dummies/badges/gpa.svg)](https://codeclimate.com/github/DarkmatterVale/DevAssist)
[![Issue Count](https://codeclimate.com/github/DarkmatterVale/DevAssist/badges/issue_count.svg)](https://codeclimate.com/github/DarkmatterVale/DevAssist)

Your one and only developer assistant

The language might change...Currently it is implemented in Python, but other versions might also be introduced.

## What is DevAssist?

DevAssist is is your personal assistant during and after developing.

There are many features planned, so make sure to check this page actively!

## Here are some things you can do with DevAssist:

- Run Python programs

## Join us!

Want to help? All contributions are encouraged! Want to add a support for another language? Want to fix a bug? Want to add a feature? Fork the repo, add specs, and send a pull request!

Have an awesome idea but are not ready to contribute? Submit an issue on Github with the tag enhancement.

## Getting started

### Installing through Pip

To install via pip:

```
pip install DevAssist
```

### Creating a custom implementation of DevAssist

It is possible to create a custom implementation of DevAssist quite easily. This can be done by manipulating numerous arguments when creating a DevAssist object.

#### Implementing speech recognition:

To implement speech recognition, you will need to add the argument ```speech_adapter``` as an option to DevAssist. The possible recognition libraries you can use (at the moment) are:

- recognize_sphinx

Examples of implementation are:

```
# Using "recognize_sphinx"
my_DevAssist = DevAssist(
  speech_adapter="recognize_sphinx"
)
```

#### Implementing different modules

It is possible to implement only specific modules. Each module accomplishes a unique task. The FileRunner module, for example, allows the user to run files. To pick only specific modules, change the ```modules``` argument passed to DevAssist(), like in the following example:

```
# Using all of the current built-in modules
my_DevAssist = DevAssist(
  modules=[
    "DevAssist.modules.file_runner.FileRunner",
    "DevAssist.modules.run_tests.TestRunner"
  ]
)
```

The current list of available modules:

- FileRunner : This module allows DevAssist to run files
- TestRunner : This module gives DevAssist the ability to run project tests and report back the results.

## License

DevAssist is provided under the MIT license
