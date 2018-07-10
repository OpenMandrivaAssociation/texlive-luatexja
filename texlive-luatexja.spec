Name:		texlive-luatexja
Version:	20180616.0
Release:	2
Summary:	Typeset Japanese with lua(la)tex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/generic/luatexja
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatexja.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatexja.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatexja.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers support for typesetting Japanese documents
with LuaTeX. Either of the Plain and LaTeX2e formats may be
used with the package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/luatex/luatexja
%doc %{_texmfdistdir}/doc/luatex/luatexja
#- source
%doc %{_texmfdistdir}/source/luatex/luatexja

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
