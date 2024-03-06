# MERLOT PDF Generation Service
This repository contains the XFSC Federated Catalogue schemas for service offerings and participants that are used in the MERLOT marketplace.

It also contains the necessary build files to build the catalogue as well as the XFSC Self-Description Wizard API with these shapes pre-loaded.

## Structure

```
├── catalog-shapes/shacl
│   ├── ontology                    # ontology files for the catalog
│   ├── shapes                      # shape files for the catalog
│   │   ├── gax-core                # shapes based on gax-core in version v22.10
│   │   ├── gax-trust-framework     # shapes based on gax-trust-framework in version v22.10
│   │   ├── merlot                  # merlot-specific shapes based on the Gaia-X v22.10 shapes
├── gxfs-catalog                    # build files for the XFSC Federated Catalogue
├── sd-creation-wizard-api          # XFSC Self-Description Wizard API
```
