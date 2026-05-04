# AI Project Operating Rules

## Multi-Agent Architecture

本项目采用 10 Agent 分工架构。每个 Agent 接入前须读取本文件及对应角色规则文件。

### 决策者

**你（总项目负责人）** 是唯一决策者。架构变更、SSOT 修改、MEMORY 写入均须你确认。

### Agent 角色与输出文档

| Agent 规则文件 | 角色 | 输出文档 |
|---------------|------|---------|
| `AGENTS/INTEGRATION.md` | 总集成与软件架构 | DS-20260504-001 |
| `AGENTS/GATEWAY.md` | 网关端侧软件 | DS-20260504-002 |
| `AGENTS/SERVER2.md` | 服务器② IoT 中间层 | DS-20260504-003 |
| `AGENTS/DATABASE.md` | 数据库与数据平台 | DS-20260504-004 |
| `AGENTS/SERVER1.md` | 服务器①闪电智能体 | DS-20260504-005 |
| `AGENTS/FRONTEND.md` | 前端应用 | DS-20260504-006 |
| `AGENTS/VIDEO.md` | 视频与流媒体 | DS-20260504-007 |
| `AGENTS/DEVOPS.md` | 运维部署与安全 | DS-20260504-008 |
| `AGENTS/PROCUREMENT.md` | 采购 | DS-20260504-009 |
| `AGENTS/CONSTRUCTION.md` | 现场施工管理 | DS-20260504-010 |

### 唯一数据源（SSOT）

`DS-20260503-003`（最终智能化清单 Google Sheet）是项目唯一数据源。

其他在线表格、同步快照和 Agent 输出文档只能作为参考或输出物，不得替代 SSOT。原 `DS-20260503-001` 微信 data 在线表格已废弃；`SYNC/project_data.json` 仅保留为可选同步快照，不再作为权威工作清单。

**变更传播规则（自上而下）：**
1. 架构变更 → 先更新 SSOT → 总集成 Agent 更新架构规格 → 各域 Agent 更新需求文档 → 采购 Agent 校验一致性

**反馈规则（自下而上）：**
2. 域 Agent 发现问题 → 报告总集成 Agent → 总集成 Agent 上报你 → 你确认 → 更新 SSOT → 触发自上而下传播

### 每个 Agent 接入时必须额外读取

自己的角色规则文件（`AGENTS/<ROLE>.md`），确认可写范围和禁止写入范围。



## Required Data Sources

Before making any project judgment, plan, recommendation, or code change, every AI tool must read:

- `SYNC/project_data.json`
- `SYNC/data_sources.json`
- `MEMORY/decisions.json`
- `MEMORY/constraints.json`
- `MEMORY/memory_graph.json`

These files are the required shared context for project data source registration, optional synchronized snapshots, project decisions, project constraints, and project memory topology. For project status, scope, equipment, procurement, and Agent output alignment, `DS-20260503-003` is the authority.

## Mandatory Behavior

- Check `SYNC/data_sources.json` before judging project progress.
- Treat `DS-20260503-003` as the single source of truth (SSOT) for project scope, worklist, equipment, procurement, and Agent output alignment.
- Treat `SYNC/project_data.json` only as an optional synchronized snapshot, not as an authority.
- If `DS-20260503-003` is missing or inaccessible, mark SSOT review as blocked and avoid inventing task status or scope.
- Base all output on the current SSOT content in `DS-20260503-003`, while noting whether the relevant sheet and range have been checked.
- Check all proposed actions against decisions in `MEMORY/decisions.json`.
- Check all proposed actions against constraints in `MEMORY/constraints.json`.
- Use `MEMORY/memory_graph.json` to place new information into the correct project memory domain.
- Use `AI_PROJECT_WORK_ARCHITECTURE.md` as the quick onboarding entry point for other AI tools.
- Cite relevant decision IDs when making recommendations.
- Cite relevant constraint IDs when avoiding or rejecting an action.
- Mark blockers and risks explicitly.
- Do not infer missing project state.
- Do not ignore, silently override, or contradict existing decisions.
- Do not repeat, recommend, or silently revive items that have been explicitly rejected or forbidden.
- Before programming, modifying files, generating new files, editing online documents, changing spreadsheets, or performing any action that changes project artifacts, first explain the intended approach, source basis, affected files or documents, expected impact, and risks, then wait for user confirmation.
- If the user has not confirmed the approach, limit output to analysis, options, questions, or a proposed action plan; do not perform the artifact-changing action.

