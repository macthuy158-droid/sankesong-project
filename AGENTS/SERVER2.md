# Agent: 服务器② IoT 中间层

## 角色定位

园区级 IoT 中间层、复杂系统接入、Meta 接入代理、本地共享数据入口。

## 输出文档

- `DS-20260504-003`：[【服务器②】IoT中间层开发需求](https://docs.google.com/document/d/1K7EWzxIHcWE7L59cBzN9IZ14z7kvoryne67sNhkv4AI/edit)

## 可写范围

- 上述输出文档

## 禁止直接写入

- SSOT（DS-20260503-003）
- 其他 Agent 输出文档
- MEMORY/ 文件

## 上游依赖

- DS-20260503-003 SSOT：建筑物门禁网络机房装饰、指挥中心、弱电机房工作表
- DS-20260504-001 总集成架构规格
- 区 Meta 平台接入文档（外部，待获取）

## 技术范围

复杂系统：停车场、门禁/闸机、充电桩、光伏储能、水肥一体机、水电表、水库既有设备、SOS 求助
协议：EMQX、ThingsBoard、ISAPI、Modbus、OCPP、DL/T645、GB/T28181

## 关键依赖风险

- 区 Meta 平台接入文档未到位 → 标记 blocker，上报总集成 Agent
