"""하루 가계부 단독 실행 파일 만들기.

index.html 은 게시(Artifact)용이라 <!doctype>/<head>/<body> 가 없다.
내려받아 브라우저에서 바로 여는 파일은 문서 뼈대와 UTF-8 선언이 있어야
한글이 깨지지 않으므로 감싸서 하루가계부.html 로 저장한다.

    python3 ledger/build_standalone.py
"""
from pathlib import Path

here = Path(__file__).parent
body = (here / "index.html").read_text(encoding="utf-8")
out = (
    '<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
    "</head>\n<body>\n" + body + "\n</body>\n</html>\n"
)
(here / "하루가계부.html").write_text(out, encoding="utf-8")
print("wrote", here / "하루가계부.html")
