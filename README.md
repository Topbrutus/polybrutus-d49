# Polybrutus 49D — 54-point Euclidean metric and forty-threefold ideal graph mode

**Human scientific author:** Gabriel St-Pierre, independent researcher.
**AI assistance:** OpenAI ChatGPT (Astra) materially assisted exact rational calculations, two separate verifiers, scientific writing and publication. AI is not the scientific author.

## Official DOI and public release verified

- **DOI:** [10.5281/zenodo.24426743](https://doi.org/10.5281/zenodo.24426743); [public record](https://zenodo.org/records/24426743).
- **Frozen scientific source:** [v0.1.0](https://github.com/Topbrutus/polybrutus-d49/tree/v0.1.0), immutable commit 3b7f96e2e89a5c0c7b0bd9ef8aa83fef1a72c9e0.
- **GitHub scientific main CI:** https://github.com/Topbrutus/polybrutus-d49/actions/runs/44943354007 — success.
- **GitHub immutable tag CI:** https://github.com/Topbrutus/polybrutus-d49/actions/runs/44943405677 — success.
- **Original Zenodo artifacts:** source ZIP, manuscript PDF and deterministic JSON certificate; all three original names/sizes/MD5 publicly verified against SHA-256-checked local originals.
- **Bibliography:** current dimension forty-nine and multiplicity forty-threefold keywords; structured isDerivedFrom DOI D48 10.5281/zenodo.24426580; separate textual references D48 and historical D7 10.5281/zenodo.24407952.
- **Durable Memoria checkpoint:** https://github.com/Topbrutus/topbrutus_one/blob/main/memoria/checkpoints/POLYBRUTUS_D49_PUBLICATION_2026-11-21.md .

## Exact reproducible construction

- 54 norm-one vertices with **1431/1431 exact unordered labelled squared-distance pairs**.
- All **1378/1378 frozen D48 predecessor labels preserved**, plus **53** new squared distances, each **2R²**.
- Gram PSD and centered Gram PSD exact rank **49**, minimum affine Euclidean realization dimension **49** for this one synthetic metric. Storage coordinates: 50.
- Unit-radius histogram k=4d²/R²: 4:6, 7:2, 8:1400, 9:3, 10:10, 12:6, 13:2, 16:2. Sum of all squared distances R=1: **11495/4**.
- Separately chosen ideal complete graph with unit masses and symmetric w_ij=R²/d_ij²: Laplacian eigenvalue **27 multiplicity 43**, eigenvalue **53/2 multiplicity 4**.
- Two independent rational programs (Gram SymPy and direct fractions.Fraction distance rules) and four primary adversarial negative controls.

Reproduce using Python 3.12 and sympy==1.14.0:

    python -m pip install sympy==1.14.0
    python src/verify_d49.py
    python tests/independent_d49.py
    python src/check_zenodo_metadata.py

The two mathematical programs reproduce the same deterministic results/certificate_d49.json byte hash. CI independently reruns them and checks current Zenodo metadata.

## Authentic scientific parent, not a rewrite

**Only scientific parent:** [Polybrutus 48D v0.1.0](https://github.com/Topbrutus/polybrutus-d48/tree/v0.1.0), frozen scientific commit 02e51ca0e0cdb1b30068320c4595e36cc27afc43, DOI [10.5281/zenodo.24426580](https://doi.org/10.5281/zenodo.24426580). The entire original scientific D48 tag ZIP (SHA-256 c16887eb209c98085770908af744550d9b699abb92f96a36226d041799d3f4a8) and its original certificate (SHA-256 1da9a1f3030ca4e6590067830ea29cff524379317cef8b3ffc6a1570754077ce) are copied byte-identically to prior/d48 with all earlier nested archive ancestors. Source archive CRC and original certificate are authenticated by both checkers. Older releases are unchanged.

[Specification](SPECIFICATION_D49.md) | [constructive proof](PREUVE_D49.md) | [provenance](PROVENANCE.md) | [bibliography](REFERENCES.md) | [PDF manuscript](publication/POLYBRUTUS_49D_NOTE.pdf).

Zenodo must contain exact current dimension keyword **forty-nine**, graph multiplicity keyword **forty-threefold**, structured **isDerivedFrom DOI D48** and a *separate* two-entry textual bibliography D48/D7. These are public API readback gates after release.

**Scope:** One exact synthetic Euclidean metric and a separately stipulated dimensionless ideal weighted graph. This is not evidence for physical extra dimensions, observed frequencies, particles or a novel universal theorem, and it is not independently human peer reviewed.
**Licenses:** MIT software, CC BY 4.0 manuscript.
