Summary:	Tool for creating fonts.dir for TrueType fonts
Summary(pl):	Narz�dzie do tworzenia plik�w fonts.dir dla font�w TrueType
Name:		ttmkfdir
Version:	none
Release:	2
Group:		Applications/File
License:	GPL
Source0:	http://www.darmstadt.gmd.de/~pommnitz/TrueType/%{name}.tar.gz
Patch0:		%{name}-make.patch
Patch1:		%{name}-foundrynames.patch
Patch2:		%{name}-nospaces.patch
BuildRequires:	freetype1-devel >= 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program creates 'font.dir' files for TrueType fonts. These files
are required if you want to use TrueType fonts with X Window.

%description -l pl
Ten program tworzy pliki 'font.dir' dla font�w TrueType. S� one
potrzebne, aby m�c korzysta� z font�w TrueType w X Window.

%prep
%setup -q -c %{name}
%patch0 -p1
%patch1 -p2
%patch2 -p2

%build
%{__make} \
	OPT_FLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

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
