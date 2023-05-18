#
# spec file for package Zeek
#
# Copyright (c) 1995-2014 The Regents of the University of California
# through the Lawrence Berkeley National Laboratory and the
# International Computer Science Institute. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# (1) Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#
# (2) Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#
# (3) Neither the name of the University of California, Lawrence Berkeley
#     National Laboratory, U.S. Dept. of Energy, International Computer
#     Science Institute, nor the names of contributors may be used to endorse
#     or promote products derived from this software without specific prior
#     written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Note that some files in the distribution may carry their own copyright
# notices.
Name:           zeek-lts
Version:        5.0.8
Release:        2.1
Summary:        Zeek is a powerful framework for network analysis and security monitoring
Group:          Productivity/Networking/Diagnostic

License:        BSD-3-Clause
URL:            http://zeek.org
Source0:        https://download.zeek.org/zeek-5.0.8.tar.gz
Patch0:         install-symlink-old-cmake.patch
Patch1:         spicy-flex.patch
Requires:       zeek-lts-core = %{version}
Requires:       zeekctl-lts = %{version}
Requires:       zeek-lts-devel = %{version}
Requires:       zeek-lts-zkg = %{version}
Requires:       zeek-lts-spicy-devel = %{version}
Requires:       zeek-lts-client = %{version}
Requires(pre):  /usr/sbin/groupadd, /usr/bin/getent

