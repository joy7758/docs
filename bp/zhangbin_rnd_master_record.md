# ZhangBin 研发总记录

> 用途：这是一份给“未来的自己”以及“新开的 AI 窗口”看的总记录。  
> 目标：在 1 次打开、3 分钟内，看清当前主线、已完成进展、外部沟通状态、比赛材料位置。  
> 维护规则：以后每次通过 agent 产生了实质进展，都在本文档最后的“更新日志”追加一条。  
> 最近更新：2026-03-13

## 1. 90 秒接手版

- 你当前最适合对外讲的主线不是“大而全架构”，而是：`AegisTrust = AI 可信执行基础设施`。
- 更大的长期架构叫 `Digital Biosphere Architecture`，是五层研究体系；`AegisTrust` 是当前最适合商业化和比赛表达的切片。
- 当前已经形成可复跑、可演示、可讲明白的四段闭环：
  - `god-spear`：上线前门禁
  - `safety-valve-spec`：关键动作收据
  - `execution-integrity-core`：执行完整性证明
  - `aro-audit`：事后证据包和独立复验
- 到 2026-03-13，本地工作区扫描到 36 个仓库，`spear-check` 已接入 18 个仓库，核心 demo 和 smoke replay 已通过。
- 你已经有 FDO 2026 海报演讲相关证据链：
  - 本地海报源文件写明 `Poster Presenter · FDO 2026 Vienna`
  - 本地 demo 页面写明 `FDO 2026 Poster Demo`
  - ARO Audit 已有 FDO Testbed Profile ID：`21.T11966/aro-audit-profile-v1`
  - 你提供的邀请函截图显示：FDO 2026 会议时间为 2026-03-24 至 2026-03-27，地点 Vienna，角色是 `Poster Presenter`
- 比赛材料方面，`docs/bp` 里已经有一整套一等奖叙事版 BP / PPT / 讲稿 / 评委问答包。

## 2. 当前定位

### 2.1 个人与研究定位

- 身份：`Bin Zhang`
- 当前公开研究定位：独立研究者，持续构建 `Digital Biosphere Architecture for governable AI agents`
- 当前最适合对外的一句话：
  - `AegisTrust` 不是另一个 AI 工具，而是一套让高风险 AI 动作更可验证、可控制、可追责的可信执行基础设施。

### 2.2 主线与上位架构的关系

- 上位架构：`Digital Biosphere Architecture`
- 五层研究主线：
  1. Persona Layer
  2. Interaction Layer
  3. Governance Layer
  4. Execution Integrity Layer
  5. Audit Evidence Layer
- 当前商业化/比赛主线：`AegisTrust`
- 关系判断：
  - `Digital Biosphere Architecture` 负责证明体系深度
  - `AegisTrust` 负责证明当前可落地、可转化、可被评委记住
- 对外表达原则：
  - 主舞台先讲 `AegisTrust`
  - `POP`、AIP、五层架构、协议谱系放在备份材料或补充说明里

## 3. 当前研发进展快照

数据基线来自本地 `docs/bp/technical_progress.md` 与 `docs/bp/github_progress_report.md`，生成时间为 2026-03-13 10:01 UTC。

### 3.1 工程快照

- 本地工作区扫描仓库数：`36`
- 最近 30 天有更新的仓库：`36`
- 最近 7 天有更新的仓库：`21`
- 本地 `spear-check` 接入数：`18`

### 3.2 当前最重要的四个模块

| 模块 | 作用 | 当前状态 |
| --- | --- | --- |
| `god-spear` | 上线前门禁，检查 trust boundary、failure signal、revocation pathway | 已有版本 `v0.2.0`，本地回放 PASS |
| `safety-valve-spec` | 关键动作必须带 `ALLOW / DENY / DEGRADE` 收据 | 已有版本 `v0.2.0-alpha.1`，本地 conformance PASS |
| `execution-integrity-core` | 用 hash chain 和导出校验证明执行过程未被偷偷改动 | 本地 self-check PASS |
| `aro-audit` | 生成可交付证据包，并可做独立复验 | 已有版本 `v1.0.1`，本地 quickstart PASS |

### 3.3 已经能现场证明的事情

- `god-spear`：`STATUS: PASS`
- `safety-valve-spec`：`Overall: PASS`
- `execution-integrity-core`：`SELF_CHECK: PASS`
- `aro-audit`：正常样本 `VERIFY_OK`，篡改样本 `Merkle mismatch`
- `verifiable-agent-demo`：PASS，可输出完整 `intent / action / result / audit_record`

### 3.4 当前一句话阶段判断

当前最准确的状态不是“还在概念阶段”，而是：

`开源验证已完成，可回放 demo 已完成，外部表达和场景转化正在推进。`

## 4. FDO 2026 相关信息

## 4.1 已确认事项

以下信息来自你提供的邀请函截图，以及仓库内已存在的海报/演示材料。

