# Biological visualization

### Requirement
> **Python2.7**: numpy,matplotlib,math,csv,seaborn,matplotlib_venn, random

> **R**: ggplot2
	

### Structure
Recommend you to organize your project like this tree.

```
.
├── README.md
├── __init__.py
├── input.json		默认输入json,
├── run.sh			调用格式
├── biov.py			主程序入口
├── charts.csv		demo配置表
├── config			
│   ├── __init__.py
│   ├── charts.csv		支持图库路径
│   └── config.py		程序配置
├── charts				图库主目录
│   ├── __init__.py
│   ├── others
│   │   └── __init__.py
│   ├── python
│   │   ├── __init__.py
│   │   └── matplotlib
│   │       ├── __init__.py
│   │       ├── bar.py
│   │       ├── bargroup.py
│   │       ├── barh.py
│   │       ├── barstacked.py
│   │       ├── contour3d.py
│   │       ├── errorbar.py
│   │       ├── histogram.py
│   │       ├── histogramh.py
│   │       ├── histsf.py
│   │       ├── histub.py
│   │       ├── pie.py
│   │       ├── piedisassemble.py
│   │       ├── radar.py
│   │       ├── venn.py
│   │       ├── violin.py
│   │       └── violinh.py
│   └── r
│       ├── __init__.py
│       └── ggplot2
│           ├── __init__.py
│           └── geom_dotplot.py
├── output			默认输出路径（此文件夹下文件写入.gitignore）
├── data			建议test data路径（此文件夹下文件写入.gitignore）
│   ├── Rplots.pdf
│   ├── SOAPfuse-S09-3D-pillar-dist.pl
│   ├── VirusIntg.SamplesHaplotype.MechStat.pl
│   ├── cc\ 11.00.09\ PM.svg
│   ├── mtcars.R
│   ├── mtcars.csv
│   └── virus.svg
├── sample_data			图库示例：示例数据
│   ├── bar.csv
│   └── ...
├── sample_detail			图库示例：图片说明
│   ├── bar.txt
│   └── ...
├── sample_img			图库示例：图片示例
│   ├── bar.svg
│   └── ...
└── sample_json			图库示例：输入json示例
    ├── bar.json
    └── ...

```
Updated at 2016/09/06, 10:35 AM
