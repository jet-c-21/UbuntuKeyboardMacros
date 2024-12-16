## update xbindkeys with config

```shell
cp ~/my_home/UbuntuKeyboardMacros/.xbindkeysrc_src ~/.xbindkeysrc && \
xbindkeys --poll-rc
```

## clear xbindkeys config

```shell
: > ~/.xbindkeysrc && xbindkeys --poll-rc
```