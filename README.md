Themix GUI designer
=====

[![Code Style](https://github.com/themix-project/oomox/actions/workflows/ci.yml/badge.svg)](https://github.com/themix-project/oomox/actions/workflows/ci.yml) [![Commit Activity](https://img.shields.io/github/commit-activity/y/themix-project/themix-gui?color=pink&logo=amp&logoColor=pink)](https://github.com/themix-project/themix-gui/graphs/commit-activity)

Graphical application for designing themes and exporting them using plugins, for example:
  * [Oomox](https://github.com/themix-project/oomox-gtk-theme/) and [Materia](https://github.com/nana-4/materia-theme/) themes (GTK2, GTK3, Cinnamon, GNOME, Openbox, Xfwm). Have a hack for HiDPI in gtk2.
  * Icons ([Archdroid](https://github.com/GreenRaccoon23/archdroid-icon-theme), [Gnome-Colors](https://www.gnome-look.org/p/1012497), [Numix](https://github.com/numixproject/numix-folders), [Papirus](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme), [Suru++](https://github.com/gusbemacbe/suru-plus) and [Suru++ Asprómauros](https://github.com/gusbemacbe/suru-plus-aspromauros)).
  * Base16 plugin, which  also allows a lot of app themes support like Alacritty, Emacs, GTK4, KDE, VIM and [many](https://github.com/chriskempson/base16-templates-source) more.

Import plugins also available, such as:
  * generating color palettes from image;
  * importing it from Xresources;
  * or [huge](https://github.com/chriskempson/base16-schemes-source/) collection of Base16 themes.

<a href="https://aur.archlinux.org/packages/themix-full-git"><img src="https://raw.githubusercontent.com/themix-project/oomox/master/packaging/download_aur.png" height="54"></a>
<a href="https://slackbuilds.org/result/?search=oomox&sv="><img src="https://raw.githubusercontent.com/themix-project/oomox/master/packaging/download_slackware.png" height="54"></a>
<a href="https://flathub.org/apps/details/com.github.themix_project.Oomox"><img src="https://flathub.org/assets/badges/flathub-badge-en.png" height="54"></a>
<a href="https://github.com/Botspot/pi-apps"><img src="https://github.com/Botspot/pi-apps/blob/master/icons/badge.png?raw=true" height="53" style="border-radius: 9px; border: 1px #bbb solid;"></a>


Table of contents:
  * [Installing with package manager](#installation "")
  * [Installing manually](#other-distributions "")
  * [CLI](#cli "")
  * [Spotify](#spotify "")
  * [Extra GTK3 CSS hacks](#extra-gtk3-css-hacks "")
  * [Using with tiling WMs](#using-with-tiling-wms "")
  * [Wiki](#wiki "")
  * [Review videos/Usage instructions](#review-articles-and-videos "")

![Screenshot image import](https://raw.githubusercontent.com/themix-project/oomox/master/screenshots/pokedex_dawn.png "Screenshot image import")

![Screenshot GUI](https://raw.githubusercontent.com/themix-project/oomox/master/screenshots/screenshot_gui.png "Screenshot GUI")

[Big screenshot with number of generated themes 🔗](http://orig15.deviantart.net/e1ee/f/2016/320/1/9/oomox_1_0_rc1_by_actionless-daomhmd.jpg)

[Latest Oomox GTK theme screenshots 🔗](https://github.com/themix-project/oomox-gtk-theme/tree/master/screenshots)



## Installation



### Arch Linux

#### Install

```
pikaur -S themix-full-git
```

AUR helpers are [not officially supported by Arch Linux](https://wiki.archlinux.org/index.php/AUR_helpers), so you can also [install it manually](https://wiki.archlinux.org/index.php/Arch_User_Repository#Installing_packages) from [rolling-release PKGBUILD](https://aur.archlinux.org/packages/themix-full-git/).

#### Open the GUI

```
themix-gui
```



### Debian, Ubuntu, Linux Mint

##### deb-based releases are currently abandoned, this way works for installing older versions of Themix
see also: https://github.com/themix-project/oomox/issues/144

[Old instructions for Deb-like distros](https://github.com/themix-project/themix-gui/blob/master/docs_markdown/Ubuntu_Old.md)



### Other distributions

[Install it manually or use that information for creating a package for your distro](https://github.com/themix-project/themix-gui/blob/master/docs_markdown/Manual_Installation.md)




### CLI


#### Multi-Export CLI


```sh
themix-multi-export --help
```

or

```sh
./multi_export_cli.sh --help
```

Example multi-export config file could be found in `./export_config_examples` directory of this git repository.

When using Multi-Export from GUI your multi-export layout would be automatically saved to `~/.config/oomox/export_config/multi_export_*.json` files.


#### Theme/Icon Plugins CLI

If your prefer CLI interface, refer to `change_color.sh` scripts inside `./plugins/`. For `xresources` and `random` themes in CLI use palettes from `/opt/oomox/scripted_colors/` directory. Using scripted palettes enables you to use bash to write simple generators for dynamic themes (as alternative to plugins in oomox-gui). GUI is not attempting to execute any scripted palettes with bash because downloading such scripted themes from random places could lead to unexpected result so you can use them only with CLI, when you really know what you're doing.


#### Base16 export CLI

In the directory with Base16 plugin you could run the CLI as well:
```
python cli.py --help
```


#### Spotify:

Spotify theme can be also exported from GUI, but if you prefer commandline interface:

```sh
./plugins/oomoxify/oomoxify.sh ./colors/gnome-colors/shiki-noble
```

Also you can normalize font weight with `-w` argument, see `-h` for usage.

Spotify theme settings are backed up to `~/.config/oomox/spotify_backup`. To undo the changes made by oomoxify, these files can be copied back to their original location `/usr/share/spotify/Apps`. Spotify can also be reinstalled, which will reset these files as well.

Users running Spotify under Flatpak should set their "Spotify path" in oomox to `/var/lib/flatpak/app/com.spotify.Client/current/active/files/extra/share/spotify/Apps` in order to apply the theme.


### Using with tiling WMs

Create/append to `~/.config/gtk-3.0/gtk.css`:

```css
/* remove window title from Client-Side Decorations */
.solid-csd headerbar .title {
    font-size: 0;
}

/* hide extra window decorations/double border */
window decoration {
    margin: 0;
    border: none;
    padding: 0;
}
```


### Extra GTK3 CSS hacks

Create/append to `~/.config/gtk-3.0/gtk.css`:

```css
* {
  text-shadow: none;
}
```

### Wiki

[https://github.com/themix-project/themix-gui/wiki](https://github.com/themix-project/themix-gui/wiki)

Direct file editing:

```
git clone git@github.com:themix-project/themix-gui.wiki.git
```


### Review articles and videos

To learn more about using the application you can check these sources:

  * 2019, [Customizing icon themes animated tutorial](https://github.com/themix-project/oomox/wiki/Customizing-icon-themes)
  * 2019, [How to contribute your theme from Github website](https://github.com/themix-project/oomox/wiki/How-to-contribute-your-theme-from-Github-website)
  * 2019, [How to import and export Base16 themes in Themix/Oomox](https://github.com/themix-project/oomox/wiki/How-to-import-and-export-Base16-themes-in-Themix-Oomox)
  * 2018, https://www.youtube.com/watch?v=XO9QA1njIOM by AddictiveTips
  * https://delightlylinux.wordpress.com/2016/08/22/customize-theme-colors-with-oomox/
  * 2016, https://www.youtube.com/watch?v=Dh5TuIYQ6jo by Spatry
  * http://www.webupd8.org/2016/05/easily-create-your-own-numix-based-gtk.html
  * http://www.webupd8.org/2016/06/tool-to-customize-numix-theme-colors.html
