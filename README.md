# Gemini 0415 내부 기술 교육 공유 자료

## 문서 목적

이 문서는 `pkkgh1519/gemini_0415` 저장소를 내부 기술 교육 공유용으로 다시 정리한 안내 문서다.
원본 저장소는 단일 애플리케이션 프로젝트가 아니라, Google Gemini / Vertex AI / ADK / RAG 관련 강의 자료를 한 번에 업로드한 교육용 패키지에 가깝다.

따라서 이 문서의 목적은 다음 두 가지다.

1. 저장소 안에 어떤 자료가 들어 있는지 빠르게 파악할 수 있게 한다.
2. 실제 실습을 어디부터 어떤 순서로 진행해야 하는지 판단할 수 있게 한다.

## 저장소 성격 요약

- 강의 슬라이드, PDF, 일정표, 참고 링크가 함께 포함된 교육 자료 저장소다.
- 실습의 중심은 Jupyter Notebook이다.
- 일부 주제는 ZIP 파일로 별도 프로젝트가 포함되어 있다.
- 재현 가능한 제품 레포라기보다, 수업 중 시연과 따라하기를 위한 샘플 모음에 가깝다.

## 포함 자료 구조

### 1. 상위 폴더 자료

- PDF 강의자료
- 과정 일정표
- Google Skills Boost 실습 목록
- 참고용 ZIP 파일
- 원본 README

### 2. 실습소스 폴더

`실습소스/` 아래가 실제 실습의 핵심이다.

주요 노트북 순서는 다음과 같다.

1. `01_Gemini API 사용 기본 예제.ipynb`
2. `02_Prompt 버전 관리.ipynb`
3. `03_RAG 기본 메카니즘.ipynb`
4. `04_Function Calling.ipynb`
5. `05_Google Built-in Tools.ipynb`
6. `06_Google ADK.ipynb`
7. `07_Agent to Agent.ipynb`

이외에도 Google Skills Boost 기반 실습 노트북이 함께 포함되어 있다.

- `intro_prompt_design_first.ipynb`
- `intro_genai_sdk.ipynb`
- `intro-textemb-vectorsearch.ipynb`
- `intro_multimodal_rag.ipynb`
- `Introduction to Function Calling with Gemini.ipynb`
- `intro_agent_engine.ipynb`
- `gemini_safety_ratings.ipynb`
- `deidentify-model-response.ipynb`
- `multimodal_retail_recommendations.ipynb`

### 3. ZIP 프로젝트 자료

실습소스 폴더에는 독립 실행형 예제 프로젝트도 포함되어 있다.

- `AI_Agent_Trip_Project_Gemini-2.zip`
  - Gemini API + LangChain + Streamlit 기반 여행 일정 추천 에이전트
- `AI_Agent_Finance_Project.zip`
  - 금융 분석 / 리스크 평가 / 리포트 자동 생성 예제
  - 이름과 달리 핵심 LLM은 OpenAI API 기반이다.
- `adk_project.zip`
  - Google ADK 기반 검색 에이전트, 감사 에이전트, 멀티 에이전트 예제
- `deploy_agent.zip`
  - Vertex AI Agent Engine 배포 예제

## 내부 교육용으로 볼 때의 핵심 포인트

### 잘 정리된 점

- Gemini API 기초부터 RAG, Function Calling, Built-in Tools, ADK, A2A까지 흐름이 이어진다.
- 실습 노트북과 미니 프로젝트가 함께 있어 개념과 구현을 연결하기 좋다.
- Vertex AI와 Gemini API, AI Studio, ADK, Agent Engine을 한 저장소에서 함께 볼 수 있다.

### 그대로 사용하기 어려운 점

- 노트북 출력 결과가 포함되어 있어 저장소가 무겁다.
- ZIP 내부에 로그, 벡터 DB, `.pyc`, 세션 DB 같은 런타임 산출물이 포함되어 있다.
- 일부 README와 실제 코드의 설정 방식이 다르다.
- ADK / Vertex AI 계열 예제는 GCP 프로젝트, 권한, 리전, 버킷 준비가 전제된다.
- 금융 예제는 Gemini 교육 저장소 안에 있지만 OpenAI API를 사용하므로 학습 목적을 분리해서 봐야 한다.

## 권장 학습 경로

내부 교육에서는 아래 순서로 보는 것이 가장 효율적이다.

1. Gemini API 기초와 프롬프트 설계 이해
2. RAG, Function Calling, Built-in Tools 실습
3. ADK와 A2A로 에이전트 협업 구조 이해
4. ZIP 프로젝트로 통합형 샘플 구조 확인
5. Agent Engine 배포 예제로 운영 환경 연결 이해
6. Safety / DLP / 멀티모달 실습으로 확장 주제 학습

자세한 절차는 `PRACTICE_GUIDE.md`를 참고한다.

## 추천 대상

- Gemini API 입문 후 응용 범위를 넓히고 싶은 개발자
- Vertex AI 기반 에이전트 구조를 빠르게 훑고 싶은 엔지니어
- ADK, A2A, RAG를 하나의 교육 흐름으로 설명해야 하는 사내 강사
- 실무 도입 전 PoC 아이디어를 찾는 팀

## 비권장 사용 방식

이 저장소를 바로 서비스 시작점으로 삼는 것은 권장하지 않는다.

다음 이유 때문이다.

- 버전 고정과 의존성 정리가 약하다.
- 실행 산출물이 함께 포함되어 재현성이 떨어진다.
- 학습용 데모와 실서비스용 구조가 혼재되어 있다.
- 클라우드 설정, API 키, 벡터 DB 초기화 방식이 통일되어 있지 않다.

실무 전환이 목적이라면, 필요한 실습 하나만 별도 저장소로 분리한 뒤 다음을 다시 정리하는 편이 낫다.

1. 의존성 버전 고정
2. 환경 변수 로딩 방식 통일
3. 런타임 산출물 제거
4. 실행 스크립트와 테스트 보강
5. 목적별 README 재작성

## 교육 운영 시 주의사항

- 원본 README에는 외부 재배포에 대한 저작권 주의 문구가 포함되어 있다.
- 내부 공유 시에도 공개 배포용 자료로 전환하지 말고, 학습 목적 범위에서만 사용 여부를 검토해야 한다.
- Vertex AI 실습은 비용과 권한 이슈가 있으므로 사전 계정 준비가 필요하다.
- 일부 실습은 Google Skills Boost 환경을 전제로 하므로 로컬 환경에서 완전히 동일하게 재현되지 않을 수 있다.

## 빠른 판단

- 개념 학습용: 적합
- 강의 보조 자료: 적합
- 사내 스터디 자료: 적합
- 바로 배포 가능한 제품 레포: 부적합
- 팀 공용 베이스 템플릿: 부적합

## 다음 문서

실습 환경 준비, 권장 순서, 트랙별 진행 방법은 `PRACTICE_GUIDE.md`에 정리되어 있다.
