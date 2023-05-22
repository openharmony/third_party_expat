%define Rversion %(echo %{version} | sed -e 's/\\./_/g' -e 's/^/R_/')
Name:           expat
Version:        2.4.1
Release:        8
Summary:        An XML parser library
License:        MIT
URL:            https://libexpat.github.io/
Source0:        https://github.com/libexpat/libexpat/releases/download/%{Rversion}/expat-%{version}.tar.gz

Patch0:         backport-CVE-2021-45960.patch
Patch1:         backport-CVE-2021-46143.patch
Patch2:         backport-CVE-2022-22822-CVE-2022-22823-CVE-2022-22824-CVE-2022-22825-CVE-2022-22826-CVE-2022-22827.patch
Patch3:         backport-CVE-2022-23852-lib-Detect-and-prevent-integer-overflow-in-XML_GetBu.patch
Patch4:         backport-CVE-2022-23852-tests-Cover-integer-overflow-in-XML_GetBuffer-CVE-20.patch
Patch5:         backport-CVE-2022-23990-lib-Prevent-integer-overflow-in-doProlog-CVE-2022-23.patch
Patch6:         backport-CVE-2022-25235-lib-Add-missing-validation-of-encoding.patch
Patch7:         backport-tests-Cover-missing-validation-of-encoding.patch
Patch8:         backport-CVE-2022-25236-lib-Protect-against-malicious-namespace-declarations.patch
Patch9:         backport-tests-Cover-CVE-2022-25236.patch
Patch10:        backport-CVE-2022-25313-Prevent-stack-exhaustion-in-build_model.patch
Patch11:        backport-CVE-2022-25314-Prevent-integer-overflow-in-copyString.patch
Patch12:        backport-CVE-2022-25315-Prevent-integer-overflow-in-storeRawNames.patch
Patch13:        backport-Fix-build_model-regression.patch
Patch14:        backport-tests-Protect-against-nested-element-declaration-mod.patch
Patch15:        backport-lib-Fix-harmless-use-of-uninitialized-memory.patch
Patch16:        backport-lib-Drop-unused-macro-UTF8_GET_NAMING.patch
Patch17:        backport-lib-Relax-fix-to-CVE-2022-25236-with-regard-to-RFC-3.patch
Patch18:        backport-tests-Cover-relaxed-fix-to-CVE-2022-25236.patch
Patch19:        backport-0001-CVE-2022-40674.patch
Patch20:        backport-0002-CVE-2022-40674.patch
Patch21:        backport-CVE-2022-43680.patch
Patch22:        backport-tests-Cover-overeager-DTD-destruction-in-XML_Externa.patch

BuildRequires:  sed,autoconf,automake,gcc-c++,libtool,xmlto

%description
expat is a stream-oriented XML parser library written in C.
expat excels with files too large to fit RAM, and where
performance and flexibility are crucial.

%package devel
Summary:        Development files
Requires:       %{name} = %{version}-%{release}
%description devel
This package provides with static libraries and  header files for developing with expat.

%package_help

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure CFLAGS="$RPM_OPT_FLAGS -fPIC" DOCBOOK_TO_MAN="xmlto man --skip-validation"
%make_build

%install
%makeinstall
find %{buildroot} -type f -name changelog -delete

%check
make check

%ldconfig_scriptlets

%files
%defattr(-,root,root)
%license COPYING AUTHORS
%{_bindir}/*
%{_libdir}/libexpat.so.1*
%exclude %{_docdir}/%{name}/AUTHORS

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/{libexpat.*a,libexpat.so}
%{_libdir}/cmake/expat-%{version}
%{_libdir}/pkgconfig/expat.pc

%files help
%defattr(-,root,root)
%doc README.md
%{_mandir}/man1/*

%changelog
* Sat Oct 29 2022 fuanan <fuanan3@h-partners.com> - 2.4.1-8
- fix CVE-2022-43680

* Tue Oct 11 2022 huangduirong <huangduirong@huawei.com> - 2.4.1-7
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Move autoreconf to build

* Thu Sep 15 2022 panxiaohe <panxh.life@foxmail.com> - 2.4.1-6
- fix CVE-2022-40674

* Mon Mar 7 2022 yangzhuangzhuang <yangzhuangzhuang1@h-partners.com> - 2.4.1-5
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Relax fix to CVE-2022-25236

* Sat Feb 26 2022 yangzhuangzhuang <yangzhuangzhuang1@h-partners.com> - 2.4.1-4
- Type:CVE
- ID:Fix CVE-2022-25235 CVE-2022-25236 CVE-2022-25313 CVE-2022-25314 CVE-2022-25315
- SUG:NA
- DESC:Fix CVE-2022-25235 CVE-2022-25236 CVE-2022-25313 CVE-2022-25314 CVE-2022-25315

* Mon Feb 7 2022 yangzhuangzhuang <yangzhuangzhuang1@h-partners.com> - 2.4.1-3
- Type:CVE
- ID:CVE-2022-23852 CVE-2022-23990
- SUG:NA
- DESC:Fix CVE-2022-23852CVE-2022-23990

* Mon Jan 17 2022 wangjie <wangjie375@huawei.com> - 2.4.1-2
- Type:CVE
- ID:CVE-2021-45960 CVE-2021-46143 CVE-2022-22822 CVE-2022-22823 CVE-2022-22824 CVE-2022-22825 CVE-2022-22826 CVE-2022-22827
- SUG:NA
- DESC:fix CVE-2021-45960 CVE-2021-46143
       CVE-2022-22822 CVE-2022-22823 CVE-2022-22824 CVE-2022-22825 CVE-2022-22826 CVE-2022-22827

* Tue Jul 6 2021 panxiaohe <panxiaohe@huawei.com> - 2.4.1-1
- update to 2.4.1
- fix CVE-2013-0340

* Wed Jan 20 2021 wangchen <wangchen137@huawei.com> - 2.2.10-1
- update to 2.2.10

* Sun Jun 28 2020 liuchenguang <liuchenguang4@huawei.com> - 2.2.9-2
- quality enhancement synchronization github patch

* Mon May 11 2020 openEuler Buildteam <buildteam@openeuler.org> - 2.2.9-1
- Type:requirement
- ID:NA
- SUG:NA
- DESC:update to 2.2.9

* Mon Oct 21 2019 shenyangyang <shenyangyang4@huawei.com> - 2.2.6-5
- Type:NA
- ID:NA
- SUG:NA
- DESC:modify the directory of AUTHORS

* Mon Oct 21 2019 shenyangyang <shenyangyang4@huawei.com> - 2.2.6-4
- Type:NA
- ID:NA
- SUG:NA
- DESC:move AUTHORS to license directory

* Sat Sep 28 2019 shenyangyang<shenyangyang4@huawei.com> - 2.2.6-3
- Type:cves
- ID:CVE-2019-15903
- SUG:NA
- DESC:fix CVE-2019-15903

* Fri Aug 30 2019 gulining<gulining1@huawei.com> - 2.2.6-2
- Type:cves
- ID:CVE-2018-20843
- SUG:NA
- DESC:fix CVE-2018-20843

* Thu Aug 29 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.2.6-1
- Package Init
