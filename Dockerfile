FROM ubuntu:16.04

RUN apt-get --yes update \
      && apt-get --yes install texlive texlive-latex-extra texlive-lang-german \
      && rm -rf /var/lib/apt/lists/*


COPY 2pdf /usr/local/bin
RUN chmod 775 /usr/local/bin/2pdf

COPY dist /foo
