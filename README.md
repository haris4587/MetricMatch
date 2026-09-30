# MetricMatch

Challenge public software benchmark claims on equal test conditions. GenLayer independently fetches both evidence pages and reaches a validator consensus on comparability. Deterministic code applies the higher-or-lower threshold and settles optional matched GEN stakes.

## Workflow

1. `create_claim` commits the product/version, metric, value, unit, conditions, original HTTPS evidence and a 1–30 day challenge window. The payable value sets the stake, from zero to 1000 GEN.
2. A different address calls `challenge` before the deadline, with one HTTPS source, an observed number and exactly the same stake.
3. Anyone calls `evaluate`. COMPARABLE applies the numeric threshold; NOT_COMPARABLE upholds this claim against this challenge. REFUTED awards the pool to the challenger; UPHELD awards it to the owner. Three INCONCLUSIVE results refund both deposits.
4. `close_unchallenged` returns the owner's stake after the challenge deadline without certifying the claim as true. `expire_unresolved` refunds both parties after the resolution deadline (one day after the challenge deadline).
5. Each credited address calls `withdraw`. Credit is cleared before an external transfer is emitted on finalization. Inspect the child transfer as well as the withdrawal transaction.

## Run and validate

```bash
npm ci
npm test
npm run test:contract
npm run typecheck
npm run build
npm run dev
node scripts/verify-live.mjs
```

The website uses `genlayer-js` 1.1.8, wallet-backed writes including payable value, and `LATEST_FINAL` reads. Visitor writes require a compatible browser wallet; the recorded live tests used only Studio's built-in accounts. Deployment address is in `src/deployment.json`. The app exposes stake settlement, aggregate accounting, credit lookup, withdrawal and deadline refunds.

## Evidence and release status

- [Public website](https://metricmatch-benchmarks.itzanza2.chatgpt.site/) — v0.2 published September 30, 2026; targets the stake-enabled contract.
- [Live proof](EVIDENCE.md) — finalized funded resolution and refunds on the stake-enabled contract, with zero outstanding funds.
- [Submission package](SUBMISSION.md) — ready for the owner to submit through the Portal.
- Studionet chain 61999: `https://studio.genlayer.com/api`.

## Limits

Studionet balances/transfers are simulated. The live fixtures are synthetic and prove workflow execution, not a real product's performance. Claims accept unsigned whole-number metrics. Evidence is bounded to 16 KB per page; pages must be public, HTTPS and text-readable. Missing, non-200 or ambiguous sources are inconclusive. Pages can change; verdict history is stored, but immutable page snapshots are not. A single challenger is allowed per claim, with at most three evaluation attempts.

Evidence text is untrusted and explicitly isolated in the prompt. Validators re-run interpretation; they do not independently execute the benchmark software. The contract is unaudited and the tests mock VM boundaries. EOA transfer behavior is demonstrated in Studio; production chain transfers and recovery behavior require separate validation before real funds are used.
