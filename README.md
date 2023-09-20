# EV-charging-station-selection
## 2021년도 서울시립대학교 빅데이터 AI 공모전
### 주제
서울시 전기차 충전소 입지 선정
2021학년도 서울시립대학교 빅데이터 AI 공모전 출품작입니다.

서울시 공공 데이터에서 전기차 충전소 데이터, 활동 인구 데이터, 동별 데이터 등을 가져와 학습을 진행했습니다.

### 필요성

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/8f84f233-3e40-451e-9e9e-6177e0376628/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/63f350a9-73b0-4a27-a556-7f6dd3469082/Untitled.png)

- 늘어나는 전기차 수요에 비해 부족한 전기차 충전소
- 서울시 추가 설치 계획에 따른 입지 선정

### 데이터셋

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/58efb1a0-c782-4e54-b46d-00d1da65f016/Untitled.png)

---

### 데이터 가공

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/dfbe18f8-ce95-4ffb-a241-16ac0825744b/Untitled.png)

---

**충전기 종류에 따른 분류**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/f8171340-8156-4937-8e7f-f5173dfc220c/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/15698a56-32c2-417e-9e2c-257b5ae56a94/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/b34f52f3-73a1-4528-bf58-0dea623fd346/Untitled.png)

---

**컬럼 용어 설명**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/642936cd-c319-4412-abd6-799b1ce241b2/Untitled.png)

**데이터 가공 - 생활인구**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/f9b4bb74-540d-4872-84ef-b5758cdab880/Untitled.png)

**고속도로 IC 데이터**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/e14d28eb-dcdb-447b-ab5d-35c0c2220a07/Untitled.png)

**가공 완료 데이터셋 (18시~09시)**

![그림1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/68311da3-444d-4526-8a89-3ff93d548a3f/%EA%B7%B8%EB%A6%BC1.png)

**데이터 히트 맵 - feature간 상관계수**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/084b7c3b-0b4f-407d-828a-89fd033cd029/Untitled.png)

**히스토그램**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/af645d7c-a258-45fc-8545-cde135856ddc/Untitled.png)

**주변 동 고려**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/4f14aa97-0958-40dc-b297-22ea9bc3f815/Untitled.png)

**데이터셋 - 주변 동 컬럼 추가**

![그림2.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/9593da8e-41e3-4dee-8676-38a59d9cfd1b/%EA%B7%B8%EB%A6%BC2.png)

**충전기 현황**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/b495f84c-3aef-45bd-bfad-6effa33e7636/Untitled.png)

### 머신러닝

**수식**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/0c609cd9-a6c7-48ca-9c96-ad8378165d13/Untitled.png)

**다중선형회귀 모델 사용**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/46b18180-c727-4a6f-a19c-bc0c1c8ba807/Untitled.png)

**DNN**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/9149fb05-93c7-4282-9d11-32d1f3a955d2/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/fb1986ff-fb14-48ae-bf18-394e8aa06da4/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/b7a81253-3064-494e-9597-fc6cbe1e1c14/Untitled.png)

### 결론

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/6a1ef396-e787-4db9-8e2f-dc28cd360e0b/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/833aedc2-97c6-4760-91bc-2aee665f01fa/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3c3deefb-8fc0-4653-b74a-37ff7e05a156/1d00e672-1a53-4136-a652-ee57f632067a/Untitled.png)

### 출처

**기획재정부 빅3 산업 과제**

https://www.moef.go.kr/com/synap/synapView.do;jsessionid=PtH781oup9lylsEqtSPTa+OF.node40?atchFileId=ATCH_000000000018214&fileSn=3

**생활인구 데이터**

https://data.seoul.go.kr/dataList/OA-14991/S/1/datasetView.do

**전기차 충전소 현황**

https://www.ev.or.kr/mobile/mevmon

**고속도로 데이터**

https://m.map.naver.com/

https://map.kakao.com/
