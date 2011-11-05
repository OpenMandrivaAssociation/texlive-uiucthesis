# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/uiucthesis
# catalog-date 2007-01-20 15:20:16 +0100
# catalog-license lppl
# catalog-version 2.25
Name:		texlive-uiucthesis
Version:	2.25
Release:	1
Summary:	UIUC thesis class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uiucthesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uiucthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uiucthesis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uiucthesis.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The class produces a document that conforms to the format
described in the University's Handbook for Graduate Students
Preparing to Deposit.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
