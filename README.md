# Google Gemini 기반 엔터프라이즈 생성형 AI 실습 자료

2026.04.15 ~ 2026.04.17 과정에서 사용한 Gemini / Vertex AI 실습 자료를 정리한 저장소입니다.
슬라이드, 노트북, 미니 프로젝트를 한곳에 모아두었고, 실습은 대부분 Google Cloud 환경에서 진행했습니다.

이 저장소는 제품 레포라기보다 교육용 실습 패키지에 가깝습니다. 빠르게 훑어보고 따라 하기에는 좋지만, 그대로 서비스 베이스로 쓰기보다는 필요한 예제만 분리해서 재정리하는 방식이 더 적합합니다.

## 이 저장소로 할 수 있는 것

- Gemini API 기본 호출 익히기
- 프롬프트 설계와 버전 관리 흐름 보기
- Vertex AI 기반 RAG와 Vector Search 실습하기
- Function Calling과 Google Built-in Tools 확인하기
- Google ADK와 A2A 예제 구조 살펴보기
- Streamlit 기반 미니 에이전트 프로젝트 실행해보기
- Agent Engine 배포 예제를 통해 Vertex AI 운영 흐름 이해하기

## 자료 구성

### 상위 폴더

- 강의 PDF
- 과정 일정표
- Google Skills Boost 실습 목록
- 참고용 ZIP 자료

### 실습소스

실제 실습의 중심은 `실습소스/` 폴더입니다.

주요 노트북은 아래 흐름으로 보면 됩니다.

1. `01_Gemini API 사용 기본 예제.ipynb`
2. `02_Prompt 버전 관리.ipynb`
3. `03_RAG 기본 메카니즘.ipynb`
4. `04_Function Calling.ipynb`
5. `05_Google Built-in Tools.ipynb`
6. `06_Google ADK.ipynb`
7. `07_Agent to Agent.ipynb`

공식 Google Cloud 실습 기반 노트북도 함께 포함되어 있습니다.

- `intro_prompt_design_first.ipynb`
- `intro_genai_sdk.ipynb`
- `intro-textemb-vectorsearch.ipynb`
- `intro_multimodal_rag.ipynb`
- `Introduction to Function Calling with Gemini.ipynb`
- `intro_agent_engine.ipynb`
- `gemini_safety_ratings.ipynb`
- `deidentify-model-response.ipynb`

### 포함된 ZIP 프로젝트

- `AI_Agent_Trip_Project_Gemini-2.zip`
	- Gemini + LangChain + Streamlit 기반 여행 에이전트 예제
- `AI_Agent_Finance_Project.zip`
	- 금융 분석 / 리포트 생성 예제
	- 저장소 주제와 달리 OpenAI API 기반입니다.
- `adk_project.zip`
	- Google ADK 기반 검색 / 감사 / 멀티 에이전트 샘플
- `deploy_agent.zip`
	- Vertex AI Agent Engine 배포 예제

## 실습 환경

이번 과정은 로컬 PC보다는 Google Cloud 환경을 기준으로 진행했습니다.

- 기본 노트북 환경: Vertex AI Workbench Jupyter Notebook
- 일부 공식 랩 환경: Google Skills Boost student 프로젝트 또는 사전 준비된 VM
- 프로젝트형 실습 실행: Google Cloud Shell 또는 로컬 Python 환경

노트북 안에 `qwiklabs-gcp-*`, `byounghwa-go`, `PROJECT_ID`, `LOCATION`, `STAGING_BUCKET` 같은 값이 직접 들어 있는 경우가 있습니다. 그대로 실행하지 말고 자신의 프로젝트 기준으로 바꿔서 사용해야 합니다.

실제 수업과 최대한 비슷한 환경에서 실습하려면 `PRACTICE_GUIDE.md`를 먼저 확인해 주세요.

## 추천 학습 순서

1. Gemini API 기초
2. 프롬프트 설계
3. RAG와 Vector Search
4. Function Calling / Built-in Tools
5. ADK / A2A
6. 여행 에이전트 프로젝트
7. Agent Engine 배포
8. Safety / DLP / 멀티모달 확장 주제

## 참고 링크

- Generative AI on Vertex AI 문서
	- https://docs.cloud.google.com/vertex-ai/generative-ai/docs?hl=ko
- Agent Development Kit 문서
	- https://adk.dev/deploy/agent-engine/
- Gemini API 문서
	- https://ai.google.dev/gemini-api/docs/api-key?hl=ko
- Google AI Studio
	- https://aistudio.google.com/app/apikey?hl=ko
- Google Cloud 공식 generative-ai 예제
	- https://github.com/GoogleCloudPlatform/generative-ai/tree/main/gemini
- Agent Starter Pack
	- https://github.com/GoogleCloudPlatform/agent-starter-pack

## 주의사항

- 일부 실습은 Google Skills Boost에서 제공하는 student 환경을 전제로 합니다.
- Vertex AI Vector Search, Agent Engine, Cloud Logging, DLP 관련 예제는 비용과 권한 설정이 필요합니다.
- ZIP 파일 안에는 로그, 벡터 DB, `.pyc`, 세션 DB 같은 실행 산출물이 포함되어 있을 수 있습니다.
- 학습용 자료이므로 공개 재배포 전에는 저작권과 배포 범위를 반드시 확인해 주세요.

## 다음 문서

동일한 GCP 환경에서 다시 실습하는 방법은 `PRACTICE_GUIDE.md`에 정리해 두었습니다.
# Google Gemini 기반 엔터프라이즈 생성형 AI 실습 자료

