# 게시본 빌드 — 로컬 index.html → 아티팩트용 HTML
s = open('/home/user/Work-pinkpole/index.html', encoding='utf-8').read()
for a, b in [('<!DOCTYPE html>\n<html lang="ko">\n<head>\n', ''),
             ('<meta charset="utf-8">\n', ''),
             ('<meta name="viewport" content="width=device-width, initial-scale=1">\n', ''),
             ('</head>\n<body>\n', ''), ('</body>\n</html>\n', ''),
             ('<title>마케팅 활용동의 획득 실적 대시보드 | 한화손해보험</title>',
              '<title>마케팅 활용동의 획득 실적</title>')]:
    assert a in s, '래퍼 태그를 찾지 못함: ' + a[:40]
    s = s.replace(a, b, 1)
# 보는 사람 PC 에 나눔고딕이 없을 수 있으므로 웹폰트로 보강
s = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2'
     '?family=Nanum+Gothic:wght@400;700;800&display=swap">\n') + s
assert '<!DOCTYPE' not in s and s.lstrip().startswith('<link')
assert 'viewnote' not in s, '보기 전용 안내가 남아 있음'

# 게시본은 반드시 마스킹 상태로 게시한다.
# 로컬 index.html 은 사용자 요청으로 maskPII:false(전체 표시)지만,
# 웹 링크는 누구에게 전달될지 통제할 수 없으므로 여기서 true 로 되돌린다.
import re
s2 = re.sub(r'maskPII:\s*false', 'maskPII: true', s)
assert s2 != s or 'maskPII: true' in s, 'maskPII 설정을 찾지 못함'
s = s2
assert re.search(r'maskPII:\s*false', s) is None, '게시본에 마스킹 해제가 남아 있음'
# 게시본(웹 링크)은 보기 전용이므로 갱신 도구 진입 링크를 뺀다.
# 코드 자체는 남지만 화면에서 들어갈 방법이 없다.
link = ('\n      · <button class="up-link" onclick="go(\'update\')">주차 데이터 갱신</button>')
assert link in s, '갱신 링크를 찾지 못함'
s = s.replace(link, '')
assert '주차 데이터 갱신</button>' not in s, '게시본에 갱신 링크가 남아 있음'

import sys; open(sys.argv[1], 'w', encoding='utf-8').write(s)
print('artifact build ok —', round(len(s)/1024, 1), 'KB')
