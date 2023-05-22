#!/bin/bash
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation version 2.1
# of the License.
#
# Copyright(c) 2023 Huawei Device Co., Ltd.

set -e
cd $1
if [ -d "expat-2.4.1" ];then
    rm -rf expat-2.4.1
fi
tar xvf expat-2.4.1.tar.gz
cd $1/expat-2.4.1
./configure
patch -p1 < $1/backport-CVE-2021-45960.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/backport-CVE-2021-46143.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/backport-CVE-2022-22822-CVE-2022-22823-CVE-2022-22824-CVE-2022-22825-CVE-2022-22826-CVE-2022-22827.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/backport-CVE-2022-23852-lib-Detect-and-prevent-integer-overflow-in-XML_GetBu.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/backport-CVE-2022-23852-tests-Cover-integer-overflow-in-XML_GetBuffer-CVE-20.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/backport-CVE-2022-23990-lib-Prevent-integer-overflow-in-doProlog-CVE-2022-23.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/backport-CVE-2022-25235-lib-Add-missing-validation-of-encoding.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/backport-CVE-2022-25236-lib-Protect-against-malicious-namespace-declarations.patch --fuzz=0 --no-backup-if-mismatch

patch -p1 < $1/backport-CVE-2022-25313-Prevent-stack-exhaustion-in-build_model.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/backport-CVE-2022-25314-Prevent-integer-overflow-in-copyString.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/backport-CVE-2022-25315-Prevent-integer-overflow-in-storeRawNames.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/backport-0001-CVE-2022-40674.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/backport-0002-CVE-2022-40674.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/backport-CVE-2022-43680.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/backport-Fix-build_model-regression.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/backport-lib-Drop-unused-macro-UTF8_GET_NAMING.patch --fuzz=0 --no-backup-if-mismatch


patch -p1 < $1/backport-lib-Fix-harmless-use-of-uninitialized-memory.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/backport-lib-Relax-fix-to-CVE-2022-25236-with-regard-to-RFC-3.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/backport-tests-Cover-CVE-2022-25236.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/backport-tests-Cover-missing-validation-of-encoding.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/backport-tests-Cover-overeager-DTD-destruction-in-XML_Externa.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/backport-tests-Cover-relaxed-fix-to-CVE-2022-25236.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/backport-tests-Protect-against-nested-element-declaration-mod.patch --fuzz=0 --no-backup-if-mismatch
patch -p1 < $1/adapt_previewer_compilation.patch --fuzz=0 --no-backup-if-mismatch

cp -r $1/expat-2.4.1/. $1
cd $1
rm -rf $1/expat-2.4.1
exit 0
