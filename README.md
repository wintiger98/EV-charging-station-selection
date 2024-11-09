# EV-charging-station-selection
## 2021년도 서울시립대학교 빅데이터 AI 공모전
### 주제
서울시 전기차 충전소 입지 선정
2021학년도 서울시립대학교 빅데이터 AI 공모전 출품작입니다.

서울시 공공 데이터에서 전기차 충전소 데이터, 활동 인구 데이터, 동별 데이터 등을 가져와 학습을 진행했습니다.

### 필요성
![image](https://github.com/user-attachments/assets/fc843618-5dc6-4279-bbe0-2be8b17e000a)
![image](https://github.com/user-attachments/assets/0a7c010b-42ab-42ec-ac97-8ddeb67f1bc2)

- 늘어나는 전기차 수요에 비해 부족한 전기차 충전소
- 서울시 추가 설치 계획에 따른 입지 선정

### 데이터셋
![image](https://github.com/user-attachments/assets/48240ed8-bc6c-45e0-879f-e4d4deb2b6e5)

---

### 데이터 가공
![image](https://github.com/user-attachments/assets/fcf1d746-5c0b-44d2-b5bf-84613a5f5829)

---

**충전기 종류에 따른 분류**
![image](https://github.com/user-attachments/assets/c98a65ad-38ea-4b78-83aa-36f05fb61f27)
![image](https://github.com/user-attachments/assets/753d35c9-52b1-44a5-926b-3a07955bcb51)
![image](https://github.com/user-attachments/assets/1f7ec2ae-26e5-4289-aa0a-6df5a2618650)

---

**컬럼 용어 설명**

![image](https://github.com/user-attachments/assets/2132f939-b9ba-4c5d-abf8-128c559d001c)

**데이터 가공 - 생활인구**

![image](https://github.com/user-attachments/assets/b5a414ae-35d4-4f11-a924-0f236c812acc)

**고속도로 IC 데이터**

![image](https://github.com/user-attachments/assets/9751d22d-c985-49af-af8f-a335a79cf27f)

**가공 완료 데이터셋 (18시~09시)**

![image](https://github.com/user-attachments/assets/76e73109-72d0-4280-ab0e-b13d664cebaa)

**데이터 히트 맵 - feature간 상관계수**

![image](https://github.com/user-attachments/assets/9abb370f-2320-4dd8-bcb6-7b7057542c44)

**히스토그램**

![image](https://github.com/user-attachments/assets/f2c07a0c-b429-4305-8b07-d3fac97421c2)

**주변 동 고려**

![image](https://github.com/user-attachments/assets/f2f00572-f2a7-4b10-b577-8450a176fbe6)

**데이터셋 - 주변 동 컬럼 추가**

![image](https://github.com/user-attachments/assets/79772a90-66ec-4db2-b66b-dbd567dd648f)

**충전기 현황**

![image](https://github.com/user-attachments/assets/8cd46a8c-fc53-4579-afe8-0978cb5eecf8)

### 머신러닝

**수식**

![image](https://github.com/user-attachments/assets/4f7dc943-c08c-4dc9-be02-99cc26c092fd)

**다중선형회귀 모델 사용**

![image](https://github.com/user-attachments/assets/37552882-5529-419e-925a-72d69f2e8ab9)

**DNN**

![image](https://github.com/user-attachments/assets/57b912c0-b9c4-49dd-a478-356dc41295ab)

![image](https://github.com/user-attachments/assets/19b921d5-ea09-40e6-b34a-5cad180ad226)

![image](https://github.com/user-attachments/assets/bc244457-17a6-4f02-848e-4fb03f018606)

### 결론

![image](https://github.com/user-attachments/assets/48c8a121-bda0-4ae0-8995-737def04830d)

![image](https://github.com/user-attachments/assets/305ef3e1-ac8e-4320-a298-f5c21419662c)

![image](https://github.com/user-attachments/assets/c5177def-19ef-4753-80b8-b3a4331c36c9)

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
