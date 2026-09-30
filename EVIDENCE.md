# MetricMatch v0.2 live evidence

Network: GenLayer Studionet, chain ID 61999. All balances and transfers below are **simulated GEN**, not mainnet funds. Both evidence pages are explicitly synthetic fixtures, not real independent software benchmarks.

## Stake-enabled deployment

- Contract: [0x3F251a2330c21312093cf76e8AC10274b40D155D](https://explorer-studio.genlayer.com/address/0x3F251a2330c21312093cf76e8AC10274b40D155D)
- Deployment: [0x70d6d081a7a7e365b60ea439761e0958e5c6c13f6ea41289d040f3a8d8b14272](https://explorer-studio.genlayer.com/tx/0x70d6d081a7a7e365b60ea439761e0958e5c6c13f6ea41289d040f3a8d8b14272), FINALIZED.
- The release contract source was recovered byte-for-byte from this deployment transaction. Its web API checks `response.status`, as declared in the Python runtime, and rejects non-200 responses before interpreting content.
- Claimant Studio account: `0x9Ce3D7D516c3cdE9210EDdc7c5E197F8f8Ad71Ff`.
- Challenger Studio account: `0xc45252EE825293C2566541c6C80D56B6122b17A3`.

## Finalized live tests

| Claim | Result | Settlement | Finalized transfer |
| --- | --- | --- | --- |
| #0: 40-second claim, 48-second challenge | COMPARABLE, REFUTED, one attempt | Two matched one-GEN deposits awarded to challenger | [2 GEN to challenger](https://explorer-studio.genlayer.com/tx/0x277d56a283795d287c80c24815ffd62e07cf1b2a84b71b631e466963df736740) |
| #1: unavailable counterevidence | INCONCLUSIVE after three attempts | Each party received its one-GEN deposit back | [1 GEN to challenger](https://explorer-studio.genlayer.com/tx/0x1b4c4b4f1a3742345715ce1d900a867c89dbb6ea4880d392cc65f8f166111dcc), [1 GEN to claimant](https://explorer-studio.genlayer.com/tx/0x98ff7801eb49a28233d12223ff184c9fd53131156b1aa1582767578344d51dff) |

Claim #0 consensus evaluation: [0x70992a2986962f1a63dd82371d93d3aca7fa8205cd750ac0f634e060fec68bbb](https://explorer-studio.genlayer.com/tx/0x70992a2986962f1a63dd82371d93d3aca7fa8205cd750ac0f634e060fec68bbb), NORMAL full-consensus mode, FINALIZED.

Claim #1 final evaluation: [0xd91110ad609e2cba0b2c2d104e6c1827af391d303b3bb6e84bbf3a14c0eb145f](https://explorer-studio.genlayer.com/tx/0xd91110ad609e2cba0b2c2d104e6c1827af391d303b3bb6e84bbf3a14c0eb145f), NORMAL full-consensus mode, FINALIZED.

Every deployment, deposit, evaluation, withdrawal and child transfer hash is recorded in [transactions.json](evidence/transactions.json). Finalized SDK reads on September 30 are recorded in [finalized-state.json](evidence/finalized-state.json): 4 GEN deposited, 4 GEN withdrawn, 0 locked, 0 credit and 0 balance. These records prove the funded workflow, consensus outcome, and simulated transfers; they do not certify a real benchmark result or mainnet escrow safety.

## Repository checks

- `npm test`: frontend parsing, integer bounds, metric directions, exact GEN conversion.
- `npm run test:contract`: 18 Python tests execute the actual release contract with a strict mocked GenVM boundary. They cover matched stakes, both metric directions, withdrawal, single settlement, HTTP errors, API mismatch, validator disagreement, retry refunds and deadline refunds. These are unit tests, not a VM integration test.
- `npm run typecheck` and `npm run build`: pass.
- `node scripts/verify-live.mjs`: verifies finalized claims and zero outstanding accounting; optional `METRICMATCH_CURL_TRANSPORT=1` uses curl in proxy-based environments.

## Publication and submission status

The existing public website remains the earlier no-stakes release until v0.2 is published. The updated source targets the stake-enabled contract above. Portal submission is not yet complete: the Portal requires the account owner's browser-wallet sign-in and acceptance of its terms. No listing approval or mainnet deployment is claimed.

---

# Historical pre-stakes evidence

Network: GenLayer Studionet (chain ID 61999)

## Previous deployment and resolved live run

- Contract: [`0xA5BD9189755004Da01b1A946C1E33f0f88a98203`](https://explorer-studio.genlayer.com/address/0xA5BD9189755004Da01b1A946C1E33f0f88a98203)
- Deployment transaction: `0x2afe9d99202b2551c5ceae72c1b1ffcb0c8be6a5a2c467b9603fcbed27223fe8` — FINALIZED.
- Release code upgrade: `0x3e3b4c743dc0124d351d683ebdc4e97a33c66b0a8c07990b79839acf57751e0d` — FINALIZED; removed the temporary diagnostic method.
- Claim #0 create: `0xfb5c04aafdd612c617170ef79df584e90c43fb81d0c8290ebceffb109da8597c` — FINALIZED by `0x406f1E831b7141C6283aee1905bb785a53Ec7E1C`.
- Challenge: `0xdc36640f5cc0ff4d666bfb65e8f577195fb268a5a850c03ce39b05b2cf939172` — FINALIZED by `0x67854FeA01339A6e5F589B2f9Da361bf673ab230`.
- [Evaluate](https://explorer-studio.genlayer.com/tx/0x7ef63064b0cddf523e2f4827d47ce3bc438c5fdd7c93713f5a4b1ca1c8253aaf): `0x7ef63064b0cddf523e2f4827d47ce3bc438c5fdd7c93713f5a4b1ca1c8253aaf` — FINALIZED in Normal (Full Consensus) mode. The equivalence output was `COMPARABLE`; a finalized `get_claim(0)` read showed `status: REFUTED`, `verdict: COMPARABLE`, `attempts: 1` for 40 versus 48 seconds with lower-is-better.

The source pages are **synthetic demonstration fixtures**, explicitly labeled as such. This transaction proves that the contract fetched their content, validators agreed on comparability, and deterministic numeric resolution ran. It does not prove a real CLI benchmark or independent measurement.

The initial contract used `gl.nondet.web.get(...)` correctly but accessed `response.status_code`, which the returned object did not expose in this Studio runtime. A finalized diagnostic call on the corrected deployment returned `ERROR_AttributeError` (`0x1cbd8eaa302d048c40dd6fbf21ced320936b7cf8e652e529d8a928b598f1afb4`). After using `response.body`, another finalized probe returned `BYTES_1715` (`0x70e2a472d25c6cc13a67962824e2ff11821c7fb60c44f17a793a4296f2d82de5`). The release contract checks for a nonempty body and catches fetch failures as `INCONCLUSIVE`. The probe method was removed in the finalized release upgrade above.

## Initial deployment and inconclusive tests

- Contract: [`0x57A01C91B20596EF67463BbBf3d74cb1aDa7ad83`](https://explorer-studio.genlayer.com/address/0x57A01C91B20596EF67463BbBf3d74cb1aDa7ad83)
- Deployment transaction: `0xd1fe755dfc20d205f44bb813d26c8953e66958f8e67a844daea8d67519e98da2` — FINALIZED in Studio.
- Deployment account (Studio built-in): `0x406f1E831b7141C6283aee1905bb785a53Ec7E1C`.

The [public app](https://metricmatch-benchmarks.itzanza2.chatgpt.site/) previously read the corrected deployment above. The two historical claims below remain on the initial contract. These transactions used Studio's built-in accounts and test GEN.

## Live workflow

The second Studio account, `0x67854FeA01339A6e5F589B2f9Da361bf673ab230`, acted as a challenger for claim #0. The accounts reversed roles for claim #1. Studio reported every transaction below as **FINALIZED**.

| Claim | Action | Transaction |
| --- | --- | --- |
| #0 | Create a synthetic 40-second, lower-is-better claim | `0x953b6bb8f51482a86c164a28fcc13bbcdf8be91c5b31799b37a803542b84b943` |
| #0 | Challenge with a synthetic 48-second observation | `0x1a75202014bac2485c020ab6aad13385870aa5cf0f2e611980adbed2d9cceb34` |
| #0 | Evaluate | `0x7d4ff03e493adaeca5eb960072ea219fd30b4413eaf2fb67ee50c00453878694` |
| #1 | Create a second synthetic 40-second claim | `0x4aa144c26d274bf37c72697f4fedb7063a38809c9a2842425e070c8ba7c75eb3` |
| #1 | Challenge with a synthetic 48-second observation | `0x64c59e436309636909c7c5d38bec65c55ad305a7fddddfea253fee6c51696eaa` |
| #1 | [Evaluate](https://explorer-studio.genlayer.com/tx/0xd157fd30df37d97f07bc77dee5525fec9818c817e34f2cb3d872c5aacc254579) | `0xd157fd30df37d97f07bc77dee5525fec9818c817e34f2cb3d872c5aacc254579` |

Finalized reads for both claims showed `CHALLENGED`, verdict `INCONCLUSIVE`, and `1/3` evaluation attempts. The Explorer shows claim #1's evaluation executed successfully in Normal mode with five initial validators, an accepted consensus result, and an `INCONCLUSIVE` equivalence output. This demonstrated the fail-closed path but did not exercise numeric resolution. The diagnostic transactions on the corrected deployment isolated the cause as the unsupported `status_code` access. The initial contract permits two further evaluation attempts on each claim, but the public app now points to the corrected deployment.

The public `/evidence/` pages are explicitly **synthetic test fixtures**. They are not independent benchmarks of a real product. Use stable, publicly fetchable, text-readable real benchmark sources for a substantive challenge and inspect the finalized verdict before citing a result.
