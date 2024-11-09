# AI를 활용한 전기차 충전소 입지 선정 연구 (EV-charging-station-selection)
> 2021년도 서울시립대학교 빅데이터 AI 공모전 출품작
> AI 기술을 활용하여 서울시 내 전기차 충전소의 최적 입지를 분석하는 프로젝트입니다. 이 프로젝트는 공공 데이터를 기반으로 하여 충전소 설치 필요성을 평가하고, 효과적인 입지 선정 방법을 제시합니다.
## 프로젝트 개요
서울시의 전기차 충전 인프라는 전기차 수요의 급증에 비해 여전히 부족한 상태입니다. 본 프로젝트는 AI 모델을 통해 최적의 충전소 위치를 추천하여 충전 인프라 확충에 기여하고자 합니다.

### 필요성
![image](https://github.com/user-attachments/assets/fc843618-5dc6-4279-bbe0-2be8b17e000a)
![image](https://github.com/user-attachments/assets/0a7c010b-42ab-42ec-ac97-8ddeb67f1bc2)

- 늘어나는 전기차 수요에 비해 부족한 전기차 충전소
- 서울시 추가 설치 계획에 따른 입지 선정

### 사용 데이터 셋
다양한 공공 데이터셋을 수집 및 가공하여 모델 학습에 활용했습니다. 주요 데이터는 다음과 같습니다.

![image](https://github.com/user-attachments/assets/48240ed8-bc6c-45e0-879f-e4d4deb2b6e5)

- **충전소 위치 데이터**: 현재 운영 중인 충전소의 위치와 이용 현황을 포함합니다.
- **인구 밀도 및 차량 등록 수**: 각 지역의 인구 통계와 전기차 등록 대수를 기반으로 수요를 분석합니다.
- **도로 네트워크 데이터**: 접근성을 평가하기 위해 주요 도로와 교통량 데이터를 수집하였습니다.
- **상업 시설 밀집도**: 충전소 설치의 편리성을 높이기 위해 상업 시설 분포를 고려했습니다.


---

### 데이터 처리 및 가공

![image](https://github.com/user-attachments/assets/fcf1d746-5c0b-44d2-b5bf-84613a5f5829)
- **데이터 전처리**: 결측값 처리, 데이터 정규화 등을 통해 모델 학습에 적합한 형태로 데이터를 가공합니다.
- **공간 데이터 처리**: 충전소와 주요 위치 데이터를 GIS 좌표로 변환하여, 지리적 분석이 가능하도록 구성합니다.
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

## AI 모델링
프로젝트에서는 다중 선형 회귀와 K-평균 군집화를 통해 충전소 최적 입지를 예측합니다.

- **다중 선형 회귀 분석**: 충전소의 이용 빈도와 관련된 요인을 분석하여, 입지 선정에 필요한 기준을 수립합니다.
- **K-평균 군집화**: 군집화를 통해 전기차 수요가 높은 지역을 구분하고, 각 군집에 최적의 충전소 입지를 선정합니다.

**수식**

![image](https://github.com/user-attachments/assets/4f7dc943-c08c-4dc9-be02-99cc26c092fd)

**다중선형회귀 모델 사용**

![image](https://github.com/user-attachments/assets/37552882-5529-419e-925a-72d69f2e8ab9)

**DNN**

![image](https://github.com/user-attachments/assets/57b912c0-b9c4-49dd-a478-356dc41295ab)

![image](https://github.com/user-attachments/assets/19b921d5-ea09-40e6-b34a-5cad180ad226)

![image](https://github.com/user-attachments/assets/bc244457-17a6-4f02-848e-4fb03f018606)

## 결론 및 시각화
AI 모델이 추천한 최적 입지를 시각화하여, 각 지역의 충전소 필요성을 한눈에 볼 수 있도록 제공했습니다. 결과 시각화는 충전소 이용량, 인구 밀집도 등 다양한 요인을 반영하여 직관적으로 표현됩니다.

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
