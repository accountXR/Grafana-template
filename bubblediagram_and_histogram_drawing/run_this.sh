#!/bin/bash
python read_mysql.py
cd bubble/
Rscript bubble.R
cd ../histogram/
Rscript histogram.R
