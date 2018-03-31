#!/usr/bin/env python
import logging
import os
import subprocess
import sys
import tempfile

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('2pdf')

TMPDIR = tempfile.mkdtemp()

infile = sys.argv[1]

log.info(f'infile={infile}')


try:
    result = subprocess.run(
        ['pdflatex', '-halt-on-error', f'-output-directory={TMPDIR}', infile],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=30,
    )
    log = result.stdout.decode('utf-8')
    basename = '.'.join(infile.split('.')[:-1])
    outfile = os.path.join(TMPDIR, f'{basename}.pdf')
    with open(outfile, 'rb') as f:
        pdf = f.read()
    print('OK. got log and pdf.')
except subprocess.TimeoutExpired as e:
    print(e.stdout.decode('utf-8'))
    raise
except subprocess.CalledProcessError as e:
    print(e.stdout.decode('utf-8'))
    raise
