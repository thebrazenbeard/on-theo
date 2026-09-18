# On-Theo Promotion Candidate Construction V2

Status: `AUTHORIZED_TO_CONSTRUCT_DRAFT / NO CANONICAL EFFECT`

Controlling subject:
- PR #31
- head `d81ab5ab58f326b0827dbc0f9903befb5580947e`
- tree `e6e94b7ed35551ca675fed64ce2a0999ea441628`

V2 supersedes the PR30 source-control binding in V1. The registry output bytes remain the reviewed PR30 rehearsal bytes because PR31 changes validation/control code and the successful PR31 rehearsal reproduces all eight output registry SHA-256 values exactly.

Construction algorithm:
1. create a fresh candidate branch from PR31 exact head;
2. copy the source manifest and all 20 active extension YAML files byte-for-byte to the collision-free `provenance/materialization-input-v1/` namespace described by `receipts/ON_THEO_PROMOTION_INPUT_ARCHIVE_PLAN_V1.yaml`;
3. verify archived Git/file bytes against the recorded SHA-256 values before removing active copies;
4. run the PR31 materializer to generate the eight active registry outputs;
5. require exact equality with the V2 gate digest set;
6. remove active extension YAMLs after archival verification so the empty materialized manifest has no validator-visible orphan extensions;
7. preserve all other repository paths unchanged;
8. add a candidate receipt with source/control head, input archive bindings, exact outputs, counts, test/validator results, role-review dispositions, and effect boundary;
9. open a draft PR only after exact readback.

The candidate is a reviewable byte proposal, not canonical materialization.
