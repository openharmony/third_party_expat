#!/bin/bash
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation version 2.1
# of the License.
#
# Copyright(c) 2023 Huawei Device Co., Ltd.

set -e
if [ "$1" == "" ] || [ "$2" == "" ]; then
    exit 1
fi

if [ -d "$2" ]; then
    rm -rf "$2"
fi

mkdir -p $2

tar zxvf $1/expat-2.4.1.tar.gz -C $2

files=$(ls $1/*.patch)

for filename in $files
do
  filenamebase=$(basename "$filename")
  patch -d $2/expat-2.4.1 -p1 < $1/$filenamebase --fuzz=0 --no-backup-if-mismatch
done
exit 0
