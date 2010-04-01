Summary:	Tool for creating fonts.dir for TrueType fonts
Summary(pl.UTF-8):	Narzędzie do tworzenia plików fonts.dir dla fontów TrueType
Name:		ttmkfdir
Version:	2.20021109
Release:	1
Epoch:		1
License:	unknown
Group:		Applications/File
URL:		http://people.redhat.com/yshao/
Source0:	http://people.redhat.com/yshao/%{name}%{version}.tar.bz2
# Source0-md5:	79e0401393c9728865aa73bb2bd68dd4
Source1:	%{name}2.1
Patch0:		%{name}2-libtool.patch
Patch1:		%{name}2-foundrynames.patch
Patch2:		%{name}2-gcc.patch
Patch3:		%{name}2-iso10646.patch
Patch4:		%{name}2-CJK-bugfix.patch
Patch5:		%{name}2-freetype2-port+cjk.patch
Patch6:		%{name}2-encodings.patch
Patch7:		%{name}2-nofileswithspaces.patch
Patch8:		%{name}2-build.patch
Patch9:		%{name}2-headers.patch
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
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
%setup -q -n %{name}2
%patch0 -p1
%patch1 -p2
%patch3 -p2
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

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
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
