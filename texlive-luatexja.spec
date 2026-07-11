%global tl_name luatexja
%global tl_revision 79037

Name:		texlive-%{tl_name}
Epoch:		1
Version:	20260517.0
Release:	%{tl_revision}.1
Summary:	Typeset Japanese with Lua(La)TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/generic/luatexja
License:	bsd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luatexja.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luatexja.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luatexja.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(luatexbase)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers support for typesetting Japanese documents with
LuaTeX. Either of the Plain and LaTeX2e formats may be used with the
package.

