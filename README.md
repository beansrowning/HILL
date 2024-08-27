# HILL: Hierarchy-aware Information Lossless Contrastive Learning for Hierarchical Text Classification

Official implementation for NAACL 2024 paper "HILL: Hierarchy-aware Information Lossless Contrastive Learning for Hierarchical Text Classification". [[arXiv](https://arxiv.org/abs/2403.17307)]

## Installation Guide

Due to some complexities with how torch-sparse and torch-scatter are packaged, PyTorch must be installed *first*, followed by torch-scatter and torch-sparse, then the remainder of the package.

Don't shoot the messenger.

```sh
pip install torch # use install steps here to determine CPU/GPU/CUDA requirements: https://pytorch.org/get-started/locally/
pip install torch-scatter torch-sparse -f https://data.pyg.org/whl/torch-2.4.0+${CUDA}.html
# where ${CUDA} should be replaced by either cpu, cu118, cu121, or cu124 depending on your PyTorch installation.
pip install git+https://github.com/beansrowning/HILL.git
```

## Data preparation

Please manage to acquire the original datasets and then run these scripts.

#### Web Of Science (WOS)

The original dataset can be acquired freely in the repository of [HDLTex](https://github.com/kk7nc/HDLTex). Please download the release of **WOS-46985(version 2)**, open `WebOfScience/Meta-data/Data.xls` and convert it to `.txt` format (Click "Save as" in Office Excel). Then, run:

```
cd ./data/wos
python preprocess_wos.py
python data_wos.py
```

#### RCV1-v2

The preprocessing code could refer to the [repository of reuters_loader](https://github.com/ductri/reuters_loader) and we provide a copy here. The original dataset can be acquired [here](https://trec.nist.gov/data/reuters/reuters.html) by signing an agreement. 

```
cd ./data/rcv1
python preprocess_rcv1.py
python data_rcv1.py
```

#### NYTimes (NYT)

The original dataset is available [here](https://catalog.ldc.upenn.edu/LDC2008T19) for a fee. 

```
cd ./data/nyt
python data_nyt.py
```

## Train

Hyper-parameters need to be specified through the commandline arguments. Please refer to our paper for the details of how we set the hyper-parameters.

```
usage: train.py [-h] [-d {wos,nyt,rcv1}] [-mn MODEL_NAME] [-n NAME] [-s SEED]
                [-b BATCH_SIZE] [-lr LEARNING_RATE] [-l2 L2_RATE] [-l LAMDA]
                [-f] [--wandb] [-k TREE_DEPTH] [-hd HIDDEN_DIM]
                [-dp HIDDEN_DROPOUT] [-tp {root,sum,avg,max}]
                [-ho {bert,tree,residual,concat}] [-gc {GCN,GAT,GIN}]
                [-gp {sum,avg,max}] [-gl CONV_LAYERS]
                [-go {graph,tree,concat}] [--residual] [--graph]
                [--contrast_loss] [--cls_loss] [--multi_label]
                [--data_dir DATA_DIR] [--ckpt_dir CKPT_DIR]
                [--cfg_dir CFG_DIR] [--begin_time BEGIN_TIME]

optional arguments:
  -h, --help            show this help message and exit
  -d {wos,nyt,rcv1}, --dataset {wos,nyt,rcv1}
                        Dataset.
  -mn MODEL_NAME, --model_name MODEL_NAME
  -n NAME, --name NAME  Name for a specific run.
  -s SEED, --seed SEED  Random seed.
  -b BATCH_SIZE, --batch_size BATCH_SIZE
                        Batch size for training (default: 16).
  -lr LEARNING_RATE, --learning_rate LEARNING_RATE
  -gp {sum,avg,max}, --graph_pooling_type {sum,avg,max}
  -gl CONV_LAYERS, --conv_layers CONV_LAYERS
  -go {graph,tree,concat}, --graph_output {graph,tree,concat}
  --residual
  --graph               Whether use graph encoder.
  --contrast_loss       Whether use contrastive loss.
  --cls_loss
  --multi_label         Whether the task is multi-label classification.
  --data_dir DATA_DIR
  --ckpt_dir CKPT_DIR
  --cfg_dir CFG_DIR
  --begin_time BEGIN_TIME
```

An example of training HILL on Web Of Science:

```
python train.py -d wos -mn hill -s 0 -b 24 -lr 1e-3 -k 3 -l 1e-3 -hd 768 -tp sum
```

## Test

The complete training and testing process is already encapsulated in `train.py`. If you wish to test a checkpoint of the model individually, please run `test.py`.

```
python test.py -n <NAME>  -e {micro, macro}
```

> `<NAME>` should be the same as specified when running train.py

## Citation

If you found the provided code with our paper useful in your work, please **star** this repo and **cite** our paper!

```
@misc{zhu2024hill,
      title={HILL: Hierarchy-aware Information Lossless Contrastive Learning for Hierarchical Text Classification}, 
      author={He Zhu and Junran Wu and Ruomei Liu and Yue Hou and Ze Yuan and Shangzhe Li and Yicheng Pan and Ke Xu},
      year={2024},
      eprint={2403.17307},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
