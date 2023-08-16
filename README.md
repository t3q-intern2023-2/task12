# task12
kc_bert topic modeling

## 폴더 구성

1. documents : 추론할 때 쓰이는 txt 파일 문서

2. report : train data와 validation data json 파일이 있는 폴더, Tokenizer 저장

3. train_result_csv : 학습이 완료된 후, 각 에폭마다 loss, accuracy 값을 csv 파일로 저장하는 폴더

4. plots : 학습이 완료된 후, loss, accuracy 그래프 png 파일로 저장하는 폴더

5. model : 학습이 진행된 체크포인트 저장 폴더, 저장한 체크포인트는 추후 추론에 활용

6. src : 수정한 ratsnlp 패키지가 다운로드되는 폴더

## 파일 구성

1. classification_finetuning.ipynb : 입력 전처리 작업, 체크포인트 모델 만드는 코드 (train, validation)

2. doc_cls_deploy_finetuning.ipynb : 추론 서비스 코드
