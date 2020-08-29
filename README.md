# BetaGen
Beta atoms based molecular generation

### demo
* [demo_gen_progress.ipynb](https://github.com/wxx07/BetaGen/blob/master/demo/demo_gen_progress.ipynb) 中展示**配体分子周围的beta原子**，和作为训练样本的**生成过程**
* **配体分子周围的beta原子**：绿色游离的是挑选过的、至少是一个配体原子的最近邻的beta原子
* **生成过程**：按照离配体质心的距离，从内到外的确定性的顺序，生成配体原子；生成的步数是 #配体原子数 - 1
