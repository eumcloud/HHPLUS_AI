import requests

def search_arxiv(keyword: str) -> list:
    base_url = "http://export.arxiv.org/api/query"
    params = {"search_query": f"all:{keyword}", "start": 0, "max_results": 5}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.text  # XML 파싱 필요 (향후 확장)
    return []
