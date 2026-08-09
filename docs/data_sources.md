1. [NiCOlit](https://github.com/julschleinitz/NiCOlit/tree/master) (2000 reactions) Ni catalyzed C-O coupling dataset. 

issues: both analytical and isolated yields

Schema:

|  # | Column name                   | Data type | Nullable | Metadata |
| -: | ----------------------------- | --------- | -------- | -------- |
|  0 | `substrate`                   | String    | YES      |          |
|  1 | `coupling_partner`            | String    | YES      |          |
|  2 | `effective_coupling_partner`  | String    | YES      |          |
|  3 | `solvent`                     | String    | YES      |          |
|  4 | `time`                        | String    | YES      |          |
|  5 | `temperature`                 | String    | YES      |          |
|  6 | `catalyst_precursor`          | String    | YES      |          |
|  7 | `reagents`                    | String    | YES      |          |
|  8 | `effective_reagents`          | String    | YES      |          |
|  9 | `effective_reagents_covalent` | String    | YES      |          |
| 10 | `reductant`                   | String    | YES      |          |
| 11 | `ligand`                      | String    | YES      |          |
| 12 | `effective_ligand`            | String    | YES      |          |
| 13 | `product`                     | String    | YES      |          |
| 14 | `analytical_yield`            | String    | YES      |          |
| 15 | `isolated_yield`              | Float64   | YES      |          |
| 16 | `coupling_partner_class`      | String    | YES      |          |
| 17 | `DOI`                         | String    | YES      |          |
| 18 | `origin`                      | String    | YES      |          |
| 19 | `eq_substrate`                | String    | YES      |          |
| 20 | `eq_coupling_partner`         | String    | YES      |          |
| 21 | `eq_catalyst`                 | String    | YES      |          |
| 22 | `eq_ligand`                   | String    | YES      |          |
| 23 | `eq_reagent`                  | String    | YES      |          |
| 24 | `2_steps`                     | Bool      | YES      |          |
| 25 | `scheme_table`                | String    | YES      |          |
| 26 | `review`                      | String    | YES      |          |
| 27 | `Mechanism`                   | String    | YES      |          |

2. [OpenExp](https://osf.io/e68v4/files/3dv4k) 
open-source dataset of chemical reactions paired with structured experimental procedures.
https://aclanthology.org/2024.findings-acl.318/

The dataset contains 274,439 reaction–procedure pairs. It was created from:
- USPTO-Applications — patent reactions
- Open Reaction Database (ORD) — experimental reactions

3. AstraZeneca ELN derived dataset https://github.com/nsf-c-cas/yield-rxn/blob/master/data/az/processed-0/az_no_rdkit.csv

source_dataset:
    AstraZeneca ELN Buchwald–Hartwig

source_repository:
    nsf-c-cas/yield-rxn

raw_records:
    1000

paper_curated_records:
    781

ML_processed_records:
    750

reaction_class:
    Buchwald–Hartwig C–N coupling

yield:
    numerical percentage

4. https://github.com/rxn4chemistry/rxn_yields/blob/master/README.md#uspto-data-sets 

5. https://github.com/blaiszik/awesome-matchem-datasets/blob/main/README.md
