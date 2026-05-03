#!/usr/bin/env bash
set -e

REPO_SSH="git@github.com:macthuy158-droid/sankesong-project.git"
REPO_HTTPS="https://github.com/macthuy158-droid/sankesong-project.git"
PROJECT_DIR="sankesong-project"

echo "Step 1: 检查 Git"
if ! command -v git >/dev/null 2>&1; then
  echo "错误：当前电脑未安装 git，请先安装 Git。"
  exit 1
fi

echo "Step 2: 检查 GitHub SSH"
if ssh -o BatchMode=yes -T git@github.com 2>&1 | grep -q "successfully authenticated"; then
  REPO_URL="$REPO_SSH"
  echo "SSH 可用，使用 SSH clone。"
else
  REPO_URL="$REPO_HTTPS"
  echo "SSH 不可用，改用 HTTPS clone。后续 push 可能需要 GitHub Token。"
fi

echo "Step 3: 获取项目仓库"
if [ -d "$PROJECT_DIR/.git" ]; then
  cd "$PROJECT_DIR"
  git pull --ff-only
else
  git clone "$REPO_URL" "$PROJECT_DIR"
  cd "$PROJECT_DIR"
fi

echo "Step 4: 检查必读文件"
REQUIRED_FILES="
AGENTS.md
AI_PROJECT_WORK_ARCHITECTURE.md
SYNC/data_sources.json
SYNC/project_data.json
MEMORY/decisions.json
MEMORY/constraints.json
MEMORY/memory_graph.json
"

for file in $REQUIRED_FILES; do
  if [ ! -f "$file" ]; then
    echo "错误：缺少必读文件 $file"
    exit 1
  fi
done

echo "Step 5: 校验 JSON 文件"
if command -v python3 >/dev/null 2>&1; then
  python3 -m json.tool SYNC/data_sources.json >/dev/null
  python3 -m json.tool SYNC/project_data.json >/dev/null
  python3 -m json.tool MEMORY/decisions.json >/dev/null
  python3 -m json.tool MEMORY/constraints.json >/dev/null
  python3 -m json.tool MEMORY/memory_graph.json >/dev/null
else
  echo "警告：未找到 python3，跳过 JSON 格式校验。"
fi

echo ""
echo "项目已接入完成。"
echo "当前目录：$(pwd)"
echo ""
echo "下一步：把下面这段提示词发给 Claude Code："
echo "--------------------------------------------------"
cat <<'EOF'
你现在接入三棵松鸿蒙公园智慧化项目。

你已经进入 Git 仓库。开始任何项目判断、文档生成、需求分析、架构讨论或文件修改前，必须先读取：

- AGENTS.md
- AI_PROJECT_WORK_ARCHITECTURE.md
- SYNC/data_sources.json
- SYNC/project_data.json
- MEMORY/decisions.json
- MEMORY/constraints.json
- MEMORY/memory_graph.json

请先完成以下动作：

1. 总结当前项目状态。
2. 列出已确认决策。
3. 列出已确认约束。
4. 标注当前风险和 blocker。
5. 说明你准备如何执行后续任务。

项目规则：

- 在线工作清单是第一审阅来源。
- 最终智能化清单是技术范围基准：
  https://docs.google.com/spreadsheets/d/1_7GxEisIwnplS1n5TT6q07i-40zQsaa_Ypzdqe3vF48/edit?gid=1194902564#gid=1194902564
- Google Drive 项目文件夹是在线文档归档位置：
  https://drive.google.com/drive/u/0/folders/1fMSi1Rs9ejQN3GKFxq1PZwjQ07P9M5aO
- 未经我确认，不要直接生成、修改、编程、写入文件、改在线文档或改表格。
- 如果识别到新的决策或禁止事项，必须主动询问是否写入 MEMORY/decisions.json 或 MEMORY/constraints.json。
EOF
echo "--------------------------------------------------"
