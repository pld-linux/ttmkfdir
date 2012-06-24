Summary:	Tool for creating fonts.dir for TrueType fonts
Summary(pl):	Narz�dzie do tworzenia plik�w fonts.dir dla font�w TrueType
Name:		ttmkfdir
Version:	none
Release:	1
Group:		X11/Utilities
Group(pl):	X11/Narz�dzia
License:	GPL
Source0:	http://www.darmstadt.gmd.de/~pommnitz/TrueType/ttmkfdir.tar.gz
Patch0:		ttmkfdir-make.patch
BuildRequires:	freetype-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6

%description
This program creates 'font.dir' files for TrueType fonts. These files are
required if you want to use TrueType fonts with X Window.

%description -l pl
Ten program tworzy pliki 'font.dir' dla font�w TrueType. S� one potrzebne, aby
m�c korzysta� z font�w TrueType w X Window.

%prep
%setup -q -c %{name}
%patch0 -p1

%build
LDFLAGS="-s" ; export LDFLAGS

make OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

install ttmkfdir $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc *.gz
