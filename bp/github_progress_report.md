# AegisTrust 本地仓库进展报告

生成时间：2026-03-13 10:01 UTC

数据来源：
- 本次直接使用本地仓库和本地 git 信息生成。
- 仓库归属：`joy7758` 的本地仓库克隆
- 本地工作区：`/Users/zhangbin/GitHub`
- 同时复跑了四个核心模块和端到端 demo 的轻量验证命令

## 一句话结论

- 当前本地仓库群共扫描到 36 个仓库，最近 30 天有更新的仓库有 36 个，说明这套体系到 2026-03-13 仍在持续推进。
- 现在最清楚、最容易对外讲明白的产品结构，已经收敛成四个模块：`god-spear`、`safety-valve-spec`、`execution-integrity-core`、`aro-audit`。
- 账号里还有 persona、interaction、runtime governance 等更大体系。这些内容能证明技术深度，但不适合放在第一页讲太多，更适合放到补充材料。
- 当前最准确的阶段描述是：开源验证已完成，可回放 demo 已完成，场景打磨和试点转化正在推进。

## 最新本地回放
- `god-spear`：PASS，时间 2026-03-13 10:02 UTC，命令 `node bin/spear.js check examples/rules.ok.json`。
- `safety-valve-spec`：PASS，时间 2026-03-13 10:02 UTC，命令 `bash conformance/run.sh`。
- `execution-integrity-core`：PASS，时间 2026-03-13 10:02 UTC，命令 `bash scripts/selfcheck.sh`。
- `aro-audit`：PASS，时间 2026-03-13 10:02 UTC，命令 `bash quickstart/run.sh`。
- `verifiable-agent-demo`：PASS，时间 2026-03-13 10:02 UTC，命令 `python3 -m demo.agent`。

## 账号概览

| 指标 | 数值 |
| --- | --- |
| 扫描到的公开仓库 | 36 |
| 最近 30 天有更新的仓库 | 36 |
| 最近 7 天有更新的仓库 | 21 |
| GitHub 星标总数 | 本地模式不统计 |
| 本地 `spear-check` 接入数 | 18 |
| 主要语言 | Python (17), Shell (4), JavaScript (2), HTML (1) |
| 分层分布 | 身份基础层: 3, 治理门禁层: 5, 执行安全与完整性层: 4, 审计证据层: 3, 外围架构仓库: 21 |

## AegisTrust 四个核心模块

