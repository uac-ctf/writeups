# Hidden inside
###### Forensics - 50 points
For this challenge we were provided with an [image](mystic-fairy-girl-magical-dark-cgi-3840x2558-5287.jpg) to analyse.


I was able to find the flag with [zsteg](https://github.com/zed-0xff/zsteg)

```
$ zsteg mystic-fairy-girl-magical-dark-cgi-3840x2558-5287.jpg
imagedata           .. file: VAX-order 68k Blit mpx/mux executable
b1,r,lsb,xy         .. text: "NarUTO_Is_hokaGE"
b1,abgr,msb,xy      .. file: PGP Secret Sub-key -
b2,r,msb,xy         .. text: "z@(Z}v-J"
b2,g,lsb,xy         .. text: "'vV4Mc$v)7"
b2,g,msb,xy         .. text: "zA(Z}}-J"
b3,bgr,msb,xy       .. text: "F7JNF8qb"
b3,abgr,msb,xy      .. text: "g{6G|DGt6gs"
b4,r,lsb,xy         .. text: "c$UR%R$C#5D2%E#%C#\#$C$UU#EUU%DR'C3B5'CS"
b4,r,msb,xy         .. text: "\"Ll*\"bNd**"
b4,g,lsb,xy         .. text: "tEUTET5dDEUDEUDES4C5TEUU4UUVEVdGd4TE7SS"
b4,rgb,lsb,xy       .. text: "H$eWUrF#TWF"
b4,bgr,lsb,xy       .. text: "XBd'UuVBS'T"
b4,rgba,lsb,xy      .. text: "4o$o4o4oU"

```

```
SHELL{NarUTO_Is_hokaGE}
```

### Attachments
[mystic-fairy-girl-magical-dark-cgi-3840x2558-5287.jpg](mystic-fairy-girl-magical-dark-cgi-3840x2558-5287.jpg)
###### 2021 - methane4