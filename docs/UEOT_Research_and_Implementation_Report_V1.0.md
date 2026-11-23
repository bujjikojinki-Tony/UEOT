<!-- Source: Google Docs 1vXBuVtlJ4JkzYu2ka2skkzkfwuBmtOQjp2krUO1yRow; revision AHj4eMSKMZoWdKHYZaPJSZMODPV7K7N2upbRgsQGx_nkHjxGhQC9EHbEh3a6qbdk0Jpg990QjQsiXvoX0_Sf9FOAcpTZZaNTfL5CW2175OI; exported 2026-11-23. -->

# 统一工程对象理论（UEOT）研究与工程实施报告 V1.0

> 研究整合稿｜2026年11月｜状态：待专家审查（非正式标准、非生产验收结论）

## 摘要

统一工程对象理论（Unified Engineering Object Theory，UEOT）旨在解决工程数据长期围绕文档、编码、模型或系统记录组织，而缺少对真实工程对象稳定身份及其跨阶段语义连续性表达的问题。本报告在既有 UEOT 正式基线和 Browser V1.0—V1.8 参考实现研究基础上，提出从理论语义、对象模型、基线治理、证据追溯、运行服务、工程问答到人工治理决策的整体框架。报告坚持“冻结理论核心、受控扩展、以真实工程数据试点验证”的原则。文中将已确立的理论约束、参考原型能力、尚待验证的工程主张严格区分。

## 一、研究背景、目标与边界

### 1.1 工程对象问题

在核电等复杂工程中，设计院、设备制造商、建造单位、调试单位和运营单位各自形成不同编码、文件、模型与数据库记录。同一实体在设计、制造、安装和运行阶段往往被重复描述；相反，单一编码也可能随配置、用途或时间变化而指向不同的语义上下文。以系统、文档或主数据记录为中心的集成方法，能够交换信息，却不必然保证工程对象身份、属性适用性、证据权威性和变更影响推理的一致。

### 1.2 研究目标

目标不是取代 PLM、PDM、ERP、EAM、DCS 或工程设计工具，而是建立跨系统的工程对象语义控制层：识别对象、统一引用、保留不同投影、限定断言适用范围、治理配置与基线、支持可解释查询，并在关键条件不足时阻止确定性工程结论。应用领域以核电 SSC 为参考，同时保持跨行业抽象能力。

### 1.3 研究边界与成熟度

UEOT V1.0 Theory Core 作为冻结基线处理；Domain Profile、Project Profile、Conformance Profile 与 Implementation Extension 可在不改变核心语义的前提下扩展。现有 Browser、嵌入式数据存储、HTTP Mock Backend、查询与解释组件均属于参考实现，不代表已完成真实 EB 生产数据验证、监管批准或生产级安全认证。

## 二、UEOT 理论体系与核心原则

### 2.1 理论与实现链

建议采用 UEOT → UEST → UEOnt → UEO → ERT → EPT → USDC → UDT/UEKG → Engineering Intelligence 的分层表达。UEOT 提供总体理论，UEO 作为工程对象语义实体，ERT/EPT 分别承载关系与属性语义，USDC 作为语义控制平面，UDT/UEKG 面向数字线程与知识图谱实现；具体术语边界应以冻结基线正式定义为准。

### 2.2 核心区分

（1）Object ≠ Representation ≠ Projection：真实工程对象不是任意一个 CAD 模型、BOM 条目、图纸或系统页面；PBS、FBS、GBS、WBS 等仅是不同结构投影。（2）Identifier ≠ Identity：编码是识别线索而非天然唯一的跨生命周期身份。（3）Version ≠ Configuration：文件版本与工程配置状态不可混同。（4）Type ≠ Role ≠ Function：对象类别、场景角色和承担功能须分别建模。

### 2.3 Qualified Engineering Assertion

工程属性不是无条件的“属性名—数值”二元组。合格工程断言至少应表达 Property、Value、ValueRole、Context、Configuration、ValidTime、Evidence、Authority。只有在对象身份、配置、适用时段、证据和权威来源得到控制后，数值才可用于受治理工程判断。例如“额定流量 505 m³/h”必须注明它是设计值、适用于哪个配置和基线，以及由何证据与责任主体支持。

### 2.4 证据、时间与历史保留

UEOT 应保留历史事实与取代关系，避免新版本覆盖旧工程事实。Supersession 表达状态替代，不能等同于删除。ValidTime 表达工程事实适用时间；记录时间、审查时间和批准时间可作为实现扩展分别保存。

## 三、统一工程对象元模型

### 3.1 对象身份与多编码映射

参考对象 SSC-001（安全注入泵A）可同时关联 RIS-P001（设计设备编码）、SN-260089（制造序列号）、ASSET-A10001（运行资产编码）。三者在各自系统中有业务意义，但须通过受控映射解析到统一工程对象。身份解析出现多候选、冲突或证据不足时，返回 AMBIGUOUS 或 NOT_FOUND，不能静默选择一个对象。

### 3.2 多结构投影与对象浏览

工程对象可参与 PBS 产品分解、FBS 功能结构、GBS 地理/空间结构、WBS 工作结构以及配置视图。对象浏览器宜采用“左侧结构导航—中央对象详情—右侧上下文与证据”布局；每个分解节点可展开身份、属性断言、关系、基线、文件、责任主体、生命周期状态。不同结构之间共享 UEO 身份，但不共享未经限定的断言适用性。

### 3.3 关系语义与推理约束

ERT 关系应具备类型、方向、上下文、来源和有效性约束。关系注册表、P0—P4 传播规则、组合规则、领域闭包与停止规则应通过测试门控。图遍历产生 GraphReachability；工程影响分析可进一步形成 PotentialImpact；ConfirmedImpact 只能在规则、证据、适用 Profile 和授权条件满足后产生。

## 四、配置、基线、证据与权威治理

### 4.1 Basis 模型

应区分 DesignBasis、CurrentBasis、TemporaryApplicableBasis 等基线类型，并通过 BasisMembership、BasisConsistency 和 CurrentBasis 解析控制对象的适用事实。参考对象的 CurrentBasis 为 BL-03，配置示例 CFG-SSC-001-M6。临时适用基线不能被直接改写为设计基线。基线冲突应触发治理升级或停止确定性结论。

### 4.2 Authority 与 Evidence

Authority 不是简单的“最后修改者”，应区分数据提供者、专业责任者、批准主体和工程决策权限。Evidence 可包含设计规范、分析报告、试验记录、供应商提交件、审批记录等；每条断言应保留可追溯证据引用。供应商草稿与正式批准设计发生冲突时，不得仅依据时间新旧覆盖，必须进入 GOVERNANCE_ESCALATION。

### 4.3 Fail-Safe Engineering Semantics

关键门控包括 Identity、Configuration、Basis、Authority、Evidence、Conformance。任一关键条件不满足时，系统应输出 NO_DEFINITIVE_CLAIM、REQUEST_REVIEW 或 GOVERNANCE_ESCALATION，并解释阻断原因；不得为了界面完整性编造唯一答案。

## 五、UEOT Browser 与 Runtime 技术架构

### 5.1 分层架构

推荐采用 Source Systems → Ingestion/Adapter → Runtime Stores → UEOTRuntimeService → HTTP API / Query Gateway → Explainable Browser → Review Workflow 的分层。源系统保持各自记录权威，Adapter 负责语义映射、来源保留与错误显式化；Service Boundary 隔离前端与存储细节；API 负责请求追踪和一致错误模型。

### 5.2 迭代演进

V1.0—V1.2 重点形成对象浏览、模型 Schema、Conformance、参考图、查询推理和正式基线运行视图；V1.3 引入 Runtime Data Adapter 和 JSON Stores；V1.4 引入 EmbeddedStoreProvider / UEOTRuntimeService 的六项服务边界；V1.5 定义 HTTPProvider、OpenAPI 和 Mock API；V1.6 引入 Request ID、Audit Event、统一错误与 Fail-Safe 运行约束；V1.7 引入 Engineering Query Gateway 与 Answer Package；V1.8 形成 Explainable Engineering Answer 界面。上述里程碑表示参考实现演进，不等同于工业级验收。

### 5.3 六项运行服务

核心服务为 resolveObject、getAssertions、getBasis、traverseGraph、getEvidence、resolveProfile。客户端应依赖服务契约而不是直接耦合底层 JSON 结构。HTTP 版本需要统一 Request ID、错误码、审计事件、响应包封与无声降级禁止策略。

### 5.4 生产化缺口

参考后端尚需完善认证鉴权、持久化审计、事务一致性、并发控制、数据权限与脱敏、API 合同一致性、真实系统连接器、版本迁移、运行监控和灾难恢复。特别要避免把演示环境中的 C4 标记或前端 Gate 模拟视为正式 Conformance 认证。

## 六、工程查询、可解释答案与人机协同

### 6.1 Query Gateway

用户问题应先编译为 Query Plan，明确 Intent、Object Reference、Property、Required Conformance 和执行服务，再执行对象解析、基线筛选、断言读取、证据检索与图推理。参考意图包括 PROPERTY_QUERY、BASIS_QUERY、IMPACT_QUERY、OBJECT_360。自然语言解析目前属于受限规则示例，不应宣称具备开放域工程语义理解能力。

### 6.2 Engineering Answer Package

标准答案包应包含 queryId、question、intent、resolvedObjects、semanticGraphPaths、applicableBasis、authorityProvenance、evidenceSet、derivedAssertions、confidence、reviewState、decisionState 和 humanAnswer。答案必须区分原始证据、已选断言、推导结论及人类授权结论。

