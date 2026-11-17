# Rhino Hunt | Digital Forensic Investigation 001

**Examiner:** Andrew Jones · **Case:** DF-2026-001 · **Examined:** November 16, 2026  
**Type:** Simulated training investigation (not a real criminal case)

## Overview

I examined the publicly available DFRWS 2005 Rhino Hunt training dataset to reconstruct activity across a USB disk image and three network captures. The primary objective was to identify at least nine distinct rhinoceros photographs in the supplied evidence.

**Result:** Nine image recovery occurrences yielded eight distinct SHA-256 hashes: four from the USB image, two from FTP traffic, two from HTTP traffic, and one from a password-protected archive. The archive image is byte-identical to a USB exhibit. The nine-distinct-image objective remains open.

## Tools and techniques

| Tool | How I used it |
| --- | --- |
| Autopsy 4.23.1 | File-system examination, file carving, metadata inspection, and evidence tagging |
| Wireshark | Protocol hierarchy, FTP authentication and transfers, TCP stream analysis, and object extraction |
| 7-Zip | Archive inspection and examination of a suspicious executable without further execution |
| John the Ripper 1.9.0-jumbo-1 | Offline password recovery from an authorized training ZIP archive |
| PowerShell | Read-only executable header and version-resource inspection |

## Key findings

- Recovered four rhino images from the USB evidence and five network-related image occurrences; one was an exact duplicate of a USB exhibit.
- Recovered a carved Word document describing possible destruction of digital evidence; original file-system timestamps were unavailable.
- Identified a repeated-text pattern in unallocated space consistent with possible overwriting, while noting that carving may combine contiguous regions.
- Correlated the diary's reference to the `gnome` account with a successful FTP login observed in packet 1538 of `rhino.log`; transfer records included upload commands and server success responses.
- Recovered an encrypted archive containing `rhino2.jpg`, derived its password verification data, and recovered the password using a dictionary attack. Confirmed successful extraction by independently matching the entry's uncompressed size and CRC32.
- Found `rhino.exe`, whose embedded version information identified it as a Microsoft DiskPart application. This finding does not establish authenticity or prove that it was used to erase a disk.

## Verified recovered exhibit

| Property | Value |
| --- | --- |
| Entry | `rhino2.jpg` |
| Uncompressed size | 230,665 bytes |
| CRC32 | `936EBE65` |
| SHA-256 | `b4f6bbb8d846d6505c9b5b67f115656fdf980a484aa441078a838a3ffc2ac705` |

## Report

[Read the full nine-page digital forensic examination report (PDF)](reports/Rhino-Hunt-DF-2026-001-Full-Examination.pdf).

The report includes an evidence register, findings, packet references, recorded PowerShell/John commands, reproducible Wireshark filters, and independently calculated hashes.

[SHA-256 exhibit inventory](docs/exhibit-inventory.md) · [Network verification notes](docs/verification.md) · [Case-specific verification script](analysis/verify_network.py)

## Dataset and limitations

Public training evidence: [NIST CFReDS — Rhino Hunt (DFRWS 2005)](https://cfreds-archive.nist.gov/dfrws/Rhino_Hunt.html). This portfolio describes a fictional investigation and is not a professional certification, original evidence acquisition, or determination of guilt. I have not published raw evidence, recovered passwords, or executable samples. All three uploaded network capture MD5 hashes were independently compared with the published values and matched. The USB source was not independently verified. The supplied exhibit inventory records eight distinct SHA-256 hashes among nine recovery occurrences. The ninth distinct image and source USB image hash remain unverified. Distinct hashes alone do not establish visual uniqueness.

## Skills demonstrated

Digital evidence examination · File carving · File-system metadata · Network forensics · FTP and HTTP object recovery · Password recovery · Evidence integrity validation · Findings documentation · Critical interpretation
