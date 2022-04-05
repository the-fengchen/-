import requests
import re

def get_html(url):
    headers = {
        'Cookie':'ISID=e26e55bb97a8840af2462d0e6f870fb4; _sid=1fhal2794d2mtacup3llc055k5q1eihi; aliyungf_tc=9abad26bb89ae5ca89740c38cd26490369a528be27656b7690f63e6ef93d3673; csrfToken=dh9Zga3SlHRh9hO1uj5AsexJ; token=dh9Zga3SlHRh9hO1uj5AsexJ; Hm_lvt_be36b12b82a5f4eaa42c23989d277bb0=1648691047,1648990504; _guard_device_id=1fvpf2tqmvVSJKH0WfZ1CuKvQ5KkHm2pHevXPtk; GAT=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJpZ2V0Z2V0LmNvbSIsImV4cCI6MTY1MTcyNzkxOSwiaWF0IjoxNjQ5MTM1OTE5LCJpc3MiOiJEREdXIEpXVCBNSURETEVXQVJFIiwibmJmIjoxNjQ5MTM1OTE5LCJzdWIiOiIyNDUwOTU3NzciLCJkZXZpY2VfaWQiOiJlMjZlNTViYjk3YTg4NDBhZjI0NjJkMGU2Zjg3MGZiNCIsImRldmljZV90eXBlIjoiaWdldHdlYiJ9.-jBODCZ6FzEsv-9fdO_GRMn7vMzmQ39qJIObZHw9S-cAinFBeYyRD8FDeYLG-SDk5jV9btL40IAQmJ5B7_7PHg; iget=eyJ3ZWNoYXRJbmZvIjp7Im9wZW5pZCI6Im9ZRk5Od1V6eVZvQlg5MzhkbDBwM0hEZEYxMTQiLCJ1bmlvbmlkIjoib0RJN0R2dXI2M2xodDF5dTJxZGNzanN4dnVwTSIsIm5pY2tuYW1lIjoiTmlrbyIsImF2YXRhciI6Imh0dHBzOi8vcGljY2RuLnVtaXdpLmNvbS91cGxvYWRlci9pbWFnZS9ub3RlLzIwMjIwMzI2MTQvMTc2OTgyMzUxMTEyOTM1OTQ2MCIsInVzZXJJZCI6MjQ1MDk1Nzc3fSwidXNlciI6eyJ1c2VySWQiOjI0NTA5NTc3Nywibmlja25hbWUiOiJOaWtvIiwiYXZhdGFyIjoiaHR0cHM6Ly9waWNjZG4udW1pd2kuY29tL3VwbG9hZGVyL2ltYWdlL25vdGUvMjAyMjAzMjYxNC8xNzY5ODIzNTExMTI5MzU5NDYwIiwiYXZhdGFyU2hvcnQiOiJodHRwczovL3BpY2Nkbi51bWl3aS5jb20vdXBsb2FkZXIvaW1hZ2Uvbm90ZS8yMDIyMDMyNjE0LzE3Njk4MjM1MTExMjkzNTk0NjA/eC1vc3MtcHJvY2Vzcz1pbWFnZS9yZXNpemUscF8yNSIsInN0YXR1cyI6Miwib3BlbmlkIjoib1lGTk53VXp5Vm9CWDkzOGRsMHAzSERkRjExNCIsInVuaW9uaWQiOiJvREk3RHZ1cjYzbGh0MXl1MnFkY3Nqc3h2dXBNIiwicGhvbmUiOiIxODkyODc2MzM2OSIsImxvZ2luVGltZSI6IjIwMjItMDQtMDUgMTM6MTg6MzkifSwiX2V4cGlyZSI6MTY0OTc0MDcyMDIwMCwiX21heEFnZSI6NjA0ODAwMDAwfQ==; acw_tc=707c9f7316491388672522579e2fe9f27e317e6a934c3bf5b647e111bea12c; Hm_lpvt_be36b12b82a5f4eaa42c23989d277bb0=1649140182',
        'Host': 'www.dedao.cn',
        'Origin': 'https://www.dedao.cn',
        'Referer': 'https://www.dedao.cn/knowledge/topic/detail?id=6MlZDjmye1kZgqNqpo3Eo8GoXbPYrd',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Mobile Safari/537.36 Edg/100.0.1185.29',
    }
    data = {
        "count":'10',
        "is_elected":'true',
        "page_id":'0',
        "topic_id_hazy":"6MlZDjmye1kZgqNqpo3Eo8GoXbPYrd",
        "version":'2'
        }
    response = requests.post(url, headers=headers, data=data)
    response.encoding = 'utf-8'
    return response.text

def get_info(html):
    pat = '"nick_name":"(.+?)"'
    names = re.findall(pat, html, re.S)
    return names

if __name__ == '__main__':
    url = 'https://www.dedao.cn/pc/ledgers/topic/notes/list'
    html = get_html(url)
    print(html)
    '''names = get_info(html)
    items = {}
    for name in names:
        items[name] = items.get(name, 0) + 1
    print(items)'''