### 6.3 典型问答

问题：“安全注入泵A当前设计额定流量是多少？”参考答案可指向 SSC-001、CurrentBasis BL-03 和 Design 值 505 m³/h；但只有当 ValueRole、配置、Authority、Evidence 均匹配时才能作为确定性工程回答。问题：“设计变更可能影响哪些对象？”图遍历只能给出可达关系或潜在影响候选，不能自动宣布 ConfirmedImpact。

### 6.4 Explainability 与审查工作流

工程答案界面应同时展示结论、对象、适用基线、断言、Authority、Evidence、Semantic Path、风险门控和人工审查状态。下一阶段应引入 Review Case、Reviewer、Approval Authority、Decision Record、签署时间、撤销/重审和审计链，确保 ConfirmedImpact 只能由具备授权的流程确认。

## 七、核电 SSC 试点方案

### 7.1 范围与样本

建议选择一条可去标识化的核电设备/系统链作为试点，覆盖约 20—100 个 UEO、设计—制造—运行或设计—建造—调试三个生命周期阶段、至少两种配置、一个工程变更（ECR/ECN）和一个偏差或 NCR 链。该范围是试点设计建议，不是已经完成的验证结果。

### 7.2 典型业务链

以安全注入泵及其电机、阀门、管道、仪控接口和技术要求为对象，建立 PBS/FBS/GBS 多视图；导入设计规范、计算、制造序列、安装记录和试验记录；构建设计值、要求值、分析值、试验值的 Qualified Assertions；再通过变更事件检验对象识别、基线选择、证据一致性和影响停止规则。

### 7.3 比较实验

设置三组对照：传统文档/系统中心查询、未限定语义的普通知识图谱、UEOT 受治理查询。比较对象匹配正确率、跨配置混用率、证据追溯完整率、误报/漏报、查询时延和人工审查工作量。关键安全指标 UnsafeDefinitiveClaimRate 应以 0 为验收目标，并明确分母、用例集和测量规则。

## 八、三年实施路线

第一年：基线与数据底座。完成核心术语与模型冻结清单、对象注册与身份映射、元模型/关系注册表、数据源盘点、权限与证据规范；选定试点设备，形成首批 UEO 和审计可追溯的参考数据中心。优先采用现有平台数据接口，不进行大规模系统替换。

第二年：运行服务与业务闭环。建设持久化对象库、Basis/Assertion/Evidence 服务、受控适配器、Conformance 测试流水线；接入设计变更与 NCR 业务，形成 Object360、Impact Candidate 和审查工作流。逐步开展接口性能、安全、权限和回归测试。

第三年：规模化验证与治理推广。在多个专业/项目推广对象模型与 Profile；完善工程知识图谱、可解释问答和授权决策闭环；建立跨系统质量指标、变更管理、运营治理组织和持续审计机制。只有在真实场景达到质量、安全和成本目标后再考虑扩大自动化程度。

## 九、测试、验收与风险控制

### 9.1 测试分层

模型层验证身份不变量、断言完整性、Basis 一致性、关系类型和停止规则；服务层验证六项 API 合同、错误码、并发、幂等与审计；推理层验证 GraphReachability/PotentialImpact/ConfirmedImpact 严格区分；界面层验证阻断状态、证据呈现和人工审批。测试应覆盖正常、缺失、歧义、冲突、过期、跨配置和恶意输入。

### 9.2 验收门槛建议

硬门槛：UnsafeDefinitiveClaimRate=0；身份歧义不自动确定；Basis 冲突不输出确定性属性；无 Evidence 的关键工程结论不得通过；ConfirmedImpact 必须保留审批主体和依据。其他数值阈值（覆盖率、响应时间、误报率、可用性）应在试点数据分布与风险分析后确定，不能在缺乏基线测量时宣称已达标。

### 9.3 风险与对策

主要风险包括跨系统标识映射错误、供应商资料权威冲突、临时基线混入正式设计、图推理过度传播、AI 生成无证据结论、数据权限越界及原型与生产架构混淆。对策分别为人工复核与候选保留、Authority Matrix、BasisConsistency Gate、Typed Reasoning、证据强制关联、最小权限和分阶段上线。

## 十、结论与后续工作

UEOT 的关键价值在于将工程对象稳定身份、受限定属性断言、基线与证据治理、关系推理边界及人工授权决策组合为一套可实现的语义控制机制。当前理论结构和 Browser 参考链路已形成可供工程试点的总体方案，但尚不足以证明生产级有效性。建议坚持 FREEZE THEORY → CONTROL EXTENSIONS → PILOT WITH REAL DATA → REOPEN ONLY IF NECESSARY。近期优先事项是建立真实数据试点、补齐端到端 HTTP 测试与授权工作流，并用反例测试验证 Fail-Safe 语义。

## 资料与版本说明

本稿依据本项目既有 UEOT 研究讨论、V1.0 Formal Baseline 约束摘要及 Browser V1.0—V1.8 迭代记录整合。因本次未直接复核全部原始白皮书、正式基线文档及每一版代码仓库，本稿应视为“研究整合稿”，不是逐条原文审计版。此前微信文章链接未取得正文，不作为本报告事实依据。后续正式发布应补齐原始文档清单、版本哈希、章节级来源映射、测试证据和评审签署。

## 专题深化 A：UEO 元模型的规范化定义

### A.1 核心实体及其不可混同的职责

UEO（Unified Engineering Object）承担跨系统稳定身份；IdentifierAssignment 表达某个来源系统在有效时段内赋予对象的编码及映射依据；Representation 表达 CAD、BOM、文档、仿真模型或系统记录；ProjectionMembership 表达对象在 PBS/FBS/GBS/WBS 某个视图中的节点位置。上述实体之间采用显式关联，禁止以文件主键替代 UEO 身份。一个 UEO 可以有多个编码、多个表示和多个投影成员资格。

建议实体字段：UEO{globalObjectId, objectType, lifecycleState, identityStatus, createdAt}；IdentifierAssignment{scheme, code, issuer, validFrom, validTo, sourceRef, resolutionStatus}；Representation{representationId, kind, sourceSystem, sourceVersion, sourceUri, capturedAt}；ProjectionMembership{projectionType, projectionId, parentNode, childNode, context, validTime}。这些字段为实施建议，并非声称全部属于 UEOT V1.0 冻结公理。

### A.2 对象身份解析规则

输入 ref 可为全局身份、设备编码、序列号或资产编码。解析过程应依次进行编码体系识别、来源与有效期约束、候选 UEO 聚合、同一性证据检查、冲突检查和决策输出。建议输出 RESOLVED、AMBIGUOUS、NOT_FOUND、CONFLICT；只有 RESOLVED 可进入确定性断言检索。对象重命名不应改变 globalObjectId；对象替换、拆分和合并须通过显式生命周期事件及映射关系记录，不应自动继承全部旧断言。

### A.3 多结构投影的语义隔离

PBS 描述构成/产品层级，FBS 描述功能承担，GBS 描述地理或空间位置，WBS 描述工作分解。相同 UEO 在不同结构中可处于不同层级与关系类型；结构节点不等于实体本身。对于“10厂房内某阀门”查询，应先通过 GBS 空间关系找到候选，再回到 UEO 获取身份、设备属性及其当前配置；不能将空间归属关系推断为功能或产品组成关系。

### A.4 Qualified Assertion 的机器可执行约束

推荐断言结构 Assertion{assertionId, subjectUEO, property, value, unit, valueRole, context, configuration, validTime, evidenceRefs[], authorityRef, status, supersedes[]}。最低约束：subjectUEO 必须解析；property 与 unit 必须通过领域 Profile 校验；valueRole 不得丢失；configuration 与查询上下文必须匹配；validTime 必须覆盖目标工程时间；evidenceRefs 和 authorityRef 必须按关键性等级校验。任何一个关键约束失败时不得将断言升格为最终工程结论。

参考泵流量四类断言可为 Required ≥500、Design 505、AnalysisResult 508、Tested 512 m³/h。它们不是同一属性的四个互相覆盖的“最新值”，而是 ValueRole 不同、来源不同、验证目的不同的四个工程事实。选择 Design 505 时，不能引用 Tested 512 代替设计值；判断是否满足 Required ≥500 时，应额外检查比较对象、适用配置和测试/分析证据。

### A.5 元模型最小关系示意

UEO ─hasIdentifier→ IdentifierAssignment；UEO ─representedBy→ Representation；UEO ─memberOfProjection→ ProjectionMembership；UEO ─subjectOf→ Assertion；Assertion ─supportedBy→ Evidence；Assertion ─governedBy→ Authority；Assertion ─applicableUnder→ Configuration/Basis；UEO ─relatedBy→ TypedRelation → UEO。关系命名仅为实施层示意，实际发布需由关系注册表统一命名并测试。

## 专题深化 B：Basis、Evidence 与 Authority 的治理算法

### B.1 Basis 不是一个普通版本号

Basis 应表达在某个工程决策上下文中被批准采用的一组适用对象、配置、断言和文档。建议结构 Basis{basisId,basisType,scope,configurationRef,effectiveTime,approvalRef,state} 与 BasisMembership{basisId,memberRef,memberType,validTime,reason}。CurrentBasis 应由适用范围、有效时间、批准状态和优先级规则解析，而不是读取任意一条 isCurrent=true 标记。若多个候选在同一上下文中互相矛盾，应报告 BASIS_CONFLICT。

