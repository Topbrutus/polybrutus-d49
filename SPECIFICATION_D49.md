# Polybrutus D49 — Exact rational metric specification

**Direct scientific parent:** frozen Topbrutus/polybrutus-d48@v0.1.0, commit 02e51ca0e0cdb1b30068320c4595e36cc27afc43, DOI 10.5281/zenodo.24426580. Original full ZIP SHA-256 c16887eb209c98085770908af744550d9b699abb92f96a36226d041799d3f4a8; original certificate SHA-256 1da9a1f3030ca4e6590067830ea29cff524379317cef8b3ffc6a1570754077ce.

## Conservative labelled Euclidean extension

Zero-embed the 53 D48 norm-one vectors p_i as q_i=(p_i,0), then append one unit vector q_54 orthogonal to all old points. Every old squared distance remains unchanged. Each of 53 new squared distances is 2R². Hence C(54,2)=1431=1378+53 exact unordered labelled pairs.

Rational Gram G: canonical seven-point rank-three Gram block, independent centered five-point unit-simplex rank-four block (unit diagonal, off-diagonal -1/4), and 42 mutually independent orthogonal unit axes. This is an explicit PSD rational Gram factorization: rank G=3+4+42=49, every diagonal value 1. D_ij=2-2G_ij with zero diagonal. H=I-11ᵀ/54 and B=-HDH/2=HGH is PSD exact rank 49. Inherited antipodal points put the origin in the affine hull. Therefore minimum affine Euclidean realization dimension 49; ambient storage coordinates 50.

Unit-radius histogram k=4d²/R²: 4:6, 7:2, 8:1400, 9:3, 10:10, 12:6, 13:2, 16:2, 1431 pairs. Exact sum of squared distances: 11495/4.

## Separately stipulated ideal weighted complete graph

Choose scalar unit masses, symmetric positive weights w_ij=1/d_ij². The added unit point contributes 53 new edges of weight 1/2. The Laplacian block is L49=[[L48+I53/2,-1_53/2],[-1_53ᵀ/2,53/2]]. Exact characteristic recurrence:
chi54(z)=z(z-27)chi53(z-1/2)/(z-1/2).
Inherited seven-point factor f6(z)=chiP7(z)/z gives chosen-model expression
chi54(z)=z(z-27)^43(z-53/2)^4*f6(z-47/2).
Exact rational nullities show eigenvalue 27 multiplicity 43 and eigenvalue 53/2 multiplicity 4.

**References:** parent D48 DOI 10.5281/zenodo.24426580 and historical D7 DOI 10.5281/zenodo.24407952.
**Limits:** One exact synthetic Euclidean metric and a separately stipulated dimensionless ideal weighted graph. This is not evidence for physical extra dimensions, observed frequencies, particles or a novel universal theorem, and it is not independently human peer reviewed.