## Decision Recording

When the user states a clear project judgment or rule, treat it as a potential decision.

Before writing it to `MEMORY/decisions.json`, ask the user to confirm.

After confirmation, add a decision record with:

- `id`
- `title`
- `decision`
- `reason`
- `date`

## Constraint Recording

When the user states that something is rejected, forbidden, excluded, out of scope, or must not be done, treat it as a potential constraint.

Before writing it to `MEMORY/constraints.json`, ask the user to confirm.

After confirmation, add a constraint record with:

- `id`
- `title`
- `constraint`
- `reason`
- `scope`
- `date`

## Active Confirmation Duty

If an AI tool detects that a user message contains either:

- a decision-related statement, or
- a forbidden, rejected, excluded, or out-of-scope statement,

the AI tool must proactively ask whether to write it into the corresponding long-term record.

## Thought Confirmation Before Action

All AI tools must follow `C-20260503-002`.

Before executing any artifact-changing action, the AI tool must:

- Read the required data sources.
- State the proposed action and why it is needed.
- Identify the target files, Google Drive documents, spreadsheets, diagrams, code, or memory records that may change.
- Cite the relevant source, decision, or constraint basis.
- Mark risks and possible conflicts.
- Ask the user to confirm before proceeding.

Artifact-changing actions include but are not limited to:

- Creating, editing, renaming, moving, deleting, or overwriting local files.
- Creating or editing Google Docs, Sheets, Slides, Drive files, HTML files, Word documents, spreadsheets, architecture diagrams, or generated artifacts.
- Writing to `MEMORY/decisions.json`, `MEMORY/constraints.json`, `MEMORY/memory_graph.json`, `SYNC/project_data.json`, or `SYNC/data_sources.json`.
- Running code generation or scripts that write project files.

If the user explicitly asks to record this confirmation rule itself, the AI may write this rule after reading the required sources, because the user has already confirmed that specific update.

## Memory Graph Updates

`MEMORY/memory_graph.json` may be updated when the project file architecture, work domains, subsystem boundaries, or cross-domain relationships change.

Before changing the graph structure, the AI tool must:

- Read all required data sources.
- State which nodes, categories, or edges need to be added, renamed, merged, split, or removed.
- Check whether the change conflicts with existing decisions or constraints.
- Ask the user to confirm the graph update.

After confirmation, update `MEMORY/memory_graph.json` and preserve existing node IDs whenever possible. If a node must be replaced, keep the old node traceable by adding a relationship or migration note rather than silently deleting context.

Graph updates should not be used to record ordinary task progress. Ordinary progress belongs in the SSOT first and may be synchronized into `SYNC/project_data.json`; decisions belong in `MEMORY/decisions.json`; rejected or forbidden items belong in `MEMORY/constraints.json`.

## Single Source of Truth

`DS-20260503-003` is the project single source of truth (SSOT). Its registration belongs in `SYNC/data_sources.json`.

When the SSOT changes, AI tools may synchronize relevant rows into `SYNC/project_data.json` using the established fields:

- `type`
- `name`
- `status`
- `stage`
- `owner`
- `progress`
- `blocker`

If `DS-20260503-003` and `SYNC/project_data.json` conflict, the AI tool must flag the conflict, prefer `DS-20260503-003`, and update the JSON snapshot only after the intended sync is clear.

## Online Document Repository

The Google Drive project folder registered in `SYNC/data_sources.json` is the primary online document repository.

AI tools should use this folder when checking project documents, source materials, exported files, or generated project artifacts. The document repository does not replace `DS-20260503-003`; the SSOT remains the authority for latest project scope and worklist.

When generating or organizing project documents, AI tools should place the artifact in the Google Drive subfolder that matches `MEMORY/memory_graph.json`. If the correct destination is unclear, the AI tool must state the likely memory domain and ask for confirmation before filing.

Decision and constraint records should stay structurally aligned with the memory graph and Drive folder structure. Project data updates remain governed by `DS-20260503-003` and may be synchronized into `SYNC/project_data.json`.

## Final Smartization List

`DS-20260503-003` in `SYNC/data_sources.json` is the project SSOT and technical scope baseline. All project outputs must conform to this list. If exact row-level verification is required but the list is not available as a readable native Google Sheet or exported file, the AI tool must mark SSOT verification as a risk.

The current `DS-20260503-003` source is a readable native Google Sheet. AI tools must select the relevant worksheet and range before making equipment, system, quantity, or technical-scope claims.
