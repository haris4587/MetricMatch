# MetricMatch — GenLayer project submission

**Category:** Developer Tools / Dispute Resolution  
**Tagline:** Public performance claims challenged on equal benchmark terms.  
**Website:** https://metricmatch-benchmarks.itzanza2.chatgpt.site/  
**Source:** https://github.com/haris4587/MetricMatch  
**Studionet contract:** https://explorer-studio.genlayer.com/address/0x57A01C91B20596EF67463BbBf3d74cb1aDa7ad83  
**Live test and transactions:** https://github.com/haris4587/MetricMatch/blob/main/EVIDENCE.md

MetricMatch lets a developer publish a software benchmark claim with the precise workload, environment, metric, original source, and challenge deadline. Another address can submit a public counterexample and observed number. A GenLayer Intelligent Contract fetches the evidence and asks validators whether the tests are genuinely comparable. It then applies a deterministic higher-or-lower threshold. Ambiguous or unavailable evidence remains inconclusive rather than producing a false refutation. Anyone can inspect finalized claims in the public app.

The contract and app are deployed. Two synthetic claims went through create, challenge, and evaluate in Studio's full consensus mode. Both evaluations finalized with `INCONCLUSIVE`, so the live test demonstrates the fail-closed route and public finalized reads; it does **not** demonstrate a comparable verdict or a resolved refutation. The fixtures are explicitly synthetic. There is no token escrow or stake payout in this release.

To try it, open the website and inspect claims #0 and #1. To submit a real claim, use the Create claim view with a public, text-readable HTTPS benchmark source and explicit conditions. Writes from the website require a compatible browser wallet; the Studio built-in accounts were used for the recorded live transactions.
