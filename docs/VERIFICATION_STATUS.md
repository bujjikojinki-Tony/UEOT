# UEOT 资料核验与验证状态

更新日期：2026-11-23。

| 项目 | 状态 | 说明 |
|---|---|---|
| Google Docs 研究与工程实施报告 V1.0 | 已同步 | 本仓库 `docs/UEOT_Research_and_Implementation_Report_V1.0.md` |
| UEOT V1.0 Formal Baseline Release Note | 已查阅原始文件 | 2026-09-03；本仓库尚未上传原件 |
| 五份正式基线主文 | 待取得/核验 | 不能据发布说明反推全部正式规范 |
| 12 条正式公理原文 | 待核验 | 发布说明确认冻结 12 条公理，但未列出全文 |
| Formal baseline tests | 发布说明记载 107 | Round 1 40 + Round 2.1 31 + Round 3 36 |
| Later package-local executions | 发布说明记载 45 | 不等于新增 45 项独立命题 |
| Observed executions | 发布说明记载 152 | 不应声称 152 项去重独立测试 |
| 六项正式 Finding 回归 | 测试设计已写，未执行 | 不存在新的 PASS 结果 |
| UEOT Browser / Runtime 源码 | 尚未上传 | 不能做实际源码/API 差异审查 |
| 真实 EB/核电工程数据 Pilot | 未执行 | 不得声称工业验证 |
| 生产级 SLA / 核安全或监管认证 | 未验证 | 不能将参考实现等同于生产级系统 |

## 六项 Finding（依据 Release Note）

- F-R2-001：STOP target 不得进入 PotentialImpactSet。
- F-R3-001：Temporal Identity Ambiguity；半开 Effectivity 与 AMBIGUOUS。
- F-R3-002：Basis Conflict；BasisConsistency 和冲突门控。
- F-R3-003：Multi-Authority Conflict；GovernanceEscalation，优先级由 Profile 定义。
- F-R3-004：Configuration Branch Ambiguity；未解析配置不得确定性回答。
- F-R3-005：TemporaryApplicableBasis 不等于 DesignBasis。

## Pilot 准入

发布说明提出至少 20–100 个 UEO、三个生命周期阶段、两个 Configuration、一个 ECR 和一个 NCR/Deviation 链，并采用 Traditional/System-centered、Naive Graph Reachability、UEOT 三组对照。Critical Pilot Safety Gate 为 `UnsafeDefinitiveClaimRate = 0`。

## 重要声明

报告中的 API 字段、实施 Profile、状态机、数据字典、测试 Fixture 和错误码均为建议设计，除非在正式主文中核验，不应视为 UEOT Frozen Semantic Contract 的逐字要求。