2026.04.15 ~ 2026.04.17 과정에서 사용한 Gemini / Vertex AI 실습 자료를 정리한 저장소입니다.
슬라이드, 노트북, 미니 프로젝트를 한곳에 모아두었고, 실습은 대부분 Google Cloud 환경에서 진행했습니다.

이 저장소는 제품 레포라기보다 교육용 실습 패키지에 가깝습니다. 빠르게 훑어보고 따라 하기에는 좋지만, 그대로 서비스 베이스로 쓰기보다는 필요한 예제만 분리해서 재정리하는 방식이 더 적합합니다.

## 이 저장소로 할 수 있는 것

- Gemini API 기본 호출 익히기
- 프롬프트 설계와 버전 관리 흐름 보기
- Vertex AI 기반 RAG와 Vector Search 실습하기
- Function Calling과 Google Built-in Tools 확인하기
- Google ADK와 A2A 예제 구조 살펴보기
- Streamlit 기반 미니 에이전트 프로젝트 실행해보기
- Agent Engine 배포 예제를 통해 Vertex AI 운영 흐름 이해하기

## 자료 구성

### 상위 폴더

- 강의 PDF
- 과정 일정표
- Google Skills Boost 실습 목록
- 참고용 ZIP 자료

### 실습소스

실제 실습의 중심은 `실습소스/` 폴더입니다.

주요 노트북은 아래 흐름으로 보면 됩니다.

1. `01_Gemini API 사용 기본 예제.ipynb`
2. `02_Prompt 버전 관리.ipynb`
3. `03_RAG 기본 메카니즘.ipynb`
4. `04_Function Calling.ipynb`
5. `05_Google Built-in Tools.ipynb`
6. `06_Google ADK.ipynb`
7. `07_Agent to Agent.ipynb`

공식 Google Cloud 실습 기반 노트북도 함께 포함되어 있습니다.

- `intro_prompt_design_first.ipynb`
- `intro_genai_sdk.ipynb`
- `intro-textemb-vectorsearch.ipynb`
- `intro_multimodal_rag.ipynb`
- `Introduction to Function Calling with Gemini.ipynb`
- `intro_agent_engine.ipynb`
- `gemini_safety_ratings.ipynb`
- `deidentify-model-response.ipynb`

### 포함된 ZIP 프로젝트

- `AI_Agent_Trip_Project_Gemini-2.zip`
	- Gemini + LangChain + Streamlit 기반 여행 에이전트 예제
- `AI_Agent_Finance_Project.zip`
	- 금융 분석 / 리포트 생성 예제
	- 저장소 주제와 달리 OpenAI API 기반입니다.
- `adk_project.zip`
	- Google ADK 기반 검색 / 감사 / 멀티 에이전트 샘플
- `deploy_agent.zip`
	- Vertex AI Agent Engine 배포 예제

## 실습 환경

이번 과정은 로컬 PC보다는 Google Cloud 환경을 기준으로 진행했습니다.

- 기본 노트북 환경: Vertex AI Workbench Jupyter Notebook
- 일부 공식 랩 환경: Google Skills Boost student 프로젝트 또는 사전 준비된 VM
- 프로젝트형 실습 실행: Google Cloud Shell 또는 로컬 Python 환경

노트북 안에 `qwiklabs-gcp-*`, `byounghwa-go`, `PROJECT_ID`, `LOCATION`, `STAGING_BUCKET` 같은 값이 직접 들어 있는 경우가 있습니다. 그대로 실행하지 말고 자신의 프로젝트 기준으로 바꿔서 사용해야 합니다.

실제 수업과 최대한 비슷한 환경에서 실습하려면 `PRACTICE_GUIDE.md`를 먼저 확인해 주세요.

## 추천 학습 순서

1. Gemini API 기초
2. 프롬프트 설계
3. RAG와 Vector Search
4. Function Calling / Built-in Tools
5. ADK / A2A
6. 여행 에이전트 프로젝트
7. Agent Engine 배포
8. Safety / DLP / 멀티모달 확장 주제

## 참고 링크

- Generative AI on Vertex AI 문서
	- https://docs.cloud.google.com/vertex-ai/generative-ai/docs?hl=ko
- Agent Development Kit 문서
	- https://adk.dev/deploy/agent-engine/
- Gemini API 문서
	- https://ai.google.dev/gemini-api/docs/api-key?hl=ko
- Google AI Studio
	- https://aistudio.google.com/app/apikey?hl=ko
- Google Cloud 공식 generative-ai 예제
	- https://github.com/GoogleCloudPlatform/generative-ai/tree/main/gemini
- Agent Starter Pack
	- https://github.com/GoogleCloudPlatform/agent-starter-pack

## 주의사항

- 일부 실습은 Google Skills Boost에서 제공하는 student 환경을 전제로 합니다.
- Vertex AI Vector Search, Agent Engine, Cloud Logging, DLP 관련 예제는 비용과 권한 설정이 필요합니다.
- ZIP 파일 안에는 로그, 벡터 DB, `.pyc`, 세션 DB 같은 실행 산출물이 포함되어 있을 수 있습니다.
- 학습용 자료이므로 공개 재배포 전에는 저작권과 배포 범위를 반드시 확인해 주세요.

## 다음 문서

동일한 GCP 환경에서 다시 실습하는 방법은 `PRACTICE_GUIDE.md`에 정리해 두었습니다.
