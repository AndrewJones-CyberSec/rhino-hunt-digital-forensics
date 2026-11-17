# Network evidence verification

This is a post-examination corroboration of the public training captures, not a claim that the examiner originally ran the additional script. The parser reads the provided classic little-endian Ethernet PCAP files, reassembles contiguous IPv4 TCP payloads and computes SHA-256 for selected FTP and HTTP objects. It is case-specific, not a general-purpose forensic tool.

## Source hashes

| Source | Frames | MD5 (matches NIST reference) | SHA-256 |
| --- | ---: | --- | --- |
| rhino.log | 6,557 | c0d0093eb1664cd7b73f3a5225ae3f30 | 64e6d55b76660eb3aaa41572c1d04e4452510a343bbf42e844424827dedfddb2 |
| rhino2.log | 370 | cd21eaf4acfb50f71ffff857d7968341 | 41939d5de0556b70279056572dee44b6fd84cd05b0788cfd0b6f52f37b161dde |
| rhino3.log | 295 | 7e29f9d67346df25faaf18efcd95fc30 | 7b0304f5e88a30c305a99b5a1e2977bced5b9c94da6f458f887bb39966bbfc46 |

## Packet references

| Capture | Frames | Finding |
| --- | --- | --- |
| rhino.log | 1538 | Successful FTP authentication for the gnome account |
| rhino.log | 1546 / 1612 | rhino1.jpg upload / completion |
| rhino.log | 1649 / 1737 and 1763 / 1851 | rhino3.jpg uploaded twice; identical data payload SHA-256 |
| rhino.log | 5647 / 5839 | contraband.zip upload / completion |
| rhino2.log | 49 / 50 | HTTP request and successful response for rhino4.jpg |
| rhino2.log | 217 / 219 | HTTP request and successful response for rhino5.gif |
| rhino3.log | 110 / 112 | HTTP request and successful response for rhino.exe |

## Reproduce the post-examination check

Download the original public dataset from [NIST CFReDS](https://cfreds-archive.nist.gov/dfrws/Rhino_Hunt.html), place copies of the three captures under `upload/` in the repository root, and run:

```powershell
Get-FileHash -Algorithm MD5 upload/rhino*.log
Get-FileHash -Algorithm SHA256 upload/rhino*.log
python analysis/verify_network.py
```

The complete payload hash table is in the PDF report. Do not execute recovered binaries. The captures, extracted evidence, and credential material are deliberately excluded from this repository.
