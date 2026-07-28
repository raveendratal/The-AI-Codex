# 🤖 LLM Model Catalog (2026)

**Unified catalog of the major Large Language Models (LLMs) across leading AI providers.**
This catalog summarizes each provider's flagship model family, typical strengths, relative intelligence, latency, cost, context capabilities, and ideal workloads. The frontier model landscape changes rapidly, so treat this as a current snapshot rather than a permanent ranking. ([AI Summit Barcelona][1])

| Model Family               | Provider        | 🧠 Intelligence | ⚡ Speed   | 💰 Cost   | 📚 Context Window* | 🌐 Multimodal | 🔧 Tool Use | 🏢 Best Use Cases                        |                |
| -------------------------- | --------------- | --------------- | --------- | --------- | ------------------ | ------------- | ----------- | ---------------------------------------- | -------------- |
| GPT-5.5                    | OpenAI          | ⭐⭐⭐⭐⭐           | Fast      | $$$       | Large              | ✅             | ⭐⭐⭐⭐⭐       | Enterprise AI, Coding, Agents, Reasoning |                |
| Claude Opus 4.x / Sonnet 5 | Anthropic       | ⭐⭐⭐⭐⭐           | Medium    | $$$       | Very Large         | ✅             | ⭐⭐⭐⭐⭐       | Long reasoning, Coding, Research         |                |
| Gemini 3.x Pro             | Google DeepMind | ⭐⭐⭐⭐⭐           | Fast      | $$        | Up to ~1M+         | ✅             | ⭐⭐⭐⭐        | Multimodal, Search, Research, Enterprise |                |
| Grok 4.x                   | xAI             | ⭐⭐⭐⭐            | Fast      | $$        | Large              | ✅             | ⭐⭐⭐⭐        | Real-time reasoning, Coding              |                |
| Llama 4                    | Meta            | ⭐⭐⭐⭐            | Fast      | Free/Open | Large              | ✅             | ⭐⭐⭐         | Self-hosted AI, Fine-tuning              |                |
| DeepSeek V4                | DeepSeek        | ⭐⭐⭐⭐            | Fast      | $         | Large              | Limited       | ⭐⭐⭐⭐        | Low-cost inference, Coding               |                |
| Qwen 3.x                   | Alibaba         | ⭐⭐⭐⭐            | Fast      | $         | Very Large         | ✅             | ⭐⭐⭐⭐        | Enterprise AI, Multilingual              |                |
| Mistral Large 3.x          | Mistral AI      | ⭐⭐⭐⭐            | Very Fast | $$        | Large              | ✅             | ⭐⭐⭐⭐        | European enterprise AI, RAG              |                |
| Command A / R+             | Cohere          | ⭐⭐⭐⭐            | Fast      | $$        | Large              | Limited       | ⭐⭐⭐⭐        | Enterprise Search, RAG                   |                |
| Amazon Nova                | AWS             | ⭐⭐⭐             | Very Fast | $$        | Large              | ✅             | ⭐⭐⭐         | AWS-native applications                  |                |
| DBRX                       | Databricks      | ⭐⭐⭐⭐            | Fast      | $$        | Large              | Text          | ⭐⭐⭐⭐        | Lakehouse AI, Enterprise Agents          |                |
| Phi-4                      | Microsoft       | ⭐⭐⭐             | Very Fast | $         | Medium             | Limited       | ⭐⭐⭐         | Lightweight copilots, Edge AI            |                |
| Nemotron                   | NVIDIA          | ⭐⭐⭐⭐            | Fast      | $$        | Large              | Limited       | ⭐⭐⭐⭐        | AI infrastructure, Inference             |                |
| GLM 5.x                    | Zhipu AI        | ⭐⭐⭐⭐            | Fast      | $         | Large              | ✅             | ⭐⭐⭐         | Chinese enterprise AI                    |                |
| Kimi K3                    | Moonshot AI     | ⭐⭐⭐⭐            | Fast      | $         | Very Large         | ✅             | ⭐⭐⭐⭐        | Long-context reasoning, Coding           | ([AP News][2]) |

> *Context window values vary by model variant and release.

---

# 📊 Provider Comparison

