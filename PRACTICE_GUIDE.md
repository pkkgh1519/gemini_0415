# Gemini 0415 GCP 실습 가이드

이 문서는 이 저장소의 실습을 실제 수업과 최대한 비슷한 Google Cloud 환경에서 다시 진행하기 위한 안내서입니다.

핵심만 먼저 정리하면 아래와 같습니다.

- 노트북 실습의 기준 환경은 Vertex AI Workbench Jupyter Notebook입니다.
- 일부 공식 실습은 Google Skills Boost student 프로젝트와 사전 준비된 VM을 전제로 합니다.
- Streamlit 프로젝트나 Python 스크립트 실행은 Cloud Shell이 가장 편합니다.
- 노트북 안에 들어 있는 프로젝트 ID, 리전, 버킷 이름은 그대로 쓰지 말고 자신의 값으로 바꿔야 합니다.

## 1. 어떤 환경에서 실습했나

저장소 안의 자료를 보면 실습 환경이 크게 세 가지로 나뉩니다.

### A. Vertex AI Workbench 기반 노트북 실습

아래 노트북들은 Vertex AI Workbench 또는 동일한 Jupyter 환경을 기준으로 보는 것이 자연스럽습니다.

- `intro_prompt_design_first.ipynb`
- `intro_genai_sdk.ipynb`
- `intro-textemb-vectorsearch.ipynb`
- `intro_multimodal_rag.ipynb`
- `intro_agent_engine.ipynb`
- `Introduction to Function Calling with Gemini.ipynb`
- `gemini_safety_ratings.ipynb`
- `deidentify-model-response.ipynb`

근거:

- Google Cloud 공식 Colab / Workbench 링크가 노트북 상단에 포함되어 있습니다.
- `PROJECT_ID`, `LOCATION`, `vertexai=True` 기반 초기화 코드가 반복해서 나옵니다.
- 일부 노트북은 `pdf_folder_path = "data/" # if running in Vertex AI Workbench` 라고 명시되어 있습니다.

### B. Google Skills Boost student 환경 기반 실습

다음 자료는 Google Skills Boost에서 제공하는 임시 student 프로젝트나 사전 준비된 리소스를 사용했을 가능성이 높습니다.

- `Google Gemini 엔터프라이즈 Skills 실습 목록.txt`
- `intro_*` 계열 공식 실습 노트북 다수

근거:

- `qwiklabs-gcp-*` 형식의 프로젝트 ID가 여러 노트북에 포함되어 있습니다.
- 실습 목록 파일에는 `Vertex AI Workbench의 Jupyter 노트북`과 `student 계정에 미리 생성되어 있는 VM`이라는 설명이 있습니다.

### C. Cloud Shell 또는 일반 셸 기반 프로젝트 실습

다음 실습은 Cloud Shell에서 실행하는 흐름이 자연스럽습니다.

- `AI_Agent_Trip_Project_Gemini-2.zip`
- `adk_project.zip`
- `deploy_agent.zip`

근거:

- 여행 에이전트 실습 질의문에 Cloud Shell에서 `streamlit run` 하는 예시가 직접 들어 있습니다.
- ADK / Agent Engine 예제는 `.env`, 패키지 설치, 배포 스크립트 실행을 전제로 합니다.

## 2. 동일환경으로 다시 실습하려면

수업과 최대한 비슷하게 하려면 아래 조합이 가장 현실적입니다.

1. Google Cloud 프로젝트 준비
2. Vertex AI Workbench Notebook 1개 준비
3. Cloud Shell 사용 가능 상태로 열어두기
4. 필요한 API를 미리 활성화
5. 노트북마다 `PROJECT_ID`, `LOCATION`, `BUCKET` 값을 자신의 환경에 맞게 교체

완전히 같은 환경이 꼭 필요하다면 Google Skills Boost 랩을 다시 열어 그 안의 student 프로젝트와 Workbench를 사용하는 것이 가장 가깝습니다.

## 3. 사전 준비 체크리스트

### 필수

- GCP 프로젝트 1개
- Billing 연결
- Vertex AI API 사용 가능
- Cloud Storage 사용 가능
- Cloud Shell 사용 가능
- Vertex AI Workbench Notebook 인스턴스 또는 동일한 Jupyter 환경

### 실습 주제별 추가 준비

#### RAG / Vector Search

- Cloud Storage 버킷
- Vector Search 사용 권한
- 리전 선택

#### Agent Engine / ADK

- Vertex AI Agent Engine 사용 가능 여부
- `us-central1` 리전 사용 가능 여부
- Cloud Logging 권한

#### DLP

- Sensitive Data Protection API 사용 가능 여부

## 4. 먼저 켜둘 API

최소한 아래 API는 미리 켜두는 편이 좋습니다.

- `aiplatform.googleapis.com`
- `storage.googleapis.com`
- `compute.googleapis.com`
- `bigquery.googleapis.com`
- `logging.googleapis.com`
- `dlp.googleapis.com`

예제에 따라 추가로 필요한 API가 생길 수 있습니다.

## 5. 권장 리전 정리

노트북을 보면 리전 사용 방식이 섞여 있습니다. 같은 프로젝트에서 다시 실습할 때는 아래 기준으로 정리하는 것이 편합니다.

- `global`
  - Gen AI SDK 기반 기본 호출
  - Prompt Design
  - 일부 Function Calling 예제
- `us-central1`
  - Agent Engine
  - Safety 관련 예제
  - 일부 공식 Vertex AI 노트북
