# SHA-256 image exhibit inventory

Case DF-2026-001 · Updated November 17, 2026

Ten image recovery occurrences; nine distinct SHA-256 digests and nine visually distinct images. Objective met.

| Exhibit | Source | Filename | SHA-256 |
| --- | --- | --- | --- |
| E-01 | USB | `f0105848_21.jpg` | `568457ed594c4e98dc503e3e244b1e316376aafb0d1c283d95601d13762a748c` |
| E-02 | USB | `f0105864_22.jpg` | `b4f6bbb8d846d6505c9b5b67f115656fdf980a484aa441078a838a3ffc2ac705` |
| E-03 | USB | `f0106320_23.gif` | `8a67d406ed130c9b5447b03fbf9dd0ac6c384a62b5028d6267e92c4abe230a80` |
| E-04 | USB | `f0106344_24.gif` | `71e9f6b94e0496cc634d5d643387c7c1405e2df9deccda1482a8c7cc5ba0b199` |
| E-05 | FTP | `rhino1.jpg` | `0f30a8777d19a4fe4b2fafd5154b6c4dfafb673202db29971e876e978da4e05d` |
| E-06 | FTP | `rhino3.jpg` | `a85aea8e47d9f5425456f3bafb9c67201c8c2b2b2cec80154c83102e802240c5` |
| E-07 | HTTP | `rhino4.jpg` | `e1c01da391669adf3559d2d87bf2157b37e27a936a1ae66c77b61e6b5b7bc4a6` |
| E-08 | HTTP | `rhino5.gif` | `f36ecc12967d5622cdc70e73d2468fab28a65db944d3157256a7212afa05b056` |
| E-09 | Encrypted ZIP | `rhino2.jpg` | `b4f6bbb8d846d6505c9b5b67f115656fdf980a484aa441078a838a3ffc2ac705` |
| E-10 | USB steganography | `rhino6.jpg` | `6dbf775b8999a006ffa74c65127e5add64234184bd2f425b2ad644e8c0d19345` |

## Duplicate and scope

E-02 and E-09 have the same SHA-256 digest. They are counted as separate recovery occurrences but one unique byte sequence. All four tagged USB exports matched their corresponding original report exports; these extra report copies, thumbnails, and interface graphics are excluded from the tally.

The examiner supplied PowerShell SHA-256 outputs for the USB and network image exports. The network hashes match independently reconstructed network payloads; the archive entry hash was independently calculated from the supplied extracted JPEG. The original USB image was subsequently supplied and its reference MD5 matched. Independent carving also reproduced the four USB hashes. E-10 was extracted from `alligator2.jpg` after a guided steganography follow-up and its MD5 matched the published solution. The examiner reports reproducing the dictionary workflow; the exact terminal transcript was not retained. A potential tenth distinct image remains unverified. Different hashes alone do not necessarily imply visually different photographs.

## Reproduction (PowerShell)

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath "C:\Evidence\exhibit.jpg"
```

Compare the full digest against this inventory. Preserve original evidence and hash the full-size exported exhibits, not thumbnails.
