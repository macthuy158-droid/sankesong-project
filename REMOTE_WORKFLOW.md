# 三棵松项目异地一键接入流程

## 目标

让 Claude Code、Codex、OpenClaw 或其他 AI 工具在异地电脑上快速接入三棵松鸿蒙公园智慧化项目，并遵守同一套数据源、决策、约束和记忆图谱。

本流程不依赖任何本机路径，只依赖：

- GitHub 仓库
- Google Drive 在线项目文件夹
- 最终智能化清单
- 仓库内结构化记忆文件

## 一键接入

在异地电脑打开终端，执行：

```bash
curl -fsSL https://raw.githubusercontent.com/macthuy158-droid/sankesong-project/master/scripts/bootstrap_remote.sh | bash
```

如果不能使用 `curl`，则手动执行：

```bash
git clone git@github.com:macthuy158-droid/sankesong-project.git
cd sankesong-project
git pull --ff-only
```

如果 SSH 未配置，则使用 HTTPS：

```bash
git clone https://github.com/macthuy158-droid/sankesong-project.git
cd sankesong-project
git pull --ff-only
```

## 接入后必须读取

AI 工具进入仓库后，必须先读取：

```text
AGENTS.md
AI_PROJECT_WORK_ARCHITECTURE.md
SYNC/data_sources.json
SYNC/project_data.json
MEMORY/decisions.json
MEMORY/constraints.json
MEMORY/memory_graph.json
```

这些文件分别承担以下作用：

- `AGENTS.md`：AI 执行规则
- `AI_PROJECT_WORK_ARCHITECTURE.md`：项目快速接入说明
- `SYNC/data_sources.json`：在线数据源注册表
- `SYNC/project_data.json`：SSOT 的可选同步快照，不作为权威来源
- `MEMORY/decisions.json`：长期决策记录
- `MEMORY/constraints.json`：禁止事项和约束记录
- `MEMORY/memory_graph.json`：项目记忆图谱

## 当前权威数据源

### 最终智能化清单

项目唯一数据源（SSOT）：

https://docs.google.com/spreadsheets/d/1_7GxEisIwnplS1n5TT6q07i-40zQsaa_Ypzdqe3vF48/edit?gid=1194902564#gid=1194902564

约束：

- 所有方案、需求、报价、设备范围、分工、采购范围和 Agent 输出必须符合此清单。
- 涉及项目状态、设备、系统、数量、范围、供应商、采购或技术方案时，必须核对该表。

### Google Drive 项目文件夹

在线项目文档归档位置：

https://drive.google.com/drive/u/0/folders/1fMSi1Rs9ejQN3GKFxq1PZwjQ07P9M5aO

约束：

- 新生成或整理的正式文档应按 `MEMORY/memory_graph.json` 对应结构归档。
- Git 仓库保存结构化规则、记忆、需求和协作流程。
- Google Drive 保存在线协作文档和正式资料。

### 项目 data 在线表格（已废弃）

原微信 data 在线表格已被 `DS-20260503-003` 替代，不再作为权威来源：

https://doc.weixin.qq.com/sheet/e3_AXoAfQaUAIACNsDplpOuiT3yvq1Te?scode=AI4Asgd9ABMzJ19o4gAXoAfQaUAIA&tab=000003

当前风险：

- AI 不应再将该表作为项目判断依据。
- 如历史资料需要迁移，应先进入 `DS-20260503-003`，再由各 Agent 同步输出文档。

## Git 工作原则

每次开始工作：

```bash
git pull --ff-only
```

工作完成后：

```bash
git status
git diff
git add .
git commit -m "docs: update remote workflow"
git push
```

提交原则：

- 一次提交只处理一个明确问题。
- 不提交密钥、账号、Token。
- 不提交临时输出文件。
- 不提交本机下载目录中的无关文件。
- `outputs/` 不作为正式项目文件提交。

推荐提交类型：

```text
docs: 文档更新
memory: 决策或约束更新
sync: 数据源或同步快照更新
requirements: 需求文档更新
chore: 项目结构维护
```

## AI 执行流程

