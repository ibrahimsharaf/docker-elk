#!/bin/bash
FILES=./logs/ariika/*.log
for f in $FILES
do
 nc localhost 5000 < $f
done
