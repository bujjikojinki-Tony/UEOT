# UEOT WP-01 Evidence Baseline Audit

Date: 2026-11-24. Status: PARTIAL_EVIDENCE / NOT_VERIFIED.

## Evidence classes

- Formal Baseline Release Note dated 2026-09-03: located in private research files. Five normative master documents and verbatim 12 axioms remain outstanding. Private files are not published here.
- Theory Whitepaper V13 discussion HTML: located; historical discussion, not frozen master.
- Industrial collaboration V12.9 HTML and app.js: located; historical reference implementation, not production validation.
- Research integration report V1.0: located; non-normative research synthesis.
- Current repository: experimental synthetic implementation, distinct from original reference implementation.

## Current repository blob inventory

| Path | Git blob SHA | Test methods |
|---|---|---:|
| runtime/ueot_runtime.py | 750a8cb8d78db97ef7a6165cd1fcc7516a4f6f9f | 0 |
| runtime/governance.py | eeba7f1463d9a4843a7737ab9d1f41ad2f06d967 | 0 |
| runtime/gateway.py | 19612d01fee56a5082ac175265b6e3adb86b381b | 0 |
| runtime/http_demo.py | 9bd71dab7718c615d622216a5115c375643cce7b | 0 |
| tests/test_findings.py | d5d319988872c1937e782ce8008c52fde4a42211 | 8 |
| tests/test_governance.py | d64fd6e428cfbfc2b74086ef150691c61ea8bae9 | 8 |
| tests/test_gateway.py | 8f71a140932c10e96aca8f7530b449be90d0d065 | 9 |
| tests/test_http_demo.py | d70af340355d24cd3e9ed2db699f89ebe318a879 | 7 |
| browser/index.html | 55174d5d4d80c0239b9c20010b9a77fd5c9a6f6e | 0 |
| index.html | 7add4d75b20c104bf78f5110500aade12ddd536f | 0 |
| .github/workflows/pages.yml | 0141ff7bf03a254ab4b58dbf7e1ffeba96302756 | 0 |

Git blob identifiers are not raw-file SHA256 digests. Test method counts are not execution counts.

## Historical evidence accounting

Release Note reports 107 formal baseline tests and 45 later package-local executions (152 observed executions, not 152 unique tests). Original execution logs not independently obtained. No industrial validation claim.

## Finding traceability (requirements from Release Note)

| Finding | Required semantic behavior | Current verification |
|---|---|---|
| F-R2-001 | STOP target excluded from PotentialImpactSet | NOT_VERIFIED |
| F-R3-001 | Half-open effectivity and AMBIGUOUS identity | NOT_VERIFIED |
| F-R3-002 | BasisConsistency conflict gate | NOT_VERIFIED |
| F-R3-003 | GovernanceEscalation; precedence defined by Profile | NOT_VERIFIED |
| F-R3-004 | Unresolved configuration blocks definitive answer | NOT_VERIFIED |
| F-R3-005 | TemporaryApplicableBasis distinct from DesignBasis | NOT_VERIFIED |

## Release gates

- Obtain five controlled master documents and original test logs; record provenance and hashes.
- Freeze exact source commit and execute current synthetic tests, retaining actual output and environment metadata.
- Independently compare implementation against frozen contract and all six Findings.
- Pages deployment failure remains unresolved; website availability is separate from conformance.
- Real SSC pilot requires 20–100 UEO, three lifecycle stages, two configurations, one ECR and one NCR/Deviation chain; compare traditional, naive graph and UEOT; UnsafeDefinitiveClaimRate=0.

Decision: GO for evidence recovery and experimental regression; NO-GO for formal conformance or industrial acceptance.
