---
title: "Powerful Technologies and Their Power Laws: Estimating Machine Learning Systems' Data Leverage Vulnerabilities"
person: "nick-vincent"
section: "by"
type: "essay"
year: 2021
date: "2021-04-01"
venue: "Observable Notebook"
authors: "Nick Vincent"
source_url: "https://observablehq.com/d/685789015c21cd9a"
retrieved: "2026-08-13"
content: "full-text"
notes: "Executable Observable notebook; retrieved via the Observable document API. Prose cells are reproduced verbatim; code cells are included in fenced blocks. Interactive charts are not reproducible as text."
---

# Powerful Technologies and Their Power Laws: Estimating Machine Learning Systems' Data Leverage Vulnerabilities

## Full text (notebook prose and code cells)

# Powerful Technologies and Their Power Laws: Estimating Machine Learning Systems' Data Leverage Vulnerabilities 


A brief summary: Machine learning (ML) research on ["learning curves"](https://scikit-learn.org/stable/modules/learning_curve.html#learning-curve) – which show how ML systems' performance measurements vary with training data size – and ["scaling laws"](https://arxiv.org/abs/1712.00409) – which aim to explain the nature of learning curves – can tell us about how effectively data leverage tactics like "data strikes" and "conscious data contribution" (CDC) can harm (in the case of strikes) or help (in the case of contribution) an organization's technologies, and ultimately give the public leverage over tech companies and other organizations deploying ML.


For an overview of data leverage, see this [article](https://www.technologyreview.com/2021/03/05/1020376/resist-big-tech-surveillance-data/) or this ["round-up" document](https://github.com/nickmvincent/DataLeverageRoundup). 

See this recent effort to compile a spreadsheet of scaling laws: https://docs.google.com/spreadsheets/d/1XHU0uyCojH6daSWEq9d1SHnlrQVW7li8iqBMasawMns/edit




```js
import {toc} from "@mbostock/toc"
```

```js
toc()
```


## Figure 1. Data Leverage Power for Power Laws


```js
{
  const svg = d3.select(DOM.svg(width, height));                       
  
  svg.append("rect")
    .attr("width", "100%")
    .attr("height", "100%")
    .attr("class", "svgBackground");
  
  svg.append('g').call(xAxis)
  
  
  if (addAxis !== "None") {
    svg.append('g').call(obsAxis);
  } else {
    svg.append('text')
    .attr("x", width/2 - margin.left/2).attr("y", height - 10)
    .text(`Participation Fraction (${niceStr})`);
  }
  
  svg.append('g').call(yAxis);
  svg.append('text')
    .attr("x",20).attr("y", height/2)  
    .attr("font-size",14)
    .text("Data Leverage Power");
  
  if (annotate) {
    let topText, bottomText;
    if (mode == 'strike'){
      topText = 'LargeCo hits worst-case performance';
      bottomText = 'LargeCo with best-case performance';
    } else {
      topText = 'SmallCo hits best-case performance';
      bottomText = 'SmallCo with worst-case performance';
    }
    svg.append('text')
      .attr("x",5).attr("y", 0+ margin.top)
      .attr("fill","darkgray")
      .attr("font-size",10)
      .text(topText);

    svg.append('text')
      .attr("x",5).attr("y", height-margin.bottom)
      .attr("font-size",10)
      .attr("fill","darkgray")
      .text(bottomText);
  }
  
  
  svg.append('g').call(lossAxis)
  svg.append('text')
    .attr("x",width - margin.right + 40).attr("y", height/2)
    .text(rightLabel);
  
  
  // Draw the line.
  svg.append('path')
      .datum(data)
      .attr('d', line);
  
    
  svg.append('g').call(crosshairVertical);
  svg.append('g').call(crosshairHorizontal);
    
  if (annotate) {
    let fromLeftColor, fromRightColor, fromLeftY, fromRightY;
    if (mode == 'strike') {
      fromLeftColor = "firebrick"; // strike from the left
      fromRightColor = "darkslateblue";
      fromLeftY = boundY(yScale(curScore) - 60);
      fromRightY = boundY(yScale(curScore) - 120);
    } else {
      fromLeftColor = "darkslateblue"; // CDC from left
      fromRightColor = "firebrick";
      
      fromLeftY = boundY(yScale(curScore) + 60);
      fromRightY = boundY(yScale(curScore) - 60);
          
    }
    const rightTextY = boundY(fromRightY) - 20;
    const leftTextY = boundY(fromLeftY) + 20;
    
    svg.append("line") // annotation line from comes from the left
    .attr("x1", `${margin.left}`)
    .attr("x2", xScale(chosenFrac))
    .attr("y1", fromLeftY)
    .attr("y2", fromLeftY)
    .style("stroke", fromLeftColor)
    .style("stroke-width", 2)
    .style("stroke-dasharray", ("6, 6"));

    svg.append("line") // annotation line from comes from the right
    .attr("x1", xScale(chosenFrac))
    .attr("x2", `${width-margin.right}`)
    .attr("y1", fromRightY)
    .attr("y2", fromRightY)
    .style("stroke", fromRightColor)
    .style("stroke-width", 2)
    .style("stroke-dasharray", ("6, 6"));
    
    const leftTextX = boundX(xScale(chosenFrac)+10);
    const leftText = leftAnnotation;
    svg.append("text")
    .attr("x", leftTextX).attr("y", leftTextY)
    .attr("class", "annotate")
    .text(leftText);

    const rightTextX = boundX(xScale(chosenFrac)+10);
    const rightText = rightAnnotation;
    svg.append("text")
    .attr("x", rightTextX).attr("y", rightTextY)
    .attr("class", "annotate")
    .text(rightText);
  }
  
  return svg.node();
}
```


**Fraction of contributors who participate** (click or drag):


```js
viewof i = Scrubber(fracs, {autoplay: false, loop: false, delay: 25}) //viewof percent = Range([0.01, 100], {value: 10, label: "Size"})
```

```js
// uncomment to animate k as well!
//viewof k = Scrubber([...Array(40).keys()].map(x=>(x+1)*0.025), {autoplay: false, alternate: true, delay: 25})
viewof k = Range([0, 1.0], {label: 'Scaling Exponent "α"', value: 0.095})
```

```js
html`
<div>
Currently showing growing <u>${niceStr}</u> from left to right <button onclick=${flip}>Flip Perspective </button></div>
<div>
Use results from prior work:
<button onclick=${loadKMH}>Language Model [KMH+20]</button>
<button onclick=${loadHNA}>Image Classifier [HNA+17]</button>
`
```

```js
viewof annotate = Toggle({label: "Uncheck to remove annotations", value:true})
```


Q: Can you give me an example of why this would be useful?

A: Yes! Imagine you want to use data leverage against LargeCo. You have a limited budget (of money, your time, etc.), so need to decide if you want to focus on helping people join a data strike or engage in CDC. If you can find a rough estimate for the scaling laws of the tech you hope to impact, you can use the power laws to reason about how much a data strike might hurt LargeCo and how much CDC will help SmallCo. If the system has a large scaling coefficient (${tex `\alpha`}), CDC may be extra valuable. Conversely, if the system has a a small scaling coefficient, data strikes may be extra effective. The exact best choice will come down to the specific costs required to get participants. Even relying on rough estimates of the scaling coefficient, the number of people involved, the costs involved, etc., we hypothesize that this approach for thinking about data leverage effectiveness can still be a useful tool.



### More About Figure 1
The above interactive figure shows how we can use scaling laws identified in prior work to estimate the average effectiveness of data strikes and data contribution. If a particular model follows power law dataset size scaling, the above plot can tell us about how effective the average data strike or conscious data contribution campaign of a particular size will be.

Reading from left to right, we can see growing participation in a "conscious data contribution" (CDC) campaign. As participation grows, more people contribute data to a small organization they want to boost up and help compete with incumbents. To make the plot and text easier to follow, we refer to the hypothetical beneficiary of data contribution as "SmallCo" and the hypothetical target of a data strike as "LargeCo"

The left-hand y-axis shows "Data Leverage Power", which is defined to range from 0 to 1. 0 corresponds to worst-case performance (i.e. when an organization has so little data they're better off using an approach like "just guess based on common cases") and 1 corresponds to "best-case" performance (i.e. when an organization has enough data to match the best published performance). The right-hand axis shows the corresponding performance measurement (e.g. error rate, "loss"). On a technical note, the true best-case performance occurs when a model achieves the irreducible "Bayes error" for a particular task, but here we define "best-case" relative to best performance published in prior work. More on this point below.

The first interactive slider lets us look how systems with different "power-law scaling factors" respond differently to data leverage. We call the scaling factor ${tex `\alpha`}. ${tex `\alpha`} corresponds to "data efficiency" (a larger value of ${tex `\alpha`} means performance grows faster as we add data). The value of ${tex `\alpha`} depends on both the nature of the data being studied as well as choices about how to model the data.

As we'll discuss more below ("The Strike - Contribution Tradeoff") a higher value of ${tex `\alpha`} means a task is stronger against data strikes but weaker to CDC. Press "Play" to animate through a variety of values, or drag the slider to a value you're interested in. For instance, past work suggests an ${tex `\alpha`} of about 0.3 for language models and 0.7 for image classifiers.




By default, the plot shows growing data *contribution* from left to right. As the participation grows, SmallCo gains more data.


However, we can read the plot "backwards" to find an equivalent data strike scenario (see the red dotted line). For instance, when SmallCo receives 10% data contribution, SmallCo the same amount of data as a large company with a experiencing a 90% data strike.

Click the below button to flip this perspective, so that as we travel along the x-axis the amount of data deletion grows (and we can read the plot backwards to find an equivalent data contribution scenario):



If you want to load a Data Leverage plot for a specific model from prior work, you can use the below buttons. Alternatively, keep scrolling to manually set up a hypothetical model yourself.



Use this drop-down menu to add extra info the x-axis. You can show the total number of "observations" (units of training data), or an estimate of total number of people participating (estimated based on an assumed ratio of observations: people):


```js
viewof addAxis = Select(["None", "# Observations", "# People"], {label: "Show # Observations on x-axis"})
```

```js
function setConfig(x){
 const config = configs[x];
 set(viewof D_min, config.D_min);
 set(viewof D_max, config.D_max);
 set(viewof L_0, config.L_0);
 set(viewof k, config.alpha);
 set(viewof samplesPerPerson, config.SPP);
 set(viewof rightLabel, config.loss);
}
```

```js
function loadKMH(){
 setConfig("[KMH+20]LM")
}
```

```js
function loadHNA(){
 setConfig("[HNA+17]Image")
}
```


Set the number of observations contributed per person.


```js
viewof samplesPerPerson = Range([1, 10000], {value:1000}) //obsPerUser = 10 / 1000
```

```js
viewof rightLabel = Text({value: 'Loss'});
```

```js
configs["[KMH+20]LM"]
```


Set the minimum data size, ${tex `D_{min}`} that we will use in Figure 1.

${tex `D_{min}`}:

```js
viewof D_min = Text({value:22e3})
```


Set the maximum data size, ${tex `D_{max}`} that we will use in Figure 1.

${tex `D_{max}`}:


```js
viewof D_max = Text({value:22e6})
```


Set the ${tex `L_0`}, the coefficient that determines loss value when ${tex `D = 1`}.


```js
viewof L_0 = Text({value: 0.0496})
```


Set the irreducible error (Currently unused):


```js
bayesError = 0
```

```js
minObs = Number(D_min)
```

```js
maxObs = Number(D_max)
```

```js
maxUsers = (maxObs / samplesPerPerson).toFixed(0)
```

```js
configs
```

```js
C = Number(L_0)
```


## Power Laws and Why They're Relevant to Data Leverage

In recent work
([[V+21]](https://arxiv.org/abs/2012.09995), [[VH21]](http://www.nickmvincent.com/static/cdc_cscw.pdf)),
we have discussed how knowledge about "learning curves" – plots that describe how machine learning performance depends on training dataset size – can inform us about the efficacy of "data leverage".

For an overview of data leverage, see this [article](https://www.technologyreview.com/2021/03/05/1020376/resist-big-tech-surveillance-data/) or this ["round-up" document](https://github.com/nickmvincent/DataLeverageRoundup). 

In this notebook, we aim to illustrate how research on learning curves and scaling laws can provide insight into how effectively data levers can give the public a louder voice in discussions around the impacts of machine learning and other data-driven technologies. Specifically, we can use learning curves to estimate how much data strikes can hurt an incument and how much data contribution can boost up potential competitors, thus making it more likely tech companies may want to listen to or bargain with the public.

Several recent studies (full list below) with suggest a rather elegant result: in many cases, learning curves follow a very consistent "power law" form. There is particularly strong support for the claim that deep learning systems follow power law learning curves very closely, but this trend appears to hold for other machine learning approaches as well.

Precisely, the relationship between various correlated performance metrics (validation loss, error rate, etc.) ${tex`L`} and training dataset size, ${tex`D`} fits the form 

${tex.block` L = L_0 D^{-\alpha} + \epsilon_b `}

* ${tex`\alpha`} is the data scaling factor.

* ${tex`L_0`} is a case-specific constant that corresponds to worst-case performance (when ${tex`D=1`} and ${tex `\epsilon_b = 0`}, L= ${tex`L_0`}) However, typically by the time we're near ${tex`D=1`}, we're already in the "low data regime" where our power law is less relevant because we'd rather use a simple guessline like "guess randomly" or "recommend most popular". See [[HNA+17]](https://arxiv.org/abs/1712.00409) for more on the different regimes.

* ${tex`\epsilon_b` } is the irreducible error (often called the "Bayes error"). Some work treats this irreducible error as zero, and finds the power law is still a good fit. [[HNA+17]](https://arxiv.org/abs/1712.00409) explain that we can think of the "high data regime" as separate from the power law regime, explaining why we can get away with ignoring the exact value of the irreducible error and still produce an accurate model.

It is certainly an overstatement to claim power law data scaling is universal, as there is some work that suggests power laws are not always the best fit. See [[VL21]](https://arxiv.org/abs/2103.10948) for an overview.



When power laws fit well, we can look at the specific value of ${tex`\alpha`} to determine how much a particular model will suffer as data is lost (e.g. during a data strike or after a data poisoning attack), as well as how easily a new start-up or co-op can create a competitive technology (e.g. using data contributed from a data contribution campaign). In other words, the exact specification of the power law that describes a particular model's learning curve tells about its vulnerability to different data levers. More broadly, we can say that for power law cases the value of ${tex`\alpha`} describes how a particular model trades off between data strike vulnerability and data contribution vulnerability. A small ${tex`\alpha`} means the model scales slowly with data, i.e. is less data efficient, and therefore data strikes are stronger and CDC is waeker. A larger ${tex`\alpha`} means the model scales quickly with data, and therefore is not vulnerable to data strikes, but may be vulnernable to c

For instance, if a data strike causes an existing tech company to lose 10% of their training data, we can imagine D being reduced to ${tex`0.9 D`}.

Alternatively, if a new start-up launches and 10% of users contribute data to that start-up, that start-up has a dataset of size ${tex`0.1 D`}.

In both cases, if we have the power law for a particular system from prior work (i.e. values for ${tex`\alpha, L_0, \epsilon_b`}, we can calculate the expected performance for the incumbent facing a data strike and the start-up benefitting from CDC. This will give us performance in terms of loss. On its own, this is already exciting. Below, we'll discuss briefly how might compare different systems by thinking in terms of "Data Leverage Power".



## Data Leverage Power: Comparing results to "worst-case" and "best-case" performance

In [[VH21]](http://www.nickmvincent.com/static/cdc_cscw.pdf), we  proposed thinking of effects in terms of a measure we called "Data Leverage Power". The idea is compare the changes in performance induced by data strikes and CDC to the best-case and worst-case performancs exhibited for a particular task. We can think of CDC in terms of "how far from worst-case to best-case does performance go" and strikes in terms of "how far from best-case to worst-case does performance go". In other words, we apply min-max normalization based on best-case and worst-case.

Concretely, for CDC, Data Leverage Power (${tex `P`}), which describes "how far from worst-case to best-case does performance go" (so that lower loss means higher DLP) can be expressed as:

${tex.block` P_{contribute} = \frac{L - max(L)}{min(L) - max(L)} `}

For a data strike-only scenario, "how far from best-case to worst-case does performance go" (so that higher loss means higher DLP) can expressed as:

${tex.block` P_{strike} = \frac{L - min(L)}{max(L) - min(L)} `}

Our definition in [[VH21]](http://www.nickmvincent.com/static/cdc_cscw.pdf) also accounts for simulataneous data strike + CDC by replacing ${tex `min(L)`} in the ${tex `P_{contribute}`} equation with ${tex `L(LargeCo)`}, but we do not focus on this scenario in this current draft; because data strikes face diminishing returns, simultaneous data strike + CDC generally has a very similar DLP to CDC only.



A useful property of the DLP definition is that if we consider some fraction of data ${tex `f * D_{max}`}, we see that it's possible to calculate DLP entirely in terms of the fraction ${tex `f`} and the ratio ${tex `r_D = \frac{D_{min}^{-\alpha}}{D_{max}^{-\alpha}}`}

Put another way, if two systems have the same scaling factor and the ratio of maximum dataset size to minimum dataset size is the same, for a given fraction of data, the two systems have the same DLP.

${tex.block` P(f D_{max}) = \frac{L(f D_{max}) - L(D_{max})}{L(D_{min}) - L(D_{max})}  `}


${tex.block` = \frac{L_0(fD_{max})^{-\alpha} + \epsilon_b - (L_0 D_{max}^{-\alpha} + \epsilon_b)}{L_0 D_{min}^{-\alpha} + \epsilon_b - (L_0 D_{max}^{-\alpha} + \epsilon_b)}`}

${tex `L_0`} and ${tex `\epsilon_b`} cancel out completely

${tex.block`  = \frac{(fD_{max})^{-\alpha} - D_{max}^{-\alpha}}{D_{min}^{-\alpha} - D_{max}^{-\alpha}}`}

Pulling out ${tex `D_{max}^{-\alpha}`}

${tex.block`  = \frac{f^{-\alpha} - 1}{\frac{D_{min}^{-\alpha}}{D_{max}^{-\alpha}} - 1} = 
\frac{f^{-\alpha} - 1}{r_D - 1}`}

The above example assumed a power law form for L, but this property holds for any scale-invariant function.



## The Missing Links for Making Data Leverage Predictions for Everything: How Many People Were Involved? How Many People Do You Need?

From what we've presented so far, it seems relatively *easy* to make predictions about data leverage. Could we just start making predictions left and right, and quickly identify cases in which data strikes will be very powerful and cases in which CDC will be very powerful? What's the catch?

A key question we need to answer is, "How are training samples distributed amongst people?" This approach tells us roughly how much performance we would expect to lose/gain when removing/adding a certain amount of data due to strikes/contributions. The problem is: if a strike consists of 1000 people, how many units of data (samples) does that entail? Our approach above (and results in prior work) have tried to avoid this issue by thinking in terms of "fraction of largest possible dataset". But when rubber meets the road, we are going to want to think of data leverage involving specific numbers of people.

Ideally, we'd want data about how data labor is distributed amongst people so we can answer questions like:
* what is the average number of samples that a person contributes
* how many samples does the median contributor contribute
* how unequally are contributions distributed. Is the model actually just memorizing the behaviors or ideas of a few "superstar" contributors?

For instance, an image classifer might be "completed" with hard work from 1000 labelers (though of course, the labels may distributed differently than from another population of 1000 labelers). On the other hand, a recommender system needs data about every individual user in order to serve them recommendations.

In general, many datasets do not keep records of who played a role in generating a particular training sample, and for good reason: this could create some serious privacy nightmares. A notable exception is recommender systems datasets, for which linking an observation to a person is critical. These datasets avoid privacy disasters by generating random user ids for each user so as to anonymize them.

However, just knowing the average number of observations contributed per eligble contributor is adequate for the predictions shown above. Indeed, in this notebook, we make some conservative assumptions about this "observations-per-person" number.

Finally, an important note is that this current notebook does account for the "ruin your own personalization" effect in personalized systems. If you delete all data about *your* preferences, you make 



## Annotated Bibliography

A brief summary of the work we cite in this notebook. Specific results from these papers appear in a table below.

* *[[HNA+17]](https://arxiv.org/abs/1712.00409) Hestness, Joel, Sharan Narang, Newsha Ardalani, Gregory Diamos, Heewoo Jun, Hassan Kianinejad, Md Patwary, Mostofa Ali, Yang Yang, and Yanqi Zhou. "Deep learning scaling is predictable, empirically." arXiv preprint arXiv:1712.00409 (2017).
    - studies four contexts.
    - results are used in [HAD+19]
* *[[HAD19]](https://arxiv.org/abs/1909.01736) Hestness, Joel, Newsha Ardalani, and Gregory Diamos. "Beyond human-level accuracy: Computational challenges in deep learning." In Proceedings of the 24th Symposium on Principles and Practice of Parallel Programming, pp. 1-14. 2019.
    - Builds off [HNA+17]

* *[[KMH+20]](https://arxiv.org/abs/2001.08361) Kaplan, Jared, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. "Scaling laws for neural language models." arXiv preprint arXiv:2001.08361 (2020).
    - Focus on neural language models (WebText2)
    - Fig. 1, p.3: ${tex `L  = (D/5.4e13)^{-0.095}; 22e6 < D < 23e9`}
* *[[HHK+20]](https://arxiv.org/abs/2010.14701) Henighan, Tom, Jared Kaplan, Mor Katz, Mark Chen, Christopher Hesse, Jacob Jackson, Heewoo Jun et al. "Scaling laws for autoregressive generative modeling." arXiv preprint arXiv:2010.14701 (2020).
    - mainly focuses on compute and model scaling, but there are results related to dataset size scaling for image models trained on low resolution images. For 16x16 images, ${tex `2013 + (D/ 5.6e+16)^{0.26}`} 
    - Models irreducible loss directly
    - four types of data: generative image modeling, video modeling, multimodal image <-> text modeling, mathematical problem solving. Apply "autoregressive decoder-only Transformer models" (p. 5) to each modality, and use cross entropy loss.
    - information theoretic interpretation of cross entropy loss - "irreducible loss estimates the entropy of the true data distribution, while the reducible loss is an estimate of the KL divergence between the true and model distributions." (p. 4) 

* *[[RRBS2020]](http://arxiv.org/abs/1909.12673) Rosenfeld, Jonathan S., Amir Rosenfeld, Yonatan Belinkov, and Nir Shavit. "A constructive prediction of the generalization error across scales." arXiv preprint arXiv:1909.12673 (2019).
    - provide a general function that includes data size and model size (but we can simplify to a function of data size only). 
    - See e.g. for CIFAR100, "(n^-.7 + .71)/ (sqrt((n^-.7 +.71)^2 + 6.93^2)), (n^-.7 + .7063) / 6.93, n 0 to 60000"
    - Language models + Image classification
    - Somewhat surprising finding: ${tex `\alpha`} values are almost all greater than 0.5. Contrast with [HAD19], which suggests ${tex `\alpha < 0.5`}. Worth looking into more!
* *[[BDKL+21]](https://arxiv.org/abs/2102.06701) Bahri, Yasaman, Ethan Dyer, Jared Kaplan, Jaehoon Lee, and Utkarsh Sharma. "Explaining Neural Scaling Laws." arXiv preprint arXiv:2102.06701 (2021).
    - Image classification (CIFAR-10, CIFAR-100, MNIST, Fashion MNIST)

* [[HKHM+21]](https://arxiv.org/abs/2102.01293) Hernandez, Danny, Jared Kaplan, Tom Henighan, and Sam McCandlish. "Scaling Laws for Transfer." arXiv preprint arXiv:2102.01293 (2021).
    - Considers the context of transfer learning for language models. Power laws for data scaling hold.

* [[JT9]](https://www.aeaweb.org/doi/10.1257/aer.20191330) Jones, Charles I., and Christopher Tonetti. "Nonrivalry and the Economics of Data." American Economic Review 110, no. 9 (2020): 2819-58.
    - discuss [HNA+17] directly, and particularly talk about translating error rate -> productivity

* [[VL21]](https://arxiv.org/abs/2103.10948) Viering, Tom, and Marco Loog. "The Shape of Learning Curves: a Review." arXiv preprint arXiv:2103.10948 (2021).
    - extensive review of learning curve research (including above work)

* Frey, Lewis J., and Douglas H. Fisher. "Modeling decision tree performance with the power law." In Seventh International Workshop on Artificial Intelligence and Statistics. PMLR, 1999.
    - "By characterizing the learning curve with a power law, the error rate for a given size training set can be projected"
    - http://proceedings.mlr.press/r2/frey99a.html


Below, we present specific details from each model studied in prior work in tabular form. 


```js
priorWork = [
  {
    'Paper': '[HNA+17]', Task: 'Translation', 'Data': '', alpha: 0.30, D_min: 0, D_max: '2^27', 
    'units': 'Tokens', L_0, 'Source': 'p6, Figure 1',  loss: 'Loss', SPP: '', Notes: ''
  },
  {
    'Paper': '[HNA+17]', Task: 'LM (word)', 'Data': '', alpha: 0.065, D_max: '2^27', 
    'units': 'Words', 'Source': 'p7, Figure 2',
  },
  {
    'Paper': '[HNA+17]', Task: 'LM (char)', 'Data': '', alpha: 0.095, D_max: '2^27', 
    'units': 'Chars',  'Source': 'p8, Figure 3'
  },
  {
    'Paper': '[HNA+17]', Task: 'Image', 'Data': 'Imagenet', alpha: 0.31, D_min: 13, D_max: 800, 
    'units': 'Images per Class', 'Source': 'p9, Figure 4', L_0: 2.24, loss: 'Error Rate', SPP: '0.1', Notes: 'Smallest D tested was 1 image per class. Visually, looks like low data regime starts at around 13 images per class.'
  },
  {
    'Paper': '[HNA+17]', Task: 'Speech', 'Data': '?', 'alpha': 0.3, D_max: '2048', 
    'units': 'Hours of audio', 'Source': 'p10, Fig 5'
  },
  {
    'Paper': '[HNA+17]', Task: 'Coin flips', 'Data': 'flips', 'alpha': 0.5, D_max: 'Inf', 
    'units': 'Coin flip observations', 'Source': 'Appendix'
  },
   
  {
    'Paper': '[KMH+20]', Task: 'LM', 'Data': 'WebText2', 'alpha': 0.095, D_min: '22e3', D_max: '23e6',
    L_0: 0.0496, 'units': 'Million BPE Tokens', loss: 'loss', 'SPP': 1000
  },
  {
    'Paper': '[HKKC+20]', Task: 'Image', Data: 'Low res', 'alpha': 0.26, D_min: '1e7', D_max: '1e10',
    'units': '16x16', 
  },
  {
    'Paper': '[HKKC+20]', Task: 'Math', Data: '', 'alpha': 0.239, D_max: '2e6', 
    'units': 'math problems',  Source: 'Figure 22'
  },
  {
    Paper: '[RRBS20]', Task: 'Image', Data: 'Cifar-100', 'alpha':
    0.7, D_max: '5e5', 
    'units': 'images',
  },
  {
    Paper:'[RRBS20]', Task: 'Image', Data: 'ImageNet', 'alpha':
    0.75, D_max: '1.2e6', 
    'units': 'images',
  },
  {
    Paper:'[RRBS20]', Task: 'LM', Data: 'WikiText-2', 'alpha':
    1.01, D_max: '2e6', 
    'units': 'words'
  },
  {
    Paper:'[BDKL+21]', Task: 'Image', Data: 'CIFAR-100', 'alpha':
    0.4, D_max: 10e5,
    'units': 'words',
  },
  
 ]
```


## Tabular Summary of Power Laws in Prior Work (WIP)


```js
viewof RW = Table(priorWork)
```

```js
configs = priorWork.reduce(function(map, obj) {
    map[obj.Paper + obj.Task] = {
      alpha: obj.alpha, D_min: obj.D_min, D_max: obj.D_max, L_0: obj.L_0, loss: obj.loss, SPP: obj.SPP
    }
    return map;
}, {});
```

## When Are These Power Laws Less Relevant?
We must note that using power law learning curves to predict data leverage outcomes is really only accurate if the data being added or deleted is similarly distributed to a random sample of data from the true distribution. The method to generate a learning curve involves starting with a "full dataset" and randomly sampling data to remove from this distribution.

However, real life data leverage campaigns may not resemble a random sample, particularly if the campaign is small. Ultimately, the efficacy of power predictions is an empirical question, and we're just going to need to observe real-life data leverage campaigns to see how accurate these predictions are.

There are several cases in which we expect power law predictions to much less relevant.

Targeted data strikes (e.g. deleting all images of a certain type of object, deleting all sentences containing a certain word) could also impact model performance in unusual, and potentially disproportionate ways. In general, because there are so many ways to organize "targeted" data strikes, this topic calls for "targeted" investigation in future work.

In most online contexts, the distribution of data contributed per person follows a power law or heavy-tailed distribution. That is, a few people ("power users") are responible for much of the data. Examples include Wikipedia, Twitter, and review platforms. If a data leverage campaign is primarily composed of power users, this could also throw off our power law predictions (because the mean # of observations per power user is much higher than the mean # of observations per user). However, if we know the total amount of data contributed by these power users, we can likely recover an accurate estimate.

Finally, this notebook has focused on strikes and CDC. What about data poisoning? Successful data poisoning attacks might do much more damage to model performance for a given particular group size. That is to say, a successful (undetected) data poisoning attack by 10% of users might reduce performance well below an equivalently sized data strike, and we'd need to know the specifics of the poisoning attack to predict the exact effect.




## The Strike - Contribution Tradeoff
An important insight from the literature of learning curves, scaling laws, and data leverage-specific experiments is that there is an inherent tradeoff between being robust against data strikes (i.e. using data efficient methods) and being robust against data contribution (i.e. using data inefficient methods that require having much more data than competitors to "win").

Conveniently, this tradeoff is captured by the exponent ${tex `\alpha`}. Power laws with larger values of ${tex `\alpha`} grow more quickly, and therefore can be seen as "more data efficient", stronger against data strikes, and weaker against CDC.

As explained above, it can be useful to measure the effects of data leverage *relative to best-case and worst-case performance*. Doing so requires selecting a "minimum dataset size" and a "maximum dataset size". The minimum dataset size corresponds to Hestness et al.s "small data region", where "models can only perform as well as "best" or "random" guessing" (Hestness et al., p. 10). It is common when working with power laws to identify a ${tex `x_{min}`}, the lowest value of ${tex `x`} for which the power law actually applies. This is the same idea. At some point on our learning curves, our data gets small enough that we'd rather use a simple baseline like random guessing or "just recommend popular stuff" (in the recommendation context) than any model trained on our very small data.

For the purposes of this notebook, we take these values from prior work, by looking at the smallest and largest values of D considered in previous experiments. We should note of course, that the idea of identifying a maximum value for D is a bit unususal. In theory, can't we always find a way to collect more data? In some cases, perhaps not (depending on the nature of the data, perhaps it is possible to create an exhaustive dataset with finite D). It's still useful to consider the largest value of D that's been studied so far.

At some point, we reach the high data regime in which the model achieves very close to the irreducible loss. At this point, we can say we've reached a true ${tex `D_{max}`}.




## What if our performance metric does not have a linear relationship with real-world utility?

Perhaps the value of getting some system 80% to 85% accuracy is much lower than from 85% to 90% (because once it's above 85%, people can't tell the difference).

Conversely, what if a system exists in a cut-throat winner take all market, and getting the absolute highest performane is of utmost importance?

We can explore these possibilites by defining a transformation that converts our loss or accuracy into some "utility" measure.

The below example assumes that the utility an organization gets from a system scales linearly with DLP, but at 0.85 DLP, there is a "jump" in 1 unit of utility.


```js
function transform(x) {
 if (x > 0.85){
   return 1 + x
 } else{
   return 0.5 + x
 }
}
```

```js
function helper(d){
  return {size: d.size, value: transform(d.value)}
}
```

```js
utilityData = data.map(helper)
```

```js
utilities = utilityData.map(d =>  d.value)
```

```js
{
  // Create an empty SVG with specified width and height.
  const svg2 = d3.select(DOM.svg(width, height));
  //create background
  svg2.append("rect")
      .attr("width", "100%")
      .attr("height", "100%")
      .attr("class", "svgBackground");
  // Draw the x and y axes.
  svg2.append('g').call(xAxis)
  svg2.append('g').call(utilityAxis);
  
  svg2.append('path')
      .datum(utilityData)
      .attr('d', utilityLine);
  return svg2.node();
}
```


## Calculations for Figure 1

From here onward is the code used to produce the Figure above. Feel free to poke around -- try to change it or break it, and feel free to reach out if you have questions, corrections, or improvements!



We'll use 1000 fractional sizes from 0.001 to 1.000 with step size 0.001.


```js
fracs = [...Array(999).keys()].map(x => (x+1)/1000)
```

```js
mode = Object({
  true: 'strike',
  false: 'cdc'
})[invert]
```

```js
sizes = fracs.map(x => x * maxObs);
```


While conceptually a bit odd, we'll allow fractional sizes for now. Would be ideal to floor these!


```js
calcLoss = D => C * (D ** -k) + bayesError
```

```js
losses = Object({
  strike: sizes.map(x=> calcLoss(maxObs-x)),
  cdc: sizes.map(calcLoss)
})[mode]
```

```js
minLoss = Math.min(...losses)
```

```js
maxLoss = Math.max(...losses)
```

```js
lossRange = maxLoss - minLoss
```

```js
dlpFunction = Object({
  strike: loss => (loss - minLoss) / (maxLoss - minLoss),
  cdc: loss => (loss - maxLoss) / (minLoss - maxLoss)
})
```

```js
scaleLoss = dlpFunction[mode]
```

```js
scaledLosses = losses.map(scaleLoss)
```

```js
scaledSizes = sizes.map(x=>x/ Math.max(...sizes))
```

```js
function formatData (x, i) {
  return {size: x, value: scaledLosses[i]}
}
```

```js
data = scaledSizes.map(formatData)
```

```js
percent = i * 100
```

```js
chosenFrac = percent / 100
```

```js
curScore = Object({
  strike: scaleLoss(calcLoss((1-chosenFrac) * maxObs)),
  cdc: scaleLoss(calcLoss(chosenFrac * maxObs))
})[mode]
```

```js
complementScore = 1 - curScore;
```

```js
curUsers = (chosenFrac * maxUsers).toFixed(0);
```


### Figure 1 Annotations


```js
leftAnnotation = Object({ //for cdc, left annotation is cdc
  cdc: `CDC by ${percent.toFixed(0)}% (${curUsers} people) brings performance from 0 to ${(curScore).toFixed(2)}`,
  strike: `Data strike by ${(percent).toFixed(0)}% (${curUsers} people) decreases perfomance by ${(curScore).toFixed(2)} to ${(complementScore).toFixed(2)}`,
})[mode]
```

```js
rightAnnotation = Object({ // for strike, right annotation is cdc
  strike: `CDC by ${100-percent.toFixed(0)}%(${maxUsers - curUsers} people) brings performance from 0 to ${(complementScore).toFixed(2)}`,
  cdc:  `Data strike by ${(100 - percent).toFixed(0)}% (${maxUsers - curUsers} people) decreases perfomance by ${(complementScore).toFixed(2)} to ${(curScore).toFixed(2)}`,
})[mode]
```

```js
niceStr = Object({
  cdc: 'Contribution',
  strike: 'Strike',
})[mode]
```

```js
function flip() {
  set(viewof i, 1 - i)
  set(viewof invert, !invert)
}
```

```js
viewof invert = Toggle({label: "Show Strike Perspective", value:false})
```


### Figure 1 Crosshairs


```js
crosshairHorizontal = (g) => g
  .append("line")
  .attr("x1", 0)
  .attr("x2", width)
  .attr("y1", yScale(curScore))
  .attr("y2", yScale(curScore))
  .style("stroke", "lightgray")
  .style("stroke-width", 2);
```

```js
crosshairVertical = (g) => g
  .append("line")
  .attr("x1", xScale(chosenFrac))
  .attr("x2", xScale(chosenFrac))
  .attr("y1", 0)
  .attr("y2", height)
  .style("stroke", "lightgray")
  .style("stroke-width", 2);
```


### Height and Margin


```js
height = 500
```

```js
margin = ({top: 50, right: 200, bottom: 50, left: 200})
```


### Misc Code: Defining d3 scale and d3 axis elements


```js
xScale = d3.scaleLinear()
    .domain(d3.extent(data, d => d.size))
    .range([margin.left, width - margin.right])
```

```js
xAxis = (g) => g
    .attr('transform', `translate(0,${height - margin.bottom})`)
    .call(d3.axisBottom(xScale))
```

```js
obsScale = {
  let obsScale;
  if (addAxis === "# Observations"){
  obsScale = d3.scaleLinear()
    .domain(d3.extent(sizes))
    .range([margin.left, width - margin.right])
} else {
  obsScale = d3.scaleLinear()
    .domain(d3.extent(sizes.map(x=>x/samplesPerPerson)))
    .range([margin.left, width - margin.right]) 
}
  return obsScale
}
```

```js
yScale = d3.scaleLinear()
    .domain([0, d3.max(data, d => d.value)]).nice()
    .range([height - margin.bottom, margin.top])
```

```js
forLossScale = Object({
  strike: [d3.min(losses), d3.max(losses)],
  cdc: [d3.max(losses), d3.min(losses)]
})[mode]
```

```js
lossScale = d3.scaleLinear()
    .domain(forLossScale).nice()
    .range([height - margin.bottom, margin.top])
```

```js
utilityScale = d3.scaleLinear()
    .domain([d3.min(utilities), d3.max(utilities)]).nice()
    .range([height - margin.bottom, margin.top])
```

```js
obsAxis = (g) => g
    .attr('transform', `translate(0,${height - margin.bottom+30})`)
    .call(d3.axisBottom(obsScale))
```

```js
yAxis = (g) => g
    .attr('transform', `translate(${margin.left},0)`)
    .call(d3.axisLeft(yScale))
```

```js
lossAxis = (g) => g
    .attr('transform', `translate(${960-margin.right},0)`)
    .call(d3.axisRight(lossScale))
```

```js
utilityAxis = (g) => g
    .attr('transform', `translate(${margin.left},0)`)
    .call(d3.axisRight(utilityScale))
```

```js
function boundY(y) {
  y = Math.min(y, height-margin.bottom-30);
  y = Math.max(y, 0+margin.top);
  return y
}
```

```js
function boundX(x) {
  x = Math.min(x, width/3);
  x = Math.max(x, 0+margin.left);
  return x
}
```


### Misc Code: Defing d3.line() elements


```js
line = d3.line()
    .defined(d => !isNaN(d.value))
    .x(d => xScale(d.size))
    .y(d => yScale(d.value))
```

```js
utilityLine = d3.line()
    .defined(d => !isNaN(d.value))
    .x(d => xScale(d.size))
    .y(d => utilityScale(d.value))
```


## Import Statements


```js
import {Button, Checkbox, Toggle, Range, Select, Table, Text, html} from "@observablehq/inputs"
```

```js
import {Scrubber} from "@mbostock/scrubber"
```

```js
html`
<style>
path {
  fill: none;
  stroke: steelblue;
  stroke-width: 1.5;
  stroke-linejoin: round;
  stroke-linecap: round;
}
button {
  background-color: #4B0082;
  border: none;
  color: white;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}

input[type=range] {
  font-size: 16px;
}
.svgBackground {fill: #fffbeb;}
.annotateBackground {background: brown;}

</style>`
```

```js
d3 = require("d3@6")
```

```js
function set(input, value) {
  input.value = value;
  input.dispatchEvent(new Event("input"));
}
```