| 模块 | 主仓库 | 最近代码提交 | 最近版本 | 本地回放 | 当前状态 |
| --- | --- | --- | --- | --- | --- |
| 上线前门禁层 | [god-spear](https://github.com/joy7758/god-spear) | 2026-03-10 `4428fe1` | v0.2.0 | PASS | 可现场演示，可直接接入 CI。 |
| 动作边界收据层 | [safety-valve-spec](https://github.com/joy7758/safety-valve-spec) | 2026-02-24 `060de71` | v0.2.0-alpha.1 | PASS | 规范、参考实现、conformance、badge 全部齐备。 |
| 执行完整性层 | [execution-integrity-core](https://github.com/joy7758/execution-integrity-core) | 2026-02-24 `087145a` | none | PASS | 最小证明闭环成熟，适合对外说明和客户演示。 |
| 审计证据层 | [aro-audit](https://github.com/joy7758/aro-audit) | 2026-03-13 `5a51612` | v1.0.1 | PASS | 演示、规范、bundle 都齐备，适合做主项目外壳。 |

## 核心模块详情

### 上线前门禁层: `god-spear`

- GitHub 地址: https://github.com/joy7758/god-spear
- 仓库描述: CI-native trust gate for risky AI automation.
- 模块作用: 上线前门禁，要求信任边界、失败信号和回滚路径明确。
- 最近推送时间: 2026-03-10 18:33 UTC
- 最近版本: v0.2.0
- 本地代码信号：tests=0, demos=2, examples=6, workflows=2, spec 文件约=0
- 本地回放（2026-03-13 10:02 UTC）：PASS，命令 `node bin/spear.js check examples/rules.ok.json`
- 关键输出：`FINDINGS: 0`

最近提交:
  - 2026-03-10 `4428fe1` docs: link post-run receipt adapter
  - 2026-03-10 `8c6a7ac` docs: link minimal MCP adapter example
  - 2026-03-10 `b8f1a70` docs: add trust gate demo assets

已实现能力:
- 对 tools/files/env/runtime 入口做前置 trust-boundary 检查
- 缺少 failure signal、revocation pathway、grace budget 时直接 FAIL
- 可输出文本、JSON、HTML 报告，并追加 immutable trace
- 提供 `god-spear-mcp-gate` 适配器，便于挂到 MCP / tool 调用前

开源验证:
- GitHub Release: `v0.2.0`
- npm 包发布与 SBOM、SHA256、release file list 已入库
- 本地 smoke check 通过：`node bin/spear.js check examples/rules.ok.json`

### 动作边界收据层: `safety-valve-spec`

- GitHub 地址: https://github.com/joy7758/safety-valve-spec
- 仓库描述: Verifiable receipt spec and conformance suite for action boundaries.
- 模块作用: 动作边界收据层，要求高风险动作必须带可验收据。
- 最近推送时间: 2026-02-24 00:23 UTC
- 最近版本: v0.2.0-alpha.1
- 本地代码信号：tests=2, demos=1, examples=21, workflows=6, spec 文件约=40
- 本地回放（2026-03-13 10:02 UTC）：PASS，命令 `bash conformance/run.sh`
- 关键输出：`OK: dist/svs-compat.latest.json`

最近提交:
  - 2026-02-24 `060de71` ci(conformance): fix workflow YAML syntax in report step
  - 2026-02-24 `3ed0826` ci(conformance): stabilize reusable workflow definition
  - 2026-02-24 `790b77a` chore: sync local updates

已实现能力:
- 定义 ALLOW / DENY / DEGRADE 收据格式与 JSON Schema
- 提供签名、验签、CA、CRL、compat attestation 工具链
- 提供 gateway demo，落实 no receipt, no action
- 提供 reusable GitHub workflow，其他仓库可复用 conformance 检查

开源验证:
- GitHub Release: `v0.2.0-alpha.1`
- 仓库内含 `dist/svs-compat.attestation.json` 与 badge 产物
- 本地 conformance 全量通过：`bash conformance/run.sh`

### 执行完整性层: `execution-integrity-core`

- GitHub 地址: https://github.com/joy7758/execution-integrity-core
- 仓库描述: Minimal structural proof for execution integrity.
- 模块作用: 最小执行完整性证明，保证执行链条可导出、可验证、可发现篡改。
- 最近推送时间: 2026-02-24 00:18 UTC
- 最近版本: none
- 本地代码信号：tests=1, demos=1, examples=0, workflows=1, spec 文件约=1
- 本地回放（2026-03-13 10:02 UTC）：PASS，命令 `bash scripts/selfcheck.sh`
- 关键输出：`SELF_CHECK: PASS`

最近提交:
  - 2026-02-24 `087145a` chore: sync local updates
  - 2026-02-24 `22db3ea` ci(security): add spear-check (CI-only)
  - 2026-02-23 `71a3cad` docs: add ecosystem adoption tracking page

已实现能力:
- 记录 execution event，并对事件做 hash chain 串联
- 支持确定性导出 JSON 与 full-chain verification
- 提供篡改前后对比演示，强调 structural integrity
- 作为执行层最小内核，适合做对外说明时的技术锚点

开源验证:
- 仓库有 `SPEC.md`、`scripts/selfcheck.sh`、`tests/test_export_verify.py`
- 已接入 `spear-check`，说明执行层也纳入治理门禁
- 本地 self-check 通过：`bash scripts/selfcheck.sh`

### 审计证据层: `aro-audit`

- GitHub 地址: https://github.com/joy7758/aro-audit
- 仓库描述: Audit evidence layer for bounded, reviewable AI execution artifacts.
- 模块作用: 事后证据层，把普通日志升级为可复核、可回放、可交付的审计包。
- 最近推送时间: 2026-03-13 09:18 UTC
- 最近版本: v1.0.1
- 本地代码信号：tests=18, demos=7, examples=30, workflows=6, spec 文件约=44
- 本地回放（2026-03-13 10:02 UTC）：PASS，命令 `bash quickstart/run.sh`
- 关键输出：`=== DONE: Quickstart OK ===`

最近提交:
  - 2026-03-13 `5a51612` feat: add FDO evidence object profile
  - 2026-03-13 `4030006` docs: publish evidence object specification
  - 2026-03-13 `58ae3fc` feat: add governance conformance test suite

已实现能力:
- 生成 append-only journal、manifest、Merkle/checkpoint 与验签流程
- 支持 quickstart 生成正常样本与 tamper 样本并独立验证
- 支持 bundle 导出与 SHA256 manifest，便于对外交付审计材料
- 已形成 one-pager、threat model、conformance vectors 等对外材料

开源验证:
- GitHub Release: `v1.0.1`
- 有 `CITATION.cff`、`SECURITY.md`、Zenodo DOI
- 本地 quickstart 通过：正常样本 `VERIFY_OK`，篡改样本 `Merkle mismatch`

## 支撑仓库分层

### 身份基础层
- [langchain-pop](https://github.com/joy7758/langchain-pop): 将 persona 层贴近 LangChain 场景。 最近提交 2026-03-08，最近版本 v0.1.2。
- [persona-object-protocol](https://github.com/joy7758/persona-object-protocol): 为更完整的大架构提供 persona / identity 层；当前不作为主模块单独对外销售。 最近提交 2026-03-11，最近版本 v0.1.7。
- [pop-persona-pack](https://github.com/joy7758/pop-persona-pack): POP 的 persona 资产包，证明 identity 层可落地。 最近提交 2026-03-09，最近版本 none。

### 治理门禁层
- [god-spear-mcp-gate](https://github.com/joy7758/god-spear-mcp-gate): 将 trust gate 前置到 MCP 风格工具执行。 最近提交 2026-03-10，最近版本 none。
- [token-governor](https://github.com/joy7758/token-governor): 更深一层的运行时预算和策略治理扩展，可作为 AegisTrust 后续控制平面。 最近提交 2026-03-13，最近版本 v0.2.0。
- [token-governor-langchain-middleware](https://github.com/joy7758/token-governor-langchain-middleware): Token Governor 的轻量中间件适配层。 最近提交 2026-03-10，最近版本 none。

### 执行安全与完整性层
- [fdo-kernel-mvk](https://github.com/joy7758/fdo-kernel-mvk): 执行完整性层的进阶演进，证明执行层不是停留在概念而在持续展开。 最近提交 2026-03-12，最近版本 v0.2.0。
- [verifiable-agent-demo](https://github.com/joy7758/verifiable-agent-demo): 跨层端到端 demo，把 persona、governance、execution、audit 串成一条评审可见路径。 最近提交 2026-03-13，最近版本 none。

### 审计证据层
- [aro-audit-langchain-receipt](https://github.com/joy7758/aro-audit-langchain-receipt): 最小 post-run receipt 适配器，便于接入现有 agent 框架。 最近提交 2026-03-10，最近版本 none。
- [langchain-aro](https://github.com/joy7758/langchain-aro): 将 audit evidence 接到 LangChain 运行时。 最近提交 2026-03-08，最近版本 none。

### 外围架构仓库
- [agent-intent-protocol](https://github.com/joy7758/agent-intent-protocol): interaction semantics 层，当前不单列为商业模块。 最近提交 2026-03-11，最近版本 none。
- [agent-object-protocol](https://github.com/joy7758/agent-object-protocol): agent object draft，作为长期协议储备。 最近提交 2026-03-11，最近版本 v1.1.2。
- [digital-biosphere-architecture](https://github.com/joy7758/digital-biosphere-architecture): 架构总览仓库，用于解释生态关系，不作为当前阶段的主交付。 最近提交 2026-03-13，最近版本 none。
- [joy7758](https://github.com/joy7758/joy7758): GitHub profile，公开展示创始人研究方向与五层架构定位。 最近提交 2026-03-11，最近版本 none。

## 当前可对外使用的判断

- 现在最适合作为主产品外壳的仓库是 `aro-audit`，因为它已经有对外说明、快速演示和证据打包能力。
- 现在最适合对外讲的结构是：`god-spear` + `safety-valve-spec` + `execution-integrity-core` + `aro-audit`。
- 当前技术成熟度可以概括为：核心流程能本地复跑，3 个核心仓库已有公开版本，`spear-check` 已在 18 个本地仓库里持续使用。
- 当前商业成熟度仍偏早期，更适合写成“技术验证完成，正在走向试点和场景验证”。
- 当前最统一的一句话定位：**AegisTrust = AI 可信执行基础设施**。

## 公开仓库清单

| 仓库 | 分层 | 语言 | 最近推送（UTC） | 备注 |
| --- | --- | --- | --- | --- |
| [digital-biosphere-architecture](https://github.com/joy7758/digital-biosphere-architecture) | 外围架构仓库 | n/a | 2026-03-13 | 架构总览仓库，用于解释生态关系，不作为当前阶段的主交付。 |
| [aro-audit](https://github.com/joy7758/aro-audit) | 审计证据层 | Python | 2026-03-13 | 事后证据层，把普通日志升级为可复核、可回放、可交付的审计包。 |
| [agent-governance-benchmark](https://github.com/joy7758/agent-governance-benchmark) | 治理门禁层 | n/a | 2026-03-13 | 治理或信任边界相关支撑仓库。 |
| [token-governor](https://github.com/joy7758/token-governor) | 治理门禁层 | Python | 2026-03-13 | 更深一层的运行时预算和策略治理扩展，可作为 AegisTrust 后续控制平面。 |
| [verifiable-agent-demo](https://github.com/joy7758/verifiable-agent-demo) | 执行安全与完整性层 | Shell | 2026-03-13 | 跨层端到端 demo，把 persona、governance、execution、audit 串成一条评审可见路径。 |
| [fdo-kernel-mvk](https://github.com/joy7758/fdo-kernel-mvk) | 执行安全与完整性层 | Shell | 2026-03-12 | 执行完整性层的进阶演进，证明执行层不是停留在概念而在持续展开。 |
| [joy7758](https://github.com/joy7758/joy7758) | 外围架构仓库 | n/a | 2026-03-11 | GitHub profile，公开展示创始人研究方向与五层架构定位。 |
| [persona-object-protocol](https://github.com/joy7758/persona-object-protocol) | 身份基础层 | Python | 2026-03-11 | 为更完整的大架构提供 persona / identity 层；当前不作为主模块单独对外销售。 |
| [agent-intent-protocol](https://github.com/joy7758/agent-intent-protocol) | 外围架构仓库 | n/a | 2026-03-11 | interaction semantics 层，当前不单列为商业模块。 |
| [agent-object-protocol](https://github.com/joy7758/agent-object-protocol) | 外围架构仓库 | Shell | 2026-03-11 | agent object draft，作为长期协议储备。 |
| [pFDO-Specification](https://github.com/joy7758/pFDO-Specification) | 外围架构仓库 | Python | 2026-03-11 | 架构、标准或外围研究仓库。 |
| [aro-audit-langchain-receipt](https://github.com/joy7758/aro-audit-langchain-receipt) | 审计证据层 | Python | 2026-03-10 | 最小 post-run receipt 适配器，便于接入现有 agent 框架。 |
| [token-governor-langchain-middleware](https://github.com/joy7758/token-governor-langchain-middleware) | 治理门禁层 | Python | 2026-03-10 | Token Governor 的轻量中间件适配层。 |
| [god-spear-mcp-gate](https://github.com/joy7758/god-spear-mcp-gate) | 治理门禁层 | Python | 2026-03-10 | 将 trust gate 前置到 MCP 风格工具执行。 |
| [god-spear](https://github.com/joy7758/god-spear) | 治理门禁层 | JavaScript | 2026-03-10 | 上线前门禁，要求信任边界、失败信号和回滚路径明确。 |
| [pop-persona-pack](https://github.com/joy7758/pop-persona-pack) | 身份基础层 | Python | 2026-03-09 | POP 的 persona 资产包，证明 identity 层可落地。 |
| [redrock-opendpp-core](https://github.com/joy7758/redrock-opendpp-core) | 外围架构仓库 | JavaScript | 2026-03-08 | 架构、标准或外围研究仓库。 |
| [edo-architecture-index](https://github.com/joy7758/edo-architecture-index) | 外围架构仓库 | n/a | 2026-03-08 | 架构、标准或外围研究仓库。 |
| [docs](https://github.com/joy7758/docs) | 外围架构仓库 | Python | 2026-03-08 | 架构、标准或外围研究仓库。 |
| [langchain-aro](https://github.com/joy7758/langchain-aro) | 审计证据层 | Python | 2026-03-08 | 将 audit evidence 接到 LangChain 运行时。 |
| [langchain-pop](https://github.com/joy7758/langchain-pop) | 身份基础层 | Python | 2026-03-08 | 将 persona 层贴近 LangChain 场景。 |
| [AASP-Core](https://github.com/joy7758/AASP-Core) | 外围架构仓库 | n/a | 2026-03-01 | 架构、标准或外围研究仓库。 |
| [gptme](https://github.com/joy7758/gptme) | 外围架构仓库 | Python | 2026-02-26 | 架构、标准或外围研究仓库。 |
| [safety-valve-spec](https://github.com/joy7758/safety-valve-spec) | 执行安全与完整性层 | Shell | 2026-02-24 | 动作边界收据层，要求高风险动作必须带可验收据。 |
| [RedRock-Constitution](https://github.com/joy7758/RedRock-Constitution) | 外围架构仓库 | n/a | 2026-02-24 | 架构、标准或外围研究仓库。 |
| [agno](https://github.com/joy7758/agno) | 外围架构仓库 | n/a | 2026-02-24 | 架构、标准或外围研究仓库。 |
| [DOIP-Segments-Specification](https://github.com/joy7758/DOIP-Segments-Specification) | 外围架构仓库 | n/a | 2026-02-24 | 架构、标准或外围研究仓库。 |
| [freeact](https://github.com/joy7758/freeact) | 外围架构仓库 | Python | 2026-02-24 | 架构、标准或外围研究仓库。 |
| [ToolAgents](https://github.com/joy7758/ToolAgents) | 外围架构仓库 | Python | 2026-02-24 | 架构、标准或外围研究仓库。 |
| [Kinetic-Robotics-FDO-Sovereignty](https://github.com/joy7758/Kinetic-Robotics-FDO-Sovereignty) | 外围架构仓库 | n/a | 2026-02-24 | 架构、标准或外围研究仓库。 |
| [China-Precision-Mold-FDO-Standard](https://github.com/joy7758/China-Precision-Mold-FDO-Standard) | 外围架构仓库 | n/a | 2026-02-24 | 架构、标准或外围研究仓库。 |
| [execution-integrity-core](https://github.com/joy7758/execution-integrity-core) | 执行安全与完整性层 | n/a | 2026-02-24 | 最小执行完整性证明，保证执行链条可导出、可验证、可发现篡改。 |
| [MCP-Legal-China](https://github.com/joy7758/MCP-Legal-China) | 外围架构仓库 | Python | 2026-02-24 | 架构、标准或外围研究仓库。 |
| [ISAS-Core](https://github.com/joy7758/ISAS-Core) | 外围架构仓库 | HTML | 2026-02-24 | 架构、标准或外围研究仓库。 |
| [mcp-agent](https://github.com/joy7758/mcp-agent) | 外围架构仓库 | Python | 2026-02-24 | 架构、标准或外围研究仓库。 |
| [pydantic-ai](https://github.com/joy7758/pydantic-ai) | 外围架构仓库 | Python | 2026-02-24 | 架构、标准或外围研究仓库。 |
