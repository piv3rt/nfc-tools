# NFC Tools

This repository contains useful python scripts for NFC tags

### mifare-1k-diff
Compare two MIFARE 1k dumps

Try it!
> python mifare-1k-diff tags/mifare-1k-blank tags/mifare-1k-locked

### mifare-1k-safe
Edit MIFARE 1k access conditions to avoid locked keys

Try it!
> python mifare-1k-safe tags/mifare-1k-locked tags/mifare-1k-unlocked
