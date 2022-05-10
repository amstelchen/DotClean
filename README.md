# DotClean - List and clean old or unused dotfiles/dotdirs

#### Installation

Steps assume that `python` (>=3.6) and `pip` are already installed.


    $ pip install DotClean

Install directly from ``github``:


    $ pip install git+https://github.com/amstelchen/DotClean#egg=DotClean

When completed, run it with:

    $ dotclean [...]

#### Usage

![demo](./images/demo.gif)

#### Safety feature

Setting the environment variable `DOTCLEAN` enables the program to really wipe entire files and directories, even if they are not empty. __USE WITH CAUTION!__

<style type="text/css">
pre { white-space: pre-wrap; }
.ef0,.f0 { color: #000000; } .eb0,.b0 { background-color: #000000; }
.ef1,.f1 { color: #AA0000; } .eb1,.b1 { background-color: #AA0000; }
.ef2,.f2 { color: #00AA00; } .eb2,.b2 { background-color: #00AA00; }
.ef3,.f3 { color: #AA5500; } .eb3,.b3 { background-color: #AA5500; }
.ef4,.f4 { color: #0000AA; } .eb4,.b4 { background-color: #0000AA; }
.ef5,.f5 { color: #AA00AA; } .eb5,.b5 { background-color: #AA00AA; }
.ef6,.f6 { color: #00AAAA; } .eb6,.b6 { background-color: #00AAAA; }
.ef7,.f7 { color: #AAAAAA; } .eb7,.b7 { background-color: #AAAAAA; }

.f9 { color: #000000; }
.b9 { background-color: #000000; }
.f9 > .bold,.bold > .f9, body.f9 > pre > .bold {
  /* Bold is heavy black on white, or bright white
     depending on the default background */
  color: #000000;
  font-weight: bold;
}
.reverse {
  /* CSS does not support swapping fg and bg colours unfortunately,
     so just hardcode something that will look OK on all backgrounds. */
  color: #000000; background-color: #AAAAAA;
}
.underline { text-decoration: underline; }
.line-through { text-decoration: line-through; }
.blink { text-decoration: blink; }

span { display: inline-block; font-size: 12px; }
</style>
</head>

#### Examples

<pre>
<span class="f0">$ dotclean -d
Options(files=False, directories=True, exclude=None, nocolor=False, clean=None)
/home/test/.config</span>
<span class="f4">qpdfview                                          576 d</span>
<span class="f4"><span class="f2">scummvm                                           111 d</span></span>
<span class="f4"><span class="f2"><span class="f2">minigalaxy                                        118 d</span></span></span>
<span class="f4"><span class="f2"><span class="f2"><span class="f4">spicetify                                         567 d</span></span></span></span>
<span class="f4"><span class="f2"><span class="f2"><span class="f4"><span class="f7">yay                                                 0 d</span></span></span></span></span>
<span class="f4"><span class="f2"><span class="f2"><span class="f4"><span class="f7"><span class="f4">metacity                                          680 d</span></span></span></span></span></span>
<span class="f4"><span class="f2"><span class="f2"><span class="f4"><span class="f7"><span class="f4"><span class="f4">catfish                                           471 d</span></span></span></span></span></span></span>
<span class="f4"><span class="f2"><span class="f2"><span class="f4"><span class="f7"><span class="f4"><span class="f4"><span class="f4">opendune                                          372 d</span></span></span></span></span></span></span></span>
<span class="f4"><span class="f2"><span class="f2"><span class="f4"><span class="f7"><span class="f4"><span class="f4"><span class="f4"><span class="f1"><span class="bold">htop                                              838 d</span></span></span></span></span></span></span></span></span></span>
<span>[0.00246 seconds elapsed]</span>
</pre>

<pre>
<span class="f0">$ dotclean -d -c 500
Options(files=False, directories=True, exclude=None, nocolor=False, clean=500)
/home/test/.config</span>
<span class="f4">qpdfview                                          576 d ... nominated.</span>
<span class="f4"><span class="f2">scummvm                                           111 d</span></span>
<span class="f4"><span class="f2"><span class="f2">minigalaxy                                        118 d</span></span></span>
<span class="f4"><span class="f2"><span class="f2"><span class="f4">spicetify                                         567 d ... nominated.</span></span></span></span>
<span class="f4"><span class="f2"><span class="f2"><span class="f4"><span class="f7">yay                                                 0 d</span></span></span></span></span>
<span class="f4"><span class="f2"><span class="f2"><span class="f4"><span class="f7"><span class="f4">metacity                                          680 d ... nominated.</span></span></span></span></span></span>
<span class="f4"><span class="f2"><span class="f2"><span class="f4"><span class="f7"><span class="f4"><span class="f4">catfish                                           471 d</span></span></span></span></span></span></span>
<span class="f4"><span class="f2"><span class="f2"><span class="f4"><span class="f7"><span class="f4"><span class="f4"><span class="f4">opendune                                          372 d</span></span></span></span></span></span></span></span>
<span class="f4"><span class="f2"><span class="f2"><span class="f4"><span class="f7"><span class="f4"><span class="f4"><span class="f4"><span class="f1"><span class="bold">htop                                              838 d ... nominated.</span></span></span></span></span></span></span></span></span></span>
<span>[0.00241 seconds elapsed]</span>
</pre>

<pre>
<span class="f0">$ env DOTCLEAN=1 dotclean -d -c 500
Options(files=False, directories=True, exclude=None, nocolor=False, clean=500)
File deletions enabled.
/home/test/.config</span>
<span class="f4">qpdfview                                          576 d Deleting directory: /home/test/.config/qpdfview ... deleted!
<span class="f2">scummvm                                           111 d</span></span>
<span class="f4"><span class="f2"><span class="f2">minigalaxy                                        118 d</span></span></span>
<span class="f4"><span class="f2"><span class="f2"><span class="f4">spicetify                                         567 d Deleting directory: /home/test/.config/spicetify ... deleted!
<span class="f4">metacity                                          680 d Deleting directory: /home/test/.config/metacity ... deleted!</span></span></span></span></span>
<span class="f4"><span class="f2"><span class="f2"><span class="f4"><span class="f4"><span class="f4">catfish                                           471 d</span></span></span></span></span></span>
<span class="f4"><span class="f2"><span class="f2"><span class="f4"><span class="f4"><span class="f4"><span class="f4">opendune                                          372 d</span></span></span></span></span></span></span>
<span class="f4"><span class="f2"><span class="f2"><span class="f4"><span class="f4"><span class="f4"><span class="f4"><span class="f1"><span class="bold">htop                                              838 d Deleting directory: /home/test/.config/htop ... deleted!</span></span></span></span></span></span></span></span></span>
<span>[0.00157 seconds elapsed]</span>
</pre>