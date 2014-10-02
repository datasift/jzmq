Name:          jzmq4
Version:       4.0.4.1
Release:       1%{?dist}
Summary:       The Java ZeroMQ bindings
Group:         Applications/Internet
License:       LGPLv3+
URL:           http://www.zeromq.org/
Source:        https://codeload.github.com/datasift/%{name}/tar.gz/v%{version}
Prefix:        %{_prefix}
Buildroot:     %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libzmq-devel >= 4.0.4.1
BuildRequires: pkgconfig
BuildRequires: libtool
BuildRequires: make 
BuildRequires: gcc48-c++
BuildRequires: java-1.7.0-openjdk
BuildRequires: java-1.7.0-openjdk-devel
# Requires:      libstdc++, libzmq

%description
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialised messaging middleware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the Java Bindings for ZeroMQ.

%package devel
Summary:  Development files and static library for the Java Bindings for the ZeroMQ library.
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}, pkgconfig

%description devel
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialised messaging middleware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains Java Bindings for ZeroMQ related development libraries and header files.

%prep
%setup -q

./autogen.sh
%build
%configure

%{__make}

%install
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

# Install the package to build area
%makeinstall

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)

# docs in the main package
%doc AUTHORS ChangeLog COPYING COPYING.LESSER NEWS README

# libraries
%{_libdir}/libjzmq4.so*
/usr/share/java/zmq4.jar
/usr/share/perf/zmq4-perf.jar

%files devel
%defattr(-,root,root,-)
%{_libdir}/libjzmq4.la
%{_libdir}/libjzmq4.a

%changelog
* Thu Dec 09 2010 Alois Belaska <alois.belaska@gmail.com>
- version of package changed to 2.1.0
* Tue Sep 21 2010 Stefan Majer <stefan.majer@gmail.com> 
- Initial packaging
