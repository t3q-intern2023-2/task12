# task12
kc_bert topic modeling

## Introduce

PyTorch Trainer와 Pretrain된 KcBERT 기반 ratsgo-nlp 실습코드를 AI-hub에서 제공해주는 요약문 및 레포트 생성 데이터를 이용해 Finetuning하고 문서 형식을 분류해주는 서비스

## 폴더 구성

1. documents : 추론할 때 쓰이는 txt 파일 문서

2. report : train data와 validation data json 파일이 있는 폴더, Tokenizer 저장

3. train_result_csv : 학습이 완료된 후, 각 에폭마다 loss, accuracy 값을 csv 파일을 저장하는 폴더

4. plots : 학습이 완료된 후, loss, accuracy 그래프 png 파일을 저장하는 폴더

5. model : 학습이 진행된 체크포인트 저장 폴더, 저장한 체크포인트는 추후 추론에 활용

6. src : 수정한 ratsnlp 패키지가 다운로드되는 폴더

## 파일 구성

1. classification_finetuning.ipynb : 입력 전처리 작업, 체크포인트 모델 만드는 코드 (train, validation)

2. doc_cls_deploy_finetuning.ipynb : 추론 서비스 코드

3. Summary.pdf : task12에 대한 내용 개요

```bash
task12-main
└── task12-main
    ├── .gitignore
    ├── classification_finetuning.ipynb
    ├── documents
    │   ├── briefing.txt
    │   ├── edit.txt
    │   ├── history.txt
    │   ├── koreabank.txt
    │   ├── meeting.txt
    │   ├── meeting2.txt
    │   ├── meeting3.txt
    │   ├── minute1.txt
    │   ├── news.txt
    │   ├── news2.txt
    │   ├── test05.txt
    │   ├── ti.txt
    │   └── untitled.txt
    ├── doc_cls_deploy_finetuning.ipynb
    ├── LICENSE
    ├── model
    │   └── readme.md
    ├── plots
    │   ├── readme.md
    │   ├── test07_acc_batch512_seq256_epoch79_lr5e-05.png
    │   └── test07_loss_batch512_seq256_epoch79_lr5e-05.png
    ├── README.md
    ├── report
    │   ├── data_frame.ipynb
    │   ├── readme.md
    │   ├── test.json
    │   └── train.json
    ├── requirements.txt
    ├── setup.py
    ├── src
    │   ├── ratsnlp
    │   │   ├── nlpbook
    │   │   │   ├── classification
    │   │   │   │   ├── arguments.py
    │   │   │   │   ├── corpus.py
    │   │   │   │   ├── deploy.py
    │   │   │   │   ├── task.py
    │   │   │   │   ├── __init__.py
    │   │   │   │   └── __pycache__
    │   │   │   ├── data_utils.py
    │   │   │   ├── metrics.py
    │   │   │   ├── trainer.py
    │   │   │   ├── utils.py
    │   │   │   └── __init__.py
    │   │   └── __init__.py
    │   ├── readme.md
    │   └── requirements.txt
    ├── summary.pdf
    └── train_result_csv
        ├── loss_acc_info_batch512_seq256_epoch79_lr5e-05_test07.csv
        └── readme.md

```