AI 接到任务后，必须按以下顺序执行：

1. 接入 Git 仓库。
2. 执行 `git pull --ff-only`。
3. 读取必读文件。
4. 判断任务类型。
5. 核对相关在线数据源。
6. 输出思路、依据、范围、影响和风险。
7. 等用户确认。
8. 再执行文件、文档、表格或代码修改。
9. 校验 JSON、Markdown 或在线文档结果。
10. 提交并推送 Git。

## 当前必须遵守的决策

- `D-20260503-001`：所有 AI 使用统一数据源和统一记忆机制；其中数据权威口径已被 `D-20260504-001` 部分覆盖。
- `D-20260503-002`：AI 识别到决策或禁止事项时，必须主动询问是否写入。
- `D-20260503-003`：项目记忆按记忆图谱结构组织。
- `D-20260503-004`：已被 `D-20260504-001` 覆盖。
- `D-20260503-005`：Google Drive 文件夹结构要与记忆图谱一致；其中数据权威口径已被 `D-20260504-001` 部分覆盖。
- `D-20260503-006`：深开鸿不参与三棵松项目实施；区 Meta 平台团队提供对接文档和技术支持；我方或服务器二分包方负责实现接入、联调和验收。
- `D-20260504-001`：`DS-20260503-003` 是项目唯一数据源（SSOT）。

## 当前必须遵守的约束

- `C-20260503-001`：所有输出必须符合最终智能化清单。
- `C-20260503-002`：AI 不得直接编程、生成文件或修改文件，必须先确认思路后动作。

## 当前架构理解

当前软件和设备接入原则：

```text
简单设备 / 国标设备 / 简单传感器
        ↓
      网关
        ↓
      Meta

复杂系统 / 停车场 / 门禁 / 海康平台 / 综合管理系统
        ↓
     服务器二
        ↓
      Meta
```

服务器二定位：

- 园区级 IoT 中间层
- 复杂系统接入
- 协议转换
- 数据汇聚
- 统一物模型
- 本地数据库和配置
- 与区 Meta 平台对接
- 本地闭环逻辑支撑

## Claude Code 启动提示词

将以下内容发给 Claude Code：

```text
你现在接入三棵松鸿蒙公园智慧化项目。

第一步，请确认你已经进入 Git 仓库：

sankesong-project

如果尚未 clone，请先执行：

git clone git@github.com:macthuy158-droid/sankesong-project.git
cd sankesong-project
git pull --ff-only

如果当前电脑没有配置 GitHub SSH，请改用 HTTPS：

git clone https://github.com/macthuy158-droid/sankesong-project.git
cd sankesong-project
git pull --ff-only

进入仓库后，必须先读取以下文件：

- AGENTS.md
- AI_PROJECT_WORK_ARCHITECTURE.md
- SYNC/data_sources.json
- SYNC/project_data.json
- MEMORY/decisions.json
- MEMORY/constraints.json
- MEMORY/memory_graph.json

读取完成后，先总结：

1. 当前项目状态
2. 已确认决策
3. 已确认约束
4. 当前风险和 blocker
5. 你准备如何执行后续任务

项目规则：

- 最终智能化清单是项目唯一数据源（SSOT）：
  https://docs.google.com/spreadsheets/d/1_7GxEisIwnplS1n5TT6q07i-40zQsaa_Ypzdqe3vF48/edit?gid=1194902564#gid=1194902564
- Google Drive 项目文件夹是在线文档归档位置：
  https://drive.google.com/drive/u/0/folders/1fMSi1Rs9ejQN3GKFxq1PZwjQ07P9M5aO
- 未经我确认，不要直接生成、修改、编程、写入文件、改在线文档或改表格。
- 如果识别到新的决策或禁止事项，必须主动询问是否写入 MEMORY/decisions.json 或 MEMORY/constraints.json。

当前架构原则：

- 简单设备、国标设备、简单传感器优先接入网关。
- 复杂系统如停车、门禁、海康平台等通过服务器二接入。
- 服务器二负责复杂系统接入、协议转换、数据汇聚、统一物模型和 Meta 对接。
```