| Provider   | Flagship Models     | Strength                                         | Weakness                          | Best For                        |                            |
| ---------- | ------------------- | ------------------------------------------------ | --------------------------------- | ------------------------------- | -------------------------- |
| OpenAI     | GPT-5.5             | Balanced intelligence, coding, agents, ecosystem | Premium pricing                   | Enterprise AI                   |                            |
| Anthropic  | Claude Opus, Sonnet | Long reasoning, code quality, safety             | Higher latency on complex tasks   | Research & software engineering |                            |
| Google     | Gemini Pro          | Huge context, multimodal, Workspace integration  | API behavior varies by tier       | Research, documents             |                            |
| Meta       | Llama               | Open-weight ecosystem                            | Self-hosting expertise required   | Private deployments             |                            |
| DeepSeek   | V4                  | Excellent price/performance                      | Smaller ecosystem                 | Budget production workloads     |                            |
| Alibaba    | Qwen                | Strong multilingual support                      | Regional adoption differences     | Enterprise multilingual AI      |                            |
| xAI        | Grok                | Current-event reasoning                          | Smaller enterprise ecosystem      | Assistants                      |                            |
| Mistral    | Large               | European compliance, fast inference              | Smaller model ecosystem           | Enterprise AI                   |                            |
| Cohere     | Command             | Enterprise RAG                                   | Narrower general ecosystem        | Knowledge assistants            |                            |
| Databricks | DBRX                | Lakehouse-native AI                              | Smaller general-purpose ecosystem | Data & AI platforms             | ([AI Summit Barcelona][1]) |

---

# 🎯 Best Models by Category

| Category                | Recommended Models                    |
| ----------------------- | ------------------------------------- |
| 🧠 General Intelligence | GPT-5.5, Claude Opus, Gemini Pro      |
| 💻 Coding               | Claude Sonnet, GPT-5.5, DeepSeek V4   |
| 📖 Long Context         | Gemini, Claude, Kimi K3               |
| 🖼️ Vision & Multimodal | GPT-5.5, Gemini, Grok                 |
| 🤖 AI Agents            | GPT-5.5, Claude, DBRX, Gemini         |
| 📚 RAG                  | Cohere Command, GPT-5.5, Qwen, DBRX   |
| 💲 Lowest Cost          | DeepSeek, Qwen, Llama                 |
| 🔓 Open Models          | Llama, Qwen, DeepSeek, Mistral        |
| 🏢 Enterprise AI        | OpenAI, Anthropic, Google, Databricks |
| 🌍 Multilingual         | Gemini, Qwen, Claude, GPT-5.5         |

---

# 🏗️ Open vs Closed Models

| Open Models        | Closed Models |
| ------------------ | ------------- |
| Llama              | GPT           |
| DeepSeek           | Claude        |
| Qwen               | Gemini        |
| Mistral            | Grok          |
| DBRX (open-weight) | Command       |
| GLM                | Nova          |

---

# ☁️ Cloud Availability

| Cloud Platform       | Available Models                                               |                           |
| -------------------- | -------------------------------------------------------------- | ------------------------- |
| Azure AI Foundry     | OpenAI, Llama, Qwen, DeepSeek, Mistral                         |                           |
| AWS Bedrock          | Claude, Llama, Mistral, Nova, Cohere                           |                           |
| Google Vertex AI     | Gemini, Llama, Qwen, Mistral, Claude                           |                           |
| Databricks Mosaic AI | DBRX, Llama, Mistral, Claude, GPT (via integrations), DeepSeek |                           |
| NVIDIA NIM           | Llama, DeepSeek, Mistral, Nemotron                             |                           |
| Ollama               | Llama, DeepSeek, Mistral, Qwen, Phi                            | ([Model Availability][3]) |

---

# 🚀 Which Model Should You Choose?

| Requirement                          | Recommended Choice      |
| ------------------------------------ | ----------------------- |
| Best Overall                         | GPT-5.5                 |
| Best Reasoning                       | Claude Opus             |
| Best Coding                          | Claude Sonnet / GPT-5.5 |
| Best Research                        | Gemini Pro              |
| Best AI Agents                       | GPT-5.5 + Claude        |
| Best Enterprise RAG                  | Cohere + Databricks     |
| Best Self-Hosted                     | Llama + Qwen + DeepSeek |
| Best Budget Option                   | DeepSeek                |
| Best Long Documents                  | Gemini                  |
| Best Data Engineering & Lakehouse AI | DBRX                    |

---

# 📈 2026 AI Ecosystem Snapshot

| Category                | Leading Providers                           |
| ----------------------- | ------------------------------------------- |
| Frontier Closed Models  | OpenAI, Anthropic, Google                   |
| Open-Weight Models      | Meta, DeepSeek, Qwen, Mistral               |
| Enterprise AI Platforms | Databricks, Microsoft, Google Cloud, AWS    |
| AI Infrastructure       | NVIDIA, AMD, Cerebras                       |
| AI Agent Frameworks     | LangGraph, CrewAI, AutoGen, Semantic Kernel |
| Enterprise Search & RAG | Cohere, Databricks, OpenAI, Google          |

 
🔗 [See OpenAI Models](../providers/openai.md)  
