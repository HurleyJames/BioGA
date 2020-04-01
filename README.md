# BioGA
![](https://img.shields.io/badge/dynamic/json?color=%231D1B1B&label=Github&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dgithub%26queryKey%3DHurleyJames) ![](https://img.shields.io/badge/dynamic/json?color=%232093DC&label=Twitter&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dtwitter%26queryKey%3DHurleyHuang23) ![](https://img.shields.io/badge/dynamic/json?color=%233FA4DA&label=Telegram&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dtelegram%26queryKey%3DHurleyJames) ![](https://img.shields.io/badge/dynamic/json?color=%23E79437&label=微博&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dweibo%26queryKey%3D5628559861) ![](https://img.shields.io/badge/dynamic/json?color=%23097BE9&label=知乎&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dzhihu%26queryKey%3Dhuang-peng-yuan-91) ![](https://img.shields.io/badge/dynamic/json?color=%23199C59&label=酷安&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dcoolapk%26queryKey%3D795519)  

### What is BEAST

> BEAST is a cross-platform program for Bayesian analysis of molecular sequences using MCMC. It is entirely orientated towards rooted, time-measured phylogenies inferred using strict or relaxed molecular clock models. It can be used as a method of reconstructing phylogenies but is also a framework for testing evolutionary hypotheses without conditioning on a single tree topology. BEAST uses MCMC to average over tree space, so that each tree is weighted proportional to its posterior probability. We include a simple to use user-interface program for setting up standard analyses and a suit of programs for analysing the results.

### Introduction

[BEAST/beast](BEAST/beast)中包含整个项目运行的BEAST源码（注意：代码需运行在配置好BEAST环境的操作系统中）。

[BEAST/Mice](BEAST/Mice)中包含了运行Mice模拟器结果处理过程，通过收集log日志的数据，用Pthon文件处理数据并绘制图片。`.txt`文件是收集的数据，`.png`文件是绘制的图片，`mouse_fitness.cc`和`mouse_network.cc`和`mouse_proximity.cc`是分别使用了不同的`Fitness`函数，神经网络和传感器后的`mouse.cc`源文件。

[BEAST/Chase](BEAST/Chase)中包含了运行10、50、100、4000、14000代的数据以及Prey和Predator的折线图。

[BEAST/doc](BEAST/doc)包括了对整个项目的配置与使用方法，可以访问[BEAST - Bioinspired Evolutionary Agent Simulation Toolkit Documentation](http://hurley.fun/download/bio)进行在线阅读。

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>

本作品采用<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">知识共享署名 4.0 国际许可协议</a>进行许可。