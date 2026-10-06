# 베베누리 디자인 협업

## 주소
- / : 회차별 공유 문서 목록
- /requests/01/ : 1차 아이콘·그래프 디자인 요청

## 로컬 확인
python3 -m http.server 9000 --bind 127.0.0.1

## 문서 수정과 추가
- 기존 회차 수정: requests/해당번호/index.html
- 새 회차: requests/02/index.html처럼 별도 폴더에 추가하고, 회차별 이미지는 assets/02/에 둡니다.
- 목록 등록: content/documents.json에 제목·설명·주소·요청 항목을 추가합니다.
- 목록 생성: python3 scripts/build_index.py
- content/index.template.html은 문서 목록의 템플릿입니다.
- 각 회차는 별도 주소를 유지하며 이전 문서를 새 요청으로 덮어쓰지 않습니다.
- 논의 전인 일정·시안·검토 결과는 임의로 등록하지 않습니다.

9000번에서 본문·이미지·모바일 표시를 확인한 뒤 main에 푸시하면 같은 Vercel 주소로 배포됩니다.

공유용 저장소이므로 계정 정보나 개인정보를 추가하지 않습니다. 참고 이미지 출처는 각 문서에 표시합니다.