- 邀请函抬头：`FAIR DIGITAL OBJECTS FORUM`
- 邀请函正文对应会议：`3rd International FAIR Digital Objects Conference (FDO 2026)`
- 会议地点：`Vienna, Austria`
- 会议时间：`2026-03-24` 至 `2026-03-27`
- 角色：`Poster Presenter`
- 被接受的摘要标题：`The Digital Biosphere`
- 邀请函正文说明：
  - 你的摘要已被 scientific committee 接受
  - 你将在 Poster Sessions 向国际 FDO 社区展示研究发现和相关技术实现（含 GitHub reference）
  - 差旅、住宿、注册、保险由个人承担，不由会务资助

说明：

- 你提供的邀请函截图页眉日期显示为 `10.2.2025`，但正文对应的会议是 `FDO 2026`，会期是 `2026-03-24` 到 `2026-03-27`。
- 出于安全考虑，这份研发总记录里不保存完整护照号和完整出生日期；如需签证或行政用途，请以原邀请函 PDF 为准。

## 4.2 仓库内对应证据

- 本地海报源文件写有：
  - `Poster Presenter · FDO 2026 Vienna`
  - `Digital Biosphere Architecture`
  - `GitHub: joy7758`
  - `ORCID: 0009-0002-8861-1481`
- 本地 demo 页面写有：
  - `Verifiable Agent Execution | FDO 2026 Poster Demo`
  - `FDO 2026 poster demo for verifiable agent execution`
- ARO Audit 的 FDO 草案规范写有：
  - `Reference Implementation DOI: https://doi.org/10.5281/zenodo.18728568`
  - `Registered Profile Identifier: 21.T11966/aro-audit-profile-v1`

## 4.3 FDO Testbed Typeregistry 截图记录

以下内容根据你提供的 `typeregistry.testbed.pid.gwdg.de` 页面截图整理。截图显示：

- 页面：`FDO Testbed Typeregistry`
- 当前结果数：`Showing 1 to 10 of 381 results`

可见对象如下：

| 名称 | Handle / ID | 类型 | 备注 |
| --- | --- | --- | --- |
| `aro-audit-demo-do-1` | `21.T11966/aro-audit-demo-do-1` | `FdoService` | Demo object for AROAUDIT_PROFILE_V1 with audit pointers |
| `AROAUDIT_PROFILE_V1` | `21.T11966/aro-audit-profile-v1` | `FdoProfile` | 审计就绪数字对象 profile，带 verifiable trace support |
| `QFDO-Model` | `21.T11966/7867ded011c90186856e` | `FdoProfile` | 截图中可见的既有 profile |
| `FDO-Number` | `21.T11966/dab82eebf36e891570b6` | `FdoAttribute` | 截图中可见的 attribute |
| `QFDO-ModelHyperparameters` | `21.T11966/81fa0a291544d81976ed` | `FdoCombinedAttribute` | 截图中可见的 combined attribute |
| `QFDOProfileModelHyperparameter` | `21.T11966/d2f93697d36c4a84f88d` | `FdoProfile` | Profile for defining model hyperparameters |
| `ARO_AUDIT_DEMO_OBJ_V1` | `21.T11966/aro-audit-demo-obj-v1` | `BasicInfoType` | Demo object declaring ARO audit trace support |
| `ARO_AUDIT_MANIFEST_V1` | `21.T11966/aro-audit-manifest-v1` | `BasicInfoType` | Manifest pointer for ARO audit packet demo |
| `ZhangBin` | `21.T11966/0b43b9d2023636df956e` | `User` | 你的 FDO Testbed 用户对象在截图中可见 |
| `XFDO_Service_S00000253` | `21.T11966/c388e830bcface5d87b0` | `FdoProfile` | 截图中可见的既有 profile |

这个截图的重要性在于：它说明你的 `aro-audit` 相关对象不是只存在于本地仓库，而是已经进入 FDO Testbed 的对象注册上下文。

## 5. 比赛与申报材料状态

## 5.1 当前比赛表达主线

当前最稳的比赛表达是：

`AegisTrust = AI 可信执行基础设施`

不是去卖“一个更聪明的模型”，而是去解释：

- 为什么高风险 AI 动作现在需要可信执行
- 为什么现有 agent stack 普遍缺少“可拦截、可留证、可复验”的闭环
- 为什么你这套东西不是单点安全 feature，而是基础设施能力

## 5.2 已有比赛材料

`docs/bp` 下已经整理出一套可直接用于比赛、答辩和路演的材料：

- 主稿 BP：`aegistrust_bp.md`
- 奖项版 BP：`aegistrust_bp_v4_award.md`
- 默认 PPT：`aegistrust_pitch.pptx`
- 奖项版 PPT：`aegistrust_pitch_v4_award.pptx`
- 评委诊断：`judge_view_diagnosis.md`
- 叙事母线：`award_storyline.md`
- 多档讲法包：`pitch_pack_v1.md`
- 高频追问：`judge_qa_top10_v1.md`
- 主舞台/备份拆分：`mainstage_vs_backup.md`
- 报名表短版：`application_form_short_v1.txt`

## 5.3 HICOOL 2026 相关证据

仓库 `aro-audit/competition/hicool-2026` 里已经有明确比赛化材料：

