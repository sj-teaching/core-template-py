#!/usr/bin/bash

for f in `ls data/test-pa1/Tests/valid*.core`
do
  base=`basename $f '.core'`
  echo '=== Testing ' $base '==='
  python Tokenizer.py $f > /tmp/res
  diff /tmp/res 'data/results/'$base'.txt'
  echo '========================'
done
