1. [NiCOlit](../data/nicolit/NiCOlit.csv) (2000 reactions) Ni catalyzed C-O coupling dataset. 

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