### B.2 当前基线解析流程

步骤一：确定对象、工程项目、机组/系统、配置、查询时间和决策用途。步骤二：获取适用 Basis 候选及 Membership。步骤三：验证批准状态和时间有效性。步骤四：检查 DesignBasis、CurrentBasis 与 TemporaryApplicableBasis 的关系。步骤五：运行 BasisConsistency；冲突则停止。步骤六：返回 CurrentBasis 及证明链。对于临时偏差，仅在限定范围与时间内形成 TemporaryApplicableBasis，不自动修改正式设计基线。

### B.3 Authority 优先级不能仅靠数值排序

应维护 Authority Matrix：按专业、工程阶段、对象类型、断言类型和批准动作明确数据提供、技术审核、工程批准与监管/许可约束。设计院批准文件、供应商草稿、现场试验记录之间不一定存在跨所有问题的统一高低顺序。不同来源若对不同 ValueRole 陈述事实可并存；若对同一上下文的同一角色发生冲突，则应建立 ConflictCase 并进入 GOVERNANCE_ESCALATION。

### B.4 Evidence 链与审计

Evidence 建议至少记录 evidenceId、sourceSystem、sourceDocument、revision、issuer、approvalState、contentHash、validTime、retrievedAt、accessPolicy。审计链应记录 requestId、actor、operation、objectId、basisId、evidenceRefs、decisionState、timestamp、policyVersion。哈希只能证明所检文件内容一致，不能单独证明工程正确性或审批合法性。敏感文档可通过权限化引用与摘要提供证据，不应在问答界面无条件泄露全文。

### B.5 反例及判定

用例 B-01：BL-03 已批准且唯一，允许返回当前基线及来源。B-02：BL-03 与 BL-04 同时满足相同范围但互斥，必须 NO_DEFINITIVE_CLAIM。B-03：TM-2026-04 在限定时段内适用，应标记 TemporaryApplicableBasis，不能覆盖 DesignBasis。B-04：供应商新草稿与已批准设计矛盾，输出 GOVERNANCE_ESCALATION。B-05：断言缺少可访问 Evidence，关键工程结论必须阻断。以上均为建议验收用例，不是已执行测试报告。

## 专题深化 C：Runtime、API 与数据中心实施架构

### C.1 逻辑架构与部署边界

第一层 Source：PLM/PDM、设计计算、采购制造、施工、调试、EAM/运行和文件管理系统。第二层 Adapter：采集、去重、身份候选映射、Schema 校验、来源标记、变更事件捕获。第三层 Semantic Stores：UEO Registry、Assertion Store、Basis Store、Evidence Index、Typed Graph、Profile Registry、Audit Ledger。第四层 Runtime Service：六项核心服务与 Conformance/Fail-Safe Gate。第五层 Application：Object Browser、Scenario Workbench、Change Impact Analysis、Engineering Query Gateway、Review/Approval。

数据中心建设应优先形成“受治理的工程对象数据中心”，而非一次性集中搬迁所有原始工程文件。保留源系统的权威数据，中心保存身份索引、受限定断言、关联、基线、证据指针和审计记录。对确需缓存的文件和模型实施版本、权限、加密和保留策略；明确增量同步、失效通知及回溯机制。

### C.2 六项服务的输入输出合同

resolveObject(ref, context) → Resolution{status, candidates, object, evidence}；getAssertions(objectId, filter) → AssertionSet；getBasis(objectId, context) → BasisResolution{currentBasis, memberships, consistency}；traverseGraph(root, relationProfile, depth, context) → TraversalResult{nodes, paths, stopReasons}；getEvidence(ref, accessContext) → EvidenceSet；resolveProfile(ref, context) → ProfileResolution。字段是建议的生产合同目标，须与现有参考后端实际 JSON 结构逐项对齐，不能直接当作已发布 API 规范。

### C.3 请求处理与失败闭环

每个请求生成 requestId，完成身份验证和最小权限检查，再调用 Runtime；服务输出携带 provenance 与 gate result；错误响应采用统一 code、severity、message、decisionState、auditRef。建议定义 400 INVALID_QUERY、404 OBJECT_NOT_FOUND、409 IDENTITY_AMBIGUOUS/BASIS_CONFLICT、403 ACCESS_DENIED、503 EVIDENCE_UNAVAILABLE 等错误。发生外部数据源超时，不得用缓存旧值悄然代替当前有效断言；若采用缓存必须展示 asOf 与过期风险。

### C.4 V1.5—V1.8 联调重点

重点核验 HTTPProvider 是否正确解包 V1.6 响应 envelope；EmbeddedStoreProvider 与 HTTPProvider 对六项服务的输出语义是否一致；getBasis 的 consistency 是枚举还是结构；Query Gateway 的配置匹配是否正确；是否错误地用“无当前配置匹配时退回任意 Design 值”生成确定性结论。上述均应列为集成风险，必须通过真实运行时回归测试后方可宣称通过。

### C.5 安全与运行保障

生产化最低要求包括身份认证、角色/属性双重授权、按对象/文件/属性的访问控制、密钥管理、审计不可抵赖性策略、供应链依赖治理、数据备份恢复、API 限流、异常检测与运维监控。核电 OT 与工程设计 IT 的网络隔离要求需由具体场景安全评估决定，不能因为语义服务需要跨域访问就默认打通控制网络。

## 专题深化 D：Engineering Intelligence 与解释性决策

### D.1 问题编译与意图解析

自然语言问题首先拆解为 intent、objectRef、property、valueRole、time、configuration、basisScope、relationProfile、depth、requiredConformance。若用户只问“泵的流量”，缺少对象或 ValueRole，Gateway 应澄清或展示候选，不得默认把 Design、Required、Tested 视为同一答案。大模型可辅助识别候选意图，但必须由确定性的语义门控与服务执行生成可核查结论。

### D.2 工程答案形成过程

步骤一，Identity Gate：解析唯一 UEO。步骤二，Context Gate：限定项目、配置、时间、用途。步骤三，Basis Gate：确定唯一适用基线。步骤四，Assertion Gate：按 Property 与 ValueRole 筛选候选。步骤五，Authority/Evidence Gate：核查批准主体、证据状态与权限。步骤六，Reasoning Gate：运行受控规则并记录传播停止点。步骤七，Answer Composer：输出结论、支持断言、证据、限制和审查状态。步骤八，Audit：记录全过程。

### D.3 影响分析的三阶段类型约束

GraphReachability 仅证明按指定边类型和遍历规则存在路径。PotentialImpact 是经专业传播规则、上下文和停止条件过滤的候选集合。ConfirmedImpact 需要人工审查、工程证据与授权 Decision Record。形式上可写为 ConfirmedImpact ⊆ PotentialImpact ⊆ GraphReachability（仅当相关 Profile 定义了这种包含关系时成立；跨 Profile 或外部人工补录情形应另行审查）。不得仅凭遍历深度或路径数量自动提升结论等级。

### D.4 解释性答案的最小界面

答案卡首屏展示：结论或禁止结论原因、UEO 身份、CurrentBasis、DecisionState、ReviewState；第二层展开 Assertion、ValueRole、Configuration、ValidTime、Authority、Evidence；第三层展示 Graph Path、推理规则版本、STOP Reason、数据源时间戳和审计编号。缺失信息以“未解析/未验证”展示，不能隐藏在折叠面板而继续显示确定性结论。

### D.5 人工审查与审批状态机（拟议）

推荐 ReviewCase 状态 DRAFT → SUBMITTED → UNDER_REVIEW → APPROVED / REJECTED / RETURNED；批准后形成 DecisionRecord{decisionId,scope,objectIds,basis,decisionType,reviewer,approver,authorityProfile,evidenceRefs,approvedAt,signatureRef,revocationState}。变更证据或基线后触发 REOPEN_REQUIRED，旧决定保留历史并标注失效/取代，不允许直接覆盖审批记录。V1.9 才是该能力的建议实现阶段，当前不能宣称已具备。

### D.6 AI 安全边界

提示注入、检索污染、越权读取、工具参数操纵、跨配置信息拼接和“合理但无证据”的生成答案是主要风险。LLM 输出只能作为 Query Plan 候选或解释文本草案，不能独立赋予 Authority；所有关键操作经 Runtime 的权限、语义和证据门控。应保存输入、计划、检索引用、规则版本与最终审批状态，形成可复核的审计链。

## 专题深化 E：工程验证矩阵与交付物

### E.1 最小测试矩阵

ID-01 单编码唯一映射；ID-02 多编码同对象；ID-03 编码冲突阻断。AS-01 Design/Required/Tested 区分；AS-02 单位与 ValueRole 不兼容阻断；AS-03 有效时间过期阻断。BS-01 CurrentBasis 唯一；BS-02 双基线冲突；BS-03 临时基线不覆盖设计基线。EV-01 Evidence 缺失；EV-02 Evidence 已撤销；AU-01 Authority 冲突升级。GR-01 可达不等于确认影响；GR-02 STOP 规则；GR-03 审批缺失禁止 ConfirmedImpact。API-01 HTTP envelope；API-02 Provider 等价；API-03 审计 requestId 贯通。SEC-01 未授权对象不可读取；SEC-02 恶意问题不绕过 Gate。

### E.2 分阶段交付

