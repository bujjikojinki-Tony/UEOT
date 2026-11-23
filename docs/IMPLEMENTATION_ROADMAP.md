# UEOT 工程实施与验证工作包

| 工作包 | 任务 | 退出条件 |
|---|---|---|
| WP-01 | 正式基线核验 | 五份主文齐套，12 条公理原文及冻结 Schema 有逐条来源映射 |
| WP-02 | Runtime/Browser 源码盘点 | 固定 commit、依赖、服务与 API 差异清单 |
| WP-03 | 合成数据回归 | 六项 Finding 与附加安全用例实际执行，有日志与判定 |
| WP-04 | SSC Independent Oracle Pilot | 真实或脱敏数据、三组对照、关键安全门达到要求 |
| WP-05 | 评审与受控发布 | 专业责任人签署，遗留风险与限制显式记录 |

## 建议仓库结构

- `specs/`：规范、Schema、Profile、API Contract。
- `fixtures/`：可复现的合成 SSC 对象、Basis、Assertion、Evidence 数据。
- `tests/`：身份、配置、基线、证据、Authority、STOP 和 Provider 等价性回归。
- `runtime/`：六项 Runtime 服务实现。
- `browser/`：对象中心的 PBS/FBS/GBS/WBS 导航与可解释审查界面。

上述目录仅为规划；**尚未提交实际源码或测试脚本**。

## 下一步

取得正式 UEOT V1.0 五份文档与 Runtime/Browser 源码后，先做冻结语义契约差异审查，再实现测试 Fixture 并执行回归。严禁将“测试用例设计完成”写成“测试通过”。
