%define release 5

Summary: Memory game
Name: lpairs
Version: 1.0.4
Release: %release
URL: http://lgames.sourceforge.net/index.php?project=LPairs
Source0: http://peterhost.dl.sourceforge.net/sourceforge/lgames/%{name}-%{version}.tar.gz
Patch0:	lpairs-1.0.4-fix-desktop.patch
License: GPLv2+
Group: Games/Puzzles
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: SDL-devel
BuildRequires: filesystem
BuildRequires: imagemagick
BuildRequires: texinfo

%description
LPairs is a classical memory game. This means you have to find pairs of
identical cards which will then be removed. Your time and tries needed will be
counted but there is no highscore chart or limit to this.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x \
 --bindir=%_gamesbindir \
 --localstatedir=%{_localstatedir}/lib/games
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
install -m644 %name.desktop $RPM_BUILD_ROOT%{_datadir}/applications/

mkdir -p %buildroot%_iconsdir/
convert -resize 32x32 %name.png %buildroot%_iconsdir/%name.png

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
%{_iconsdir}/*.png
%{_datadir}/applications/*.desktop


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-4mdv2011.0
+ Revision: 620259
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.0.4-3mdv2010.0
+ Revision: 439606
- rebuild

* Sun Apr 05 2009 Funda Wang <fwang@mandriva.org> 1.0.4-2mdv2009.1
+ Revision: 364186
- Br imagemagick
- adjust desktop file

* Tue Oct 14 2008 Funda Wang <fwang@mandriva.org> 1.0.4-1mdv2009.1
+ Revision: 293535
- New version 1.0.4
- simplify BR

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-3mdv2009.0
+ Revision: 251405
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Wed Mar 05 2008 Guillaume Bedot <littletux@mandriva.org> 1.0.3-1mdv2008.1
+ Revision: 179892
- 1.0.3

* Sat Jan 26 2008 Funda Wang <fwang@mandriva.org> 1.0.1-2mdv2008.1
+ Revision: 158189
- fix menu entry

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Thierry Vignaud <tv@mandriva.org> 1.0.1-1mdv2008.1
+ Revision: 133909
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- import lpairs


* Wed Jul 20 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.1-1mdk
- 1.0.1

* Fri Jul 01 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.0-2mdk
- Rebuild

* Thu Jan 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.0-1mdk
- Initial MDK release (for Pablo)
