# AI Document Assistant

A Streamlit chatbot that lets you upload any PDF or text file and ask questions about it using Llama 3 via the Groq API. Built for the MC - SDIR AI Integration Mini-Lab using Agile (Scrum) methodology.

---

## How to Run

### 1. Install dependencies
```bash
pip install streamlit groq pypdf python-dotenv
```

### 2. Set your API key
Create a `.env` file in the project folder:
```
GROQ_API_KEY=your_key_here
```
Get a free key at [console.groq.com](https://console.groq.com) → API Keys → Create API Key

### 3. Run the app
```bash
streamlit run aibot.py
```

The app opens at `http://localhost:8501`. Upload a PDF or `.txt` file from the sidebar, then start asking questions.

---

## Model Information

| Field        | Detail                                           |
|--------------|--------------------------------------------------|
| **Model**    | `llama-3.3-70b-versatile` (Meta Llama 3.3)       |
| **Provider** | Groq API                                         |
| **Source**   | [console.groq.com](https://console.groq.com)     |
| **License**  | Meta Llama 3 Community License (open-source)     |

### Rationale for Model Selection
`llama-3.3-70b-versatile` was selected for three reasons:
1. **Open-source foundation** — Llama 3.3 is developed by Meta and released under an open-source license, making it transparent, auditable, and free to use — directly relevant to SLO 4 on open-source software development.
2. **Strong instruction-following** — The 70B parameter model reliably stays within the system-prompt-defined scope ("answer ONLY from the uploaded document"), reducing hallucination compared to smaller models.
3. **Free and fast via Groq** — Groq's inference hardware (LPUs) serves Llama 3.3 with no rate limits and no credit card required, making it ideal for student projects.

---

## ⚖Ethical AI Reflection on Responsible Use

AI language models like Llama 3.3 carry real risks that developers must actively address. The most immediate concern in a document Q&A system is **hallucination** — the model may generate confident-sounding answers that are not actually present in the uploaded file. To mitigate this, the system prompt explicitly instructs the model to say "I don't know" if the answer isn't in the document, rather than guessing. A second concern is **data privacy**: when a user uploads a document, its contents are transmitted to Groq's API servers for processing. Users should be informed not to upload sensitive personal, medical, or confidential documents without understanding this. Third, **bias in model outputs** means the model may interpret ambiguous document content through the lens of its training data, potentially skewing summaries in subtle ways. Responsible use requires transparency about these limitations and human review of any AI-generated outputs used for important decisions.

---

## Agile Process (Scrum)

| Sprint | Goal                                              | Status  |
|--------|---------------------------------------------------|---------|
| 1      | Define user stories & select model/API            | ✅ Done |
| 2      | Implement file upload and Groq API connection     | ✅ Done |
| 3      | Add Streamlit chat UI and session state           | ✅ Done |
| 4      | Bug fixes, PDF text extraction, polish            | ✅ Done |
| 5      | README, ethical reflection, final submission      | ✅ Done |

**User Stories:**
- *As a student*, I want to upload a PDF and ask questions in plain English so I can quickly find information without reading the whole document.
- *As a user*, I want the chatbot to tell me when it doesn't know something so I can trust that its answers come from my actual document.

---

## Project Structure

```
├── aibot.py          # Main Streamlit application
├── .env              # API key (not committed to git)
├── .gitignore        # Excludes .env, temp_doc, __pycache__
└── README.md         # This file
```

---
