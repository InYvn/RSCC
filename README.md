<h1 align="center">
RSCC: A Rule-Based Soft Compression Multi-Agent Framework for
Efficient Code Generation in Large-Scale Software Projects
</h1>
<p align="center">
<img src="https://img.shields.io/badge/OS-Ubuntu22.4-blue" />
<img src="https://img.shields.io/badge/Python-3.10-red" />
<img src="https://img.shields.io/badge/Build-Success-green" />
<img src="https://img.shields.io/badge/License-BSD-blue" />
<img src="https://img.shields.io/badge/Release-0.1-blue" />
</p>

<p align="center">
<img src="doc/png/fig.codeagents.png" width=80%/> <br>
<b>Figure 1</b>. Structure of RSCC.
</p>


## Conda Enviroment Setup

``` shell
conda create -n RSCC python=3.10
conda activate RSCC
# CUDA 12.1
conda install pytorch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 pytorch-cuda=12.1 -c pytorch -c nvidia
# OR CUDA 11.8
# conda install pytorch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 pytorch-cuda=11.8 -c pytorch -c nvidia
# OR CPU Only
# conda install pytorch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 cpuonly -c pytorch
pip install packaging
pip install transformers==4.34.0 datasets==2.13.4 accelerate==0.24.1 sentencepiece==0.1.99 flash-attn==2.3.5 wandb
# Flash rotary embeddings (requires setting correct CUDA_HOME variable)
pip install git+https://github.com/Dao-AILab/flash-attention.git#subdirectory=csrc/rotary
```

## Usage
### 1. Move the code of the large project to the directory '/RSCC/large_scale_project'
### 2. Run the program using the following command
```python
python startup.py
```

