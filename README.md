# NFC Tools

This repository contains useful python scripts for NFC tags

### mifare-1k-blank
Replace MIFARE sectors with arbitrary data

Try it!
> python mifare-1k-blank -b ff tags/mifare-1k-blank tags/mifare-1k-ff

### mifare-1k-diff
Compare two MIFARE 1k dumps

Try it!
> python mifare-1k-diff tags/mifare-1k-blank tags/mifare-1k-locked

### mifare-1k-safe
Edit MIFARE 1k sector trailer to avoid locking access bits forever

Try it!
> python mifare-1k-safe tags/mifare-1k-locked tags/mifare-1k-unlocked
