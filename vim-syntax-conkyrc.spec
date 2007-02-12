%define		_syntax	conkyrc
%define		_vimdatadir	%{_datadir}/vim/vimfiles
%define 	_snap	20050923
Summary:	Vim syntax: Highlight code in conky config file
Summary(pl.UTF-8):   Opis składni dla Vima: podświetlanie kodu wewnątrz plików konfiguracyjnych conky'ego
Name:		vim-syntax-conkyrc
Version:	%{_snap}
Release:	1
# can't find license information.
License:	as-is
Group:		Applications/Editors/Vim
Source0:	http://vim.sourceforge.net/scripts/download_script.php?src_id=4621
# Source0-md5:	14af15829b26e101df5e020397fa0536
URL:		http://vim.sourceforge.net/scripts/script.php?script_id=1367
# for _vimdatadir existence
Requires:	vim >= 4:6.3.058-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This script highlights code in conky config file.

%description -l pl.UTF-8
Ten skrypt podświetla kod w pliku konfiguracyjnym conky'ego.

%prep

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,ftdetect}
install %{SOURCE0} $RPM_BUILD_ROOT%{_vimdatadir}/syntax/%{_syntax}.vim

cat > $RPM_BUILD_ROOT%{_vimdatadir}/ftdetect/%{_syntax}.vim <<EOF
au BufNewFile,BufRead *%{_syntax} set filetype=%{_syntax}
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/*
%{_vimdatadir}/ftdetect/*