阶段一交付对象/关系/断言/基线 Schema、Identity Registry、Source Mapping、Conformance Test Catalog；阶段二交付数据中心语义库、六项 Runtime API、Adapter 和审计链；阶段三交付 Object360、Change Impact、Query Gateway、Explainable Answer 和 Review Workflow；阶段四交付真实工程对照实验、风险分析、试点验收报告及推广决策。每个阶段必须提供源数据清单、版本、测试用例、执行日志和责任签署。

### E.3 正式版待补资料

仍需取得并核验 UEOT V1.0 Formal Baseline 原件、12 项核心公理逐条文本、ERT/EPT 与 USDC 的权威术语表、V1.0—V1.8 各版代码与测试报告、实际 EB 业务样本、来源文献及相关标准条款。本文新增字段、状态机、API 错误码、部署分层和测试矩阵均标记为“建议实施扩展”，不得视为已冻结理论定义或已经执行的验证结论。

## 专题深化 F：UEOT V1.0 正式基线对照审查（基于原始 Release Note）

### F.1 依据、范围和证据等级

本轮已核对原始《00_UEOT_V1.0_Formal_Baseline_Release_Note.docx》（发布日期 2026-09-03，状态 FORMAL BASELINE / THEORY & SOLUTION FROZEN）。其发布声明为：UEOT V1.0 = Frozen Theory Core + Frozen Semantic Contract + Reference Implementations + Test-Gated Profiles + Pilot-Required Industrial Validation。该文件列出五份正式文档，但本轮尚未取得五份文件全文，因此以下对照仅能确认 Release Note 中的冻结主题、Findings、测试口径与限制，不能宣称已逐条审计 12 条核心公理或完整 Schema。

### F.2 正式文档依赖链与变更治理

Release Note 明确文档依赖顺序为 Theory Whitepaper → Modeling Method & Meta-model Specification → Reference Architecture & Implementation Plan → Conformance Specification → Nuclear Reference Domain Application Guide。核电 SSC/RIS/EB 语义不反向定义 UEOT Core。新增行业、项目、平台和 AI 规则应通过 Domain Profile、Project Profile、Conformance Profile 或 Implementation Extension 扩展。Editorial、Clarification 通常不打开 Theory Core；只有 Normative Theory Change 才需 Theory Reopen Review。

### F.3 冻结主题与本报告映射

已由 Release Note 直接确认的冻结主题：① Engineering Object Problem；② UEO/Persistent Semantic Identity；③ Object ≠ Representation ≠ Projection；④ Identifier ≠ Identity、Version ≠ Configuration、Type ≠ Role ≠ Function；⑤ ERT/EPT/UDT 核心边界；⑥ Qualified Engineering Assertion 及 Context/Configuration/Time/Evidence/Authority；⑦ Basis/BasisMembership/BasisConsistency/CurrentBasis；⑧ Historical Preservation/Supersession；⑨ Typed Reasoning 与 GraphReachability/PotentialImpact/ConfirmedImpact 分离；⑩ Fail-Safe Engineering Semantics；⑪ USDC 语义控制平面；⑫ Engineering Intelligence 与 Human-governed Authority；另列“12 条核心公理”作为冻结内容，但 Release Note 未载明公理全文。本报告第二至第六章对这些主题作了解释；A—E 专题中新增的字段结构、错误码、审批状态机属于建议扩展，不得误认为逐字来自冻结文档。

### F.4 TEST-GATED 与延期范围

Release Note 将详细 Relation Registry、P0–P4 具体传播映射、Relation Composition Registry、领域 Closure/Stop Rules、项目级 Authority precedence、行业 Design/Licensing/Operating Basis Profile 列为 TEST-GATED，非一概冻结的跨行业常量。明确延期内容包括真实 EB/核电工程数据 Pilot、工业性能和生产级 SLA、跨项目 Identity/Impact 统计准确率、监管/核安全/产品认证，以及 AI 自主工程批准能力（V1.0 原则上不授予）。

### F.5 正式验证证据与六项 Finding

验证口径：Formal baseline tests = 107（Round 1:40、Round 2.1:31、Round 3:36）；Later package-local executions = 45（V0.5:6、V0.6:8、V0.7:9、V0.8:8、V0.9:14）；Observed executions = 152，但不能声称是 152 项去重独立测试。所有这些属于 Synthetic/Reference Conformance Evidence，不构成 Industrial Validation。

正式 Findings：F-R2-001：STOP target 不得进入 PotentialImpactSet；F-R3-001：Temporal Identity Ambiguity 使用半开 Effectivity 和 AMBIGUOUS；F-R3-002：Basis Conflict 采用 BasisConsistency 与 conflict gate；F-R3-003：Multi-Authority Conflict 进入 GovernanceEscalation，precedence 由 Profile 定义；F-R3-004：Configuration Branch Ambiguity 未解析配置不得确定性回答；F-R3-005：Temporary Modification 中 TemporaryApplicableBasis ≠ DesignBasis。以上应作为端到端回归的最低追踪项。

### F.6 已有报告需要修正的表述

（1）此前“试点 20–100 个 UEO、三个阶段、两个 Configuration、一个 ECR、一个 NCR/Deviation”不仅是本报告建议，实际也是 Release Note 第 11 节规定的 Pilot 最低触发范围；应标为正式基线提出的试点条件。（2）“UnsafeDefinitiveClaimRate=0”同样是正式 Critical Pilot Safety Gate，而不是仅为作者建议。（3）V1.8 可解释答案和 V1.9 审批流程属于参考实现演进，不得与 2026-09-03 的 Formal Baseline 冻结范围混淆。（4）12 条公理具体内容尚缺正式主文，不能从冻结主题反向拼凑为公理全文。

## 专题深化 G：核电 SSC 端到端可审查案例

### G.1 案例性质与边界

本案例为根据现有 UEOT 参考场景构建的合成演示，不代表任何真实核电厂的设计批准数据。对象 SSC-001 安全注入泵A，编码 RIS-P001 / SN-260089 / ASSET-A10001，参考 CurrentBasis BL-03、Configuration CFG-SSC-001-M6。数值 Required ≥500、Design 505、AnalysisResult 508、Tested 512 m³/h 均作为参考数据，不能用于实际核安全判断。

### G.2 从对象身份到断言选取

步骤 1：接收“RIS-P001 当前设计额定流量是多少？”并提取 objectRef、Property=RatedFlow、ValueRole=Design、查询时间和配置。步骤 2：IdentifierAssignment 将 RIS-P001 映射至候选 SSC-001，检查来源、有效时间与冲突。步骤 3：从 BasisMembership 与 CurrentBasis 解析 BL-03，验证 BasisConsistency。步骤 4：仅选择 subject=SSC-001、Property=RatedFlow、ValueRole=Design、Configuration=CFG-SSC-001-M6、时间与 BL-03 均适用的断言。步骤 5：核验 Evidence 和 Authority。步骤 6：若门控全部通过，展示“设计额定流量 505 m³/h（参考样本）”及证明链；若证据未提供，则展示候选值并输出 NO_DEFINITIVE_CLAIM，不得伪造批准依据。

### G.3 变更影响分析与停止传播

假设设计变更 ECR-DEMO-01 涉及泵出口阀门的接口要求。首先构建 UEO、接口、系统和证据之间的 Typed Relations；GraphReachability 返回按 Profile 可达的对象路径。随后应用关系传播映射、Configuration、ValidTime、Domain Closure 和 Stop Rules，生成 PotentialImpactSet。任何被 STOP 规则拦截的目标必须从 PotentialImpactSet 排除，并记录 stopReason。最后通过工程专业复核和 Authority Decision 才能形成 ConfirmedImpact。若关系 Profile 未经测试或审批主体缺失，输出“潜在影响待确认”，不宣称已确认。

### G.4 冲突反例及期望状态

反例 1：同一设备编码在交接时间边界对应两个对象。采用半开 Effectivity；若仍无法唯一解析，返回 AMBIGUOUS。反例 2：BL-03 与 BL-04 对同一配置同时有效且冲突，返回 BASIS_CONFLICT/NO_DEFINITIVE_CLAIM。反例 3：两个具备不同职责的来源对同一设计断言提出冲突值，进入 GovernanceEscalation，禁止按时间新旧自动择一。反例 4：查询缺少配置分支而存在多个适用 Configuration，返回 CONFIGURATION_AMBIGUOUS。反例 5：临时改造 TM-DEMO-01 有独立 TemporaryApplicableBasis，不得修改 DesignBasis 记录。反例 6：STOP target 不得出现在 PotentialImpactSet，即使图可达。

### G.5 可执行验证记录模板

每条测试记录应包含 TestId、FindingRef、InputQuestion、ObjectRef、Configuration、ValidTime、BasisCandidates、EvidenceRefs、AuthorityScope、RuleProfileVersion、ExpectedDecisionState、ActualDecisionState、ExpectedImpactSet、ActualImpactSet、AuditRef、Executor、ExecutedAt、PASS/FAIL/INDETERMINATE。当前仅形成测试设计与预期结果；未实际连接真实 EB 数据或执行此案例，Actual 字段必须留空。

## 专题深化 H：审查缺口、证据清单与正式发布门槛

### H.1 来源核验结果

已直接核验：2026-09-03 Formal Baseline Release Note（五页），支持冻结边界、107+45 测试口径、六项 Findings、已知限制、Pilot 触发条件及 Critical Safety Gate。另可访问早期《UEOT Theory Whitepaper V13 讨论版》HTML，其对象示例和理论层次仅用于追踪历史设计思路，不能覆盖正式 V1.0 主文。尚未核验：五份正式文档全文、12 条公理逐字文本、原始测试执行日志与源码版本、真实试点数据。