%if %{defined rhel_version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%endif

%define _prefix /opt/zeek
%define _sysconfdir %{_prefix}/etc
%define _vardir %{_prefix}/var
%define _libdir %{_prefix}/lib
%define _mandir %{_prefix}/share/man

%if 0%{?suse_version}
%define __cmake /usr/bin/cmake
%endif

%if 0%{?fedora_version} == 36
# fix 
# [ 3021s] /usr/bin/ld.gold: error: /home/abuild/rpmbuild/BUILD/zeek-nightly/.package_note-zeek-nightly-5.1.0-18.1.x86_64.ld:41:8: syntax error, unexpected STRING
# [ 3021s] /usr/bin/ld.gold: fatal error: unable to parse script file /home/abuild/rpmbuild/BUILD/zeek-nightly/.package_note-zeek-nightly-5.1.0-18.1.x86_64.ld
# [ 3021s] collect2: error: ld returned 1 exit status
%undefine _package_note_flags
%endif

%description
Zeek is a powerful network analysis framework that is much different from the
typical IDS you may know.  While focusing on network security monitoring, Zeek
provides a comprehensive platform for more general network traffic analysis as
well. Well grounded in more than 15 years of research, Zeek has successfully
bridged the traditional gap between academia and operations since its
inception. Today, it is relied upon operationally in particular by many
scientific environments for securing their cyberinfrastructure. Zeek's user
community includes major universities, research labs, supercomputing centers,
and open-science communities.

%package -n zeek-lts-core
Summary:        The core zeek installation without zeekctl
Group:          Productivity/Networking/Diagnostic
Requires(pre):  /usr/sbin/groupadd, /usr/bin/getent
Requires: libpcap
# Opensuse uses a different name for libmaxminddb (but has sle_version set, so id does not add the above requirement)
# and tumbleweed does not have is_opensuse.
%if ( 0%{?is_opensuse} ) || ( 0%{?suse_version} > 1500 )
Requires: libmaxminddb0
%else
# sle has no maxminddb
%if ! ( 0%{?sle_version} )
Requires: libmaxminddb
%endif
%endif
BuildRequires: flex bison cmake openssl-devel zlib-devel swig gcc-c++
BuildRequires: libpcap-devel
%if ! ( 0%{?sle_version} && !0%{?is_opensuse} )
BuildRequires: libmaxminddb-devel
%endif
BuildRequires: python3 python3-devel
%if 0%{?centos_version} == 700
BuildRequires: cmake3 devtoolset-8-gcc-c++ devtoolset-8-elfutils devtoolset-8-binutils devtoolset-8-make devtoolset-8-toolchain
# devtoolset needs python-libs
BuildRequires: python-libs
%endif
%if 0%{?sle_version} == 150300
BuildRequires: gcc10 gcc10-c++
%endif
%if 0%{?sle_version} == 150400
BuildRequires: gcc11 gcc11-c++
%endif


%description -n zeek-lts-core
Zeek is a powerful network analysis framework that is much different from the
typical IDS you may know.  While focusing on network security monitoring, Zeek
provides a comprehensive platform for more general network traffic analysis as
well. Well grounded in more than 15 years of research, Zeek has successfully
bridged the traditional gap between academia and operations since its
inception. Today, it is relied upon operationally in particular by many
scientific environments for securing their cyberinfrastructure. Zeek's user
community includes major universities, research labs, supercomputing centers,
and open-science communities.

%package -n zeek-lts-devel
Summary:        Development files for Zeek
Group:          Productivity/Networking/Diagnostic
Requires(pre):  /usr/sbin/groupadd, /usr/bin/getent
Requires:       libbroker-lts-devel = %{version}
Requires:       openssl-devel zlib-devel libpcap-devel

%description -n zeek-lts-devel
Development files for Zeek; these files are needed when building binary packages
for Zeek.

%package -n zeek-lts-spicy-devel
Summary:        Development files for Spicy
Group:          Productivity/Networking/Diagnostic
Requires(pre):  /usr/sbin/groupadd, /usr/bin/getent
Requires:       openssl-devel zlib-devel libpcap-devel

%description -n zeek-lts-spicy-devel
Development files for Spicy; these files are needed when building spicy analyzers
for Zeek.

%package -n libbroker-lts-devel
Summary:        Development files for Zeek's Messaging Library
Group:          System/Libraries
Requires(pre):  /usr/sbin/groupadd, /usr/bin/getent

%description -n libbroker-lts-devel
The Broker library implements Zeek's high-level communication patterns.
This package bundles the library files and headers that were used during the Zeek
build process; they may be needed when building packages for Zeek.

%package -n zeekctl-lts
Summary:        Zeek Control
Group:          Productivity/Networking/Diagnostic
Requires(pre):  /usr/sbin/groupadd, /usr/bin/getent
Requires:       python3
Requires:       zeek-lts-core = %{version}
%if 0%{?suse_version}
Requires:       python3-curses
%endif

%description -n zeekctl-lts
ZeekControl is Zeek's interactive shell for operating Zeek installations.

%package -n zeek-lts-zkg
Summary:       The Zeek Package Manager
Group:         Productivity/Networking/Diagnostic
Requires(pre):  /usr/sbin/groupadd, /usr/bin/getent
Requires:      python3
%if ! ( 0%{?centos_version} == 700 )
Requires:      python3-semantic-version python3-gitpython
%endif
Requires:      zeek-lts-core = %{version}
Requires:      zeek-lts-devel = %{version}
Requires:      zeek-lts-spicy-devel = %{version}
Requires:      zeek-lts-btest = %{version}
Requires:      zeek-lts-btest-data = %{version}

%description -n zeek-lts-zkg
Zkg is Zeek's package manager.

%package -n zeek-lts-btest
Summary:       The BTest test framework
Group:         Productivity/Networking/Diagnostic
Requires(pre):  /usr/sbin/groupadd, /usr/bin/getent
Requires:      python3

%description -n zeek-lts-btest
A Generic Driver for Powerful System Tests

%package -n zeek-lts-btest-data
Summary:       Data for testing
Group:         Productivity/Networking/Diagnostic
Requires(pre):  /usr/sbin/groupadd, /usr/bin/getent

%description -n zeek-lts-btest-data
This package contains test data in the form of pcaps that can he helpful when writing btests.

%package -n zeek-lts-client
Summary:        The Zeek Cluster Management Client
Group:          Productivity/Networking/Diagnostic
Requires:       zeek-lts-core = %{version}
Requires(pre):  /usr/sbin/groupadd, /usr/bin/getent

%description -n zeek-lts-client
This is an experimental version of the future client application for managing Zeek clusters. zeek-client connects to Zeek's cluster controller, a Zeek instance that exists in every cluster. The controller in turn is connected to the cluster's instances, physical machines each running an agent that maintains the data nodes composing a typical Zeek cluster (with manager, workers, proxies, and loggers).

%pre
/usr/bin/getent group zeek >/dev/null || /usr/sbin/groupadd -r zeek

%pre -n zeek-lts-core
/usr/bin/getent group zeek >/dev/null || /usr/sbin/groupadd -r zeek

%pre -n zeek-lts-devel
/usr/bin/getent group zeek >/dev/null || /usr/sbin/groupadd -r zeek

%pre -n zeek-lts-spicy-devel
/usr/bin/getent group zeek >/dev/null || /usr/sbin/groupadd -r zeek

%pre -n zeekctl-lts
/usr/bin/getent group zeek >/dev/null || /usr/sbin/groupadd -r zeek

%pre -n libbroker-lts-devel
/usr/bin/getent group zeek >/dev/null || /usr/sbin/groupadd -r zeek

%pre -n zeek-lts-zkg
/usr/bin/getent group zeek >/dev/null || /usr/sbin/groupadd -r zeek

%pre -n zeek-lts-btest
/usr/bin/getent group zeek >/dev/null || /usr/sbin/groupadd -r zeek

%pre -n zeek-lts-btest-data
/usr/bin/getent group zeek >/dev/null || /usr/sbin/groupadd -r zeek

%pre -n zeek-lts-client
/usr/bin/getent group zeek >/dev/null || /usr/sbin/groupadd -r zeek

%prep
%setup -n zeek-5.0.8 -q
# some platforms do in-source builds when using cmake. I don't really care, so just patch the error out.
find ./ -name "ProhibitInSourceBuild.cmake" | xargs -I file sh -c 'cat /dev/null > "file"'
# %patch1 -p1

%build
%if 0%{?centos_version} == 700
CXXFLAGS="${CXXFLAGS// -g / }" PATH=/opt/rh/llvm-toolset-7/root/bin/:/opt/rh/devtoolset-8/root/bin/:$PATH ./configure --prefix=%{_prefix} --libdir=%{_libdir} --binary-package --enable-static-broker --enable-static-binpac --disable-broker-tests --build-type=Release
PATH=/opt/rh/llvm-toolset-7/root/bin/:/opt/rh/devtoolset-8/root/bin/:$PATH make
%else
%if 0%{?sle_version}
%if 0%{?sle_version} == 150300
CXXFLAGS="${CXXFLAGS// -g / } -g1" CC=/usr/bin/gcc-10 CXX=/usr/bin/g++-10 ./configure --prefix=%{_prefix} --libdir=%{_libdir} --binary-package --enable-static-broker --enable-static-binpac --disable-broker-tests  --build-type=Release
%endif
%if 0%{?sle_version} == 150400
CXXFLAGS="${CXXFLAGS// -g / } -g1" CC=/usr/bin/gcc-11 CXX=/usr/bin/g++-11 ./configure --prefix=%{_prefix} --libdir=%{_libdir} --binary-package --enable-static-broker --enable-static-binpac --disable-broker-tests --build-type=Release
%endif
%else
CXXFLAGS=${CXXFLAGS// -g / }" -g1" ./configure --prefix=%{_prefix} --libdir=%{_libdir} --binary-package --enable-static-broker --enable-static-binpac --disable-broker-tests --build-type=Release
%endif
# make %{?_smp_mflags}
make
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{defined rhel_version}
make install DESTDIR=$RPM_BUILD_ROOT
%else
%make_install
%endif
rm -f %{?buildroot}/opt/zeek/spool/zeekctl-config.sh
touch %{?buildroot}/opt/zeek/spool/zeekctl-config.sh
mkdir -p  %{?buildroot}/opt/zeek/lib/zeek/plugins/packages/
mkdir -p  %{?buildroot}/opt/zeek/share/zeek/site/packages/
#mkdir -p %{?buildroot}/opt/zeek/spool/tmp
#mkdir -p %{?buildroot}/opt/zeek/logs

%files

%files -n zeek-lts-core
%defattr(-,root,zeek,0755)
%dir %{_prefix}
%dir %{_bindir}
%dir %{_datadir}
%dir %{_datadir}/zeek
%dir %{_mandir}
%dir %{_mandir}/man1
%dir %{_mandir}/man8
%dir %{_libdir}
%dir %{_libdir}/zeek
%dir %{_libdir}/zeek/plugins
%{_bindir}/zeek
%{_bindir}/zeek-wrapper
%{_bindir}/zeek-archiver
%{_bindir}/bro
%{_bindir}/zeek-cut
%{_bindir}/bro-cut
%{_bindir}/zeek-config
%{_bindir}/bro-config
%{_bindir}/adtrace
%{_bindir}/rst
%{_bindir}/gen-zam
%{_bindir}/paraglob-test
%{_datadir}/zeek/base
%{_datadir}/zeek/builtin-plugins
%{_datadir}/zeek/policy
%{_datadir}/zeek/zeekygen
%{_datadir}/zeek/test-all-policy.zeek
%{_mandir}/man1/zeek-cut.1
%{_mandir}/man8/zeek.8
%defattr(0664,root,zeek,2775)
%dir %{_datadir}/zeek/site
%config %{_datadir}/zeek/site/local.zeek

%files -n zeekctl-lts
%defattr(-,root,zeek,0755)
%dir %{_prefix}
%dir %{_bindir}
%dir %{_datadir}
%dir %{_datadir}/zeek
%dir %{_libdir}
%dir %{_libdir}/zeek
%dir %{_libdir}/zeek/python
%dir %{_mandir}
%dir %{_mandir}/man1
%dir %{_mandir}/man8
%{_bindir}/zeekctl
%{_bindir}/broctl
%{_bindir}/capstats
%{_bindir}/trace-summary
%{_datadir}/zeekctl
%{_datadir}/zeek/zeekctl
%{_libdir}/broctl
%{_libdir}/zeek/python/*Subnet*
%{_libdir}/zeek/python/zeekctl
%{_libdir}/zeek/python/broker
%{_mandir}/man8/zeekctl.8
%{_mandir}/man1/trace-summary.1
%defattr(0664,root,zeek,2775)
%dir %{_sysconfdir}
%config %{_sysconfdir}/zeekctl.cfg
%config %{_sysconfdir}/networks.cfg
%config %{_sysconfdir}/node.cfg
%defattr(0664,root,zeek,2770)
%{_prefix}/spool
%{_prefix}/logs

%files -n zeek-lts-devel
%defattr(-,root,zeek,0755)
%dir %{_prefix}
%dir %{_bindir}
%dir %{_includedir}
%dir %{_libdir}
%dir %{_datadir}
%dir %{_datadir}/zeek
%{_bindir}/bifcl
%{_bindir}/binpac
%{_includedir}/binpac
%{_includedir}/zeek
%{_includedir}/paraglob
%{_libdir}/libbinpac.a
%{_libdir}/libparaglob.a
%{_datadir}/zeek/cmake

%files -n zeek-lts-spicy-devel
%defattr(-,root,zeek,0755)
%dir %{_prefix}
%dir %{_bindir}
%dir %{_includedir}
%dir %{_libdir}
%dir %{_datadir}
%{_bindir}/hilti-config
%{_bindir}/hiltic
%{_bindir}/spicy-build
%{_bindir}/spicy-config
%{_bindir}/spicy-driver
%{_bindir}/spicy-dump
%{_bindir}/spicy-precompile-headers
%{_bindir}/spicyc
%{_bindir}/spicyz
%{_libdir}/libhilti*
%{_libdir}/libspicy*
%{_libdir}/zeek-spicy
%{_includedir}/hilti
%{_includedir}/spicy
%{_datadir}/hilti
%{_datadir}/spicy

%files -n libbroker-lts-devel
%defattr(-,root,zeek,0755)
%dir %{_prefix}
%dir %{_includedir}
%dir %{_libdir}
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/Broker
%{_includedir}/broker
%{_libdir}/libbroker.a
%{_libdir}/cmake/Broker/BrokerConfig.cmake
%{_libdir}/cmake/Broker/BrokerConfigVersion.cmake
%{_libdir}/cmake/Broker/BrokerTargets-release.cmake
%{_libdir}/cmake/Broker/BrokerTargets.cmake


%files -n zeek-lts-zkg
%defattr(-,root,zeek,0755)
%dir %{_prefix}
%dir %{_bindir}
%dir %{_libdir}
%dir %{_libdir}/zeek
%dir %{_libdir}/zeek/plugins
%dir %{_libdir}/zeek/python
%dir %{_vardir}
%dir %{_vardir}/lib
%dir %{_datadir}
%dir %{_datadir}/zeek
%dir %{_mandir}
%dir %{_mandir}/man1
%{_libdir}/zeek/python/zeekpkg
%{_bindir}/zkg
%{_mandir}/man1/zkg.1
%{_libdir}/zeek/plugins/packages
%{_datadir}/zeek/site/packages
%{_vardir}/lib/zkg
%defattr(0664,root,zeek,2775)
%dir %{_datadir}/zeek/site
%{_sysconfdir}/zkg

%files -n zeek-lts-btest
%defattr(-,root,zeek,0755)
%dir %{_prefix}
%dir %{_bindir}
%dir %{_libdir}
%dir %{_libdir}/zeek
%dir %{_libdir}/zeek/python
%dir %{_datadir}
%dir %{_datadir}/btest
%{_bindir}/btest
%{_bindir}/btest-*
%{_libdir}/zeek/python/btest-*
%{_datadir}/btest/scripts

%files -n zeek-lts-btest-data
%defattr(-,root,zeek,0755)
%dir %{_prefix}
%dir %{_datadir}
%dir %{_datadir}/btest
%{_datadir}/btest/data

%files -n zeek-lts-client
%defattr(-,root,zeek,0755)
%dir %{_prefix}
%dir %{_bindir}
%dir %{_libdir}
%dir %{_libdir}/zeek
%dir %{_libdir}/zeek/python
%{_bindir}/zeek-client
%{_libdir}/zeek/python/zeekclient

%doc CHANGES COPYING NEWS README VERSION

%changelog
* Mon Feb 09 2015 Johanna Amann <build@xxon.net> 5.0.8-0
Zeek build version specification
* Wed Jan 28 2015 Johanna Amann <build@xxon.net> 2.3.2
Update to Zeek 2.3.2
* Wed Oct 29 2014 Johanna Amann <build@xxon.net> 2.3.1
Initial version
-
