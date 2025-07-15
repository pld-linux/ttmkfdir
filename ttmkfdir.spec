Summary:	Tool for creating fonts.dir for TrueType fonts
Summary(pl.UTF-8):	Narzędzie do tworzenia plików fonts.dir dla fontów TrueType
Name:		ttmkfdir
Version:	3.0.9
Release:	2
Epoch:		1
License:	LGPL v2+
Group:		Applications/File
Source0:	http://ftp.debian.org//debian/pool/main/t/ttmkfdir/%{name}_%{version}.orig.tar.gz
# Source0-md5:	c22b8b7f8401fd924200c8e0e04a78f9
Source1:	%{name}2.1
Patch0:		%{name}-3.0.9-cpp.patch
Patch1:		%{name}-3.0.9-zlib.patch
Patch2:		%{name}-3.0.9-fix-freetype217.patch
Patch3:		%{name}-3.0.9-namespace.patch
Patch4:		%{name}-3.0.9-fix-crash.patch
Patch5:		%{name}-3.0.9-warnings.patch
Patch6:		%{name}-3.0.9-segfaults.patch
Patch7:		%{name}-3.0.9-encoding-dir.patch
Patch8:		%{name}-3.0.9-font-scale.patch
Patch9:		%{name}-3.0.9-bug434301.patch
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
Provides:	ttmkfdir2
Obsoletes:	ttmkfdir2
# our freetype1 < 1.3.1-4 (formerly freetype-1.x.x) contained old ttmkfdir
Conflicts:	freetype < 2.0.1
Conflicts:	freetype1 < 1.3.1-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program creates 'font.dir' files for TrueType fonts. These files
are required if you want to use TrueType fonts with X Window.

%description -l pl.UTF-8
Ten program tworzy pliki 'font.dir' dla fontów TrueType. Są one
potrzebne, aby móc korzystać z fontów TrueType w X Window.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	DEBUG= \
	OPTFLAGS="%{rpmcxxflags} %{rpmcppflags}" \
	LDFLAGS='%{rpmldflags} $(FREETYPE_LIB) -lz'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/ttmkfdir.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
