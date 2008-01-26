%define release  %mkrel 2

Summary:	Memory game
Name:		lpairs
Version:	1.0.1
Release:	%release
URL:		http://lgames.sourceforge.net/index.php?project=LPairs
Source0:	http://peterhost.dl.sourceforge.net/sourceforge/lgames/%{name}-%{version}.tar.bz2
License:	GPLv2+
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

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Categories=Game;LogicGame;
Name=LPairs
Comment=Memory game
Exec=/usr/games/lpairs
EOF

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
%{_datadir}/applications/mandriva-%{name}.desktop
