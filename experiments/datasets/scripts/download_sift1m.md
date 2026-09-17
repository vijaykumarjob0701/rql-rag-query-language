# Download SIFT1M — see companion repro

Canonical instructions + script:

- [`rql-repro/datasets/scripts/download_sift1m.md`](../../../../rql-repro/datasets/scripts/download_sift1m.md) (local)
- [`rql-repro/datasets/scripts/download_sift1m.sh`](../../../../rql-repro/datasets/scripts/download_sift1m.sh)

**Preferred:** Hugging Face `qbo-odp/sift1m` HTTPS.  
**Fallback:** IRISA FTP `sift.tar.gz`.  
**Dead:** TexMex HTTPS (SSL/404 as of 2026-09-17).

```bash
bash /workspace/rql-repro/datasets/scripts/download_sift1m.sh
# or from a rql-repro checkout:
bash datasets/scripts/download_sift1m.sh
```
