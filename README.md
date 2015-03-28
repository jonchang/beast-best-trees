# Get the best N trees from a BEAST treelog based on posterior probability

Sometimes you need to get a sample of the best trees from a BEAST 1.x treelog. This script will help you do that.

## Installation

```
pip install git+https://github.com/jonchang/best-trees.git
```

## Usage

```
best_trees benchmark2.trees --max-trees=20 --output=best_20.trees
```

You can find `benchmark2.trees` in the `examples/` folder of the BEAST download.

## Caveats

In the interest of speed, this script doesn't do any parsing of the treelog, so it assumes a certain format that might not hold true for other versions of BEAST or other treelog formats.

## Developing

```
git clone https://github.com/jonchang/best-trees.git
cd best-trees
virtualenv env
source env/bin/activate
./setup.py develop
```

## License

This software is licensed under the [GNU Affero GPL](http://choosealicense.com/licenses/agpl-3.0/). For more information, see the `LICENSE` file.

## References

* [BEAST software](http://beast.bio.ed.ac.uk/)
