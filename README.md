# g-brief IBAN/BIC
- http://www.mrunix.de/forums/archive/index.php/t-50142.html
g-brief2: http://kambing.ui.ac.id/ctan/macros/latex/contrib/g-brief/g-brief.pdf

# Python 3.6 static binary
- via https://stackoverflow.com/questions/39913847/is-there-a-way-to-compile-python-application-into-static-binary
- Given: Python 3.6 virtualenv via pyenv/pyenv-virtualenv
- http://cx-freeze.readthedocs.io/en/latest/script.html#script

```
cxfreeze 2pdf.py --target-dir dist

./build
./shell
```
