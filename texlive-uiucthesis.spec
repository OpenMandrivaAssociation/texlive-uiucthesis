Name:		texlive-uiucthesis
Version:	15878
Release:	2
Summary:	UIUC thesis class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uiucthesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uiucthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uiucthesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uiucthesis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class produces a document that conforms to the format
described in the University's Handbook for Graduate Students
Preparing to Deposit.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/uiucthesis/uiucthesis.cls
%{_texmfdistdir}/tex/latex/uiucthesis/uiucthesis.sty
%doc %{_texmfdistdir}/doc/latex/uiucthesis/README
%doc %{_texmfdistdir}/doc/latex/uiucthesis/thesis-ex.pdf
%doc %{_texmfdistdir}/doc/latex/uiucthesis/thesis-ex.tex
%doc %{_texmfdistdir}/doc/latex/uiucthesis/uiucthesis.pdf
#- source
%doc %{_texmfdistdir}/source/latex/uiucthesis/uiucthesis.dtx
%doc %{_texmfdistdir}/source/latex/uiucthesis/uiucthesis.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
