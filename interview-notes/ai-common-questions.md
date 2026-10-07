# AI 工程师跨公司通用面试题摘要

> 要点提炼自 wonschangge/ai-engineering-interview-questions-company-wise 的通用题部分（2026 年 10 月版），技术名词保留英文。
> 原文：https://github.com/wonschangge/ai-engineering-interview-questions-company-wise
> 注：该 repo 官方自带中文版 README.zh-CN.md，完整中文内容请看官方版。

## 考法说明

这部分是各家公司反复考的通用题，作者建议先刷这部分。每题只列一次，并标注考过它的公司。

## LLM Internals and Architecture

- scaled dot-product attention：1/√d_k 缩放因子的作用
- KV cache：是什么、大规模下的内存影响、推导公式（OpenAI、xAI、Mistral、Amazon、Apple、NVIDIA、Together、Character.AI 都考）
- MQA / GQA：是什么，trade away 什么（Meta、Mistral）
- MLA：是什么，DeepSeek 为什么引入（DeepSeek、Moonshot）
- FlashAttention：不减少 FLOPs，为什么更快（Together）
- BPE：原理及 failure modes（数字、代码、非拉丁文字）
- positional encoding 演进 sinusoidal → learned → RoPE → ALiBi；RoPE + position interpolation / YaRN 如何扩展 context（Meta、Moonshot、Alibaba）
- Chinchilla scaling laws（Anthropic）
- MoE：架构，如何不增加 FLOPs 扩大容量（Mistral、Cohere、DeepSeek、Moonshot、Zhipu、Alibaba）
- pre-training vs SFT vs preference optimisation 的区别（Meta、Scale AI）
- 解码策略对比 greedy / beam search / top-k / top-p / temperature，各自何时失效（DeepMind、Apple、Perplexity）
- lost-in-the-middle 问题及解法（Moonshot）
- LayerNorm 为何放 pre-block，RMSNorm 是什么
- SwiGLU：为何 gated activation 取代 ReLU/GELU（Meta）
- tensor by tensor 走一遍 decoder-only transformer 的 forward pass（Anthropic）

## Inference, Serving and GPU Performance

- prefill vs decode：为何 prefill compute-bound、decode memory-bandwidth-bound
- continuous (in-flight) batching：为何取代 static batching（Anthropic、xAI、Mistral、NVIDIA、Together）
- PagedAttention：解决 KV-cache fragmentation 的什么问题（NVIDIA、Together）
- speculative decoding：为何输出质量不变、何时没用（NVIDIA、Together）
- prefix / prompt caching：何时用、何种情况失效（Moonshot、Character.AI）
- 量化对比 FP16 / BF16 / FP8 / INT8 / INT4 / FP4，每降一档坏什么
- 并行策略对比 tensor / pipeline / data / sequence / expert parallelism，何时组合（DeepMind、Meta、Amazon、NVIDIA）
- 估算 70B 模型 serving 的显存：weights、KV cache、activations、fragmentation（NVIDIA）
- TTFT / TPOT / ITL / throughput：定义与 trade-off（Microsoft、Apple、Perplexity）

## 后续小节（同文件）

RAG and Retrieval、Agents and Tool Use、Fine-Tuning / Post-Training / Alignment、Evaluation and Observability、Safety, Security and Responsible AI、Multimodal, Speech and Voice AI、AI System Design、Coding and Data Structures——结构与上面相同。

---
出处：wonschangge/ai-engineering-interview-questions-company-wise
