# LiteLLM 多 Provider LLM 统一代理配置

> 使用 LiteLLM 作为统一网关，将多个 LLM 提供商（通义千问、Kimi、智谱、DeepSeek）聚合为一个 OpenAI 兼容 API 端点。

## 概述

**LiteLLM** 是一个开源 LLM 代理服务器，支持 100+ LLM 提供商，提供统一的 OpenAI 兼容 API。本文档记录在 Alibaba Cloud Linux 3 上使用 LiteLLM v1.83 搭建多 Provider 代理的完整配置方案。

**核心价值：**
- 统一接口：所有模型通过 `http://localhost:4000/v1` 访问
- 多 Provider 聚合：通义千问、Kimi、智谱 GLM、DeepSeek 一站式调用
- 负载均衡 & 故障转移（后续可扩展）
- 与 Claude Code 等工具无缝集成

## 架构图

```
┌─────────────┐
│  Claude Code │──┐
└─────────────┘  │
                 ▼
┌─────────────────────────────────┐
│   LiteLLM Proxy (localhost:4000) │
│   OpenAI 兼容 API (/v1/chat/...) │
└────────┬───────┬───────┬────────┘
         │       │       │
    ┌────▼──┐ ┌──▼──┐ ┌──▼─────┐
    │DashScope│ │DashScope│ │DeepSeek│
    │qwen3.6+│ │kimi-k2│ │v4-pro  │
    │glm-5   │ │       │ │v4-flash│
    └────────┘ └──────┘ └────────┘
```

## 环境准备

### 系统要求
- Python 3.13+（通过 pyenv 安装）
- pip 24+
- Alibaba Cloud Linux 3 / 兼容发行版

### 安装 LiteLLM

```bash
# 通过 pyenv 安装 Python 3.13（如需要）
pyenv install 3.13.2
pyenv global 3.13.2

# 安装 LiteLLM
pip install litellm

# 验证
litellm --version  # LiteLLM: Current Version = 1.83.14
```

## 配置文件

### 目录结构

```
~/litellm/
├── config.yaml   # 模型列表和代理配置
├── .env          # API Key（不提交 git）
└── start.sh      # 启动脚本
```

### config.yaml — 模型列表

```yaml
model_list:
  # ===== Alibaba DashScope (Anthropic 兼容端点) =====

  # 通义千问 qwen3.6-plus
  - model_name: "qwen3.6-plus"
    litellm_params:
      model: "anthropic/qwen3.6-plus"
      api_key: "os.environ/DASHSCOPE_API_KEY"
      api_base: "https://coding.dashscope.aliyuncs.com/apps/anthropic"

  # Kimi kimi-k2.5
  - model_name: "kimi-k2.5"
    litellm_params:
      model: "anthropic/kimi-k2.5"
      api_key: "os.environ/DASHSCOPE_API_KEY"
      api_base: "https://coding.dashscope.aliyuncs.com/apps/anthropic"

  # 智谱 glm-5
  - model_name: "glm-5"
    litellm_params:
      model: "anthropic/glm-5"
      api_key: "os.environ/DASHSCOPE_API_KEY"
      api_base: "https://coding.dashscope.aliyuncs.com/apps/anthropic"

  # ===== DeepSeek (Anthropic 兼容端点) =====

  # DeepSeek deepseek-v4-pro
  - model_name: "deepseek-v4-pro"
    litellm_params:
      model: "anthropic/deepseek-v4-pro"
      api_key: "os.environ/DEEPSEEK_API_KEY"
      api_base: "https://api.deepseek.com/anthropic"

  # DeepSeek deepseek-v4-flash
  - model_name: "deepseek-v4-flash"
    litellm_params:
      model: "anthropic/deepseek-v4-flash"
      api_key: "os.environ/DEEPSEEK_API_KEY"
      api_base: "https://api.deepseek.com/anthropic"

# LiteLLM 全局设置
litellm_settings:
  drop_params: true      # 丢弃模型不支持的参数
  max_budget: 0          # 0 = 无预算限制
```

**关键配置说明：**

| 字段 | 说明 |
|------|------|
| `model_name` | 对外暴露的模型名称（Claude Code 中使用的名字） |
| `model` | `anthropic/xxx` 前缀表示使用 Anthropic 兼容端点 |
| `api_key` | `os.environ/XXX` 从环境变量读取，不硬编码 |
| `api_base` | 提供商 Anthropic 兼容 API 地址 |
| `drop_params: true` | 自动丢弃模型不支持的参数，避免调用失败 |

### .env — 环境变量

