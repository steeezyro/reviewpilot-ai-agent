# 🤖 ReviewPilot: A Product Page Agent

**ReviewPilot** is a Gen Z-style intelligent **LLM-powered agent** that:

- Scrapes and analyzes e-commerce product pages
- Summarizes listings in a vibrant, persuasive voice
- Diagnoses UX/content flaws like a product designer
- Generates realistic fake customer reviews in varied sentiments

Built to behave like a **lightweight product marketing agent** with scraping + reasoning + writing skills. Originally tested on [Books to Scrape](https://books.toscrape.com).

---

## 🚀 Features

- ✅ Gen Z-style product summaries
- ✅ Smart UX critique of content quality and layout
- ✅ Fake customer reviews (positive, neutral, skeptical)
- ✅ Automatic file-saving to `outputs/` for logs and summaries
- ✅ API key security via `.env` and `python-dotenv`
- ✅ Dual-model fallback: if primary LLM fails, the agent switches to a backup

---

## 🛠 Tech Stack

### 🔧 Core Tools

| Tech               | Purpose                                          |
| ------------------ | ------------------------------------------------ |
| **Python 3.12.4**  | Backend language                                 |
| **BeautifulSoup4** | HTML parsing from product pages                  |
| **Requests**       | HTTP requests for web scraping & API interaction |
| **dotenv**         | Secure environment variable loading              |

### 🧠 Language Models (LLMs)

| Model                                         | Role                                                     |
| --------------------------------------------- | -------------------------------------------------------- |
| `nvidia/llama-3.3-nemotron-super-49b-v1:free` | Primary LLM via OpenRouter for text generation           |
| `arliai/qwq-32b-rpr-v1:free`                  | Fallback LLM via OpenRouter                              |
| _(Optional)_ `gpt-4-turbo` via OpenAI         | Future upgrade for high-quality results & production use |

---

### 🔮 Potential Add-ons

| Tool                             | Why Add It?                                                                             |
| -------------------------------- | --------------------------------------------------------------------------------------- |
| **OpenAI API**                   | Upgrade to GPT-4 for higher precision and industry-standard results                     |
| **LangChain**                    | For modularizing LLM workflows, enabling prompt chaining, memory, and tool use          |
| **Flask**                        | To build a lightweight web app UI for non-technical users (shareable as a product demo) |
| **SQLAlchemy + SQLite/Postgres** | To persist review summaries, critiques, and scraped metadata                            |
| **Streamlit**                    | Alternate GUI option for launching a local dashboard with one command                   |

---

## 🔧 Setup

```bash
git clone https://github.com/steeezyro/reviewpilot-ai-agent.git
cd reviewpilot-ai-agent
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
