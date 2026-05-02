# Photos

Build and observatory photos referenced from BUILD_JOURNAL.md.

## Naming convention

```
YYYY-MM-DD_description.jpg
```

Examples:
```
2026-05-15_tripod_assembled_patio.jpg
2026-05-15_tripod_height_adjustment.jpg
2026-08-01_dish_assembly_petals.jpg
2026-08-14_first_light_cas_a_spectrum.jpg
```

## Note on file size

Screenshots (GQRX, EZRa, Stellarium spectra) and typical phone
photos are fine to commit directly — the .gitignore excludes
large science data files (.fits, .raw) but not images.

If a photo is unusually large (>10MB), compress it before committing.
Standard phone photos at normal quality settings are typically
2–5MB and commit cleanly.

GitHub renders images inline in Markdown — reference them in
BUILD_JOURNAL.md as:

```markdown
![Caption text](photos/YYYY-MM-DD_description.jpg)
```
