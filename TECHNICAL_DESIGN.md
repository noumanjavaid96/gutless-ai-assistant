# Gutless AI Slack Assistant - Technical Design Document

## 1. Introduction

This document outlines the technical design for the Proof of Concept (POC) / Minimum Viable Product (MVP) of the Gutless AI Slack Assistant. It builds upon the requirements specified in the [Business Requirements Document (BRD)](BRD.md) and details the architecture, modules, data flow, and technology stack for the assistant.

The primary goal is to create a Slack bot capable of answering questions related to Week 1 content of the Gutless program by leveraging AI, specifically GPT-4, and a vector database (Pinecone) for efficient information retrieval.

## 2. High-Level Architecture

*(A diagram or detailed description of the interaction between Slack, the Bot Backend, Content Ingestion Pipeline, Embedding Service, and Pinecone Vector DB will be added here.)*

**Core Components:**

1.  **Slack Interface**: Handles incoming messages from Slack and sends formatted responses back.
2.  **Content Ingestion Pipeline**: Processes raw content (transcripts, PDFs) into a queryable format.
3.  **Embedding Service**: Generates vector embeddings for content chunks.
4.  **Vector Database (Pinecone)**: Stores and allows searching of content embeddings.
5.  **Core Logic / Orchestration Layer**: Manages the flow from query to answer, including context retrieval and answer synthesis.
6.  **LLM (GPT-4)**: Synthesizes answers based on retrieved context.

## 3. Module Breakdown

### 3.1. Content Ingestion Module

*   **Responsibilities**: Transcribe audio, extract text from PDFs, segment content, attach metadata.
*   **Key Technologies/Services**:
    *   Transcription: (e.g., AssemblyAI, OpenAI Whisper API)
    *   PDF Extraction: (e.g., `PyMuPDF`, `pdfplumber` Python libraries)
    *   Segmentation: Strategy to be defined (e.g., by paragraph, fixed size chunks with overlap).
    *   Metadata: Source (video name, PDF name), timestamp (if applicable), content type (transcript, PDF section).

### 3.2. Embedding and Vector Storage Module

*   **Responsibilities**: Generate embeddings for content chunks, store them in Pinecone, and provide search capabilities.
*   **Key Technologies/Services**:
    *   Embedding Model: (e.g., OpenAI `text-embedding-ada-002`)
    *   Vector Database: Pinecone
        *   Index Schema: Define fields (embedding, text chunk, metadata).
        *   Indexing Strategy: How and when new content is indexed.

### 3.3. Slack Bot Interface Module

*   **Responsibilities**: Receive messages from Slack, parse user queries, format and send responses.
*   **Key Technologies/Services**:
    *   Slack SDK: (e.g., `slack_bolt` for Python)
    *   Slack Events API: For receiving messages (`app_mention`, direct messages).
    *   Slack Web API: For sending messages (`chat.postMessage`).
    *   Response Formatting: Markdown, potentially Slack blocks for richer UI.

### 3.4. Core Logic Module

*   **Responsibilities**: Orchestrate the process of answering a user's query.
*   **Steps**:
    1.  **Query Preprocessing**: Clean and potentially rephrase the user's query.
    2.  **Embedding Generation (for Query)**: Generate embedding for the user query.
    3.  **Vector Search**: Query Pinecone to find relevant content chunks.
    4.  **Context Assembly**: Select and combine the most relevant chunks to form a context.
    5.  **Answer Synthesis**: Pass the query and assembled context to GPT-4 to generate an answer.
    6.  **Information Linking**: Include references/links to the source material in the response.
*   **Key Technologies/Services**:
    *   LLM: GPT-4 API
    *   Prompt Engineering: Design effective prompts for answer synthesis.

### 3.5. Logging Module (Optional for MVP - Basic Recommended)

*   **Responsibilities**: Log important events, errors, and user interactions for debugging and monitoring.
*   **Key Technologies/Services**: Python `logging` module, potentially structured logging.

### 3.6. Configuration Management (Optional for MVP - Basic Recommended)

*   **Responsibilities**: Manage API keys, model names, and other configurations securely.
*   **Key Technologies/Services**: Environment variables, `.env` files (e.g., using `python-dotenv`).

