# UbuntuKeyboardShortcuts

keyboard macro scripts for ubuntu

## Supported OS

- literally `linux` with `X11` only so far, it's tested on `ubuntu 22.04`

## Python Version

- tested on python `>=` `3.12.0`

## Designed Concepts

- make the traditional keyboard to a macro keyboard
- define your own `combination_trigger_key` (`ctk`), and the keyboard event listener will detect if any event is
  triggerred by any combination start with `ctk` key pressed
- `ctk` is designed as a modifier (`mod3`) key, in order to execute combination easily, also `mod3` is designed for
  customization by default to the OS

## Set up your `mod3` key, by `xmodmap`

please see the file [.Xmodmap_src](.Xmodmap_src), the content is an example from my use case.
for more information, please refer to the [xmodmap wiki](https://github.com/jet-c-21/UbuntuKeyboardMacros/wiki/xmodmap)

#### you can use `xev` or `sudo evtest` to your preferred key to be replaced as `ctk`

### create `.Xmodmap` file

```shell
cp -r .Xmodmap_src ~/.Xmodmap && xmodmap ~/.Xmodmap
```

#### verify if `mod3` is defined

```shell
xmodmap -pm
```

#### you can create a Startup Application to let `xmodmap` to reload the config every boot

![Reload-Xmodmap-File-Startup-Application-Example.png](https://hackmd.io/_uploads/Sk5Ld8T4yg.png)