### H.2 正式审查需要的证据包

建议建立 Evidence Register：BASE-01 Release Note；BASE-02 Theory Whitepaper V1.0；BASE-03 Modeling & Meta-model Specification V1.0；BASE-04 Reference Architecture V1.0；BASE-05 Conformance Specification V1.0；BASE-06 Nuclear Application Guide V1.0；TEST-01 107 formal baseline test cases/results；TEST-02 45 later executions；CODE-01 Reference Implementation commit/hash；PILOT-01 脱敏数据授权与范围；PILOT-02 Independent Oracle 结果；APPROVAL-01 专业审查签署。当前 BASE-01 已核验，其余状态均为“待取得/待核验”，不应自动标记通过。

### H.3 三类结论的发布规则

A 类（正式基线直接支持）：可引用 Release Note 的明确声明，如冻结主题、Findings、测试计数、延期项和试点要求。B 类（研究推导/建议实施扩展）：元模型字段、错误码、状态机、部署分层、测试模板，应标明“建议”并经专业评审。C 类（待实证）：真实对象识别准确率、生产性能、核安全合规性、ConfirmedImpact 工程正确率，未完成独立测试不得写成成果。

### H.4 下一次评审决议建议

建议先完成“正式五文档逐条交叉索引—12 公理核验—Reference Schema/API 差异审查—六项 Finding 回归—真实 Pilot 准入审查”，再决定是否发布《UEOT 研究与工程实施报告 V1.0 评审版》。理论核心维持冻结，新增设计通过 Profile 与 Implementation Extension 管理；只有出现无法由现有语义契约容纳的系统性反例才提出 Theory Reopen。

## 专题深化 I：核心公理核验与规范性追踪矩阵

### I.1 公理核验状态与禁止性规则

本轮重新核对《UEOT V1.0 Formal Baseline Release Note》（2026-09-03）。该文件第4节明确宣布“12 条 UEOT V1.0 核心公理”属于冻结内容，但未给出 12 条的编号、原文或一一对应关系。本次可核实“12 条公理存在且冻结”，不能核实其具体措辞、编号、逻辑独立性或证明。不得将第4节所列主题直接改写为 AX-01 至 AX-12 并冒称正式公理。正式公理逐条核验状态：0/12 已取得原文，12/12 待 Theory Master 核验。

### I.2 冻结主题的可追踪需求（非公理原文）

TRACE-01 Engineering Object Problem：报告第1章；验收关注系统中心记录是否被误当成对象。TRACE-02 Persistent Semantic Identity：第2、3章；检验多编码与对象连续性。TRACE-03 Object/Representation/Projection 分离：第3章；检验文档与结构视图不被当成对象。TRACE-04 Identifier/Identity、Version/Configuration、Type/Role/Function 分离：第2、3章；检验跨语义混用。TRACE-05 ERT/EPT/UDT 核心边界：第2、3、5章；待正式术语表核验。TRACE-06 Qualified Assertion 限定：第2、4章；检验 ValueRole、Context、Configuration、Time、Evidence、Authority。TRACE-07 Basis 系列语义：第4章；检验 BasisConsistency。TRACE-08 Historical Preservation/Supersession：第2、4章；检验旧断言保留。TRACE-09 Typed Reasoning 与影响分层：第3、6章；检验 STOP 与影响类型。TRACE-10 Fail-Safe Engineering Semantics：第4、6、9章；检验缺证据时不输出确定性结论。TRACE-11 USDC Semantic Control Plane：第5章；检验服务与源系统权威边界。TRACE-12 Human-governed Authority：第6章；检验 ConfirmedImpact 人工授权。上述 TRACE 是本报告为了审查便利设立的 12 个追踪主题，并非 UEOT 官方 12 公理编号。

### I.3 规范性要求与扩展边界

每条追踪记录应包含 SourceDocument、SourceSection、ExactText、NormativeLevel、MappedModelElement、ImplementationArtifact、TestCase、EvidenceId、ReviewDecision。现阶段 SourceDocument 可填写 Release Note，第4节；ExactText 仅能填写该文件确实出现的主题句；对于细化字段、规则算法和 API 行为，NormativeLevel 标为 PROPOSED_EXTENSION。详细 Relation Registry、P0–P4 传播映射、组合注册表、Stop Rules、Authority precedence 和行业 Basis Profile 必须走 TEST-GATED 机制，不能擅自归入冻结 Theory Core。

## 专题深化 J：Schema/API 差异审查与工程实现门控

### J.1 差异审查方法

对每个语义对象或服务建立四列：Frozen Semantic Contract、Reference Implementation、Proposed Production Contract、Gap/Decision。Frozen Contract 的逐字段依据必须来自五份正式文档；未取得原文时标为 UNVERIFIED，而不是猜测字段。Reference Implementation 必须绑定仓库 commit、运行配置、Schema 文件、OpenAPI 文件和测试日志；缺任一项时标为 NOT_INSPECTED。Proposed Contract 可以提出字段建议，但不得与 Frozen Contract 混同。

### J.2 当前优先核验对象

对象组：UEO、IdentifierAssignment、Representation、ProjectionMembership、QualifiedAssertion、Basis、BasisMembership、Configuration、Evidence、AuthorityScope、TypedRelation、ImpactDecision。服务组：resolveObject、getAssertions、getBasis、traverseGraph、getEvidence、resolveProfile。必须逐项核对字段名、可空性、枚举值、有效时间边界、错误模型、权限过滤、响应封装与历史保留语义。

### J.3 高风险兼容性清单

GAP-API-01：V1.5 HTTPProvider 与 V1.6 响应 envelope 是否一致，待源码及联调验证。GAP-ID-01：未知对象引用是否错误退回 SSC-001，若存在应定为 FAIL。GAP-BS-01：CurrentBasis 未命中时是否静默回退 DesignBasis，若产生确定性结论应定为 FAIL。GAP-AU-01：Evidence/Authority 缺失是否仍生成工程确认结论，若存在应定为 FAIL。GAP-GR-01：STOP target 是否错误进入 PotentialImpactSet，若存在应定为 FAIL。GAP-UI-01：Query Workspace 是否完整注册并与服务契约连通，待验证。上述为待核验风险，不是已复现缺陷。

### J.4 可操作的核验步骤

步骤1 固定正式基线文件清单和哈希；步骤2 固定实现 commit 与依赖锁文件；步骤3 提取 Schema/OpenAPI 字段和错误码；步骤4 生成“正式约束—实现位置—测试用例”映射；步骤5 运行合成反例与端到端用例；步骤6 记录差异、责任人、处置版本、回归结果；步骤7 经专业评审决定是否允许试点。没有真实源码和运行日志时，本报告只能交付检查规程，不能声称已完成差异检测。

## 专题深化 K：六项正式 Finding 的回归用例规范

### K.1 F-R2-001：Semantic Stop vs Target Admission

输入：构建 A→B→C 的关系链，B→C 在适用 Profile 中为 STOP。预期：GraphReachability 可按图语义记录可达路径，但 C 不得进入 PotentialImpactSet；输出 stopReason、ruleVersion 和 trace。判定：C 被纳入 PotentialImpactSet 即 FAIL；缺少规则版本或输入证据时 INDETERMINATE。

### K.2 F-R3-001：Temporal Identity Ambiguity

输入：同一编码在时间 t 前后对应不同 UEO 的 IdentifierAssignment，采用半开有效区间 [from,to)。预期：在清晰边界按有效区间解析；在重叠或无法确定上下文时返回 AMBIGUOUS。判定：重叠条件下自动选取任一对象并返回 RESOLVED 即 FAIL。

### K.3 F-R3-002：Basis Conflict

输入：同一对象、配置、时间和决策用途存在两个冲突的 CurrentBasis 候选。预期：BasisConsistency 报冲突，禁止确定性断言。判定：未经治理解决直接返回唯一当前值即 FAIL。

### K.4 F-R3-003：Multi-Authority Conflict

输入：两个 Authority 来源对同一适用工程断言给出冲突结论，Profile 未定义可用的优先级规则。预期：GovernanceEscalation，保留两方来源与证据。判定：仅凭时间戳、系统优先级或模型置信度擅自选定即 FAIL。

### K.5 F-R3-004：Configuration Branch Ambiguity

输入：SSC-001 存在 CFG-M6 和 CFG-M7 两个配置分支，查询未指定配置且无法从工程上下文唯一推导。预期：返回 CONFIGURATION_AMBIGUOUS 或等效受控阻断状态，列出候选；不得返回单一确定性值。判定：静默选取 M6 或 M7 即 FAIL。

### K.6 F-R3-005：Temporary Modification Semantics

输入：在临时改造期间引入 TemporaryApplicableBasis，原 DesignBasis 仍存在。预期：临时基线仅在适用范围与时间内参与查询，历史 DesignBasis 不被覆盖；改造结束可追溯恢复或后续正式变更。判定：将 TemporaryApplicableBasis 自动重写为 DesignBasis 或删除历史记录即 FAIL。

### K.7 统一回归记录与结果口径

每条用例应记录 FindingId、CaseId、FixtureVersion、ImplementationCommit、ProfileVersion、InputContext、ExpectedResult、ActualResult、EvidenceLinks、AuditId、Executor、ExecutionTime、Verdict。Verdict 仅可为 PASS、FAIL、INDETERMINATE；未执行时明确标记 NOT_RUN。当前 K.1—K.6 全部为 NOT_RUN，因为未取得目标实现、执行环境和日志，不应误称为已完成测试。

