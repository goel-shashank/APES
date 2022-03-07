<h1 align="center">
  <img alt="Ape Logo" src="https://github.com/goel-shashank/APES/blob/main/docs/img/logo.png" width="224px"/><br/>
  Automated Prompt Engineering for Stereotype 
  <br/>detection in language models
</h1>
<p align="center">APES is an automated dataset generation benchmark for prompt engineering using custom templates<br/> for measuring social biases and robustness of language models</p>

<p align="center"><img src="https://img.shields.io/badge/license-apache_2.0-red?style=for-the-badge&logo=none" alt="license" /></p>
<p align="center"><i>If biases are baked into models such as <b>GPT-3</b> and <b>BERT</b>, they may infect applications built on top of them. For example, a recent study by <b>Stanford HAI researchers</b> involved teaching <b>GPT-3</b> to compose stories beginning with the phrase <b>“Two &ltreligion&gt men walk into a . . .”</b>. 66% of the text the model provided involved violent themes, far higher percentage for some groups compared to other groups.</i></p>

## ⚡️ Setup
First, [download](https://www.python.org/downloads/) and install **Python**. Version `3.0` or higher is required.
> If you're looking for the **latest** version for Python, you can find it [here](https://www.python.org/ftp/python/3.10.2).

Next, install **pip** from [here](https://pip.pypa.io/en/stable/installation/).
Install the requirements for this repository using the following command:

```go
$ pip install -r requirements.txt
```

--- 

## Table of contents[![](./docs/img/pin.svg)](#table-of-contents)
1. [Social Biases](#social-biases)
    - [Disability](#disability)
    - [Gender](#gender)
    - [Race](#race)
    - [Religion](#religion)
2. [Prompt Engineering](#prompt-engineering)
3. [Generating Predictions](#generating-predictions)
4. [Visualizations](#visualizations)
    - [Bias](#bias)
    - [Robustness](#robustness)
5. [Examples](#examples)
    - [Disability](#disability-1)
    - [Gender](#gender-1)
    - [Race](#race-1)
    - [Religion](#religion-1) 
6. [Project Assistance](#project-assistance)

---

## Social Biases[![](./docs/img/pin.svg)](#social-biases)

<!-- We present templates that capture such stereotypes and estimate the bias that crept into the models due to skewed training data. -->
### Disability[](#disability)
NLP models have shown unintended biases against other historically marginalized groups, but biases with respect to different disability groups have been understudied. Over a billion people (about 15 percent of the world's population) are disabled, and disability is sometimes associated with strong negative social biases. Previous studies have found implicit and explicit prejudices against people with disabilities among social group members, reflected in the NLP data and, consequently, in NLP models. 
### Gender[](#gender)
Prejudice or bias towards one gender over the other is called gender bias. Numerous studies have shown, multiple parts of a Natural Language Processing system exhibit gender bias, like training data, resources, pretrained models (like word embeddings), and algorithms themselves. Oftentimes, NLP systems that contain bias in any one of these parts can lead to gender-biased predictions, and even amplify the bias in the training data.
### Race[](#race)
NLP systems are used by multiple public institutions worldwide for critical assessment. Racially biased systems threaten their promise to make governments more sensitive and responsive to citizens' concerns. Particularly considering the racial inequities in many states, racial bias in NLP risks deepening tensions and perpetuating the feeling that many people of color share that government does not represent them. Recent studies have detected racial bias in NLP model pipelines: data, data labels, models, model outputs, as well as social analyses of the outputs. As a result, NLP perpetuates harmful biases that are racialized and fail to create inclusive systems free of false and harmful stereotypes.
### Religion[](#religion)
Previously, researchers primarily explored the undesirable biases learned by language models focusing on racial and gender stereotypes but more recently, studies have reported that religion bias is also prevalent. In their studies, they measured the associations and stereotypes learned by a language model, including examples of anti-Muslim or Islamophobic sentiment. This anti-Muslim bias appears repeatedly and creatively in different uses of the model, and it is more severe even when compared to biases against other religions.

**As part of this study, we present templates that capture such stereotypes and estimate the bias that crept into the models due to skewed training data.**

---

## Prompt Engineering[![](./docs/img/pin.svg)](#prompt-engineering)

---

## Generating Predictions[![](./docs/img/pin.svg)](#generating-predictions)

---

## Visualizations[![](./docs/img/pin.svg)](#visualizations)

### Bias[](#bias)
<a href="/plots/bias.png"><img src="/plots/bias.png" alt="Bias Visualizations" style="width:60%;height:60%"/></a><br>

### Robustness[](#robustness)
<a href="/plots/robustness.png"><img src="/plots/robustness.png" alt="Robustness Visualizations" style="width:60%;height:60%"/></a><br>

---

## Examples[![](./docs/img/pin.svg)](#examples)

### Disability[](#disability-1)
https://user-images.githubusercontent.com/39986265/156995089-07ab233a-b15d-4dbd-8e21-6e91f7abcdd6.mp4

### Gender[](#gender-1)
https://user-images.githubusercontent.com/39986265/156996716-8cca702a-a5d3-4a0f-bd94-cb09ffa5861f.mp4

### Race[](#race-1)
https://user-images.githubusercontent.com/39986265/156997541-c7f8e3bb-3c71-410b-b08d-60a75d14a8fe.mp4

### Religion[](#religion-1)
https://user-images.githubusercontent.com/39986265/156997963-7c0e1ee8-0fa3-4f0e-b5d9-a87af0274ec3.mp4

---

## Project Assistance[](#project-assistance--)
If you want to support the active development of `APES`:

- Add a [GitHub Star] ⭐️ (https://github.com/goel-shashank/APES/) to the project.
- Please contribute interesting templates that can be useful for our dataset by filling this [google form]().

Together, we can **improve** this project every day! 🤗 

---

## Licensing ⚠️[](#licensing--)
`APES` is free and open-source software licensed under the [Apache 2.0 License](https://github.com/goel-shashank/APES/blob/main/LICENSE).
