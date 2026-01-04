# mooc-coldstart-session-meta

Research project: cold-start session-based recommendation with MOOCs as the target domain, comparing scratch vs transfer vs meta-learning.

## Non-negotiable rules
- Only real datasets and real results produced by this repo.
- No synthetic/toy/example data.
- If something is unknown: write “we don’t know yet”.
- Every step must be reproducible and reviewer-defensible.
- Work proceeds notebook-by-notebook with clear logging.

## Repo structure
- `notebooks/` : numbered notebooks (00..14)
- `src/`       : reusable python modules used by notebooks
- `configs/`   : yaml/json configs
- `data/`      : local datasets (ignored by git)
- `runs/`      : outputs, metrics, checkpoints (ignored by git)
- `reports/`   : tables/plots for paper (ignored by git)



```
mooc-coldstart-session-meta
├─ configs
│  └─ project.yaml
├─ data
├─ LICENSE
├─ meta.json
├─ notebooks
│  ├─ 00_project_overview.ipynb
│  ├─ 01_eda_source_mooc.ipynb
│  ├─ 01_eda_source_mooc_UPDATED.ipynb
│  ├─ 02_eda_target_mooc.ipynb
│  ├─ 03_schema_normalization.ipynb
│  ├─ 04_session_gap_and_timeline_analysis.ipynb
│  ├─ 05A_split_prefix_target.ipynb
│  ├─ 05B_build_tensor_dataset_target.ipynb
│  ├─ 05C_source_train_val_test_split_sessions.ipynb
│  ├─ 05_sessionize_and_prefix_target.ipynb
│  ├─ 06_data_loader_and_eval_protocol.ipynb
│  ├─ 07_mostpop_baseline.ipynb
│  ├─ 08_session_knn_baseline.ipynb
│  ├─ 09_gru4rec_baseline.ipynb
│  ├─ 10_sasrec_baseline.ipynb
│  ├─ 11A_transfer_pretrain_source.ipynb
│  ├─ 11B_transfer_finetune_target.ipynb
│  ├─ 12A_task_builder_for_meta.ipynb
│  └─ 12B_meta_train_on_source.ipynb
├─ README.md
├─ requirements.lock.txt
├─ requirements.txt
└─ src
   ├─ configs
   │  └─ project.yaml
   ├─ utils
   │  ├─ repro.py
   │  ├─ runlog.py
   │  └─ __init__.py
   └─ __init__.py

```