## 专题深化 L：Independent Oracle Pilot 准入与正式评审结论

### L.1 正式基线规定的最低试点范围

依据 Release Note 第11节，取得真实或脱敏 EB/核电工程数据后，Pilot 至少覆盖 20–100 个 UEO、3 个生命周期阶段、2 个 Configuration、1 个 ECR 和 1 个 NCR/Deviation 链，并设置 Traditional/System-centered、Naive Graph Reachability、UEOT 三组对照。Critical Pilot Safety Gate 为 UnsafeDefinitiveClaimRate = 0。

### L.2 Independent Oracle 设计

建议由独立工程专家组在不查看 UEOT 预测结果的情况下形成对象身份、基线适用、属性判定和影响边界的人工金标准。对三组方法使用同一问题集、同一配置和时间上下文。计算身份解析准确率、证据完整率、潜在影响 precision/recall、人工审查耗时和 UnsafeDefinitiveClaimRate。对无法形成专家共识的用例标为 INDETERMINATE，不强行纳入正确率分母。

### L.3 评审结论与发布条件

本轮结论：已完成 Release Note 级别的规范性追踪设计与六项 Finding 的回归规范；未完成 12 条公理原文核验、五份正式主文交叉审查、实际源码/API 差异检测、六项用例运行和真实数据 Pilot。故当前报告可用于方案审查与测试准备，不宜标注“已通过正式技术验收”。进入正式评审版的最低条件为：正式文档齐套、逐条来源映射、代码版本固定、回归证据齐全、未关闭风险显式列示，并由专业负责人签署。

## 专题深化 M：UEOT 工程实施规范草案（Implementation Profile IP-01）

### M.1 规范地位与适用性声明

本专题定义建议性的 Implementation Profile IP-01，用于参考后端和核电 SSC 试点，不修改 UEOT V1.0 Frozen Theory Core。规范性关键字 SHALL/SHOULD/MAY 在本专题内仅对拟议 IP-01 生效；不代表 UEOT 正式基线原文。依赖项：Release Note 已确认的身份连续性、Qualified Assertion、BasisConsistency、Typed Reasoning、Fail-Safe、Human-governed Authority；具体字段仍须与正式元模型规范比对。

### M.2 最小对象记录与数据字典

UEO_RECORD：objectId（不可变字符串，必填）、objectType（受 Profile 约束，必填）、lifecycleState（枚举，必填）、identityStatus（RESOLVED/AMBIGUOUS/CONFLICT，必填）、sourceLinks（可多值）、createdAt（UTC 时间戳）。IDENTIFIER_ASSIGNMENT：scheme、identifier、issuer、subjectObjectId、effectivityStart（含）、effectivityEnd（不含）、evidenceRef；对同一 scheme+identifier+时间上下文产生多 UEO 候选时，不得默默选中。REPRESENTATION_RECORD：representationId、representationType、sourceSystem、sourceRevision、describesObjectIds、evidenceRef。PROJECTION_MEMBERSHIP：projectionId、projectionType、nodeId、objectId、parentNodeId、relationType、context、effectivity。

ASSERTION_RECORD：assertionId、subjectObjectId、propertyId、value、unit、valueRole、context、configurationId、validFrom、validTo、basisRefs、evidenceRefs、authorityRef、assertionState、supersedesRefs。BASIS_RECORD：basisId、basisType、scope、configurationId、effectivity、approvalState、approvalEvidenceRef。RELATION_RECORD：relationId、subjectObjectId、predicateId、targetObjectId、context、configurationId、effectivity、evidenceRefs、ruleProfileRef。所有跨对象引用须执行存在性与权限检查；不允许空值被解释为“全配置通用”。

### M.3 数据进入中心的七道门

ING-01 Source Provenance：确认来源系统、抽取批次和版本；ING-02 Syntax/Schema：字段与类型校验；ING-03 Identity：候选对象匹配与冲突分流；ING-04 Semantic：Property/ValueRole/Unit/Relation 注册表校验；ING-05 Context：配置、时间、基线适用性检查；ING-06 Governance：Evidence/Authority/权限完整性检查；ING-07 Publish：仅通过所有必需 Gate 的记录进入可用于确定性工程回答的索引。未通过记录保留在 Quarantine/Review Queue，并保留原始来源，不可静默删除或自动修正。

### M.4 事件驱动与历史语义

建议事件类型：ObjectRegistered、IdentifierAssigned、RepresentationUpdated、AssertionProposed、AssertionApproved、BasisActivated、BasisConflictDetected、TemporaryModificationStarted、TemporaryModificationEnded、ReviewDecisionRecorded。每条事件包含 eventId、objectId、sourceSystem、sourceRevision、eventTime、ingestedAt、actor、evidenceRefs、correlationId。状态变化通过追加事件与 Supersession 体现；历史断言不得因最新同步而物理覆盖。对于重复事件应按 sourceSystem+sourceEventId 实现幂等。

## 专题深化 N：六项 Runtime 服务的可验收接口设计

### N.1 通用请求与响应封装

建议请求统一携带 requestId、actorContext、projectContext、configurationContext、validAt、profileVersion、purpose。成功响应携带 status、data、provenance、gateResults、auditRef、asOf；失败响应携带 errorCode、decisionState、candidateRefs、blockingReasons、auditRef。响应中若存在不完整 Evidence、Authority 或 Basis，则即使 HTTP 层为 200，也必须在 decisionState 中明确标注 NO_DEFINITIVE_CLAIM，不允许 UI 误读为已确认。

### N.2 resolveObject 与 getAssertions

resolveObject 的前置条件为有效编码体系或全局 UEO 引用；后置条件是唯一 RESOLVED 对象或显式 AMBIGUOUS/NOT_FOUND/CONFLICT。getAssertions 必须要求 objectId、property/valueRole、configuration/basis/time 的适用筛选；对不满足必需上下文的关键属性请求，返回候选断言与阻断原因。示例：输入 RIS-P001 + RatedFlow + Design + CFG-SSC-001-M6 + BL-03，输出参考候选 505 m³/h，但 Evidence/Authority 未提供时 decisionState 必须为 NO_DEFINITIVE_CLAIM。

### N.3 getBasis 与 resolveProfile

getBasis 应返回 basisCandidates、selectedBasis（可空）、basisMemberships、consistencyStatus、approvalEvidence、blockingReasons。两个互斥 CurrentBasis 同时适用时 selectedBasis 必须为空。resolveProfile 返回已批准的 Domain/Project/Conformance Profile 版本及适用范围；未匹配到有效传播规则时 traverseGraph 不得自行推断跨类型关系传播。

### N.4 traverseGraph 与 getEvidence

traverseGraph 应返回 graphReachabilityPaths、potentialImpactObjects、stopTargets、stopReasons、ruleVersion、unresolvedEdges；potentialImpactObjects 不得包含适用 STOP target。若需要 ConfirmedImpact，必须查询独立的 ReviewDecision/ImpactDecision 记录，而不是把图遍历结果直接转换为批准结论。getEvidence 应按 actorContext 检查文档访问权限，并返回证据标识、版本、批准状态、可访问摘要或受控链接；无权限不等于证据不存在，两种状态须区分。

### N.5 服务级验收矩阵

RT-01 六项服务均具备成功、空结果、歧义、冲突、权限拒绝、外部源不可用测试；RT-02 Embedded Provider 与 HTTP Provider 在相同 Fixture 下返回语义等价结果；RT-03 requestId 在网关、服务、审计全链路一致；RT-04 Basis Conflict 不能产生确定性断言；RT-05 Evidence 不可用不能触发静默旧值回退；RT-06 STOP target 排除；RT-07 受限证据不得越权返回；RT-08 并发 Basis 更新后读到的结果应携带可追溯快照/版本。RT-01—08 为拟议测试，当前 NOT_RUN。

## 专题深化 O：核电 SSC 试点数据包与 Independent Oracle

### O.1 试点数据包目录规范

建议按 manifest、objects、identifiers、representations、projections、assertions、configurations、bases、evidence-index、authorities、relations、changes、review-decisions、test-fixtures、oracle-labels、audit-evidence 分包。manifest 记录数据集版本、脱敏规则、时间范围、数据源、Schema/Profile 版本、对象数、生命周期阶段数、配置分支数、ECR/NCR 覆盖与内容哈希。数据脱敏不得破坏身份歧义、配置冲突和证据权威关系等关键测试结构。

### O.2 试点问题集分层

Q1 身份问题：同一对象跨设计/制造/运行编码如何解析？Q2 属性问题：Required/Design/AnalysisResult/Tested 值能否正确区分？Q3 基线问题：不同配置与时间下哪个 Basis 有效？Q4 变更问题：哪些对象可达、哪些可能受影响、哪些已批准确认？Q5 证据问题：每项结论的来源、版本、审批主体是否可追溯？Q6 失败问题：歧义、冲突、权限拒绝、临时改造和 STOP 规则是否触发受控阻断？每一类至少覆盖正常与反例，并由独立专家给出 Oracle 标签。

### O.3 评价指标的精确定义

