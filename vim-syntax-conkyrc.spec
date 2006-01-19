%define		_vimdatadir	%{_datadir}/vim/vimfiles
%define 	_rc 20050923
Summary:	Vim syntax: Highlight code in conky config file 
Summary(pl):	Opis sk³adni dla Vima: pod¶wietlanie kodu wewnatrz plikow konfiguracyjnych conky'ego.
Name:		vim-syntax-conkyrc
Version:	1.0
Release:	0.%{_rc}.1
# can't find license information.
License:	as-is
Group:		Applications/Editors/Vim
Source0:	http://vim.sourceforge.net/scripts/download_script.php?src_id=4621
# Source0-md5:	14af15829b26e101df5e020397fa0536
URL:		http://vim.sourceforge.net/scripts/script.php?script_id=1367
Requires:	vim >= 6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_syntax conkyrc

%description
This script highlights code in conky config file.

%description -l pl
Ten skrypt pod¶wietla kod w pliku konfiguracyjnym conky'ego.

%prep
%setup -q -c -T
install %{SOURCE0} %{_syntax}.vim

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,ftdetect}
install %{_syntax}.vim $RPM_BUILD_ROOT%{_vimdatadir}/syntax

cat > $RPM_BUILD_ROOT%{_vimdatadir}/ftdetect/%{_syntax}.vim <<-EOF
au BufNewFile,BufRead *%{_syntax} set filetype=%{_syntax}
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/*
%{_vimdatadir}/ftdetect/*
