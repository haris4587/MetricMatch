# MetricMatch v0.3

Challenge software benchmark claims under committed test conditions. GenLayer validators independently authenticate evidence bytes and judge comparability; deterministic code applies the numeric threshold and settles matched GEN stakes.

## Steward security changes

There is no challenge reservation or exclusive challenge slot. Every payable `challenge` authenticates, assesses, records and settles one attempt atomically under full consensus. Inaccessible, changed, unsupported, inconclusive and non-comparable evidence refunds that challenger's deposit and leaves the claim OPEN. A comparable but non-refuting attempt awards only its deposit to the owner and also leaves the claim OPEN. Only a comparable refutation closes the claim and awards the original stake plus the refuting deposit to that challenger. Attempts have no three-retry limit.

`create_claim` requires a SHA-256 digest and exact byte count (1–16000). Validators fetch and authenticate the entire UTF-8 original page, then store its immutable snapshot. All subsequent assessments use that snapshot, never a freshly fetched original URL. Changing or removing the original page cannot change the committed benchmark or block later challenges. Each candidate is authenticated independently against its submitted digest and byte count; changed candidates are refunded. Validators agree on the exact snapshot, authentication reason and semantic verdict before any state changes. Append-only attempt receipts bind the claim commitment, both evidence fingerprints, candidate snapshot, assessment and credited amounts through a decision hash. Failed transactions revert without reserving anything.

## Workflow

1. `create_claim(title, product, metric, claimed_value, unit, lower_is_better, conditions, evidence_url, evidence_sha256, evidence_bytes, challenge_days)`: 1–30 days, payable stake 0–1000 GEN. A missing or changed original source rejects creation.
2. A different address calls `challenge(claim_id, evidence_url, observed_value, evidence_sha256, evidence_bytes)` before the fixed deadline, depositing exactly the original stake. Assessment and settlement happen in that transaction. Invalid attempts cannot monopolize the claim.
3. Read `get_claim`, `get_challenge` (latest receipt), and `get_attempt` (immutable receipt ID). Follow `previous_attempt` to inspect the complete per-claim history.
4. Once the deadline passes, anyone may call `close_unchallenged` on an OPEN claim. It returns the original stake and records CLOSED_UNREFUTED, without certifying the benchmark as true. Invalid attempts never extend the deadline.
5. Credited accounts call `withdraw`. Credit is cleared before emitting the finalized transfer; duplicate withdrawals fail.

The app calculates evidence fingerprints from a selected local copy of the exact public page. It provides source URLs, on-chain snapshots, paginated receipt history, accounting, credit lookup and withdrawal. Reads use LATEST_FINAL; visitor writes require a compatible browser wallet. Recorded deployment and tests use Studio built-in accounts only.

## Validation

```bash
npm ci
npm test
npm run test:contract
npm run typecheck
npm run build
METRICMATCH_CURL_TRANSPORT=1 node scripts/read-live.mjs
node scripts/verify-live.mjs
```

38 adversarial Python contract tests exercise the release source with mocked GenVM boundaries. Four frontend logic tests verify input and GEN conversions. See [EVIDENCE.md](EVIDENCE.md) for actual Studio consensus and transfer proof, [STEWARD_RESPONSE.md](STEWARD_RESPONSE.md) for the review response, and [SUBMISSION.md](SUBMISSION.md) for submission details.

## Deployment and limits

- Public app: https://metricmatch-benchmarks.itzanza2.chatgpt.site
- v0.3 Studionet contract: `0x58E44E52fABfbFcF83759F8eB8296B81cc517E11`
- Previous v0.2 contract is historical; its storage/API is not upgraded in place.

Studionet GEN balances are simulated. Demonstration fixtures are synthetic, not independently measured benchmarks. Validators assess supplied evidence, rather than executing benchmark software. SHA-256 authenticates bytes; it does not authenticate authorship or guarantee truth. Prompt injection is isolated as untrusted data but semantic assessment remains model-dependent. Whole-number positive u32 metrics only; exact public HTTPS UTF-8 pages up to 16000 bytes. Highly dynamic pages may fail authentication. Consensus disagreement reverts the transaction without an active reservation; another transaction can retry. Network-level transaction congestion and validator availability remain external dependencies. This release is unaudited and has not been validated with production funds.
