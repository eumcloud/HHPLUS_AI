## 목표

---

이번 실습에서는 LangChain으로 개발한 RAG를 다음 블로그의 정보와 연동합니다.

요구사항은 다음과 같습니다.

- [ ]  RAG internet source를 <https://spartacodingclub.kr/blog/all-in-challenge_winner> 로 설정합니다.
  - RAG에서 활용할 source로 위의 링크를 전달합니다.
  - 사이트가 달라졌기 때문에 이전 실습 코드와 다르게 load 해야 합니다. 어디를 어떻게 수정해야 할지 고민해보도록 합시다.
  - LLM은 GPT를 사용하시면 됩니다. 모델은 `gpt-4o-mini`로 설정하시면 됩니다.
- [ ]  GPT에게 `“ALL-in 코딩 공모전 수상작들을 요약해줘.”`를 물은 뒤의 답변을 출력합니다.

## 제출자료

---

요구사항을 충족하는 코드를 github repository에 업로드합니다.
