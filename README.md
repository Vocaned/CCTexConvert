# CCTexConvert

Convert Minecraft 1.12.2 texture packs into ClassiCube texture packs

## Installation

Install [Python 3](https://www.python.org/downloads/)

Run

```
pip install cctexconvert
```

or compile from source by running

```
git clone https://github.com/Fam0r/CCTexConvert
cd CCTexConvert
python setup.py
```

## Usage

Use `cctexconvert -h` to see list of all possible commands

Example:

```
cctexconvert Faithful.zip
```

creates a file called Faithful.cc.zip which contains the converted textures.

## Progress:

- [x] Partial 1.12.2 support
- [ ] Support classic's wool colours
- [ ] Animation support
- [ ] Extended blocksets (venk's, redux etc.)
- [ ] Support more versions