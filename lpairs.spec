%define release  %mkrel 1


Summary:	Memory game
Name:		lpairs
Version:	1.0.1
Release:	%release

URL:		http://lgames.sourceforge.net/index.php?project=LPairs

Source0:	http://peterhost.dl.sourceforge.net/sourceforge/lgames/%{name}-%{version}.tar.bz2
Source4:	%{name}.menu

License:	GPL
Group:		Games/Puzzles
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	SDL-devel libSDL_mixer-devel X11-devel alsa-lib-devel
BuildRequires:	filesystem esound-devel texinfo

%description
LPairs is a classical memory game. This means you have to find pairs of
identical cards which will then be removed. Your time and tries needed will be
counted but there is no highscore chart or limit to this.

%prep
%setup -q

%build
%configure \
    --localstatedir=%{_localstatedir}/games
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall inst_dir="$RPM_BUILD_ROOT%{_gamesdatadir}/%{name}" bindir="$RPM_BUILD_ROOT%{_gamesbindir}"

install -D -m644 %SOURCE4 $RPM_BUILD_ROOT%{_menudir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root)
%doc README
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}/*
%{_menudir}/%{name}

