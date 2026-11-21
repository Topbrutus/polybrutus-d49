# Polybrutus 49D: Exact 54-point Euclidean metric and a forty-threefold ideal graph mode

**Gabriel St-Pierre** — Independent researcher
**21 November 2026**
**Exact mathematical case study / scientific preprint**
**AI assistance:** OpenAI ChatGPT (Astra) materially assisted two independently implemented exact programs, rational calculations, manuscript and publication. AI is not a scientific author.

## Abstract

We construct an exact Euclidean labelled squared-distance metric for 54 norm-one points by adding one independent perpendicular unit vertex to the frozen Polybrutus 48D metric [1]. All 1378 old labelled pairs are preserved and 53 new squared distances equal 2R² at unit radius, for 1431 unordered labelled pairs. The uniquely centered Euclidean Gram is positive semidefinite rank 49, proving minimum affine Euclidean realization dimension 49 for this specified synthetic metric. For a separately freely stipulated ideal complete weighted graph with unit scalar masses and w_ij=1/d_ij², exact Laplacian eigenspaces have eigenvalue 27 of multiplicity 43 and 53/2 of multiplicity 4. Two independently implemented exact rational programs verify all labelled distances, ancestor bytes, Gram ranks and graph nullities. No physical frequency or extra spacetime dimensions are demonstrated.

## 1. Authentic immutable scientific ancestry

The sole immediate parent is St-Pierre, Polybrutus 48D [1], DOI 10.5281/zenodo.24426580, frozen source Topbrutus/polybrutus-d48@v0.1.0, actual Git commit 02e51ca0e0cdb1b30068320c4595e36cc27afc43. The complete original D48 source ZIP is included byte-identically at prior/d48/frozen_scientific_tag_v0.1.0.zip (2572142 bytes, 31 entries, CRC PASS, SHA-256 c16887eb209c98085770908af744550d9b699abb92f96a36226d041799d3f4a8), with all earlier nested original source archives. The original D48 certificate is preserved byte-identically under prior/d48/results/certificate_d48.json, SHA-256 1da9a1f3030ca4e6590067830ea29cff524379317cef8b3ffc6a1570754077ce. Two independent checkers authenticate the archive SHA-256, ZIP CRC and original certificate bytes.

Embed each of the 53 parent norm-one vectors p_i into one higher coordinate space as q_i=(p_i,0). Add q_54 perpendicular to all the old vectors and norm one. Every old pairwise squared distance is unchanged, including its labels. Each new squared distance is ||q_54-q_i||²=1+1-0=2 for R=1. Thus C(54,2)=1431=1378+53 exact unordered labelled pairs. This constructs one synthetic Euclidean extension.

## 2. Gram matrices and complete distance audit

Seven canonical rational unit vertices produce rank-three Gram G_core, while five independent centered unit simplex points produce rank four, unit diagonal, and all mutual products -1/4. Forty-two further independent orthogonal unit axes yield rank 3+4+42=49 for full Gram G. The block construction is positive semidefinite by explicit rational vector realization and all diagonal entries are one.

Let D be the exact squared-distance matrix with zero diagonal and D_ij=2-2G_ij. Center by H=I-11ᵀ/54. Then B=-(1/2)HDH=HGH is PSD and exact rank 49. Inherited canonical antipodal vertices ensure origin belongs to the affine hull, proving minimum Euclidean affine dimension 49 for this complete labelled metric, with 50 storage coordinates.

The complete exhaustive normalized histogram k=4d²/R² at R=1 is 4:6, 7:2, 8:1400, 9:3, 10:10, 12:6, 13:2, 16:2, totaling 1431 labelled unordered pairs. The exact sum of all squared pair distances is 11495/4. All 1378 predecessor labelled values are compared against the authenticated frozen D48 certificate. Matching a histogram alone would not establish label conservation.

## 3. Separately selected ideal weighted graph

Take scalar unit vertex masses and define graph edge weights w_ij=1/d_ij², not physically measured couplings. Each new perpendicular unit vertex connects to each of the 53 old vertices at weight 1/2. The Laplacian has exact block form L49=[[L48+I53/2,-1_53/2],[-1_53ᵀ/2,53/2]] and characteristic-polynomial recurrence chi54(z)=z(z-27)chi53(z-1/2)/(z-1/2). With inherited nonzero seven-point factor f6(z)=chiP7(z)/z, the chosen-model expression is chi54(z)=z(z-27)^43(z-53/2)^4*f6(z-47/2).

Independent rational rank/nullity computations verify Laplacian eigenvalue 27 of multiplicity 43 and eigenvalue 53/2 of multiplicity 4. These are dimensionless graph modes. No acoustic frequency, physical oscillator, particle mass or additional physical spacetime dimension follows from their numerical labels.

## 4. Independent verification and falsification

The primary src/verify_d49.py constructs the exact rational Gram and full distance matrix with SymPy, checks all 1431 labelled pairs, inherited 1378 pair labels, ancestor original ZIP SHA/CRC, parent certificate and exact centered Euclidean rank. Four adversarial controls detect an altered pair, duplicated point, nonorthogonal tilt, and histogram-preserving relabelling. The separately implemented tests/independent_d49.py computes squared distances via Python fractions.Fraction without importing the Gram constructor, independently reconstructs all labels and checks centered Gram and ideal graph spectral nullities. Both produce an identical SHA-256 of deterministic results/certificate_d49.json; continuous integration repeats them.

Older D47 publication has a previously disclosed incorrect *textual* reference to its own D46 Git parent commit; it is preserved unchanged inside the original nested archives. The immediate D48 tag and D48 certificate used here were independently authenticated. No historical data is silently corrected.

## 5. Scientific scope and bibliographic metadata

This is one freely specified exact synthetic Euclidean metric and a separately selected ideal graph. Orthogonal Euclidean completions and uniform graph joins are established constructions. We do not claim new laws, independently peer-reviewed discoveries, measured hertz, particles or extra physical dimensions. The code requires Python 3.12 and sympy==1.14.0.

Zenodo must carry a structured isDerivedFrom relation to the D48 DOI 10.5281/zenodo.24426580; separately its references field must cite both immediate parent D48 [1] and historical original Polybrutus 7D [2]. Metadata keywords must use current dimension forty-nine and ideal graph multiplicity forty-threefold, verified after public publication.

## References

[1] St-Pierre, Gabriel (2026). Polybrutus 48D: Exact 53-Point Euclidean Metric and Forty-Twofold Ideal Graph Mode. Zenodo. DOI: 10.5281/zenodo.24426580. https://doi.org/10.5281/zenodo.24426580

[2] St-Pierre, Gabriel (2026). Polybrutus 7D: An Exact Twelve-Point Orthogonal Completion, the 12-35-37 Identity, and an Oscillator Model. Zenodo. DOI: 10.5281/zenodo.24407952. https://doi.org/10.5281/zenodo.24407952

[3] St-Pierre, Gabriel (2026). Polybrutus D48 original frozen scientific source v0.1.0. GitHub: https://github.com/Topbrutus/polybrutus-d48/tree/v0.1.0; commit 02e51ca0e0cdb1b30068320c4595e36cc27afc43. Complete original ZIP is embedded intact.
