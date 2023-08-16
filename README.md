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


## 프로젝트 트리 구조
📦task12-main
 ┣ 📂documents
 ┃ ┣ 📜briefing.txt
 ┃ ┣ 📜edit.txt
 ┃ ┣ 📜history.txt
 ┃ ┣ 📜koreabank.txt
 ┃ ┣ 📜meeting.txt
 ┃ ┣ 📜meeting2.txt
 ┃ ┣ 📜meeting3.txt
 ┃ ┣ 📜minute1.txt
 ┃ ┣ 📜news.txt
 ┃ ┣ 📜news2.txt
 ┃ ┣ 📜test05.txt
 ┃ ┣ 📜ti.txt
 ┃ ┗ 📜untitled.txt
 ┣ 📂model
 ┃ ┗ 📜readme.md
 ┣ 📂plots
 ┃ ┣ 📜readme.md
 ┃ ┣ 📜test07_acc_batch512_seq256_epoch79_lr5e-05.png
 ┃ ┗ 📜test07_loss_batch512_seq256_epoch79_lr5e-05.png
 ┣ 📂report
 ┃ ┣ 📜data_frame.ipynb
 ┃ ┣ 📜readme.md
 ┃ ┣ 📜test.json
 ┃ ┗ 📜train.json
 ┣ 📂src
 ┃ ┣ 📂ratsnlp
 ┃ ┃ ┣ 📂nlpbook
 ┃ ┃ ┃ ┣ 📂classification
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜arguments.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜argumentsCopy1.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜corpus.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜deploy.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜task.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┣ 📜arguments.py
 ┃ ┃ ┃ ┃ ┣ 📜corpus.py
 ┃ ┃ ┃ ┃ ┣ 📜deploy.py
 ┃ ┃ ┃ ┃ ┣ 📜task.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📜data_utils.py
 ┃ ┃ ┃ ┣ 📜metrics.py
 ┃ ┃ ┃ ┣ 📜trainer.py
 ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜readme.md
 ┃ ┗ 📜requirements.txt
 ┣ 📂train_result_csv
 ┃ ┣ 📜loss_acc_info_batch512_seq256_epoch79_lr5e-05_test07.csv
 ┃ ┗ 📜readme.md
 ┣ 📜.gitignore
 ┣ 📜classification_finetuning.ipynb
 ┣ 📜doc_cls_deploy_finetuning.ipynb
 ┣ 📜LICENSE
 ┣ 📜README.md
 ┣ 📜requirements.txt
 ┣ 📜setup.py
 ┗ 📜summary.pdf
