
[![Actions Status](https://github.com/yudzhum/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/yudzhum/python-project-50/actions)
![Github Actions Status](https://github.com/yudzhum/python-project-50/actions/workflows/check.yml/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/3c46f84820c6fad359a5/maintainability)](https://codeclimate.com/github/yudzhum/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/3c46f84820c6fad359a5/test_coverage)](https://codeclimate.com/github/yudzhum/python-project-50/test_coverage)

## Command line utility that compares two configuration files and shows a difference.
 - Take configuration files in 2 formats: `json` and `yaml`
 - Show output in formats: `stylish`, `plain` and `json`. Default format: `stylish`

## Usage: 
`gendiff [-h] [-f FORMAT] first_file second_file`

## Setup
 Clone repository\
 `git clone git@github.com:yudzhum/python-project-50.git`\
 Install poetry\
 `make install`\
 Install package\
 `make package-install`\

### Example with plain json files. Formatter 'stylish'
[![asciicast](https://asciinema.org/a/NDAeZuyjDw54TVVtMyfAB7M1Y.svg)](https://asciinema.org/a/NDAeZuyjDw54TVVtMyfAB7M1Y)

### Example with plain yaml files. Formatter 'stylish'
[![asciicast](https://asciinema.org/a/dlAKmycEUojlG7klfzRuqksXB.svg)](https://asciinema.org/a/dlAKmycEUojlG7klfzRuqksXB)

### Example with nested json files. Formatter 'stylish'
[![asciicast](https://asciinema.org/a/9jZoTUeGlj1dGGXvByfcS0MY8.svg)](https://asciinema.org/a/9jZoTUeGlj1dGGXvByfcS0MY8)

### Example with formatter 'plain'
[![asciicast](https://asciinema.org/a/P8UMN7H4Dg6HnoRcjePXqMutJ.svg)](https://asciinema.org/a/P8UMN7H4Dg6HnoRcjePXqMutJ)

### Example with formatter 'json'
[![asciicast](https://asciinema.org/a/qem4mRRgxlxn8rSZL1r48TXz4.svg)](https://asciinema.org/a/qem4mRRgxlxn8rSZL1r48TXz4)
