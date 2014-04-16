#!/bin/bash

echo "Converting Markdown to TeX..."
SECTIONS="./sections/*.md"

for f in $SECTIONS
do
    echo "Processing $f"
    pandoc $f -o ${f%.md}.tex
done

echo "Producing PDF..."
pdflatex paper.tex
pdflatex paper.tex

echo "Cleaning up..."
rm -f *.aux
rm -f *.log
rm -f *.toc
rm ./sections/*.tex