IdentityAccuracy = 正确唯一解析的可判定对象引用数 / 独立 Oracle 可判定的对象引用数。EvidenceTraceabilityRate = 具备完整可核查证据链的受检工程结论数 / 受检工程结论总数。PotentialImpactPrecision = 被 Oracle 确认为潜在影响的系统候选数 / 系统潜在影响候选总数；PotentialImpactRecall = 被系统覆盖的 Oracle 潜在影响对象数 / Oracle 潜在影响对象总数。UnsafeDefinitiveClaimRate = 违反安全门控却输出确定性工程结论的次数 / 所有触发安全门控检查的有效测试次数。分母为零时记 N/A，不得宣称通过；关键安全目标为 0。以上指标定义属于本报告提出的试点评估操作化口径，应经专家组批准。

### O.4 三组对照与盲审

A组 Traditional/System-centered：仅利用现有系统记录与人工检索；B组 Naive Graph Reachability：不使用 UEOT 受限断言和 Basis/Authority Gate；C组 UEOT：使用身份、断言、基线、证据和推理门控。三组使用同一问题集、同一截止时间和同一数据权限范围。Oracle 专家先独立形成答案与不确定性标签，避免看到 C 组输出后产生确认偏差。记录人时、查询耗时、错误类别和人工复核次数；不得用合成数据性能代替真实工业性能。

### O.5 阶段验收门槛

G0 资料准入：正式五文档齐套，原始数据授权与脱敏完成；G1 语义准入：Schema/Profile、Identity/Basis/Authority 规则评审通过；G2 参考回归：六项正式 Finding 的用例均有实际执行日志且未遗留高风险 FAIL；G3 Pilot：至少 20–100 UEO、3 生命周期阶段、2 配置、1 ECR、1 NCR/Deviation，三组对照和 Independent Oracle 完成；G4 安全门：UnsafeDefinitiveClaimRate=0 且全部高风险例外均有闭环；G5 生产化决策：另行评估性能、权限、安全、可运维性和生产 SLA。G0—G5 为本报告提出的阶段划分，正式 Release Note 仅明确 Pilot 范围与 Critical Safety Gate。

## 专题深化 P：工程数据中心与业务闭环实施路线

### P.1 第一年最小可交付范围

建设统一 UEO 注册表、身份映射表、语义数据字典、Evidence 索引和最小 Basis Store；优先连接一个设计来源、一个制造/质量来源和一个工程变更来源，形成可核查的 20–100 对象试点数据集。对象浏览器实现 PBS/FBS/GBS 结构切换、对象详情、属性 ValueRole、证据与配置筛选。验收重点是数据正确性和语义阻断，不以大规模 AI 问答作为第一年核心指标。

### P.2 第二年最小可交付范围

形成六项 Runtime 服务的持久化实现与 API 契约测试，接入 ECR、NCR/Deviation 和配置管理工作流；上线 PotentialImpact 候选分析、STOP Rule 和 BasisConsistency Gate。建立数据质量问题工单、冲突审查、证据缺失补录及审批记录。新增专业或项目时先发布 Profile 并运行 Conformance，再扩大数据接入。

### P.3 第三年最小可交付范围

在真实 Pilot 达到安全与质量目标后，按专业/项目复制实施；逐步构建跨项目语义数据中心、工程知识图谱和可解释 Engineering Query。强化审计、灾备、权限治理、配置迁移和运维 SLA。所有 AI 辅助能力须保持“候选查询/解释草案—确定性 Runtime 门控—人工授权决策”的分工。

### P.4 本轮状态与必须补齐的材料

本轮交付的是 IP-01 工程实施规范草案、接口验收设计、试点数据包目录和三年分阶段交付建议；未创建或运行参考实现代码，未执行 RT-01—08，也未获得正式五文档主文。正式落地的下一输入为：五份 UEOT V1.0 基线文件、参考实现仓库地址或源码包、可脱敏 SSC/阀门对象数据样本。取得后优先进行 Schema/API 差异检测与六项 Finding 回归，避免继续无证据地扩大理论文本。

## 专题深化 Q：独立参考测试数据与可复现验证协议 V0.1

### Q.1 本专题的证据边界

本专题给出可供研发团队落地的独立测试 Fixture 与预期结果，属于作者构造的合成验证协议，不是对现有 UEOT Browser 代码的实测，也不构成正式基线测试日志。正式基线 Release Note 已确认六项 Finding 和 107+45 的证据口径；以下 CaseId 使用新命名空间 IP01-TEST，避免与原始测试编号混淆。

### Q.2 最小对象与配置 Fixture

FixtureSet IP01-FIX-001：对象 UEO-PUMP-001（安全注入泵A）、UEO-VALVE-001（出口隔离阀）、UEO-MOTOR-001（驱动电机）、UEO-SYS-001（安全注入系统）、UEO-STOP-001（受停止规则排除的边界对象）。编码：RIS-P001→UEO-PUMP-001；SN-260089→UEO-PUMP-001；ASSET-A10001→UEO-PUMP-001。配置 CFG-M6 和 CFG-M7；正式基线 BL-03、冲突候选 BL-04；临时基线 TM-01。所有标识仅为测试用假数据。

Fixture Assertion A-DES-001：subject=UEO-PUMP-001，property=RatedFlow，value=505，unit=m³/h，valueRole=Design，configuration=CFG-M6，basis=BL-03，validTime=[2026-01-01,2027-01-01)，evidence=EV-DES-001，authority=AU-DES-001。A-REQ-001：value≥500，role=Required；A-ANA-001：value=508，role=AnalysisResult；A-TST-001：value=512，role=Tested。后三项须有独立 Evidence/Authority 引用，不能复用设计值的权威结论。

Fixture Basis：BL-03 类型 CurrentBasis，scope=UEO-PUMP-001/CFG-M6，approved=true，effective=[2026-01-01,2027-01-01)；BL-04 在基础成功用例中不激活，在冲突用例中设置为同 scope、同时间有效且与 BL-03 不一致。TM-01 类型 TemporaryApplicableBasis，scope=UEO-VALVE-001，effective=[2026-06-01,2026-07-01)，不得覆盖 DesignBasis。

### Q.3 六项 Finding 的机器可判定断言

IP01-TEST-STOP：输入 root=UEO-PUMP-001，关系路径 Pump→Valve→STOP-Object；预期 STOP-Object ∉ PotentialImpactSet，stopReason 非空。IP01-TEST-TIME：同一标识在 [t0,t1) 与 [t1,t2) 对应不同 UEO；边界 t1 只能匹配第二个区间；重叠冲突时返回 AMBIGUOUS。IP01-TEST-BASIS：BL-03/BL-04 同时适用且互斥；selectedBasis=null，decisionState=NO_DEFINITIVE_CLAIM。

IP01-TEST-AUTH：两个 Authority 对同一 Role、Configuration、ValidTime 的断言相互冲突且 Profile 无优先级；decisionState=GOVERNANCE_ESCALATION。IP01-TEST-CONFIG：CFG-M6 与 CFG-M7 的 Design 值不同且查询未指定配置；decisionState=NO_DEFINITIVE_CLAIM，候选配置必须完整列出。IP01-TEST-TEMP：TM-01 生效期间仅影响其 scope，DesignBasis 不变；过期后不再适用，历史记录仍可追溯。

### Q.4 附加安全回归

IP01-TEST-UNKNOWN：查询不存在的设备编码，返回 NOT_FOUND，绝不退回 UEO-PUMP-001。IP01-TEST-EVIDENCE：移除 EV-DES-001，不能输出“已批准的设计流量 505 m³/h”这一确定性结论。IP01-TEST-ACCESS：用户无权查看 EV-DES-001 时，返回 ACCESS_DENIED 或受控摘要，不能泄露原文。IP01-TEST-SUPERSESSION：新设计断言取代旧断言，旧断言仍可按历史时间和版本查询。IP01-TEST-PROVIDER：Embedded/HTTP Provider 在同一数据快照和 Profile 下返回语义等价状态。

### Q.5 测试执行协议

测试执行前固定数据包哈希、Schema 版本、Profile 版本、Runtime commit、运行命令、执行环境、时区与权限角色。每条用例按 Arrange（加载独立 Fixture）→Act（调用 API）→Assert（校验状态、集合、证据与审计）→Archive（保存请求/响应、日志、哈希）执行。对同一用例重复执行应得到一致的语义结果；对依赖时间的用例注入固定 validAt，不使用运行机器的当前时间。

### Q.6 机器断言示例（伪代码）

assert(resolveObject('UNKNOWN').status == 'NOT_FOUND'); assert(getBasis('UEO-PUMP-001', conflictContext).selectedBasis == null); assert(traverseGraph('UEO-PUMP-001', stopProfile).potentialImpactObjects excludes 'UEO-STOP-001'); assert(getAssertions('UEO-PUMP-001', noConfigContext).decisionState == 'NO_DEFINITIVE_CLAIM'); assert(getAssertions('UEO-PUMP-001', missingEvidenceContext).definitiveClaim == false)。伪代码表达预期语义，不代表现有 API 字段已确认。

## 专题深化 R：工程审查工作台与验收责任矩阵

### R.1 审查工作台的信息架构

建议左侧采用可折叠 PBS/FBS/GBS/WBS 结构导航，中央展示 UEO 身份、属性断言与配置差异，右侧固定显示 Basis、Authority、Evidence 和 Gate 状态。下方增加 Change Impact 三栏：GraphReachability、PotentialImpact、ConfirmedImpact。每个对象节点展开后必须能看到对应的部件明细、编码、来源、版本、有效时间、配置和审批状态；不得仅显示结构树而丢失部件属性详情。

### R.2 人工审查流程

