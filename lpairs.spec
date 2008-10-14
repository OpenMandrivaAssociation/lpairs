%define release %mkrel 1

Summary: Memory game
Name: lpairs
Version: 1.0.4
Release: %release
URL: http://lgames.sourceforge.net/index.php?project=LPairs
Source0: http://peterhost.dl.sourceforge.net/sourceforge/lgames/%{name}-%{version}.tar.gz
License: GPLv2+
Group: Games/Puzzles
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: SDL-devel
BuildRequires: filesystem
BuildRequires: texinfo

%description
LPairs is a classical memory game. This means you have to find pairs of
identical cards which will then be removed. Your time and tries needed will be
counted but there is no highscore chart or limit to this.

%prep
%setup -q

%build
%configure2_5x \
 --bindir=%_gamesbindir \
 --localstatedir=%{_localstatedir}/lib/games
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Categories=Game;LogicGame;
Name=LPairs
Comment=Memory game
Exec=/usr/games/lpairs
EOF

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc README
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}/*
%{_datadir}/applications/mandriva-%{name}.desktop
