# toy01_table_stripper

Oracle 데이터베이스의 테이블 정의를 Excel 파일로 내보내는 스크립트를 포함한 예제 프로젝트입니다.

## 개발 환경 설정

가상 환경을 만들고 패키지를 편집 모드로 설치합니다.

```bash
uv venv
uv pip install -e .
```

## 사용법

### Oracle 스키마 내보내기

1. 필요한 패키지를 설치합니다.

   ```bash
   pip install cx_Oracle openpyxl
   ```

2. 다음 환경 변수를 설정합니다.

   - `ORACLE_DSN` – Oracle 인스턴스 DSN (예: `localhost/orclpdb`)
   - `ORACLE_USER` – 데이터베이스 사용자명
   - `ORACLE_PASSWORD` – 데이터베이스 비밀번호
   - `OUTPUT_EXCEL` – 결과 Excel 파일 경로

3. 스크립트를 실행합니다.

   ```bash
   python export_table_schema.py
   ```

각 테이블은 열 이름, 타입, NULL 허용 여부를 포함하여 개별 시트로 저장됩니다.

## 프로젝트 구조

- `export_table_schema.py` – Oracle 스키마를 Excel로 추출하는 스크립트
- `pyproject.toml` – 프로젝트 메타데이터와 uv 설정
