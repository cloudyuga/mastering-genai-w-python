# 🛡️ Content Safety with guardrails.ai, NeMo Guardrails & Human-in-the-Loop

This module focuses on building **safe, controllable, and human-in-the-loop AI applications**. You will learn how to apply **NeMo Guardrails** for managing LLM behavior and integrate human oversight into decision-making processes. We upload validators from https://hub.guardrailsai.com and filter our message or question using these validators.

---

## 🧪 Included Labs & Apps

| Lab | Notebook/File                          | Focus Area            | Description                                                                 |
|-----|----------------------------------------|------------------------|-----------------------------------------------------------------------------|
| 1   | `Lab-1-Guardrails_AI_Demo.ipynb`       | 🛡️  Guardrails.ai validators     | Demonstrates how to upload validators from https://hub.guardrailsai.com and filter the message or question using these validators and enforce safety. |
| –   | `NemoGuardrails/`                      | ⚙️ Config + Rules       | `NemoGuardrails_Demo.ipynb` builds the same rails config inline and runs standalone in Colab; `app.py` + `config/*.co`/`*.yml` is the original script + separate-files version. |
| –   | `Human-in-the-Loop/`                   | Flask App + 👤 Manual Oversight      | A live app example (in `app.py`) showing how humans can intervene in AI workflows to approve the decisions. |

---

## 🔐 Key Concepts Covered

- **Safe AI Output:** Block or filter harmful or off-topic content before it reaches the user.
- **Rule-Based Moderation:** Use `.co` and YAML rules to govern model behavior.
- **Human Feedback:** Insert manual decision points into workflows.
- **LangChain & NeMo Integration:** Combine tools to build reliable LLM applications.

---
