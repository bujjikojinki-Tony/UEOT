# UEOT — Unified Engineering Object Theory

统一工程对象理论（UEOT）研究与工程实施资料库。

## 当前资料

- [研究与工程实施报告 V1.0（Markdown）](docs/UEOT_Research_and_Implementation_Report_V1.0.md)
- [来源、证据与验证状态](docs/VERIFICATION_STATUS.md)
- [工程实施与回归测试路线](docs/IMPLEMENTATION_ROADMAP.md)

在线编辑原稿：[Google Docs](https://docs.google.com/document/d/1vXBuVtlJ4JkzYu2ka2skkzkfwuBmtOQjp2krUO1yRow/edit)

## 当前成熟度

本仓库初始提交为**研究报告及实施/测试设计**，不包含 UEOT Runtime/Browser 源码，不代表任何软件测试已经执行或通过，也不代表已完成真实核电工程数据 Pilot、生产级验证或监管认证。

UEOT V1.0 Formal Baseline Release Note 确认冻结理论核心、语义契约及参考验证边界。正式主文、12 条公理全文、原始测试执行记录和 Runtime 源码仍待逐项核验。

## 目录规划

```text
docs/        研究报告、原始资料索引、核验状态
specs/       元模型、Profile 与 API 契约（待验证后纳入）
fixtures/    合成测试数据（待实现）
tests/       Finding 回归与 API 合同测试（待实现）
runtime/     Runtime 源码（尚未取得）
browser/     Object Browser 源码（尚未取得）
```

> **注意：** 本仓库目前为公开仓库。请勿提交真实核电敏感工程数据、密钥、未授权图纸或受限文件。
