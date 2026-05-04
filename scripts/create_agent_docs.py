#!/usr/bin/env python3
"""
三棵松鸿蒙公园智慧化项目 — 创建 10 个 Agent 在线文档
运行前请确保已安装依赖：
  pip3 install google-api-python-client google-auth-httplib2 google-auth-oauthlib

首次运行会弹出浏览器要求 Google 账号授权，之后自动保存 token。
"""

import json
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# ── 配置 ─────────────────────────────────────────────────────────────────────
SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/spreadsheets",
]

# Google Drive 项目根文件夹 ID（DS-20260503-002）
PROJECT_FOLDER_ID = "1fMSi1Rs9ejQN3GKFxq1PZwjQ07P9M5aO"

TOKEN_FILE = os.path.join(os.path.dirname(__file__), "google_token.json")
CREDENTIALS_FILE = os.path.join(os.path.dirname(__file__), "google_credentials.json")

# ── 10 个文档定义 ─────────────────────────────────────────────────────────────
DOCUMENTS = [
    {
        "id": "DOC-INTEGRATION",
        "name": "【总集成】软件架构规格",
        "type": "doc",
        "agent": "agent/integration",
        "folder": "03_技术方案",
        "description": "总体软件架构规格，接口规范，数据规范，联调验收计划",
    },
    {
        "id": "DOC-GATEWAY",
        "name": "【网关】端侧软件开发需求",
        "type": "doc",
        "agent": "agent/gateway",
        "folder": "05_软件开发",
        "description": "网关端侧设备接入、星闪、NFC、本地闭环开发需求",
    },
    {
        "id": "DOC-SERVER2",
        "name": "【服务器②】IoT中间层开发需求",
        "type": "doc",
        "agent": "agent/server2",
        "folder": "05_软件开发",
        "description": "服务器②IoT中间层、物模型、Meta对接、复杂系统接入开发需求",
    },
    {
        "id": "DOC-DATABASE",
        "name": "【数据库】数据平台开发需求",
        "type": "doc",
        "agent": "agent/database",
        "folder": "05_软件开发",
        "description": "PostgreSQL、TimescaleDB、ChromaDB、Redis、数据字典开发需求",
    },
    {
        "id": "DOC-SERVER1",
        "name": "【服务器①】闪电智能体开发需求",
        "type": "doc",
        "agent": "agent/server1",
        "folder": "05_软件开发",
        "description": "闪电智能体、大模型、RAG、ASR/TTS、数字人开发需求",
    },
    {
        "id": "DOC-FRONTEND",
        "name": "【前端】应用开发需求",
        "type": "doc",
        "agent": "agent/frontend",
        "folder": "05_软件开发",
        "description": "小程序、鸿蒙元服务、灯杆屏、瀑布屏、管理后台开发需求",
    },
    {
        "id": "DOC-VIDEO",
        "name": "【视频】流媒体开发需求",
        "type": "doc",
        "agent": "agent/video",
        "folder": "05_软件开发",
        "description": "摄像机接入、NVR、GB28181、直播、转码开发需求",
    },
    {
        "id": "DOC-DEVOPS",
        "name": "【运维】部署与安全开发需求",
        "type": "doc",
        "agent": "agent/devops",
        "folder": "05_软件开发",
        "description": "部署、监控、日志、备份、SSL、权限开发需求",
    },
    {
        "id": "DOC-PROCUREMENT",
        "name": "【采购】智慧化设备采购清单",
        "type": "sheet",
        "agent": "agent/procurement",
        "folder": "04_智慧化施工",
        "description": "全园智慧化设备采购清单，参数校验，供应商，到货状态",
    },
    {
        "id": "DOC-CONSTRUCTION",
        "name": "【施工】现场施工管理记录",
        "type": "doc",
        "agent": "agent/construction",
        "folder": "04_智慧化施工",
        "description": "施工日志、现场记录、设备安装确认、验收跟踪",
    },
]


def authenticate():
    """OAuth 认证，首次运行弹出浏览器授权窗口"""
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_FILE):
                print(f"""
❌ 缺少 Google OAuth 凭据文件：{CREDENTIALS_FILE}

请按以下步骤获取：
1. 打开 https://console.cloud.google.com/
2. 新建项目（或使用已有项目）
3. 进入「API和服务」→「已启用的API」→ 启用 Google Drive API 和 Google Docs API
4. 进入「API和服务」→「凭据」→「创建凭据」→「OAuth 2.0 客户端 ID」
5. 应用类型选「桌面应用」，下载 JSON 文件
6. 将文件重命名为 google_credentials.json 放到 scripts/ 目录下
7. 重新运行此脚本
""")
                return None
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as f:
            f.write(creds.to_json())
    return creds


def get_or_create_subfolder(drive_service, parent_id, folder_name):
    """在 parent_id 下查找或创建子文件夹"""
    query = (
        f"name='{folder_name}' and "
        f"'{parent_id}' in parents and "
        f"mimeType='application/vnd.google-apps.folder' and trashed=false"
    )
    results = drive_service.files().list(q=query, fields="files(id, name)").execute()
    files = results.get("files", [])
    if files:
        return files[0]["id"]
    folder_meta = {
        "name": folder_name,
        "mimeType": "application/vnd.google-apps.folder",
        "parents": [parent_id],
    }
    folder = drive_service.files().create(body=folder_meta, fields="id").execute()
    print(f"  📁 创建子文件夹：{folder_name}")
    return folder["id"]


def create_doc(drive_service, name, folder_id):
    """在指定文件夹创建 Google Doc"""
    file_meta = {
        "name": name,
        "mimeType": "application/vnd.google-apps.document",
        "parents": [folder_id],
    }
    f = drive_service.files().create(body=file_meta, fields="id, webViewLink").execute()
    return f["id"], f["webViewLink"]


def create_sheet(drive_service, name, folder_id):
    """在指定文件夹创建 Google Sheet"""
    file_meta = {
        "name": name,
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "parents": [folder_id],
    }
    f = drive_service.files().create(body=file_meta, fields="id, webViewLink").execute()
    return f["id"], f["webViewLink"]


def main():
    print("🚀 三棵松项目 — 创建 Agent 文档\n")

    creds = authenticate()
    if not creds:
        return

    drive_service = build("drive", "v3", credentials=creds)

    # 缓存子文件夹 ID
    folder_cache = {}
    results = []

    for doc in DOCUMENTS:
        folder_name = doc["folder"]
        if folder_name not in folder_cache:
            folder_cache[folder_name] = get_or_create_subfolder(
                drive_service, PROJECT_FOLDER_ID, folder_name
            )
        folder_id = folder_cache[folder_name]

        print(f"  📄 创建：{doc['name']} ...", end=" ", flush=True)
        if doc["type"] == "sheet":
            file_id, url = create_sheet(drive_service, doc["name"], folder_id)
        else:
            file_id, url = create_doc(drive_service, doc["name"], folder_id)
        print(f"✅")

        results.append({
            "id": doc["id"],
            "name": doc["name"],
            "agent": doc["agent"],
            "type": doc["type"],
            "folder": folder_name,
            "file_id": file_id,
            "url": url,
            "description": doc["description"],
        })

    # 输出结果
    output_path = os.path.join(os.path.dirname(__file__), "created_docs.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 全部完成！结果已保存到：{output_path}\n")
    print("创建的文档：")
    for r in results:
        print(f"  [{r['id']}] {r['name']}")
        print(f"    {r['url']}")

    print("\n下一步：将 created_docs.json 中的 URL 注册到 SYNC/data_sources.json")


if __name__ == "__main__":
    main()