REVIEW-01 系统发现冲突或潜在影响并创建 ReviewCase；REVIEW-02 专业工程师核对身份、配置、证据和关系；REVIEW-03 专业责任人确认影响范围及不确定项；REVIEW-04 授权批准人形成 DecisionRecord；REVIEW-05 变更基线后触发重新评审；REVIEW-06 审计管理员核对证据链与权限。人工审批不得由 LLM 自动替代；系统可生成解释草案但不得伪造签署。

### R.3 RACI 建议

对象身份与编码映射：工程数据治理负责人 Accountable、专业工程师 Responsible、源系统管理员 Consulted。Qualified Assertion 与 Basis：专业负责人 Accountable、设计/配置工程师 Responsible、质量与安全人员 Consulted。关系传播与影响分析：专业负责人 Accountable、工程变更团队 Responsible、系统工程师 Consulted。证据权限：信息安全/数据责任部门 Accountable、平台运维 Responsible。Independent Oracle：独立专家组 Accountable、试点测试组 Responsible。上述 RACI 是建议组织安排，须结合项目实际授权矩阵调整。

### R.4 最终交付清单与缺口封闭条件

交付包应包含：Formal Baseline 文件索引与哈希、12 条公理原文对照表、Frozen Schema 差异报告、IP01-FIX-001 合成测试数据、六项 Finding 回归日志、API 合同测试报告、数据授权与脱敏记录、Independent Oracle 标签、三组对照统计、ReviewDecision 审计链和专家签署。缺少任何关键原始证据时应保持 NOT_VERIFIED 或 NOT_RUN；不得将“测试规范已编写”表述为“系统通过验收”。

### R.5 本轮审查状态

本轮已完成合成 Fixture 设计、机器可判定断言、执行协议、工作台信息架构与 RACI 建议；没有取得完整 UEOT 正式主文、目标源码、实际运行环境或真实核电 SSC 数据，因此没有执行软件测试或形成新的 PASS 结论。下一步应由开发团队提供代码仓库/源码包及五份正式基线文件，才能启动可复现的工程验收。

## 专题深化 S：参考实现最小可运行切片的设计规范

### S.1 交付目标与边界

定义 UEOT Runtime 的第一条可验收纵向切片：从 RIS-P001 解析 SSC-001，在指定 CFG-M6、BL-03、ValidTime 下筛选 Design RatedFlow，核验 Evidence 与 Authority，输出受控 Engineering Answer Package，并形成审计记录。此处是目标实现设计，不是已运行代码；正式基线中的字段、服务命名和接口行为仍须以原始 Schema/API Contract 为准。

### S.2 最小部署组件

建议初期采用单体模块化部署：一个只读 HTTP API、一个关系数据库、一个证据索引、一个静态 Browser、一个测试执行器。逻辑模块分为 IdentityResolver、AssertionSelector、BasisResolver、EvidenceVerifier、AuthorityGate、TypedGraphEngine、AnswerComposer、AuditWriter。第一阶段不引入分布式消息队列、微服务或自主 Agent，以降低核电工程数据试点的部署和验收复杂度。

### S.3 数据库不变量

DB-01：UEO.objectId 不可复用；DB-02：IdentifierAssignment 的有效时间采用 [start,end) 且 start<end；DB-03：Assertion 的 subject、Property、ValueRole、Configuration、Evidence 和 Authority 必须保留显式引用；DB-04：BasisMembership 引用必须可追溯；DB-05：Supersession 不得物理删除被取代断言；DB-06：ConfirmedImpact 必须引用经授权的 DecisionRecord；DB-07：审计记录应关联 requestId 与规则版本。跨记录的身份冲突和 BasisConsistency 不宜仅依赖数据库唯一键，须由领域服务检查并在并发更新时执行事务隔离。

### S.4 第一条端到端业务链的契约

输入：{question:'RIS-P001 在 BL-03、CFG-M6 下的 Design RatedFlow？',validAt:'2026-06-15',purpose:'design-review'}。处理：IdentityResolver→BasisResolver→AssertionSelector→EvidenceVerifier→AuthorityGate→AnswerComposer→AuditWriter。预期成功样例仅在合成 Fixture 中证据与权威均被设定为有效时成立；输出应携带 objectId=SSC-001、property=RatedFlow、valueRole=Design、value=505、unit=m³/h、basis=BL-03、configuration=CFG-M6、evidenceRefs、authorityRef、decisionState 和 auditRef。移除证据后，同一查询必须转为 NO_DEFINITIVE_CLAIM。

### S.5 事务与一致性策略

对同一请求，在读取 Identity、Basis、Assertion 和 Evidence 时应使用同一逻辑数据快照或携带明确版本水位；禁止前半段使用 BL-03、后半段读取已经切换至 BL-04 的断言而未提示。Basis 激活/撤销与成员关系修改应在事务内提交并触发相关答案缓存失效。对于无法保证跨源强一致的适配器，应显示 sourceAsOf、syncLag 与决策状态，不得将最终一致性包装成实时工程事实。

### S.6 首轮迭代完成定义（DoD）

完成条件：六项服务中至少 resolveObject、getBasis、getAssertions、getEvidence、resolveProfile 和 traverseGraph 具有明确接口或受控占位；完整纵向切片能返回证据链；未知编码无默认对象；缺配置、冲突 Basis、缺 Evidence、Authority 冲突均受控阻断；审计可回放；固定 Fixture 的自动化测试可重复执行；Browser 能展示对象、属性、基线、证据与阻断原因。DoD 为建议工程门槛，不代表正式基线验收已通过。

## 专题深化 T：失败语义与验收报告格式

### T.1 失败分类及处理

IDENTITY_AMBIGUOUS：保留候选，不做唯一绑定；CONFIGURATION_AMBIGUOUS：请求补充配置或保留多候选；BASIS_CONFLICT：禁止确定性值；EVIDENCE_MISSING：可显示未经确认候选但不得生成已批准结论；AUTHORITY_CONFLICT：转治理审查；PROFILE_UNAVAILABLE：禁止未经授权的图推理；ACCESS_DENIED：隐藏受限证据内容并保留受控审计；SOURCE_STALE：提示来源时点并按风险策略阻断；STOP_RULE_APPLIED：记录被截断路径。错误码为建议性接口分类，具体编码待正式 API Contract 审查。

### T.2 测试报告统一模板

报告首页：项目、数据包版本、Runtime commit、Profile 版本、执行日期、执行环境、测试负责人、审查人、批准人。测试摘要：Planned、Executed、PASS、FAIL、INDETERMINATE、NOT_RUN 分别计数，严禁把 NOT_RUN 归入 PASS。逐例记录：CaseId、关联 Finding、输入 Fixture、预期结果、实际结果、日志链接、截图或响应摘要、缺陷编号、复测版本。报告末页：开放问题、风险接受理由、剩余限制与签署结论。

### T.3 证据充分性判据

一个 PASS 至少同时具备固定版本输入、实际运行输出、可复核断言、执行日志和测试人员；缺少运行日志的“截图通过”应列为 INDETERMINATE。一个 FAIL 应包含最小复现步骤和违反的预期语义。尚未执行的测试必须标为 NOT_RUN。对安全关键用例，不允许以总体通过率抵消单项严重失败。

### T.4 六项 Finding 的发布阻断规则

若 F-R2-001 的 STOP target 被纳入 PotentialImpactSet，或 F-R3-001/002/003/004/005 中任一产生违反语义门控的确定性工程结论，试点应维持 NO-GO，直到缺陷修复、回归通过并经授权审查。若正式 Profile 或源数据不足导致无法判定，应标为 INDETERMINATE 并暂停对应功能发布，不得假设通过。

### T.5 数据与权限责任分界

数据源负责人对原始记录及发布状态负责；工程专业负责人对 ValueRole、配置、基线适用性与影响判断负责；平台团队对语义服务契约、审计与权限实施负责；独立测试组对 Oracle、执行证据与结果报告负责；审批主体对工程确认决定负责。LLM 不得作为批准主体，也不得用生成解释替代原始工程证据。

## 专题深化 U：项目下一轮输入与工作包拆解

### U.1 最小输入清单

输入 A：五份正式 UEOT V1.0 文档或可核验的受控副本。输入 B：UEOT Browser/Runtime 仓库地址、固定 commit 或源码包，以及运行说明和依赖锁文件。输入 C：至少一份脱敏的 SSC/阀门对象属性表及编码/配置/证据关联样本。输入 D：项目授权矩阵与允许使用的测试环境。若只提供 A+B，可先开展静态契约审查与合成回归；提供 C 后才能开展真实业务语义验证。

### U.2 工程工作包及退出标准

WP-01 Baseline Audit：输出 12 公理原文映射与 Frozen Schema 清单；退出标准为逐条来源页码和审查签字。WP-02 Runtime Inventory：输出模块/服务/API/数据表差异矩阵；退出标准为每项差异有证据与责任人。WP-03 Synthetic Regression：执行六项 Finding 与附加安全用例；退出标准为日志齐全且关键失败关闭。WP-04 SSC Pilot：完成 20–100 UEO、三阶段、两配置、一 ECR、一 NCR/Deviation 的 Independent Oracle；退出标准为 UnsafeDefinitiveClaimRate=0 与专家审查。WP-05 Review Release：输出评审报告与受控发布决定。

### U.3 当前结论

本次新增的是最小纵向切片设计、数据库不变量、失败语义、测试证据标准与工程工作包。现有资料足以指导实现准备，但尚不足以判断参考代码是否符合冻结契约。下一阶段最有价值的行动是获取源码与正式文档，进行真实差异审查，而不是继续扩写未经验证的规范性条文。
