# Response to MetricMatch steward

Implemented in v0.3: challenges now authenticate, assess and settle in one consensus transaction with no reserved slot. Invalid, inaccessible, changed, inconclusive and non-comparable submissions refund their challenger and keep the claim OPEN. Comparable non-refuting submissions also keep it OPEN, so they cannot immunize the claim. The original evidence is authenticated by SHA-256 and byte length and stored as an immutable on-chain snapshot; later assessments never re-fetch it. Candidate evidence must match its fingerprint. Immutable linked receipts retain snapshots, decisions and credits.

38 adversarial contract tests pass, plus frontend tests, TypeScript checks and build. The new Studio full-consensus proof shows claim #0 receiving an invalid submission (1 GEN refund credit), followed by a distinct legitimate challenger whose 48-second evidence refutes the 40-second claim (2 GEN pool credit). Both receipts are finalized. GEN and fixtures are simulated/synthetic. The withdrawal click was blocked by automatic approval review; 3 GEN remains withdrawable, and no new payout transfer is claimed.

Contract: https://explorer-studio.genlayer.com/address/0x58E44E52fABfbFcF83759F8eB8296B81cc517E11  
App: https://metricmatch-benchmarks.itzanza2.chatgpt.site  
Evidence: https://github.com/haris4587/MetricMatch/blob/main/EVIDENCE.md  
Tests: https://github.com/haris4587/MetricMatch/blob/main/tests/test_contract.py

Portal response is prepared but unsubmitted because the available session requires a wallet connection, which the owner instructed not to make.
