# Cold Compress Inside
###### Forensics - 100 points
For this challenge we were provided with an [image](COLD_COMPRESS.jpg) to analyse.

Upon running `binwalk` 2 files were extracted. `o` and `o.exe`

I ran strings on `o` and found an interesting string that then incapsulated with SHELL{} made the flag.

```
CRazy_MosQUIto_nEEDS_odoMOS
```

### Attachments
[COLD_COMPRESS.jpg](COLD_COMPRESS.jpg)