# Live evidence

Network: GenLayer Studionet (chain ID 61999)

- Contract: [`0x57A01C91B20596EF67463BbBf3d74cb1aDa7ad83`](https://explorer-studio.genlayer.com/address/0x57A01C91B20596EF67463BbBf3d74cb1aDa7ad83)
- Deployment transaction: `0xd1fe755dfc20d205f44bb813d26c8953e66958f8e67a844daea8d67519e98da2` — FINALIZED in Studio.
- Deployment account (Studio built-in): `0x406f1E831b7141C6283aee1905bb785a53Ec7E1C`.

Public app: [metricmatch-benchmarks.itzanza2.chatgpt.site](https://metricmatch-benchmarks.itzanza2.chatgpt.site/). It reads finalized contract state, including both claims below. The deployment and transactions were executed using Studio's built-in accounts and test GEN.

## Live workflow

The second Studio account, `0x67854FeA01339A6e5F589B2f9Da361bf673ab230`, acted as a challenger for claim #0. The accounts reversed roles for claim #1. Studio reported every transaction below as **FINALIZED**.

| Claim | Action | Transaction |
| --- | --- | --- |
| #0 | Create a synthetic 40-second, lower-is-better claim | `0x953b6bb8f51482a86c164a28fcc13bbcdf8be91c5b31799b37a803542b84b943` |
| #0 | Challenge with a synthetic 48-second observation | `0x1a75202014bac2485c020ab6aad13385870aa5cf0f2e611980adbed2d9cceb34` |
| #0 | Evaluate | `0x7d4ff03e493adaeca5eb960072ea219fd30b4413eaf2fb67ee50c00453878694` |
| #1 | Create a second synthetic 40-second claim | `0x4aa144c26d274bf37c72697f4fedb7063a38809c9a2842425e070c8ba7c75eb3` |
| #1 | Challenge with a synthetic 48-second observation | `0x64c59e436309636909c7c5d38bec65c55ad305a7fddddfea253fee6c51696eaa` |
| #1 | Evaluate | `0xd157fd30df37d97f07bc77dee5525fec9818c817e34f2cb3d872c5aacc254579` |

Finalized reads for both claims showed `CHALLENGED`, verdict `INCONCLUSIVE`, and `1/3` evaluation attempts. Thus the live run verifies deployment, signed writes, challenge ownership, finalization, public reads, and the fail-closed inconclusive path. It **does not** verify that the validator judged the pages comparable or that deterministic numeric resolution executed. Repeating the test with canonical fixture URLs also returned `INCONCLUSIVE`; the cause was not isolated in Studio's available result view. The contract permits two further evaluation attempts on each claim.

The public `/evidence/` pages are explicitly **synthetic test fixtures**. They are not independent benchmarks of a real product. Use stable, publicly fetchable, text-readable real benchmark sources for a substantive challenge and inspect the finalized verdict before citing a result.
