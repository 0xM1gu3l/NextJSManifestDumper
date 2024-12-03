# Next.JS Manifest Dumper

A Simple python script that downloads every JavaScript file that's in a `__BUILD_MANIFEST_` object in a Next.JS website.

This is useful because we can search for api routes or anything else locally and not needing to load the same page a lot of times...

# Setup

Requirements:
- Python >= 3.11
- Network connection

~~So, this script does not dumps the `__BUILD_MANIFEST` by itself, so you'll have to do it by yourself.~~ Good news! Now you just need to put the url and that's it!

Simply:
- Download dependencies if already not using `pip3 install -r requirements.txt`
- Run `main.py`

And that's it! Happy hacking!

TODO List:
- Download main-\*.js and vendor-\*.js files