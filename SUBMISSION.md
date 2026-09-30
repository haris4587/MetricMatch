# MetricMatch — GenLayer Project Explorer submission

Application date: 09/30/2026. Contribution type: Builder → Projects → Project.

**Name:** MetricMatch  
**Suggested primary tag:** Developer Tools (use the closest available Portal category).  
**Topics:** Benchmarking; AI consensus.  
**One-liner:** Challenge software benchmarks on comparable evidence, with matched stakes settled by GenLayer.  
**Website:** https://metricmatch-benchmarks.itzanza2.chatgpt.site/  
**Repository:** https://github.com/haris4587/MetricMatch  
**Contract:** https://explorer-studio.genlayer.com/address/0x3F251a2330c21312093cf76e8AC10274b40D155D  
**Logo:** https://github.com/haris4587/MetricMatch/raw/refs/heads/main/assets/metricmatch-logo.png

## Description

MetricMatch lets a developer commit a software performance claim with its exact product version, metric, workload, environment, original evidence and challenge window. Another address submits public benchmark evidence and an observed value, matching the optional GEN stake. A GenLayer Intelligent Contract fetches both sources and validators decide whether the tests are genuinely comparable and substantiate the submitted numbers. Deterministic rules apply the numeric threshold and credit the matched pool to the winning party. Unavailable or ambiguous evidence remains inconclusive; retry exhaustion and resolution timeouts refund both deposits. Users inspect finalized claims, settlement and accounting in the app and withdraw their own credits.

## Why GenLayer is central

The main decision requires understanding whether hardware, datasets, versions, workloads, units and settings support a fair comparison. Validator/LLM consensus makes that semantic judgment from independently fetched public evidence. Contract code controls permissions, one challenger, matched deposits, deadlines, retries, score direction, credit allocation and withdrawals.

## Evidence links

- Contract source: https://github.com/haris4587/MetricMatch/blob/main/contracts/metric_match.py
- Live evidence and all transaction records: https://github.com/haris4587/MetricMatch/blob/main/EVIDENCE.md
- Finalized state: https://github.com/haris4587/MetricMatch/blob/main/evidence/finalized-state.json
- Full-consensus COMPARABLE/REFUTED evaluation: https://explorer-studio.genlayer.com/tx/0x70992a2986962f1a63dd82371d93d3aca7fa8205cd750ac0f634e060fec68bbb
- Finalized two-GEN challenger transfer: https://explorer-studio.genlayer.com/tx/0x277d56a283795d287c80c24815ffd62e07cf1b2a84b71b631e466963df736740
- Finalized one-GEN claimant refund: https://explorer-studio.genlayer.com/tx/0x98ff7801eb49a28233d12223ff184c9fd53131156b1aa1582767578344d51dff
- Finalized one-GEN challenger refund: https://explorer-studio.genlayer.com/tx/0x1b4c4b4f1a3742345715ce1d900a867c89dbb6ea4880d392cc65f8f166111dcc
- Contract tests: https://github.com/haris4587/MetricMatch/blob/main/tests/test_contract.py

## Validation and limitations

A NORMAL full-consensus live run refuted a synthetic 40-second claim against a comparable 48-second challenge and transferred the two-GEN pool to the challenger. A second claim tested unavailable evidence, three inconclusive retries and two one-GEN refunds. Finalized accounting shows four GEN deposited, four withdrawn and zero outstanding balance, credits or locks. Repository checks include 18 Python contract tests, frontend tests, TypeScript checking and a production build.

Studionet GEN is simulated; fixtures are synthetic. This proves the workflow, not real benchmark accuracy or mainnet safety. The contract is unaudited. The public app update must be published before citing v0.2 as live. Portal wallet sign-in and terms acceptance remain necessary; this file is a submission draft, not proof of a submitted or approved listing.
