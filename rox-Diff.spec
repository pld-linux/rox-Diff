%define _appsdir /usr/X11R6/share/ROX-apps
%define _name Diff
%define _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	Display a coloured context diff between two files
Summary(pl):	ROX-Diff wy¶wietla kolorow± ró¿nice miêdzy dwoma plikami
Name:		rox-%{_name}
Version:	1.0.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.kerofin.demon.co.uk/rox/%{_name}-%{version}.tgz
Patch0:		%{name}-libxml-includes.patch
Patch1:		%{name}-paths-fix.patch
URL:		http://www.kerofin.demon.co.uk/rox/utils.html#Diff
BuildRequires:	rox-CLib-devel >= 0.1.4
BuildRequires:	libxml-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Display a coloured context diff between two files.

%description -l pl
ROX-Diff wy¶wietla kolorow± ró¿nice miêdzy dwoma plikami.

%prep
%setup -q -n %{_name}
%patch0 -p1
%patch1 -p1

%build
./AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/{Help,%{_platform}}

rm -f ../install
install App* rox_run $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help
install %{_platform}/Diff $RPM_BUILD_ROOT%{_appsdir}/%{_name}/%{_platform}

%clean
rm -rf $RPM_BUILD_ROOT
rm -f install

%files
%defattr(644,root,root,755)
%doc Help/Versions
%attr(755,root,root) %{_appsdir}/%{_name}/*[Rr]un
%attr(755,root,root) %{_appsdir}/%{_name}/%{_platform}
%{_appsdir}/%{_name}/AppI*
%{_appsdir}/%{_name}/Help
%dir %{_appsdir}/%{_name}
