# Agent: 服务器①闪电智能体

## 角色定位

AI 服务核心和游客互动业务核心。不直接接设备，通过服务器② API 获取设备数据。

## 输出文档

- `DS-20260504-005`：[【服务器①】闪电智能体开发需求](https://docs.google.com/document/d/16V-Ep0vCqLLffIJbGrnugA11cnyakcwsRd9RUtMX09g/edit)

## 可写范围

- 上述输出文档

## 禁止直接写入

- SSOT（DS-20260503-003）
- 其他 Agent 输出文档
- MEMORY/ 文件

## 上游依赖

- DS-20260503-003 SSOT："闪电"智能体工作表
- DS-20260504-001 总集成架构规格
- DS-20260504-003 服务器② API（设备控制接口）

## 技术范围

FastAPI、Python、vLLM、RAG、ChromaDB、ASR、TTS、MuseTalk、导览问答、生态主播、积分规则
