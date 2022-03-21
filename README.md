# Project: Weakly supervised learning-- label noise and correction


### [Full Project Description](doc/project3_desc.md)

Term: Spring 2022

+ Team #1
+ Team members
	+ Aakanksha Agaewal
	+ Lichun He
	+ Kexin Tang
	+ Kaimin Wang
	+ Xinran Wang
	+ Jiaxin Yu

+ Project summary: 
        + For model 1, we first built predicting models including VGG19, ResNet, CNN and Vision Transformer to compare the running time and the validation accuracy. taking the noisy labels as clean ones, the sophisticated models all performed relatively better than the baseline model. ResNet showed that the validation accuracy was 45.76%, although it took 155 mins to run which failed to meet our requirement.The vision transformer model provided 43.86% accuracy with 1 min's running time. As for CNN, the validation accuracy was 43.36% with 12 mins' running time. The model with the best performance is VGG19, which gave us 60.34% accuracy with 13.32 mins' running time.
	
+ Contribution statement: 

Following [suggestions](http://nicercode.github.io/blog/2013-04-05-projects/) by [RICH FITZJOHN](http://nicercode.github.io/about/#Team) (@richfitz). This folder is orgarnized as follows.

```
proj/
├── lib/
├── data/
├── doc/
├── figs/
└── output/
```

Please see each subfolder for a README file.
