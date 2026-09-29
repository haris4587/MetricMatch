# MetricMatch

MetricMatch challenges public software performance claims on GenLayer. A claimant commits a result, benchmark conditions, original evidence, and a deadline. Another address submits a public benchmark and observed value. The Intelligent Contract independently fetches both pages during `evaluate`, asks validators to reproduce a three-way comparability decision, then applies a deterministic directional threshold. Unavailable or ambiguous evidence becomes `INCONCLUSIVE`; it never silently refutes a claim.

## Workflow

1. `create_claim` fixes the conditions and 1–30 day challenge window.
2. `challenge` accepts one challenger and one HTTPS source while the claim is open.
3. Anyone calls `evaluate`. `COMPARABLE` uses the numeric threshold; `NOT_COMPARABLE` upholds the claim against this challenge. `INCONCLUSIVE` can be retried at most three times.
4. Anyone can `close_unchallenged` after the deadline. That state does **not** assert that the benchmark is true.

The challenger-supplied numeric value must appear on the fetched evidence page, as judged by GenLayer validators. Evidence pages are untrusted input; their content is bounded to 16 KB each and instructed not to override the evaluation. No token escrow or monetary payout is implemented or accepted in this release. Claims are limited to unsigned whole-number values. Test against stable, public, text-readable pages; login walls and dynamic pages may be inconclusive. This is a public challenge tool, not a formal reproducibility certificate.

## Run

```bash
npm install
npm run build
npm test
npm run dev
```

The contract is deployed in [GenLayer Studio](https://studio.genlayer.com/) on Studionet; its address is in `src/deployment.json`. The [public app](https://metricmatch-benchmarks.itzanza2.chatgpt.site/) reads `LATEST_FINAL` state and uses `genlayer-js` for signed browser-wallet writes, fee estimation, and finalization. Studio’s built-in accounts were used for the live test; a visitor needs a compatible browser wallet to write from the website. The address field lets an operator inspect another deployment without rebuilding.

## Source and proof

- Contract: `contracts/metric_match.py`
- Client: `src/genlayer.ts` and `src/main.tsx`
- Deployment, transaction IDs, and the live test's limitations: [`EVIDENCE.md`](EVIDENCE.md).
- Network: Studionet chain 61999, `https://studio.genlayer.com/api`.

Security constraints: inputs are bounded, source URLs must use HTTPS, claim ownership blocks self-challenges, resolution is single-challenge per claim, and unknown claim IDs fail. Source sites can change after a decision; the on-chain verdict records the outcome rather than an immutable snapshot of page bytes. This version does not transfer or escrow funds.