## 4. Data Flow

*(A step-by-step description of data movement, e.g., User sends message -> Slack API -> Bot Backend -> Query Embedding -> Pinecone Search -> Context Retrieval -> GPT-4 -> Formatted Response -> Slack API -> User.)*

1.  **Content Ingestion (Offline/Batch Process)**:
    *   Raw Content (Video/Audio, PDF) -> Transcription/Extraction Service -> Text Chunks + Metadata.
    *   Text Chunks -> Embedding Service -> Vector Embeddings.
    *   Vector Embeddings + Text Chunks + Metadata -> Pinecone.
2.  **Query Processing (Real-time)**:
    *   User posts question in Slack.
    *   Slack Bot receives message via Events API.
    *   Core Logic preprocesses query.
    *   Query -> Embedding Service -> Query Vector.
    *   Query Vector -> Pinecone Search -> Relevant Text Chunks (Context).
    *   (Query + Context) -> GPT-4 -> Synthesized Answer.
    *   Answer + Source Links -> Slack Bot formats response.
    *   Formatted Response -> Slack Web API -> User.

## 5. API Design

*   **External APIs Used**:
    *   Slack Events API & Web API
    *   Pinecone API
    *   OpenAI API (Embeddings, GPT-4)
    *   Transcription Service API (if external)
*   **Internal APIs (between microservices, if applicable for future scaling)**:
    *   (To be defined if a microservices architecture is chosen later. For MVP, likely a monolithic Python application.)

## 6. Technology Stack

*   **Programming Language**: Python
*   **Slack Integration**: `slack_bolt` (Python SDK)
*   **Vector Database**: Pinecone
*   **LLM & Embeddings**: OpenAI API (GPT-4, `text-embedding-ada-002`)
*   **PDF Processing**: `PyMuPDF` or `pdfplumber`
*   **Transcription**: (To be decided: e.g., AssemblyAI, OpenAI Whisper)
*   **Configuration**: `python-dotenv`
*   **Dependency Management**: `requirements.txt` or `Poetry`/`PDM`
*   **Web Framework (if needed for callbacks/admin)**: Flask/FastAPI (optional for basic bot)

## 7. Deployment Strategy (Initial Thoughts for POC)

*   **Hosting**: (e.g., AWS EC2, Heroku, Google Cloud Run, or even local ngrok for development).
*   **Containerization**: Docker (recommended for portability).
*   **Process Management**: (e.g., `systemd`, `supervisor` if on a server).

## 8. Security Considerations

*   **API Keys**: Store securely (environment variables, secrets manager).
*   **Data Privacy**: Ensure compliance with data handling policies, especially for user queries and content.
*   **Input Sanitization**: Basic checks for Slack inputs.

## 9. Future Considerations / Scalability

*   Support for more content types.
*   Advanced context window management.
*   User feedback mechanism.
*   More sophisticated logging and monitoring.
*   Potential for microservices architecture if load increases significantly.
*   CI/CD pipeline for automated testing and deployment.

## 10. Project Structure (Initial Proposal)

```
gutless-ai-assistant/
├── BRD.md
├── TECHNICAL_DESIGN.md
├── .env.example         # Example environment variables
├── .gitignore
├── README.md
├── requirements.txt
├── config/
│   └── settings.py      # Configuration settings
├── src/
│   ├── __init__.py
│   ├── bot.py             # Slack bot interface and event handling
│   ├── core_logic.py      # Orchestration, query processing, answer synthesis
│   ├── embedding_service.py # Handles embedding generation
│   ├── pinecone_service.py  # Pinecone integration
│   ├── content_ingestion/
│   │   ├── __init__.py
│   │   ├── transcribe.py
│   │   ├── pdf_parser.py
│   │   └── ingest.py      # Main script for ingestion pipeline
│   └── utils/
│       ├── __init__.py
│       └── logging_config.py
├── scripts/                 # Utility scripts (e.g., one-off ingestion)
│   └── ingest_data.py
└── tests/
    ├── __init__.py
    ├── test_bot.py
    └── test_core_logic.py
```
