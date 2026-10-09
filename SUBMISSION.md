# MetricMatch v0.3 project update

Existing submission is in Needed Action according to the owner. This revision addresses the steward security request. Portal update has not been sent: the available browser session is signed out and the user instructed not to connect a wallet.

**Project:** MetricMatch  
**One-liner:** Benchmark challenges with immutable evidence, independent GenLayer comparability consensus and matched GEN settlement.  
**Website:** https://metricmatch-benchmarks.itzanza2.chatgpt.site  
**GitHub:** https://github.com/haris4587/MetricMatch  
**Contract:** https://explorer-studio.genlayer.com/address/0x58E44E52fABfbFcF83759F8eB8296B81cc517E11

**Description:** MetricMatch lets software teams publish benchmark claims and independent reviewers contest them under committed conditions. GenLayer validators authenticate exact evidence bytes and assess comparability using the original on-chain snapshot. Challenges assess and settle atomically, without an exclusive slot. Invalid, unavailable or inconclusive evidence refunds its challenger while leaving the claim open; a comparable non-refuting attempt also leaves it open. A comparable refutation awards the matched pool. Immutable receipts retain fingerprints, snapshots, decisions and credits. The app provides finalized reads, fingerprint calculation, receipt history and withdrawals. Studio uses simulated GEN and synthetic demonstration fixtures.

**Review path:** Open the public app. Confirm contract address above, claim #0 REFUTED and two attempts. Expand challenge receipts and load the history. Attempt #0 is SOURCE_UNAVAILABLE / REFUNDED with 1 GEN credit; attempt #1 is VERIFIED / COMPARABLE / REFUTED with 2 GEN credit from a distinct account. Expand original and candidate snapshots to check exact SHA-256 and byte counts. Inspect EVIDENCE.md and run the 38 adversarial contract tests.

**Expected outcome:** A legitimate challenge settled the same claim after an invalid attempt. Finalized accounting shows 3 GEN deposited, zero locked, 3 GEN withdrawable. Withdrawal execution was blocked by automatic approval review, so no new transfer is claimed. Historical v0.2 transfers remain documented separately.

**Evidence URL:** https://github.com/haris4587/MetricMatch/blob/main/EVIDENCE.md  
**Steward response:** https://github.com/haris4587/MetricMatch/blob/main/STEWARD_RESPONSE.md  
**Finalized state:** https://github.com/haris4587/MetricMatch/blob/main/evidence/v03-finalized-state.json
