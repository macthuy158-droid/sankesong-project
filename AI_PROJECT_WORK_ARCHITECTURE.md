# AI Project Work Architecture

## Purpose

This file is the fast onboarding entry point for any AI tool working on the 三棵松鸿蒙公园智慧化项目.

Before making recommendations, generating documents, editing files, or judging project status, read the required sources below and follow the execution rules. Do not work from memory alone.

## Required Reading Order

1. `SYNC/data_sources.json`
2. `SYNC/project_data.json`
3. `MEMORY/decisions.json`
4. `MEMORY/constraints.json`
5. `MEMORY/memory_graph.json`
6. `AGENTS.md`

## Source Roles

`SYNC/data_sources.json` registers online and offline authority sources.

- `DS-20260503-001`: 项目 data 在线表格，intended primary worklist review source. Current status: Weixin document URL recorded, but direct AI access is blocked.
- `DS-20260503-002`: Google Drive 在线项目文件夹，primary online document repository. Current status: active.
- `DS-20260503-003`: `20260421 最终智能化清单`, technical scope baseline. Current status: active native Google Sheet with structured cell reading verified.

`SYNC/project_data.json` is the structured synchronized snapshot of the project worklist. Current status: no tasks synchronized yet.

`MEMORY/decisions.json` stores long-term project decisions.

`MEMORY/constraints.json` stores rejected, forbidden, excluded, or mandatory compliance constraints.

`MEMORY/memory_graph.json` stores the project memory topology aligned with the Drive folder structure.

## Current Decisions

- `D-20260503-001`: AI tools must read shared project data and decision sources before execution.
- `D-20260503-002`: AI must proactively ask whether to record decision-related or prohibition-related statements.
- `D-20260503-003`: Project memory follows the file management architecture and is maintained through `MEMORY/memory_graph.json`.
- `D-20260503-004`: The online worklist is the first review source; `SYNC/project_data.json` is its structured snapshot.
- `D-20260503-005`: Google Drive folder filing and project memory structure must stay aligned.

## Current Constraints

- `C-20260503-001`: All project outputs must conform to `DS-20260503-003` `20260421 最终智能化清单`.

`DS-20260503-003` is a readable native Google Sheet. Any AI output that depends on equipment, system, quantity, or technical scope must check the relevant sheet and cite any unresolved verification risk.

## Memory Domains

Use `MEMORY/memory_graph.json` to classify work into these domains:

- `01_项目管理`: progress, meetings, issues, risks, changes
- `02_商务合同`: contracts, quotes, bidding, vendor communications, submission materials
- `03_技术方案`: architecture, business loops, interface specs, design documents
- `04_智慧化施工`: drawings, equipment lists, construction methods, site records, acceptance
- `05_软件开发`: code, configuration, tests, deployment
- `06_联调记录`: joint debugging, interface tests, issue records
- `07_汇报材料`: owner/government reports and media materials
- `08_运维（开园后）`: manuals, knowledge updates, operations-stage device planning

## Execution Flow

1. Read all required sources.
2. Identify the requested work type: status judgment, document generation, technical proposal, file organization, decision capture, constraint capture, or data sync.
3. Check whether the request depends on the latest worklist. If yes, check `DS-20260503-001` and `SYNC/project_data.json`; if unavailable or empty, mark the latest-worklist review as blocked.
4. Check whether the request depends on technical scope or equipment details. If yes, check `DS-20260503-003`; if cell-level access is blocked, mark final-list verification as a risk.
5. Check all decisions and constraints for conflicts.
6. Map the work to the correct memory graph node and Drive folder.
7. Produce output with cited decision/constraint IDs and explicit risks.
8. If the user states a new decision or prohibition, ask whether to record it.

## Document Generation Rules

Generated documents should be stored in the Google Drive project folder registered as `DS-20260503-002`.

Choose the destination folder by memory domain:

- Management docs -> `01_项目管理`
- Business/vendor docs -> `02_商务合同`
- Technical architecture/spec docs -> `03_技术方案`
- Construction/spec/acceptance docs -> `04_智慧化施工`
- Software/deployment/test docs -> `05_软件开发`
- Integration records -> `06_联调记录`
- Reports and presentations -> `07_汇报材料`
- Operations manuals -> `08_运维（开园后）`
- Reference architecture/source materials -> `09 参考资料`

If the correct destination is unclear, state the likely folder and ask before filing.

## Data Update Boundary

The project online worklist controls project status updates. Do not invent tasks, owners, progress, blockers, or stage data.

Use `SYNC/project_data.json` only as a synchronized snapshot. If online source and local snapshot conflict, prefer the online source and flag the conflict before updating the snapshot.

## Known Blockers

- `DS-20260503-001`: Weixin online worklist link is recorded but direct AI access is blocked.
- `SYNC/project_data.json`: no worklist rows have been synchronized.
- `DS-20260503-003`: final smartization list is now readable as a native Google Sheet. The remaining risk is selecting and checking the correct worksheet/range for each task.
- Existing Drive files can be listed and inspected, but current Drive connector does not expose a direct move/update-parent operation for existing files.

## Standard Output Template

When replying about project work, include:

- Current basis: sources read and relevant decision/constraint IDs.
- Current problem: what is blocked, inconsistent, or missing.
- Priority: high, medium, or low.
- Next action: concrete, scoped action.
- Risks: especially worklist access, final-list verification, or Drive filing uncertainty.

## Hand-Off Prompt For Other AI

Use this when assigning work to another AI:

```text
You are working on the 三棵松鸿蒙公园智慧化项目. Before doing anything, read:
1. SYNC/data_sources.json
2. SYNC/project_data.json
3. MEMORY/decisions.json
4. MEMORY/constraints.json
5. MEMORY/memory_graph.json
6. AGENTS.md

Follow the project memory graph and Google Drive folder structure. Cite relevant decision and constraint IDs. All outputs must conform to DS-20260503-003《20260421 最终智能化清单》; check the relevant worksheet/range before making equipment, system, quantity, or technical-scope claims. Do not invent project progress. Ask for confirmation before recording new decisions or constraints.
```
