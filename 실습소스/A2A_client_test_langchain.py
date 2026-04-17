import requests
import json

def stream_mcp_message():
    url = "http://localhost:8000"
    headers = {"Content-Type": "application/json"}
    
    # 요청 페이로드 설정
    payload = {
        "jsonrpc": "2.0",
        "method": "message/stream",
        "params": {
            "message": {
                "messageId": "123456",
                "role": "user",
                "parts": [{"kind": "text", "text": "A2A 프로토콜의 주요 장점 3가지를 알려줘"}]
            }
        },
        "id": "3"
    }

    try:
        # stream=True를 사용하여 응답을 실시간으로 받아옵니다.
        response = requests.post(url, headers=headers, json=payload, stream=True)
        
        # 응답 상태 확인
        response.raise_for_status()

        print("--- 스트리밍 응답 시작 ---")
        
        for line in response.iter_lines():
            if line:
                # 1. 'data: ' 접두사 제거 (sed 역할)
                decoded_line = line.decode('utf-8')
                if decoded_line.startswith("data: "):
                    json_str = decoded_line.replace("data: ", "")
                    
                    try:
                        data = json.loads(json_str)
                        
                        # 2. "kind":"artifact-update" 필터링 (grep 역할)
                        # JSON 구조 내에 kind가 직접 있거나 result 내부에 있는 경우를 모두 체크합니다.
                        if data.get("kind") == "artifact-update" or \
                           (isinstance(data.get("result"), dict) and data["result"].get("kind") == "artifact-update"):
                            
                            # 3. 보기 좋게 출력 (jq 역할)
                            print(json.dumps(data, indent=2, ensure_ascii=False))
                            
                    except json.JSONDecodeError:
                        # JSON 형식이 아닌 줄은 무시합니다.
                        continue

    except requests.exceptions.RequestException as e:
        print(f"에러 발생: {e}")

if __name__ == "__main__":
    stream_mcp_message()