```bash
# 通义千问 DashScope API Key
# 获取地址: https://dashscope.console.aliyun.com/apiKey
DASHSCOPE_API_KEY=sk-xxxxxxxxxxxxxxxx

# DeepSeek API Key
DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxxxx

# LiteLLM 主密钥（管理接口认证）
LITELLM_MASTER_KEY=sk-xxxxxxxxxxxxxxxx
```

⚠️ **安全提示：** `.env` 包含 API Key，不要提交到 Git。建议加入 `.gitignore`。

### start.sh — 启动脚本

```bash
#!/bin/bash
# LiteLLM Gateway 启动脚本
cd ~/litellm

# 加载环境变量并导出
if [ -f .env ]; then
  set -a  # 自动导出所有变量
  source .env
  set +a
fi

echo "========================================="
echo "  LiteLLM Gateway"
echo "========================================="
echo "  地址:    http://localhost:4000"
echo "  配置:    ~/litellm/config.yaml"
echo "========================================="
echo ""

litellm --config config.yaml --port 4000 --detailed_debug
```

**启动参数说明：**
- `--config config.yaml`：指定配置文件
- `--port 4000`：监听端口
- `--detailed_debug`：详细调试日志（生产环境可选）

## 后台运行

LiteLLM 默认在前台运行，关闭终端后服务会停止。以下是几种后台运行方式。

### nohup（最简单）

```bash
nohup bash ~/litellm/start.sh > ~/litellm/litellm.log 2>&1 &
```

| 参数 | 说明 |
|------|------|
| `nohup` | 终端关闭后进程不退出 |
| `> ~/litellm/litellm.log 2>&1` | 标准输出和错误都写入日志 |
| `&` | 放入后台 |

**查看日志：**
```bash
tail -f ~/litellm/litellm.log
```

### tmux（推荐，方便随时查看/重启）

```bash
tmux new -d -s litellm 'bash ~/litellm/start.sh'
```

| 参数 | 说明 |
|------|------|
| `-d` | 后台创建 |
| `-s litellm` | 会话名 |

**管理会话：**
```bash
tmux attach -t litellm    # 进入查看
# Ctrl+B 然后按 D          # 退出（不停止进程）
tmux kill-session -t litellm  # 停止
```

### macOS launchd（开机自启）

如果需要开机自动启动，可以创建 `~/Library/LaunchAgents/com.litellm.plist`，不过日常使用 tmux 或 nohup 就够了。

## 运行与验证

### 启动服务

```bash
chmod +x ~/litellm/start.sh
~/litellm/start.sh
```

启动后服务运行在 `http://localhost:4000`。

### 验证 API

```bash
# 使用 LITELLM_MASTER_KEY 认证
curl http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -d '{
    "model": "qwen3.6-plus",
    "messages": [{"role": "user", "content": "你好，请用一句话介绍自己"}]
  }'
```

### 查看可用模型

访问 `http://localhost:4000/v1/models` 获取所有已配置模型的列表。

## 已知问题与解决

### DeepSeek 认证失败

**现象：** DeepSeek 模型返回认证错误。

**原因：** DeepSeek 的 Anthropic 兼容端点可能不支持某些认证方式，或 API Key 格式不兼容。

**解决方案（待验证）：**
1. 确认 API Key 有效且有余额
2. 尝试使用 DeepSeek 原生端点（去掉 `anthropic/` 前缀）
3. 联系 DeepSeek 确认 Anthropic 兼容端点版本

### 模型参数兼容性

**原因：** 不同提供商支持的参数不同（如 `thinking`、`reasoning_content` 等）。

**解决：** 配置中已启用 `drop_params: true`，LiteLLM 会自动丢弃不支持参数。

## 与 Claude Code 集成

在 Claude Code 中配置 LiteLLM 作为自定义 Provider：

```json
{
  "providers": {
    "litellm-gateway": {
      "baseUrl": "http://localhost:4000/v1",
      "apiKey": "sk-xxxxxxxxxxxxxxxx",
      "models": ["qwen3.6-plus", "kimi-k2.5", "glm-5", "deepseek-v4-pro", "deepseek-v4-flash"]
    }
  }
}
```

## 扩展方向

- **负载均衡：** 为同一模型配置多个 Provider 实例
- **故障转移：** 主 Provider 失败自动切换到备用
- **速率限制：** 配置每个模型的 RPM/TPM 限制
- **成本追踪：** 启用 LiteLLM 的 cost tracking 功能
- **Docker 部署：** 容器化运行，便于管理

## 参考资源

- [LiteLLM 官方文档](https://docs.litellm.ai)
- [DashScope Anthropic 兼容端点文档](https://help.aliyun.com/zh/model-studio/anthropic)
- [DeepSeek API 文档](https://platform.deepseek.com/api-docs)

---

*配置时间：2026-05-01 | LiteLLM 版本：1.83.14 | Python 版本：3.13.2*