- `asia-northeast3`
  - 강사 커스텀 RAG / Vector Search 예제
  - 일부 Google Maps / RAG 관련 코드

중요한 점은 노트북 안에 들어 있는 값이 모두 같은 기준으로 작성된 것이 아니라는 점입니다. 리전과 버킷은 실습마다 맞춰서 바꿔야 합니다.

## 6. 노트북 실행 방식

### Vertex AI Workbench에서 실행 권장

아래 유형은 Workbench에서 돌리는 것이 가장 편합니다.

- `intro_prompt_design_first.ipynb`
- `intro_genai_sdk.ipynb`
- `intro-textemb-vectorsearch.ipynb`
- `intro_multimodal_rag.ipynb`
- `intro_agent_engine.ipynb`
- `gemini_safety_ratings.ipynb`
- `deidentify-model-response.ipynb`

실행 순서:

1. Workbench Notebook 열기
2. 저장소 파일 업로드 또는 Git clone
3. 상단의 `%pip install` 셀부터 차례대로 실행
4. `PROJECT_ID`, `LOCATION`, `STAGING_BUCKET` 값 교체
5. 인증 및 API 활성화가 필요한 셀 실행
6. 결과 확인

### 주의할 점

- 노트북 안의 `qwiklabs-gcp-*` 값은 예시 또는 랩 전용 값입니다.
- Agent Engine 리소스 이름, Vector Search 엔드포인트 ID, RAG Corpus 이름 등은 자신의 환경에서 새로 생성된 값으로 바꿔야 합니다.
- 공식 랩 노트북 일부는 Colab 설명과 Workbench 설명을 함께 갖고 있으므로 경로를 확인해야 합니다.
  - 예: `/content/data/` 는 Colab용
  - 예: `data/` 는 Workbench용

## 7. 프로젝트형 실습 실행 방식

### A. 여행 에이전트

권장 환경: Cloud Shell 또는 로컬 Python 환경

실행 순서:

1. ZIP 해제
2. 가상 환경 생성
3. `pip install -r requirements.txt`
4. 프로젝트 루트에 `.env` 생성
5. `GEMINI_API_KEY` 설정
6. 아래 중 하나로 실행

```bash
python main.py
```

```bash
cd ui
streamlit run app.py
```

Cloud Shell에서 실행할 때는 아래 방식이 더 안정적입니다.

```bash
export PATH=$PATH:~/.local/bin
cd ui
streamlit run app.py --server.enableCORS=false --server.enableXsrfProtection=false
```

### B. ADK 프로젝트

권장 환경: Cloud Shell 또는 Vertex AI Workbench Terminal

`.env` 예시:

```env
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=global
MODEL=gemini-2.5-flash
```

실행 전 확인할 것:

- `google-adk` 설치
- Vertex AI 인증 가능 상태
- 필요한 경우 Cloud Logging 권한 부여

### C. Agent Engine 배포 예제

권장 환경: Cloud Shell

배포 전에 반드시 수정할 값:

- `PROJECT_ID`
- `LOCATION`
- `STAGING_BUCKET`
- 이미 배포된 Agent Engine 리소스 이름

특히 `us-central1` 리전과 staging bucket 준비 여부를 먼저 확인해야 합니다.

## 8. 추천 실습 순서

같은 GCP 환경에서 다시 해본다면 아래 순서를 권장합니다.

1. `01_Gemini API 사용 기본 예제.ipynb`
2. `02_Prompt 버전 관리.ipynb`
3. `04_Function Calling.ipynb`
4. `05_Google Built-in Tools.ipynb`
5. `03_RAG 기본 메카니즘.ipynb`
6. `intro-textemb-vectorsearch.ipynb`
7. `06_Google ADK.ipynb`
8. `07_Agent to Agent.ipynb`
9. `intro_agent_engine.ipynb`
10. 여행 에이전트 또는 ADK ZIP 프로젝트

이 순서는 API 호출 → 프롬프트 → 도구 → RAG → 에이전트 → 배포 흐름으로 이어져서 학습하기 편합니다.

## 9. 자주 막히는 지점

### 프로젝트 ID를 그대로 쓰는 경우

노트북 안에 보이는 `byounghwa-go`, `qwiklabs-gcp-*` 는 그대로 쓰면 안 됩니다.

### 리전이 맞지 않는 경우

Agent Engine은 대체로 `us-central1`, 강사 커스텀 RAG는 `asia-northeast3`, 기본 GenAI SDK는 `global` 을 섞어 쓰고 있습니다. 리전을 섞어 쓰면 리소스 조회가 안 될 수 있습니다.

### Skills Boost 전용 랩을 일반 프로젝트에서 그대로 실행하는 경우

사전 생성된 리소스가 없어서 막힐 수 있습니다. 이런 경우는 Skills Boost 랩에서 다시 실행하는 쪽이 빠릅니다.

### Cloud Shell에서 Streamlit이 바로 안 뜨는 경우

질의문에도 적혀 있듯이 `--server.enableCORS=false --server.enableXsrfProtection=false` 옵션을 붙이는 편이 안전합니다.

## 10. 마지막 정리

이 저장소를 수업과 비슷한 환경에서 다시 실습하려면 기준은 아래 하나로 잡으면 됩니다.

- 노트북: Vertex AI Workbench
- 프로젝트 실행: Cloud Shell
- 공식 랩 재현: Google Skills Boost

이 세 가지를 기준으로 보면 저장소 안의 자료가 훨씬 덜 혼란스럽게 정리됩니다.