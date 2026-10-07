# Meta AI 工程师面试备考笔记（2026 版）

> 要点提炼自 landedjobs/awesome-ai-engineer-interview 的 Meta 公司页（2026 年 10 月版）。
> 原文：https://github.com/landedjobs/awesome-ai-engineer-interview/blob/HEAD/company/meta.md

## 流程

- MLE 线：HR 电面（45 分钟，2 道 LeetCode medium）→ onsite：**5 轮 coding + 1 轮 system design + 1 轮 behavioral**
- Research Scientist 加：2 轮 research deep-dive + 新增的 **"Coding with AI"** 轮
- 全程 4–8 周，committee 决策
- 2026 年最大变化：业内首个主流化的 "Coding with AI" 轮——考察你**会不会用 AI 助手干活**，而不是不用

## 考过的题（候选人报告）

| 轮次 | 题目 |
|---|---|
| Coding（每轮） | 2 道 LeetCode medium 难度 |
| System design | 给 Instagram Reels 设计推荐系统；或设计 Instagram Feed / Messenger |
| ML theory | L1 和 L2 正则的区别；bias/variance、precision-recall |
| Research | 讲自己过去的工作（presentation + 深挖） |
| Coding with AI | 用 AI 助手做 code review / 改代码风格 |
| Behavioral | 讲一次和同事有分歧的经历 |

## 高概率 follow-up（原文标注为推测，非候选人报告）

- AI 轮：AI 生成的 diff，你信哪部分、验哪部分、怎么验？
- Reels 推荐：排序模型的延迟预算花在哪，缓存什么？
- L1/L2 之后：什么时候两个都不用、改用 early stopping？

## 考察实质

- **Coding 量**：5 轮 coding 考的是重复高压下的速度和正确率，不是一道巧题
- **会不会带 AI 干活**：review、验证、纠正 AI 输出——Meta 赌工程师标配技能
- **经典 ML 基本功**：L1/L2、bias/variance、precision-recall 一直在考
- **产品级系统设计**：ranking、caching、十亿用户量级的延迟
- **协作**：behavioral 挖"分歧"和"开放"

## 备考

- LeetCode medium 按电面节奏刷量
- 练 review AI 生成的 diff：信什么、测什么
- 推荐 / Feed 系统设计：retrieval + ranking 模式，延迟和缓存
- ML 理论三件套：L1/L2、bias/variance、precision-recall
- Research：准备一份讲自己工作的 crisp presentation
- Behavioral：准备"快速交付、公开表达分歧"的具体故事（Move Fast, Be Bold, Be Open）

---
出处：landedjobs/awesome-ai-engineer-interview（MIT）
