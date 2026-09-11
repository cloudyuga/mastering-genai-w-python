# 🛡️ Risks, Ethics & Guardrails

Where GenAI actually breaks — hallucinations, prompt injection, information
leaks, bias — and the guardrail patterns (content, process, and operational)
that keep a deployment safe, plus where 2026 AI regulation stands.

---

## 📊 Slides

Maintained as a Canva design ("Module 6: Risks, Ethics & Guardrails").
Covers hallucinations and prompt injection with real 2026 case studies
(legal sanctions, the EchoLeak zero-click exploit), bias/fairness/
transparency, the guardrail tools landscape (NeMo, LangChain guardrails,
OpenAI Moderation), human-in-the-loop, the EU AI Act / US regulatory
landscape, and a practical governance checklist for managers.

## 🧪 Labs & Demos

### `Guardrailing/`
| Item | Description |
|------|-------------|
| `Lab-1-Guardrails_AI_Demo.ipynb` | Pull validators from guardrails hub and filter a message/question against them. |
| `NemoGuardrails/` | A live NeMo Guardrails app — as a standalone Colab notebook (`NemoGuardrails_Demo.ipynb`) or as `app.py` with `.co`/`.yaml` rule configuration files. |
| `Human-in-the-Loop/` | A live Flask app demonstrating a human approving/rejecting an AI decision mid-workflow. |

See `Guardrailing/Readme.md` for details.

### `Securing-LLM-Applications/`
| Item | Description |
|------|-------------|
| `Information-Leak/` | Paired before/after demo — `info_leak.py` reproduces a data leak, `prevent_info_leak.py` shows the fix. |
| `Prompt-Injection/` | A live prompt-injection demo showing an attacker overriding system instructions — as a standalone Colab notebook (`Prompt_Injection_Demo.ipynb`) or as `app.py`. |

See `Securing-LLM-Applications/Readme.md` for details.

---
