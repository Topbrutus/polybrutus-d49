#!/usr/bin/env python3
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
c=json.loads((R/'results/certificate_d49.json').read_text('utf8'))
m=json.loads((R/'publication/zenodo_metadata_blueprint.json').read_text('utf8'))
assert c['status']=='PASS' and c['dimension']==m['scientific_dimension']==49
assert c['vertices']==m['norm_one_vertices']==54
assert c['pairs']==m['exact_labelled_squared_pairs']==1431
assert c['affine_rank']==c['centered_gram_rank']==49
assert c['eigenvalue_27_multiplicity']==m['model_eigenvalue_27_multiplicity']==43
assert c['eigenvalue_53_over_2_multiplicity']==m['model_eigenvalue_53_over_2_multiplicity']==4
assert c['parent_tag_commit']=='02e51ca0e0cdb1b30068320c4595e36cc27afc43'
assert c['parent_doi']==m['scientific_parent_doi']=='10.5281/zenodo.24426580'
assert m['related_identifiers']==[{'identifier':'10.5281/zenodo.24426580','relation':'isDerivedFrom','resource_type':'publication-preprint','scheme':'doi'}]
assert len(m['keywords'])==9
assert 'affine Euclidean dimension forty-nine' in m['keywords']
assert 'forty-threefold ideal eigenvalue' in m['keywords']
assert len(m['references'])==2
assert '10.5281/zenodo.24426580' in m['references'][0]
assert '10.5281/zenodo.24407952' in m['references'][1]
assert not any(x in str(m['keywords']) for x in ('thirty-one','twenty-fivefold','forty-eight','forty-twofold'))
doc=(R/'publication/POLYBRUTUS_49D_NOTE.md').read_text('utf8')
assert all(x in doc for x in ('## References','10.5281/zenodo.24426580','10.5281/zenodo.24407952'))
print('D49_ZENODO_KEYWORDS_REFERENCES_PARENT_RELATION_GATE_PASS')
