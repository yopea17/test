# 환경 설정 가이드 (Environment Setup)

## 📋 프로젝트 구성

### 로컬 개발 환경
- **메인 파일**: `app.py` (Supabase 연동 Streamlit 앱)
- **데이터베이스**: Supabase (클라우드 데이터베이스)
- **테이블**: `daily_sales_data` (일일 매출 데이터)

---

## 🔐 Supabase 연결 정보

### Supabase 프로젝트
- **Project URL**: `https://ljhzwbbtcmyvtcaecflf.supabase.co`
- **Project Ref**: `ljhzwbbtcmyvtcaecflf`
- **Region**: 자동 할당

### 인증 정보 (Credentials)
- **API Key (Anon)**: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxqaHp3YmJ0Y215dnRjYWVjZmxmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODA1NDc3MTQsImV4cCI6MjA5NjEyMzcxNH0.I0HhY8hSYtF8mkgr1wQC0_8PWezWhA9tXQcpawtHpQw`

---

## 📁 로컬 환경 설정

### 1. Streamlit Secrets 파일
**경로**: `.streamlit/secrets.toml`

```toml
# 간단한 액세스 형식
SUPABASE_URL = "https://ljhzwbbtcmyvtcaecflf.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxqaHp3YmJ0Y215dnRjYWVjZmxmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODA1NDc3MTQsImV4cCI6MjA5NjEyMzcxNH0.I0HhY8hSYtF8mkgr1wQC0_8PWezWhA9tXQcpawtHpQw"

# 섹션 형식 (확장 가능)
[supabase]
project_url = "https://ljhzwbbtcmyvtcaecflf.supabase.co"
api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxqaHp3YmJ0Y215dnRjYWVjZmxmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODA1NDc3MTQsImV4cCI6MjA5NjEyMzcxNH0.I0HhY8hSYtF8mkgr1wQC0_8PWezWhA9tXQcpawtHpQw"
table_name = "daily_sales_data"
```

**⚠️ 주의**: 이 파일은 `.gitignore`에 의해 GitHub에 업로드되지 않습니다.

---

## 📦 필수 패키지

**파일**: `requirements.txt`

```
streamlit==1.40.1
pandas==2.2.0
plotly==5.20.0
requests==2.32.3
```

### 설치 방법
```bash
pip install -r requirements.txt
```

---

## 🚀 로컬 개발 서버 실행

```bash
cd C:\jihyun
streamlit run app.py
```

접속: `http://localhost:8501`

---

## ☁️ Streamlit Cloud 배포

### 1. GitHub Repository
- **URL**: https://github.com/yopea17/test
- **Branch**: main
- **App File**: app.py

### 2. Streamlit Cloud Secrets 설정

**배포된 앱**: https://testgit-qjl6ezdynd4iqtnsxr4qef.streamlit.app/

#### Secrets 설정 방법:
1. https://share.streamlit.io 에 접속
2. "yopea17's apps" 목록에서 "test" 앱 찾기
3. 앱 우측의 **⋯ (메뉴)** 클릭
4. **Settings** 선택
5. **Secrets** 탭에서 다음 내용 추가:

```toml
SUPABASE_URL = "https://ljhzwbbtcmyvtcaecflf.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxqaHp3YmJ0Y215dnRjYWVjZmxmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODA1NDc3MTQsImV4cCI6MjA5NjEyMzcxNH0.I0HhY8hSYtF8mkgr1wQC0_8PWezWhA9tXQcpawtHpQw"
```

6. **Save** 클릭

---

## 🗄️ Supabase 테이블 스키마

### 테이블명: `daily_sales_data`

| 컬럼명 | 타입 | 설명 |
|--------|------|------|
| id | BIGSERIAL | 고유 식별자 |
| date | DATE | 판매 날짜 |
| visitors | INTEGER | 방문자 수 |
| pv | INTEGER | 페이지뷰 |
| orders | INTEGER | 주문 건수 |
| conversion_rate | DECIMAL | 주문 전환율 (%) |
| net_payment | BIGINT | 순결제금액 |
| total_payment | BIGINT | 총결제금액 |
| created_at | TIMESTAMP | 생성 시간 |

---

## 📊 앱 기능

### 메트릭 (Metrics)
- ✅ 오늘 매출
- ✅ 어제 매출
- ✅ 어제 대비 증감률

### 차트 (Charts)
- ✅ 일별 매출 추이 (라인 차트)
- ✅ 최근 10일 PV 비중 (파이 차트)

### 상세 데이터
- ✅ 상세 데이터 보기 (테이블)

---

## 🔄 데이터 갱신

- **로컬**: 10초마다 자동 갱신 (캐시 TTL)
- **Streamlit Cloud**: 10초마다 자동 갱신 (동일)

---

## 📝 파일 목록

```
C:\jihyun\
├── app.py                          # 메인 Streamlit 앱 (Supabase 연동)
├── requirements.txt                # Python 패키지 의존성
├── ENVIRONMENT_SETUP.md            # 이 파일
├── .streamlit/
│   ├── secrets.toml               # Supabase 자격증명 (로컬만)
│   └── config.toml                # Streamlit 설정
├── .gitignore                      # Git 무시 파일
│   ├── .streamlit/secrets.toml    # Secrets 파일 제외
│   ├── *.pyc
│   └── __pycache__/
└── daily_sales_data.csv           # CSV 데이터 (참조용)
```

---

## ✅ 체크리스트

### 로컬 환경
- [x] Python 설치
- [x] 패키지 설치 (`pip install -r requirements.txt`)
- [x] Streamlit secrets 파일 생성 (`.streamlit/secrets.toml`)
- [x] 로컬 서버 실행 확인

### GitHub
- [x] Repository 생성
- [x] app.py 업로드
- [x] requirements.txt 업로드
- [x] .gitignore 설정 (secrets.toml 제외)

### Streamlit Cloud
- [ ] 배포 연결
- [ ] Secrets 설정 (SUPABASE_URL, SUPABASE_KEY)
- [ ] 앱 재배포 확인

---

## 🔗 유용한 링크

- [Streamlit 공식 문서](https://docs.streamlit.io/)
- [Supabase 공식 문서](https://supabase.com/docs)
- [GitHub Repository](https://github.com/yopea17/test)
- [Streamlit Cloud](https://share.streamlit.io/)

---

## 📞 문제 해결

### 에러: "Oh no. Error running app"
**해결**: Streamlit Cloud에서 Secrets이 설정되지 않았을 가능성
→ Settings → Secrets에서 SUPABASE_URL, SUPABASE_KEY 추가

### 에러: "데이터 조회 실패"
**해결**: Supabase 연결 정보 확인
→ SUPABASE_URL, SUPABASE_KEY가 올바른지 확인

### 로컬에서는 작동하지만 Cloud에서 에러
**해결**: Streamlit Cloud secrets 설정 필요
→ 위 "Streamlit Cloud Secrets 설정" 섹션 참고
