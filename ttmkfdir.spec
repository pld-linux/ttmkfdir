Summary:	Tool for creating fonts.dir for TrueType fonts
Summary(pl):	Narzêdzie do tworzenia plików fonts.dir dla fontów TrueType
Name:		ttmkfdir
Version:	2.20001030
Release:	5
Epoch:		1
License:	unknown
Group:		Applications/File
Source0:	%{name}2.tar.bz2
# Source0-md5:	643d8b84da8eeed136867abe87cae29e
Source1:	%{name}2.1
Patch0:		%{name}2-libtool.patch
Patch1:		%{name}2-foundrynames.patch
Patch2:		%{name}2-gcc.patch
Patch3:		%{name}2-iso10646.patch
Patch4:		%{name}2-CJK-bugfix.patch
Patch5:		%{name}2-freetype2-port+cjk.patch
Patch6:		%{name}2-encodings.patch
Patch7:		%{name}2-nofileswithspaces.patch
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
Provides:	ttmkfdir2
Obsoletes:	ttmkfdir2
# our freetype1 < 1.3.1-4 (formerly freetype-1.x.x) contained old ttmkfdir
Conflicts:	freetype1 < 1.3.1-4
Conflicts:	freetype < 2.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program creates 'font.dir' files for TrueType fonts. These files
are required if you want to use TrueType fonts with X Window.

%description -l pl
Ten program tworzy pliki 'font.dir' dla fontów TrueType. S± one
potrzebne, aby móc korzystaæ z fontów TrueType w X Window.

%prep
%setup -q -n %{name}2
%patch0 -p1
%patch1 -p2
%patch2 -p1
%patch3 -p2
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
%{__make} clean
%{__make} \
	CXX="%{__cxx}" \
	DEBUG="%{rpmcflags}" \
	FREETYPE_BASE="/usr/include/freetype2"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install ttmkfdir $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/ttmkfdir.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
