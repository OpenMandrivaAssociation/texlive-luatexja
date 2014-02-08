# revision 27593
# category Package
# catalog-ctan /macros/luatex/generic/luatexja
# catalog-date 2012-06-23 09:21:42 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-luatexja
Version:	20120623
Release:	4
Summary:	Typesest Japanese with lua(la)tex
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
The package supports typesetting Japanese documents with
LuaTeX. Both the Plain and LaTeX2e formats may be used with the
package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/luatex/luatexja/addons/luatexja-ajmacros.sty
%{_texmfdistdir}/tex/luatex/luatexja/addons/luatexja-fontspec.sty
%{_texmfdistdir}/tex/luatex/luatexja/addons/luatexja-otf.sty
%{_texmfdistdir}/tex/luatex/luatexja/addons/luatexja-preset.sty
%{_texmfdistdir}/tex/luatex/luatexja/jfm-banjiao.lua
%{_texmfdistdir}/tex/luatex/luatexja/jfm-jis.lua
%{_texmfdistdir}/tex/luatex/luatexja/jfm-kaiming.lua
%{_texmfdistdir}/tex/luatex/luatexja/jfm-min.lua
%{_texmfdistdir}/tex/luatex/luatexja/jfm-mono.lua
%{_texmfdistdir}/tex/luatex/luatexja/jfm-prop.lua
%{_texmfdistdir}/tex/luatex/luatexja/jfm-quanjiao.lua
%{_texmfdistdir}/tex/luatex/luatexja/jfm-ujis.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-base.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-base.sty
%{_texmfdistdir}/tex/luatex/luatexja/ltj-cctbreg.sty
%{_texmfdistdir}/tex/luatex/luatexja/ltj-charrange.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-cid-adobe-cns1.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-cid-adobe-gb1.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-cid-adobe-japan1.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-cid-adobe-korea1.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-compat-ptex.sty
%{_texmfdistdir}/tex/luatex/luatexja/ltj-compat.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-debug.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-infomute.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-inputbuf.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-jfmglue.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-jfont.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-jisx0208.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-latex.sty
%{_texmfdistdir}/tex/luatex/luatexja/ltj-math.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-otf.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-plain.sty
%{_texmfdistdir}/tex/luatex/luatexja/ltj-pretreat.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-rmlgbm.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-setwidth.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-stack.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-tangle.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltjclasses/ltjarticle.cls
%{_texmfdistdir}/tex/luatex/luatexja/ltjclasses/ltjbk10.clo
%{_texmfdistdir}/tex/luatex/luatexja/ltjclasses/ltjbk11.clo
%{_texmfdistdir}/tex/luatex/luatexja/ltjclasses/ltjbk12.clo
%{_texmfdistdir}/tex/luatex/luatexja/ltjclasses/ltjbook.cls
%{_texmfdistdir}/tex/luatex/luatexja/ltjclasses/ltjltxdoc.cls
%{_texmfdistdir}/tex/luatex/luatexja/ltjclasses/ltjreport.cls
%{_texmfdistdir}/tex/luatex/luatexja/ltjclasses/ltjsize10.clo
%{_texmfdistdir}/tex/luatex/luatexja/ltjclasses/ltjsize11.clo
%{_texmfdistdir}/tex/luatex/luatexja/ltjclasses/ltjsize12.clo
%{_texmfdistdir}/tex/luatex/luatexja/ltjsclasses/ltjsarticle.cls
%{_texmfdistdir}/tex/luatex/luatexja/ltjsclasses/ltjsbook.cls
%{_texmfdistdir}/tex/luatex/luatexja/ltjsclasses/ltjskiyou.cls
%{_texmfdistdir}/tex/luatex/luatexja/ltjsclasses/ltjspf.cls
%{_texmfdistdir}/tex/luatex/luatexja/luatexja-compat.sty
%{_texmfdistdir}/tex/luatex/luatexja/luatexja-core.sty
%{_texmfdistdir}/tex/luatex/luatexja/luatexja-kinsoku.tex
%{_texmfdistdir}/tex/luatex/luatexja/luatexja.lua
%{_texmfdistdir}/tex/luatex/luatexja/luatexja.sty
%{_texmfdistdir}/tex/luatex/luatexja/patches/lltjcore.sty
%{_texmfdistdir}/tex/luatex/luatexja/patches/lltjdefs.sty
%{_texmfdistdir}/tex/luatex/luatexja/patches/lltjfont.sty
%{_texmfdistdir}/tex/luatex/luatexja/patches/lltjp-listings-jpt.tex
%{_texmfdistdir}/tex/luatex/luatexja/patches/lltjp-listings.sty
%{_texmfdistdir}/tex/luatex/luatexja/patches/lltjp-unicode-math.sty
%{_texmfdistdir}/tex/luatex/luatexja/patches/lltjp-xunicode.sty
%{_texmfdistdir}/tex/luatex/luatexja/patches/ltj-unicode-ccfix.tex
%doc %{_texmfdistdir}/doc/luatex/luatexja/COPYING
%doc %{_texmfdistdir}/doc/luatex/luatexja/README
%doc %{_texmfdistdir}/doc/luatex/luatexja/jfm-test.lua
%doc %{_texmfdistdir}/doc/luatex/luatexja/ltjclasses.pdf
%doc %{_texmfdistdir}/doc/luatex/luatexja/ltjltxdoc.pdf
%doc %{_texmfdistdir}/doc/luatex/luatexja/ltjsclasses.pdf
%doc %{_texmfdistdir}/doc/luatex/luatexja/luatexja-en.pdf
%doc %{_texmfdistdir}/doc/luatex/luatexja/luatexja-ja.pdf
%doc %{_texmfdistdir}/doc/luatex/luatexja/luatexja-zh.pdf
%doc %{_texmfdistdir}/doc/luatex/luatexja/luatexja.dtx
%doc %{_texmfdistdir}/doc/luatex/luatexja/luatexja.ins
#- source
%doc %{_texmfdistdir}/source/luatex/luatexja/ltjclasses.dtx
%doc %{_texmfdistdir}/source/luatex/luatexja/ltjclasses.ins
%doc %{_texmfdistdir}/source/luatex/luatexja/ltjlist.lua
%doc %{_texmfdistdir}/source/luatex/luatexja/ltjltxdoc.dtx
%doc %{_texmfdistdir}/source/luatex/luatexja/ltjltxdoc.ins
%doc %{_texmfdistdir}/source/luatex/luatexja/ltjsclasses.dtx
%doc %{_texmfdistdir}/source/luatex/luatexja/ltjsclasses.ins
%doc %{_texmfdistdir}/source/luatex/luatexja/luatexja-kinsoku_make.tex
%doc %{_texmfdistdir}/source/luatex/luatexja/mk-rmlgbm-data.tex
%doc %{_texmfdistdir}/source/luatex/luatexja/tool/blocks2defcharrange.rb
%doc %{_texmfdistdir}/source/luatex/luatexja/tool/chars2defcharrange.rb
%doc %{_texmfdistdir}/source/luatex/luatexja/tool/jfm-readable.rb
%doc %{_texmfdistdir}/source/luatex/luatexja/tool/jisx0208table.tex
%doc %{_texmfdistdir}/source/luatex/luatexja/tool/kyoikukanji.txt
%doc %{_texmfdistdir}/source/luatex/luatexja/tool/kyoikukanjiChars.tex
%doc %{_texmfdistdir}/source/luatex/luatexja/tool/otf-AdobeMingStd-Light.txt
%doc %{_texmfdistdir}/source/luatex/luatexja/tool/otf-AdobeMyungjoStd-Medium.txt
%doc %{_texmfdistdir}/source/luatex/luatexja/tool/otf-AdobeSongStd-Light.txt
%doc %{_texmfdistdir}/source/luatex/luatexja/tool/otf-KozMinPr6N-Regular.txt
%doc %{_texmfdistdir}/source/luatex/luatexja/tool/unicodeBlocks.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
