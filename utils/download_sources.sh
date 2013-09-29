#!/usr/bin/env bash

SOURCES=$HOME/rpmbuild/SOURCES

download_file() {
  echo "Downloading file $1"
  curl $1 -o $SOURCES/${1##*/}
}

download_file http://www.leptonica.org/source/leptonica-1.69.tar.gz

download_file https://tesseract-ocr.googlecode.com/files/tesseract-ocr-3.02.02.tar.gz

for l in eng rus grc epo_alt ukr tur tha tgl tel tam swe swa srp sqi spa_old spa slv slk ron por pol nor nld msa mlt mkd mal lit lav kor kan ita_old ita isl ind chr hun hrv hin heb glg frm frk fra fin eus est equ epo enm ell deu dan ces cat bul ben bel aze ara afr jpn chi_sim chi_tra vie ; do
  download_file https://tesseract-ocr.googlecode.com/files/tesseract-ocr-3.02.${l}.tar.gz
done