- `README.md`：统一参赛叙事
- `PITCH_15P_CN_EN.md`：双语 pitch
- `DEFENSE_QA_CN_EN.md`：双语答辩问答
- `EVIDENCE.md`：证据快照

其中已经可确认的比赛信息包括：

- 比赛：`HICOOL 2026`
- 赛道：`人工智能/软件和信息服务`
- 当前推荐报名名：`AegisTrust: Verifiable AI Action Governance Stack`
- `spear-check adoption count`：`18`

## 5.4 当前判断

- 如果是技术同行或长期合作方，先讲 `Digital Biosphere Architecture`
- 如果是评委、路演、比赛、融资、机构沟通，先讲 `AegisTrust`
- 如果被追问研究深度，再把五层架构、POP、AIP、MVK 拉出来

## 6. 论坛沟通与外部交流

你已经有一组可继续复用的论坛/社区沟通资产，重点不在“发了多少帖子”，而在于你已经把不同社区需要的入口切清楚了。

### 6.1 LangChain 方向

- `persona-object-protocol/docs/outreach/langchain-forum-post.md`
  - 核心主题：`POP v0.1.7` 的 LangChain-facing execution contract surface
- `persona-object-protocol/docs/outreach/langchain-forum-post.zh.md`
  - 中文版简述
- `persona-object-protocol/docs/outreach/langchain-maintainer-short-note.md`
  - 面向 maintainer 的短说明

### 6.2 FDO / 数字对象方向

- `digital-biosphere-architecture/docs/outreach/fdo_forum_post_final.md`
  - 核心主题：面向 FDO 系统的 AI runtime governance Evidence Object

### 6.3 CrewAI / 多智能体方向

- `digital-biosphere-architecture/docs/outreach/crewai_forum_post_final.md`
  - 核心主题：多智能体系统里的审计证据与 runtime governance

### 6.4 LangChain 治理栈方向

- `digital-biosphere-architecture/docs/outreach/langchain_forum_post_final.md`
  - 核心主题：Governance Architecture for Autonomous Agents

### 6.5 外部沟通摘要

- `digital-biosphere-architecture/docs/community_discussion_summary.md`
  - 这里是当前最适合给外部读者快速看懂你整套方向的英文摘要之一

## 7. 新窗口推荐阅读顺序

以后如果换电脑、换 AI 窗口，建议按这个顺序补上下文：

1. 先读本文件：`docs/bp/zhangbin_rnd_master_record.md`
2. 再读主稿：`docs/bp/aegistrust_bp.md`
3. 再看 PPT：`docs/bp/aegistrust_pitch.pptx`
4. 再看讲稿：`docs/bp/pitch_pack_v1.md`
5. 再看评委问答：`docs/bp/judge_qa_top10_v1.md`
6. 如需看上位架构，再读：`joy7758/README.md`
7. 如需看外部沟通摘要，再读：`digital-biosphere-architecture/docs/community_discussion_summary.md`

## 8. 当前最值得继续推进的事项

- 持续把 `AegisTrust` 讲成“可信执行基础设施”，而不是“又一个 agent 安全工具”
- 把 FDO 2026 海报演讲与 GitHub 公开资产之间的关系继续收紧
- 继续沉淀可直接面向评委或合作方的短讲法、答辩稿和报名摘要
- 每次 agent 有新进展，先更新这份总记录，再去做下一轮材料分发

## 9. 敏感信息处理规则

- 这份文档可以记录：
  - 项目进展
  - 对外公开材料
  - 已公开或可公开的注册信息
  - 比赛材料和论坛沟通状态
- 这份文档不要记录：
  - 完整护照号
  - 完整出生日期
  - 私密联系方式
  - 不适合放进仓库的签证或行政细节

## 10. 更新日志

### 2026-03-13

- 统一当前主线为：`AegisTrust = AI 可信执行基础设施`
- 完成一等奖叙事版材料整理，产物位于 `docs/bp`
- 已生成并整理：
  - `aegistrust_bp_v4_award.md`
  - `aegistrust_pitch_v4_award.pptx`
  - `judge_view_diagnosis.md`
  - `award_storyline.md`
  - `pitch_pack_v1.md`
  - `judge_qa_top10_v1.md`
  - `mainstage_vs_backup.md`
  - `application_form_short_v1.txt`
- 默认主稿和默认 PPT 已切到 v4 奖项版
- 已完成本地 replay / smoke 检查：
  - `god-spear` PASS
  - `safety-valve-spec` PASS
  - `execution-integrity-core` PASS
  - `aro-audit` PASS
  - `verifiable-agent-demo` PASS
- 已把这批奖项材料推送到 `docs` 仓库：
  - repo: `https://github.com/joy7758/docs.git`
  - branch: `add-langchain-aro-integration`
  - commit: `b0912c6b`
- 新建本文件，作为后续所有 agent 工作的总同步入口
- 记录论文提交流程状态：
  - Conference: `ASE 2026`
  - Submission ID: `360`
  - Title: `From Observability to Verifiability`
  - Status: `Ready for review`
