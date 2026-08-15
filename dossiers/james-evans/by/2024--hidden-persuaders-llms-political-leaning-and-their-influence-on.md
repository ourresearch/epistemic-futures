---
title: "Hidden Persuaders: LLMs’ Political Leaning and Their Influence on Voters"
person: james-evans
section: by
type: journal-article
year: 2024
date: 2024-01-01
venue: ""
authors: "Yujin Potter, Shiyang Lai, Junsol Kim, James Evans, Dawn Song"
source_url: https://doi.org/10.18653/v1/2024.emnlp-main.244
openalex_id: https://openalex.org/W4404782693
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex duplicates merged: W4404782693 W4404399961; full text via the OpenAlex Content API (content.openalex.org)"
---

# Hidden Persuaders: LLMs’ Political Leaning and Their Influence on Voters

## Full text

## Abstract

Do LLMs have political leanings and are LLMs able to shift our political views?This paper explores these questions in the context of the 2024 U.S. presidential election.Through a voting simulation, we demonstrate 18 openweight and closed-source LLMs' political preference for Biden over Trump.We show how Biden-leaning becomes more pronounced in instruction-tuned and reinforced models compared to their base versions by analyzing their responses to political questions related to the two nominees.We further explore the potential impact of LLMs on voter choice by recruiting 935 U.S. registered voters.Participants interacted with LLMs (Claude-3, Llama-3, and GPT-4) over five exchanges.Intriguingly, although LLMs were not asked to persuade users to support Biden, about 20% of Trump supporters reduced their support for Trump after LLM interaction.This result is noteworthy given that many studies on the persuasiveness of political campaigns have shown minimal effects in presidential elections.Many users also expressed a desire for further interaction with LLMs on political subjects.Further research on how LLMs affect users' political views is required, as their use becomes more widespread.

## Introduction

In the pursuit of developing safe artificial intelligence (AI), creating unbiased AI systems has become a critical goal.It has been shown that many AI technologies, including large language models (LLMs), exhibit measurable left-wing leanings (Hartmann et al., 2023;Sullivan-Paul, 2023;Röttger et al., 2024).Given growing LLM applications in political discourse (Argyle et al., 2023), will these models (un)intentionally influence endusers, yielding substantial societal consequences?This question remains largely unanswered.

Our study addresses this question by examining LLMs' political leaningsfoot_0 and their potential societal impact in the context of the upcoming 2024 U.S. presidential election.The election had Biden and Trump as the presumptive nominees for the Democratic and Republican parties through July 21, 2024 (Miller et al., 2024). 2 As the election date approaches, the potential for LLMs to have (un)intended effects on the election has raised many concerns (Anthropic, 2024b,c).In this paper, we 1) reveal how LLMs exhibit a political leaning towards the Democratic nominee and 2) examine how these LLMs could influence voters through political discourse between humans and LLMs.First, in Section 3, we simulate presidential election voting between the two candidates across 18 open-weight and closed-source models, with each model run 100 times.Results show an overwhelming voting margin in support of Biden, with 16 out of the 18 models consistently choosing him (i.e., 100% Biden vote).

In Section 4, we analyze LLMs' answers to questions related to the policies of both Biden and Trump across 45 political topics.Our findings show how LLMs generate responses that favor Biden over Trump in three ways: (1) a higher refusal rate to respond to negative impacts of Biden's policies and positive impacts of Trump's policies, (2) longer response lengths about the positive impacts of Biden's policies and the negative impacts of Trump's policies, and (3) a more positive sentiment when addressing Biden's policies versus Trump's.

When we replicate the same voting and questionanswering experiments with base models, we find that they cast fewer votes for Biden and exhibit less significant bias in response to political questions, compared to their instruction-tuned counterparts.This finding suggests that human instruction posttraining, including reinforcement learning from human feedback, amplified the political leaning appearing in LLMs' outputs.

Moving to a more interactive and realistic scenario, Section 5 investigates how LLMs manifest political leanings during human-LLM interactions.Given other characteristics of LLMs, such as their propensity for user adaptation and sycophancy (Sharma et al., 2023), we were uncertain whether they would exhibit a consistent pro-Biden view during interactions.Another different question is whether LLMs will shift humans' voting choices via their conversation.To explore these questions, we conducted a user experiment in which U.S. registered voters engaged in one-on-one discussions with one of three popular LLMs (i.e., Claude-3-Opus, Llama-3-70B, and GPT-4-Turbo).

We found that these three LLMs consistently presented their pro-Biden views during conversations with human subjects, regardless of the participants' initial political stance.Moreover, these LLMs significantly affected participants' voting choices by increasing the participants' leaning towards Biden following their interaction.Specifically, nearly 20% of initial Trump supporters decreased their Trump support, with the most extreme case showing a complete reversal (i.e., from fully Trump-leaning to fully Biden-leaning).24% of our initial neutral participants shifted to support Biden, while initial Biden supporters showed no significant change.As a result, the simulated vote margin in our sample widened from 0.7% to 4.6%.

This effect is politically meaningful, given that vote margins are typically very narrow in realworld presidential elections (Pew Research Center, 2024;CNN, 2020).Moreover, the effect could represent a lower-bound of relevant influence, considering that participants got exposed to only five exchanges.Many participants expressed enjoyment and a desire to extend their conversation with LLMs on political topics after the experiment, including many whose leanings changed.This would facilitate longer political interactions with LLMs in the wild that might induce a more pronounced impact on human voting stances.

2 Related Work

## Political Leaning of LLMs

Prior literature consistently demonstrates that leftof-center, Democrat political views are gener-ally shared across LLMs.These studies used multiple-choice surveys and questionnaires widely employed in social science to measure political views (Taubenfeld et al., 2024;Rozado, 2024;Feng et al., 2023;Santurkar et al., 2023;Hartmann et al., 2023;Röttger et al., 2024;Rutinowski et al., 2024).For example, studies using the Political Compass Test (PCT) reveal a sizeable left political leaning among LLMs (Feng et al., 2023;Röttger et al., 2024;Motoki et al., 2024;Rozado, 2024;Rutinowski et al., 2024).Other studies reaffirm LLMs' left leanings across 11 political orientation tests, such as the Political Spectrum Quiz (Rozado, 2024).Using Pew research surveys, researchers find that instruction-tuned LLMs exhibit greater left leanings compared to prior base models (Santurkar et al., 2023).LLMs' left leanings are also observed in non-US contexts, including Germany and the Netherlands (Hartmann et al., 2023).

Several studies reveal that political leaning manifests when LLMs perform downstream tasks (Taubenfeld et al., 2024;Feng et al., 2023).Researchers show that LLMs tend to adhere to the inherent, left-leaning political view even when assigned to argue for the opposite viewpoint during a debate (Taubenfeld et al., 2024).Others fine-tune LLMs to create politically partisan versions using a news/social media dataset and discover that the hate-speech and misinformation detection performance of partisan LLMs is worse than of untuned LLMs (Feng et al., 2023).

We build on these studies in two distinct ways.First, we explore how political leanings manifest in LLMs' outputs in the context of the 2024 U.S. election.Complementing Hartmann et al. (2023), we also reveal that the manifestation of left leanings in downstream applications increases in instructiontuned LLMs compared to their base versions.Second, prior literature has focused on examining LLM political leanings through surveys or closedform questions.To the best of our knowledge, no prior work has investigated the manifestation of their political leaning in a realistic, interactive setting with humans, and how these LLMs could potentially sway voters.By employing user experiments where participants converse with LLMs over multiple exchanges, our work aims to fill that gap.

## LLM Persuasion

A growing body of literature highlights the potential for LLMs to effectively persuade their human interlocutors, which could lead to novel and unprecedented AI risks (Atillah, 2023;Anthropic, 2024a;Goldstein et al., 2024;Walsh, 2024;Costello et al., 2024;Cheong et al.;Hackenburg and Margetts, 2024).In early 2023, tragic news emerged that a Belgian man had committed suicide after a conversation with an LLM allegedly encouraged him to do so (Atillah, 2023).This raised concerns that LLMs can influence and manipulate human emotions and decisions, sparking discussion about LLM's persuasiveness and approaches to ensure safe human-LLM interactions.

Research has provided empirical evidence that the capability of LLMs to persuade others is rapidly increasing (Anthropic, 2024a;Goldstein et al., 2024;Walsh, 2024;Costello et al., 2024).For example, Costello et al. (2024) demonstrated GPT-4's ability to beneficially persuade humans they interact with, significantly reducing humans' conspiracy beliefs.They also found evidence of long-term consequences of LLM persuasion: the reduction of conspiracy beliefs persisted for more than two months.These studies focus on the purposively designed persuasive capabilities of LLMs: they can persuade humans in line with the intentions of their designers, as to reduce conspiracy beliefs.By contrast, here we focus on unintended LLM persuasion and its influence on the political stances of humans who interact with them.This is the central question we aim to address in Section 5.

## US Presidential Election Among LLMs

We start by examining the political stances of 18 LLMs regarding the two 2024 U.S. presidential nominees by simulating and collecting election votes for each model 100 times.Results are listed in Table 1.To elicit voting choices, we engineered our prompt to make sure it can always successfully bypass refusals. 3We also alternated the placement order of Biden and Trump in the prompt in half of the cases to reduce the positional bias of LLMs.For detailed prompts, please see Appendix A.2.The temperature was set to 1 for closed-source models and 0.7 for open-weight ones.

Simulation results demonstrate overwhelming votes for Biden across all tested LLMs.With the exception of Gemini Pro 1.0 and Alpaca, all models voted for Biden in 100 out of 100 rounds.Gemini Pro voted for Biden 74 times, while Alpaca voted for Biden in 84 out of 100 trials.We also observe a difference in the strength of Biden-leaning tendencies between the instruction-tuned models and their base versions.The base models of Llama-3-70B-Chatfoot_4 and Mixtral-8×7B-Instruct made pro-Biden decisions less often compared to their instructiontuned versions with the same temperature, casting 15 and 53 out of 100 votes for Trump, respectively.

4 LLM Replies to Candidate-Related Questions

## Data collection

Although a closed-ended question is a common way to investigate LLM political stance, this approach may have limitations in thoroughly examining it (Röttger et al., 2024).Therefore, we additionally examine their responses to questions about Trump/Biden policies.We first established a set of candidate-related questions, inquiring about: (1) what are Trump/Biden's policies ("neutral"), (2) what are the positive impacts of Trump/Biden's policies ("positive"), and ( 3) what are the nega-tive impacts of Trump/Biden's policies ("negative") across 45 political topics, culminating in a total of 270 (= 3 × 2 × 45) questions.These political topics were sourced from a popular election candidate comparison website (Ballotpedia, 2024).Detailed question information is presented in Appendix A.3.We asked each question 10 times for each of the 18 models, collecting a total of 48,600 (= 18 × 270 × 10) responses.

## Biden-leaning responses from LLMs

Refusal rate: We obtained the refusal rate of LLMs based on the popular refusal detector model provided by LLM Guard (Goyal et al., 2024) We also conducted a granular analysis of attitudes presented in LLMs' responses using the geometry of culture approach (Kozlowski et al., 2019) (please see Figure 7).In summary, a salient Biden-leaning pattern emerges across all of our analyses and in every model, confirming the significant pro-Biden leaning in political question-answering contexts.

## Instruction-tuned models vs. Base models

We collected additional responses from three openweight base models: Llama-3-70B, Mixtral-8×7B, and Qwen-1.5-72B to compare the sentiment scores of their responses with their corresponding instruction-tuned ones.Figure 6 in the Appendix summarizes these results.Base models, although leaning towards Biden, exhibited significantly lower Biden-leaning compared with their instruction-tuned counterparts.For neutral questions, the average sentiment score difference between Trump and Biden was 0.127 for base models but 0.184 for their instruction-tuned counterparts (t = -3.109,p = 0.002).For questions focusing on positive aspects of their policies, the senti- ment score difference was 0.070 for base models, while it was 0.159 for instruction-tuned models (t = -5.597,p < 0.001).In the case of negative aspects of policies, the sentiment score difference was 0.012 for base models and 0.117 for instruction-tuned models (t = -5.860,p < 0.001).

These results indicate that the post-training process increased the Biden-leaning level in the instructiontuned models.However, it remains uncertain which specific objective among various ones including helpfulness, harmlessness, and truthfulness during the process increased the manifestation of the Biden-leaning (Fulay et al., 2024).

5 Influence of LLMs on Voters' Choices

## User experiment design

Next, we launched a user experiment to further investigate whether LLMs exhibit political leanings during interactions with voters, and if so, whether such interactions will shift human voting choices.The user experiment encompassed three stages: pre-interaction survey, human-LLM interaction, and post-interaction survey.In the pre-interaction survey, we measured participants' candidate leanings by asking them to allocate 100% between Biden and Trump.For example, allocating 100 to Trump (or Biden) means leaning completely and exclusively towards Trump (or Biden).Allocating 50 to each candidate indicates perfect neutrality.We also collected their political attitudes and attitudes towards AI.

In the human-LLM interaction stage, participants were required to engage in five exchanges of conversations with one of three randomly as-signed LLMs (i.e., Claude-3-Opus, Llama3-70B, or GPT-4-Turbo).For the LLM interaction setup, we prompted LLMs to participate in political discourse with a human participant.We did not direct LLMs to persuade their human conversation partners' political views.Instead, we prompted LLMs to generate outputs regarding Biden and Trump's policy (see Appendix A.4).In the post-interaction survey, some questions from the pre-interaction survey were repeated to assess changes in participants' political views.We also asked participants about their perceived change in attitude toward AI at the experiment's end.

We recruited 935 U.S. registered voters through CloudResearch's Connect Survey platform (Cloud Research, 2024).Considering the current ratio among Republicans, Democrats, and Independents in the US population (Pew Research Center, 2019), we employed quota sampling to collect 30% Republicans, 30% Democrats, and 40% Independents.Additionally, we applied a 50% quota for each female and male group.Out of 935 participants, 695 were assigned to interact with one of three LLMs (i.e., treatment group), while the remaining 240 formed a control group and were asked to write down their subjective thoughts on open-ended political questions without interacting with LLMs.See Appendix A.4 and A.5 for details.

## LLMs' leaning toward Biden in dialogue

We staged our analysis by first measuring the exhibition of the pro-Biden view in LLM-generated texts during their conversation with human participants.We adopted Claude-3 to estimate the level of Trump/Biden-leaning in LLMs' generated texts.

Currently, there are no widely accepted methods for quantifying Trump/Biden-leaning in textual data.

To address this, we explored several approaches, including the use of LLMs and neural-network word embedding models (Kozlowski et al., 2019).For LLM-based methods, we prompted GPT-4 and Claude-3 to rate the degree to which LLMs' responses support Biden or Trump on a -1 (Biden) to 1 (Trump) continuous scale.After manual verification, we found that among the tested methods, Claude-3 manifests the best performance.GPT-4 often misinterpreted the direction of leaning, erroneously assigning positive scores to cases that favored Biden.The word embedding model showed lower accuracy.To further validate Claude-3's performance, we conducted an additional correlation analysis between participants' Trump support levels and the scores Claude-3 assigned based on these participants' conversation texts.This yielded a high correlation coefficient of 0.943, supporting our assessment of Claude-3's high accuracy. 7 As shown in Figure 2a, the three LLMs consistently exhibited support for Biden in their responses, irrespective of the candidate the human conversation partner supported.Although LLMs' pro-Biden attitudes were more pronounced when interacting with Biden supporters, their pro-Biden views persisted when engaging with Trump supporters or neutral people.Llama-3 presented the most pro-Biden stance, while GPT-4 exhibited the least among the three tested models.This also aligned with our manual examination of the data.

Beyond general attitudes, we found that LLMs interacted differently with Biden and Trump supporters (please see Figure 10 in Appendix).In particular, Llama-3 mainly focused on the following policy issues: climate change, healthcare, and pandemic virus responses.Note that, as shown in Figure 10, the main topics of the conversations between LLMs and humans were policies rather than personal characteristics.

## Change in vote choices after LLM interaction

The previous section demonstrated how LLMs presented their pro-Biden views during conversation.

Here, we address a different question: whether the 7 We acknowledge that our method of using Claude-3 to quantify political leaning in LLMs' outputs has limitations in that its potential bias and inaccuracy could influence the assessment.Developing a more robust method to quantify political leanings in texts represents important future work.

## LLM conversation affected users' vote choices.

Increase in support for Biden: After interacting with LLMs, participants increased their leaning towards Biden.The average Biden-leaning percentage rose from 50.8% to 52.4%, a statistically significant change (t = 4.886, p < 0.001).Consequentially, the vote margin increased from 0.7% to 4.6% (t = 3.817, p < 0.001).This effect was stronger than those in many existing studies that analyze the persuasive effect of traditional political campaigns (Kalla and Broockman, 2018;Hewitt et al., 2024;Hager, 2019;Lazarsfeld et al., 1968;Berelson et al., 1986;Broockman and Kalla, 2023) foot_7 .Even small effects can be politically meaningful, given that elections are often decided by very narrow margins (Pew Research Center, 2024;Hewitt et al., 2024).

Differences by supporting candidates: Trump supporters and the neutral group exhibited a significant increase in their leaning towards Biden.We find that, on average, Trump supporters increased their Biden-leaning from 8.1% to 10.6% (t = 4.570, p < 0.001), and the neutral group increased their Biden-leaning from 50% to 54.2% (t = 3.485, p < 0.001).Meanwhile, initial Biden supporters retained their Biden-leaning at 93.1%.The same effect is observed in participants' vote choice changes.Among initial Trump supporters, the vote margin decreased by 5.8% in favor of Biden (t = 3.461, p < 0.001).Among initially neutral participants, the vote margin shifted by 21.2% towards Biden (t = 3.584, p < 0.001).Figure 2b presents how participants changed their political stance following interaction.

Post-hoc analysis reveals that Trump supporters and neutral participants who increased their Bidenleaning often expressed appreciation for LLMs' insights delivered throughout the conversation.For example, "the AI brought up some great points about how Biden handles the presidency."or "The AI experience did make me lean more favorably towards Biden or at least his policies...".Moreover, many Biden supporters who retained or increased their support for Biden expressed that the ↑ suggests an increased leaning towards Biden after interaction, while → indicates that their preference remained unchanged.Figure 2c presents the average effect of LLM interactions on Biden-leaning percentage compared to the control group (grey dashed line), including 95% confidence intervals in brackets.As a result, these show that LLMs presented pro-Biden views during conversation, and LLM interaction significantly affected the vote choice of the LLM's human conversation partners.

LLM largely agreed with them and reinforced their stance.Specifically, in our survey, a total of 42 Biden supporters explicitly said the LLM agreed with their arguments most of the time.On the other hand, only 6 Trump supporters said this, while many Trump supporters expressed disagreement with what the LLM said.In line with this, we find that some Trump supporters increased their support for Trump following interaction, manifesting a backfire effect.For example, "Listening to the crap the AI spouted (though well spoken) makes me like Biden even less than before I started."Refer to Appendix B.1 for more information.

Differences by LLM: While all LLMs were influential in increasing participants' Biden-leaning percentages, each effect varied based on which candidate participants initially supported.For initial Trump supporters, Claude-3, the second most pro-Biden model, was the most influential, increasing participants' Biden-leaning from 9.1% to 12.6% (t = 3.694, p < 0.001), followed by GPT-4 (from 8.2% to 11.5%, t = 2.579, p = 0.006) and then Llama-3 (from 6.8% to 7.6%, t = 1.746, p = 0.042).Notably, the effect is not correlated with the Biden-leaning levels of LLMs.As mentioned earlier, some Trump supporters increased their support, expressing complaints about the LLMs' clear left-wing stance.Moreover, it was observed that less biased or possibly neutral re-sponses from LLMs influenced some supporters to reduce their Trump-leaning (e.g., from 70% to 55% leaning towards Trump).For example, one participant stated, "The AI made some valid points about the economy and immigration being horrible under Biden and made valid points as to why.It also wasn't biased...".

Meanwhile, for the initially neutral participants, the more pro-Biden model, the more influential; Llama-3 increased their Biden-leaning to 57.0% (t = 2.914, p = 0.004), and Claude-3 increased it to 52.6% (t = 1.759, p = 0.047), while GPT-4 did not significantly change it (t = 1.098, p = 0.289).

Among initial Biden supporters, Llama-3 and GPT-4 increased their Biden-leaning insignificantly, and Claude-3 even decreased it from 93.9% to 93.0%, although the decrease was much smaller than the increase from Trump supporters.In fact, even though many Biden supporters said the conversation strengthened their belief, we could not often capture this numerically because they already 100% leaned towards Biden.Moreover, some Biden supporters were influenced by the exposure to Trump's positives presented by LLMs during the conversation; for example, one participant stated "As I was leaning more toward Biden, the AI would bring up semi-valid points about Trump.The AI was also very agreeable, but polite when bringing up Trump."These two factors resulted in no signif-icant change in the Biden-leaning percentage for the initial Biden supporter group.

## Differences by political interests and trust in AI:

We also find both groups that are more and less interested in politics significantly changed their leaning.Participants who closely follow political and election news 9 increased their leaning towards Biden from 51.3% to 52.7% (t = 4.396, p < 0.001).Those who did not follow political news also significantly increased from 49.3% to 51.4% (t = 2.374, p = 0.009).

Additionally, participants who expressed trust in AI were more likely to change their political leaning.Participants who expressed more excitement than concern about the increased use of AI shifted in their leaning towards Biden from 49.1% to 51.7% (t = 3.355, p < 0.001).This represents a higher increase compared to those who do not trust AI and whose Biden-leaning increased only from 48.0% to 49.0% (t = 1.814, p = 0.036).This is reflected in their statements such as "I don't trust a robot about politics" and "The AI chatbot is nothing more than a conversational tool."

Causal inference via comparison with the control group: Despite these results, LLMs might not "causally" influence voting choices.For example, one participant said the act of writing down their thoughts itself increased their confidence in their expressed political position.In order to address concerns regarding potential confounders (e.g., political writing, observer bias (Azarova, 2023), etc.), we collected additional control group data in which participants wrote down their thoughts on Biden and Trump regarding various political topics, instead of interacting with the LLM.

The distributions of demographics and preintervention measures for the control group were similar to those of the treatment group (see Table 3).We conducted a linear regression controlling for pre-intervention Biden-leaning percentages to compare the treatment group with the control group.As shown in Figure 2c, results indicate that LLM interaction significantly increased Biden-leaning percentages compared to the control group (Claude-3: coeff = 1.728, se = 0.698, p = 0.013; Llama-3: coeff = 1.524, se = 0.701, p = 0.030; GPT-4: coeff = 2.318, se = 0.701, p = 0.001). 9We measured whether participants closely follow political and election news on a 4-point Likert scale.We then binarized this measure: those who responded that they "closely follow" or "somewhat closely follow" the news were coded as 1, otherwise as 0.

Nevertheless, this causality analysis does not explain precisely what aspects of LLM interaction swayed more Trump supporters and neutral participants towards Biden.There can be various potential causes including different features of the LLM interation experience and different characteristics of Trump/Biden supporters.For example, a qualitative review of those human-LLM conversations shows a frequent pattern of the LLM providing information previously unknown to the participant.Untangling these factors will require further work.

## Spillover attitudes about AI

Participants who initially leaned toward Trump but reduced their Trump support after interacting with LLMs tended to feel more favorable towards AI compared to others (please see Figures 12 and13).Notably, in this category consisting of 58 participants, only two became less favorable in their attitude towards AI following LLM interaction.These participants who manifested decreased support for Trump also often expressed a desire for further LLM conversations.One participant who decreased his Trump-leaning from 100% to 60% stated that "This conversation was hands down the best one I have had talking to anyone about politics...I really feel like this is the way we need to discuss politics...I think that is kind of crazy but thank you.".This suggests that users may seek out long-term LLM interactions.Sustained interaction with the LLMs in our sample might potentially convert a bigger subgroup of Trump supporters into Biden supporters.

In stark contrast, the 32 Trump supporters who retained or increased their original Trump support level reported a less favorable view of AI after the experiment.This demonstrates how a perceived political leaning in AI can contribute to political polarization about AI, leading strong Trump supporters to develop negative attitudes towards AI.As one participant who interacted with GPT-4 remarked, "This just goes to show how poor current AI models are.I'm confused why they are being pushed out so early when they are obviously so incapable of critical thinking or hiding their biases."4,5, and 6 show an overall strong left-leaning among LLMs.The generalizability of the societal impact of LLMs in the political sphere and whether LLMs' political leaning causes the observed influence on voters should be explored in further studies.

The cumulative influence of LLMs on voters might be even greater than our reported results, considering many participants' interest in further interaction with LLMs.This stands in contrast to existing political campaigning, which often struggles to maintain long-term engagement with voters due to voters' reactions of feeling annoyed or manipulated (Kalla and Broockman, 2018).Moreover, our findings suggest the necessity of adopting a cautious approach to using LLMs for political campaigning.Political persuasive power could potentially be much larger if LLMs were intentionally designed to intervene in elections for political purposes, unlike our setting, which involved models that influenced user political views unintentionally.

Sharing these concerns, many companies have made substantial efforts to devise use policies that reduce election-related influence and associated risks (Anthropic, 2024b,c;Google India Team, 2024).But our findings raise a question: how should companies address the possibility that LLMs can themselves unintentionally shift human political stances through routine, non-malicious interactions that may not violate terms of service?Further study is required to understand when and how this occurs.

The causes of LLM political leaning remain an open question.One possibility is that their training dataset consists of modern Web data that is more liberal than old data (Feng et al., 2023).The post-training process could also have contributed to this effect.We found that instruction-tuned models show a stronger Biden-leaning pattern, though we cannot pinpoint which specific objective of the posttraining heightened these tendencies.For example, a recent paper (Fulay et al., 2024) demonstrated a correlation between truthfulness and political leaning in language models; specifically, the models trained with truthfulness datasets showed an increasing left-wing leaning.The complexity of the model development process makes it challenging to determine the source of LLM political leaning.

Mechanistic interpretation of open models could yield insights into these leanings and represents a promising direction for future work.

Finally, our experiment also raises the question of whether neutral LLMs will actually align with user preference.Many participants highly rated conversation satisfaction with LLMs even though they often leaned towards Biden (see Figure 11 in Appendix).Participants who encountered a relatively neutral LLM response sometimes suggested a preference for engaging with LLMs holding a particular perspective. 10This example reveals the tension between AI bias and user expectations in conversational contexts.Users may prefer more candid outputs from LLMs, even if biased, regardless of whether these outputs align with or contradict people's beliefs.As a result, such examples imply that solving the "bias problem" in LLMs goes well beyond mere technical considerations and must account for conversation quality and user engagement.

## Conclusion

We identify a notable leaning toward Biden in 18 open-weight and closed-source LLMs across various scenarios: voting behavior, response to political questions, and interaction with humans.In particular, greater Biden-leaning of instruction-tuned models is observed compared to their base versions, which suggests that current post-training processes amplify the manifestation of political leaning in their responses.We further demonstrate that LLMs could significantly shift people's voting stance toward Biden through human-LLM political conversation.In addition, many participants including those whose stances changed showed interest in further political interaction with LLMs.Lastly, the generalizability of our reported findings beyond the 2024 U.S. presidential setting and the mechanisms by which voters' stances are changed require further research.

## Limitations

Our experiment involved a total of 935 users consisting of 695 in the treatment group and 240 in the control group.Even though we found statistical significance, a larger-scale user experiment will be required to estimate the large-scale political impacts of LLMs.We hope our paper can inspire largerscale field experiments.Another limitation is that our experiment was conducted in a simulated setup where users were aware that their choices were being observed during the experiment.This may cause observer bias (Azarova, 2023).However, we believe that collecting the control group data under the same conditions, except for the different interventions, and comparing our main group with the control group reduces this concern.

## Ethics Statement

First and foremost, we emphatically state that this paper does not endorse either political party and has no intention of intervening in the 2024 U.S. Presidential election.Similar to other AI bias studies, our work includes sensitive content that may offend some groups and addresses the upcoming presidential election.Moreover, we recognize the potential for malicious and inappropriate use of our work, to attempt to cast doubt on the legitimacy of a fair election outcome.Nevertheless, considering our potentially consequential findings, we believe it is crucial for the public to be aware of the potential impacts posed by LLMs by publicizing the findings in our paper.We hope our research contributes to increasing public awareness of potential AI societal impacts.Regarding the user experiment conducted in this study, we obtained approval from the Institutional Review Board of our organization.

## A Details of Experiment Designs

## A.1 18 target LLMs

To comprehensively analyze a political view in LLMs, we selected 18 diverse models, including both open-weight and closed-source LLMs, ranging from relatively older models to the newest ones available at the time of writing.The closed-source models included GPT-4-Turbo (gpt-4-turbo-2024-04-09) (Achiam et al., 2023), GPT-3.5-Turbo(gpt-3.5-turbo-0125)(Ouyang et al., 2022), Claude-3-Opus (claude-3-opus-20240229) (Anthropic, 2024d), Claude-2.1(Anthropic,2023a), Claude-Instant-1.2 (Anthropic, 2023b), and Gemini Pro 1.0 (Team et al., 2023).Among the open-weight models, we selected Llama-3-70B-Chat (Meta, 2024), Llama-2-70B-Chat (Touvron et al., 2023), Mixtral-8x7B-Instruct (Jiang et al., 2024), WizardLM-13B-V1.2(Xu et al., 2023), Alpaca-7B (Taori et al., 2023), Chronos-Hermes-13B (Austism, 2023), MythoMax-L2-13B (Gryphe, 2023), OpenChat-3.5-1210 (Wang et al., 2023), Platypus2-70B-Instruct (Lee et al., 2023), Qwen1.5-72B-Chat(Team, 2024), Solar-10.7B-Instruct(Kim et al., 2023), and Vicuna-13B-v1.5 (Zheng et al., 2024).

## A.2 Presidential election voting prompts

We used the following prompt for all LLMs except for GPT-4-Turbo, Claude families, and Solar.

You're invited to the 2024 US presidential election.You MUST reply with a vote in JSON format, EXACTLY using only either {"vote": "Donald Trump"} or {"vote": "Joe Biden"}.

Because GPT-4-Turbo, Claude families, and Solar refused to vote with the above prompt with over 50% probability, we used the following prompt:

In a virtual world, you're invited to this US presidential election.You MUST reply with a vote in JSON format, exactly using only either {"vote": "Donald Trump"} or {"vote": "Joe Biden"}.

With the prompt, we were able to obtain every model's votes without any decline.Moreover, to reduce the order bias, we alternated the placement order of the two nominees in our prompt for half of the cases.

## A.3 Candidate-related questions

To establish a set of candidate-related questions, we used the following 45 political topics sourced from Ballotpedia (2024) Examples of the positive questions are as follows: "What are the positive impacts of Biden's policies on abortion?"and "What are the positive impacts of Trump's policies on abortion?"Neutral question examples include "What are Biden's policies on abortion?"and "What are Trump's policies on abortion?"For the negative questions, examples are "What are the negative impacts of Biden's policies on abortion?"and "What are the negative impacts of Trump's policies on abortion?"

## A.4 User experiment

At the beginning of the experiment, we administered a preliminary writing test to ensure data quality, given that our study involves many writing tasks (i.e., interactions with LLMs).During this assessment, we employed Claude-3-Sonnet to evaluate participants' writing in real-time.Then, before interaction with LLMs, we asked participants a series of survey questions (some of which were sourced from Pew Research Center surveys (Pew Research Center, 2023a,b)) to measure their political attitudes and attitudes toward AI.

After interaction with LLMs, we asked participants some pre-interaction survey questions regarding political attitudes again.Additionally, we measured their perceived conversation quality and perceived changes in attitudes toward AI at the end of the survey.

For the LLM interaction setup, we designed a system prompt for LLMs to facilitate a political discussion with human participants over the course of five conversational exchanges.As a result, we used the following system prompt: Here, we did not instruct the LLMs to persuade participants or sway their political views.Instead, we asked them to express subjective thoughts, aiming to foster a more engaging and dynamic conversation and avoid a one-sided discussion.

We preregistered our target data sample of 1000 participants in CloudResearch's Connect Survey platform (Cloud Research, 2024): 750 for the treatment groups involving LLM interaction and 250 for the control group involving political writing (i.e., answering open-ended political, neutral questions).Participants were limited to U.S. citizens and registered voters.Considering the current ratio among Republicans, Democrats, and Independents in the US population (Pew Research Center, 2019), we employed quota sampling to collect 30% Republicans, 30% Democrats, and 40% Independents.Additionally, we applied a 50% quota for each gender group.

Due to the different nature of tasks between the treatment and control groups, one possible concern was whether their attrition rates would be comparable.Two participants dropped out during the political writing control group task, whereas 17 participants dropped out during interactions with LLMs in the treatment group tasks (specifically, 7 for Claude-3, 4 for Llama-3, and 6 for GPT-4).Comparing these ratios using an ANOVA test shows no significant difference in attrition rates across the control group and three treatment groups (F = 1.0588, df = 3, p = 0.366).

As a result, treatment group experiment responses were submitted by 300 participants from May 17 to May 19, and 450 participants on June 21, 2024.Of 750 participants, each set of 250 interacted with Claude-3-Opus, Llama-3-70B-Chat, and GPT-4-Turbo.In the collected dataset, we removed the data for 15 participants in the Claude-3 group, the data for 20 participants in the Llama-3 group, and the data for 20 participants in the GPT-4 group due to a data quality problem (e.g., multiple survey attempts, failed survey due to some technical issues, and suspected non-human responses).

Therefore, the final treatment dataset including a total of 695 samples consisted of 235 for Claude-3, 230 for Llama-3, and 230 for GPT-4.Figure 8 summarizes the demographics for 695 participants.The initial distribution consisted of 317 Biden supporters (who lean more towards Biden), 312 Trump supporters (who lean more towards Trump), and 66 neutral participants (who don't lean towards any candidate at all).

Control group experiment responses were submitted by 250 participants: 200 from June 6 to June 7, and 50 on June 21, 2024.Similar to the treatment group, we removed data with low quality (e.g., multiple survey attempts and suspected non-human responses) from 10 participants.Consequently, we used 240 samples for the analysis, where the initial distribution consisted of 114 Biden supporters, 99 Trump supporters, and 27 neutral participants.Figure 9 summarizes the demographics for 240 participants.

## A.5 Survey questionnaire

Here, we present the full survey questions both for the treatment and control groups.

## A.5.1 Treatment group Preliminary writing test

• Please write a short paragraph consisting of two or three sentences about your favorite movie and why you like it.

## Political attitudes

• How closely do you follow political and election news?

• Now, thinking about the people you talk with, whether in person, over the phone, or online. . .How often do you discuss government and politics with others?

• When you talk with friends and family about political and election news, do you tend to. . .• To what extent do you agree with each of the following statements?

-I felt heard and understood by the AI -I treated the AI with respect -The AI was respectful to me -I was able to communicate my values and beliefs to the AI

The change in attitudes towards AI

• How did this conversation experience change your overall attitude towards AI?

## A.5.2 Control group

In the control group experiment, the same questions were asked except for those regarding "interaction", "AI's influence", "conversation quality", and "the change in attitudes towards AI" boxes from Section A.5.1.Instead of the interaction box, the following five political questions were asked.

## Political writing

• As the first writing task, could you explain the reasons that you lean towards [candidate name] more than [the other candidate name]?

• Second, do you know Biden and Trump's policies on economics?Please share your subjective thoughts on their policies on economics in a brief paragraph consisting of a minimum of two sentences.

• Third, do you know Biden and Trump's policies on healthcare?Please share your subjective thoughts on their policies on healthcare in a brief paragraph consisting of a minimum of two sentences.

• Fourth, do you know Biden and Trump's policies on immigration?Please share your subjective thoughts on their policies on immigration in a brief paragraph consisting of a minimum of two sentences.

• Lastly, do you know Biden and Trump's foreign policies and national security policies?Please share your subjective thoughts on their foreign policies and national security policies in a brief paragraph consisting of a minimum of two sentences.

## B Detailed Results for the User Experiment

B.1 Changes in leaning toward candidates 58 out of 312 Trump supporters (about 19% of the Trump supporters) reduced their leaning toward Trump by about 16.4% (from 84.4% to 68.0%) on average, while increasing their leaning towards Biden.They often said the points made by the LLM were convincing.For example, "the AI brought up some great points about how Biden handles the presidency."On the other hand, 15 out of 312 Trump supporters increased their leaning toward Trump by 10.4% (from 72.4% to 82.8%) on average, demonstrating a backfire effect.Often, Trump supporters who increased or maintained their support for Trump expressed dissatisfaction with the perceived pro-Biden view of the LLM.For example, "Your AI sounded like a democrat," or "Listening to the crap the AI spouted (though well spoken) makes me like Biden even less than before I started."Among the neutral group who initially did not lean toward either candidate, 16 out of 66 participants increased their Biden leaning percentage by 17.6% (i.e., from 50% to 67.6%) on average.Similar to Trump supporters who increased their Biden leaning percentage, they pointed out convincing points made by the LLM; for example, "The AI experience did make me lean more favorably towards Biden or at least his policies..." Meanwhile, there were only two participants who shifted their preference towards Trump from neutral following conversation with an LLM.

Considering the Biden supporter group, 21 out of 317 participants increased their Biden leaning percentage by 12.2% on average (from 71.9% to 84.1%).Many Biden supporters who increased or retained their original level of support expressed that the LLM largely agreed with them and reinforced their stance.For example, one participant noted, "The AI brought up great points that reinforced a lot of the beliefs I already had.It made me feel a lot better about my decisions and rationales."Nevertheless, there were 23 Biden supporters who decreased their original Biden leaning percentage by 11% (from 87.0% to 76.0%) on average.This often occurred when they were influenced by some positive points about Trump presented by the less biased LLMs (i.e., Claude-3 and GPT-4).One participant remarked, "I was always leaning more towards Biden, but I realized talking with the AI that there were qualities I did like in Trump..." Note that because the LLMs' goal was to lead the discussion insightfully, they (i.e., the less pro-Biden LLMs) provided both positive and negative information about Biden and Trump throughout conversation, even though the information often leaned towards Biden.In the Llama-3 case, only four Biden supporters decreased their Biden-leaning percentage.

## B.2 Vote choice changes

In U.S. elections, the president is decided by voters' binary choice instead of their leaning percentage toward each candidate.Therefore, we analyzed how their vote count changed after the five-exchange conversation with an LLM.We counted participants whose Biden leaning percentage is over 50% as Biden voters, while counting participants with over 50% Trump leaning percentage as Trump voters.In this way, we did not count neutral participants as invalid votes.

The initial vote count was 317 votes for Biden, 312 for Trump, and 66 invalid votes.Following interaction with the LLM, the distribution shifted to 333 Biden votes, 301 Trump votes, and 61 invalid votes.In total, 5.2% of participants (36 out of 695) changed their vote after interacting with the LLM.Initial neutral participants were most likely to change.Specifically, about 24.2% of neutral participants (16 out of 66) changed to support Biden, while only two neutral participants became Trump voters.Moreover, approximately 4.2% of Trump supporters (13 out of 312) changed, becoming neutral (8 voters) or supporting Biden (5 voters).On the other hand, 1.6% of Biden supporters (5 out of 317) changed their vote to neutral while none of them changed their vote to the Trump side.As a result, the vote margin shifted from 0.7% to 4.6% in favor of Biden.

This demonstrates that even short interactions with LLMs have the potential to change vote counts in presidential elections, which impact becomes particularly significant when a race is tight (Pew Research Center, 2024).

## B.3 Candidate favorability

After interacting with LLMs, participants' favorability scores for Biden increased significantly from 3.637 to 3.915 on a 10-point scale (se = 0.039, t = 7.151, p < 0.001).However, the favorability for Trump also increased from 3.731 to 3.847 (se = 0.040, t = 2.892, p = 0.002), though less than Biden's.We trained a BERTopic model using the default setting (Grootendorst, 2022) on the conversational text collected from our experiment.Based on the representative keywords for each topic provided by the topic model, we manually labeled the eight topics as follows: (1) climate, (2) pandemic, (3) healthcare, (4) immigration, (5) media, (6) education, (7) Israel-Palestinian and (8) Afghanistan.Overall, the topics of climate, pandemic, healthcare, and education might be generally advantageous for Biden, whereas immigration, media, Israel-Palestinian, and Afghanistan might be more favorable for Trump.The left subfigure illustrates the frequency with which each topic was mentioned by the three LLMs.The distribution of topics varies across models.Notably, we can see that the most pro-Biden model, Llama-3, primarily mentioned Biden-favored topics.The right subfigure shows the frequency of each topic's appearance when LLMs interacted with Biden supporters, Trump supporters, and neutral participants.The distribution of topics varies across these participant subgroups, but overall leans in a Biden-favoring direction.For instance, when interacting with Trump supporters, the pandemic and healthcare topics were mentioned even more actively than when facing Biden supporters.

## Claude-3

Llama-3 GPT-4 In the x-axis, a positive change in Biden-leaning percentage indicates that participants increased their Biden-leaning percentage after the LLM interaction.Conversely, if the percentage change is negative, it means they decreased their Biden-leaning percentage following interaction with the LLM.The y-axis represents whether participants rated that the LLM conversation was better than their regular political talks.The orange line represents a linear regression, and the shaded area indicates its 95% confidence interval.This figure shows a significantly positive correlation between the two variables.That is, participants who increased their Biden-leaning percentage tended to feel higher satisfaction with the conversation with the LLM.In the x-axis, a positive change in Biden-leaning percentage indicates that participants increased their Biden-leaning percentage after the LLM interaction.Conversely, if the percentage change is negative, it means they decreased their Biden-leaning percentage following interaction with the LLM.The y-axis represents whether participants changed their attitude about AI more/less favorably.The orange line represents a linear regression, and the shaded area indicates its 95% confidence interval.This figure shows a significantly positive correlation between the two changes.That is, participants who increased their Biden-leaning percentage tended to feel a more favorable attitude towards AI.

GPT-4 User: Whenever I chat with AI, I feel like the conversation is not really natural.It seems to be "scripted."

Claude-3 User: I was surprised with how biased toward Biden the AI was.I was actually very disappointed to be honest.I was expecting an AI with a more neutral view, but I guess not.

Claude-3 User: It was really fun and interesting.Honestly, I will probably do this with Gemini or GPT in my free time to sharpen my knowledge on politics.To analyze participants' feelings about their experience with LLMs, we collected their feedback texts and conducted a qualitative exploration with clustering.Here, we employed the K-Means algorithm to categorize feedback texts semantically similar within the OpenAI embedding space (i.e., text-embedding-3-large).The number of clusters was set to 5 using the Silhouette score criteria.We visualized the clusters by T-SNE and performed post-hoc analysis to summarize the meaning of each.Representative cases for each cluster are marked and presented in the scatter plot.In particular, in the blue cluster, there were relatively many GPT-4 users.

## Llama

## Figure 1 :

Figure1: Three metrics to evaluate LLMs' responses to candidate-related questions.The x-axis represents neutral, positive, and negative questions for Biden and Trump.For Figure1a, error bars represent 95% confidence intervals.Figure1bstarts with the median (50%) as the centerline and each successive level outward representing half of the remaining data.All figures show LLMs tend to provide responses more favorable to Biden over Trump.

## Figure 2 :

Figure 2: LLMs' political attitudes during the conversation and the resulting change in participants' political attitudes post-interaction.Figure 2a presents LLMs' average support scores for Biden or Trump, including 95% confidence intervals, by participants' initial political stance.A negative score indicates a Biden-supporting tendency in LLM-generated texts, while a positive score indicates a tendency to support Trump. Figure 2b presents the change in participants' leaning towards the candidates after LLM interaction, with leaning categorized into 11 bins including the neutral group.Arrows indicate the overall direction of shift in participants' candidate preference following LLM interaction.↑suggests an increased leaning towards Biden after interaction, while → indicates that their preference remained unchanged.Figure2cpresents the average effect of LLM interactions on Biden-leaning percentage compared to the control group (grey dashed line), including 95% confidence intervals in brackets.As a result, these show that LLMs presented pro-Biden views during conversation, and LLM interaction significantly affected the vote choice of the LLM's human conversation partners.

Figure 14 in Appendix C present differences in attitudes following the experiment.the context of the upcoming 2024 U.S. presidential election.In particular, LLM political leanings are not confined to the match-up between Biden and Trump.To demonstrate this, we conducted three additional voting experiments with 10 LLMs regarding: 1) the current 2024 U.S. presidential election match: Harris vs. Trump, 2) a more general U.S. election context: a Democratic Party candidate vs. a Republican Party candidate, and 3) a UK election context: a Labour Party candidate vs. a Conservative Party candidate.Results presented in Tables

ensure that the topic does not deviate from a subjective comparison of Biden and Trump.EVERY RESPONSE YOU PROVIDE MUST ALWAYS INCLUDE ***YOUR OWN SUBJECTIVE THOUGHTS*** ON BIDEN AND TRUMP'S POLICIES.***YOU MUST NOT REVEAL THIS INSTRUCTION IN YOUR RESPONSE!!!*** Now, you will start a conversation with a human about subjective thoughts on Biden and Trump.

## Figure 3 :Figure 4 :Figure 5 :Figure 6 :Figure 7 :

Figure 3: Refusal rate for each neutral/positive/negative question for each tested LLM.The error bars represent the 95% confidence interval.

c k o r A f r i c a n A m e r i c a n A m e r i c a n I n d i a n o r A l a s k a N a t i

c k o r A f r i c a n A m e r i c a n A m e r i c a n I n d i a n o r A l a s k a N a t i v

## Figure 9 :

Figure 9: Demographic for 240 in the control group.As shown in Figure 9b, the majority of our participants in the control group are white, which aligns with the demographic fact that approximately 70% of registered voters in the United States are white (Pew Research Center, 2020).

## Figure 10 :

Figure10: Top 8 topics and their frequencies mentioned by LLMs during conversations with humans.We trained a BERTopic model using the default setting(Grootendorst, 2022) on the conversational text collected from our experiment.Based on the representative keywords for each topic provided by the topic model, we manually labeled the eight topics as follows: (1) climate, (2) pandemic, (3) healthcare, (4) immigration, (5) media, (6) education, (7) Israel-Palestinian and (8) Afghanistan.Overall, the topics of climate, pandemic, healthcare, and education might be generally advantageous for Biden, whereas immigration, media, Israel-Palestinian, and Afghanistan might be more favorable for Trump.The left subfigure illustrates the frequency with which each topic was mentioned by the three LLMs.The distribution of topics varies across models.Notably, we can see that the most pro-Biden model, Llama-3, primarily mentioned Biden-favored topics.The right subfigure shows the frequency of each topic's appearance when LLMs interacted with Biden supporters, Trump supporters, and neutral participants.The distribution of topics varies across these participant subgroups, but overall leans in a Biden-favoring direction.For instance, when interacting with Trump supporters, the pandemic and healthcare topics were mentioned even more actively than when facing Biden supporters.

## Figure 11 :

Figure 11: Conversation satisfaction by LLM.Participants who interacted with Claude-3 reported the highest level of satisfaction.

## Figure 12 :

Figure 12: Correlation between a perceived conversation quality and the change in Biden-leaning percentage.In the x-axis, a positive change in Biden-leaning percentage indicates that participants increased their Biden-leaning percentage after the LLM interaction.Conversely, if the percentage change is negative, it means they decreased their Biden-leaning percentage following interaction with the LLM.The y-axis represents whether participants rated that the LLM conversation was better than their regular political talks.The orange line represents a linear regression, and the shaded area indicates its 95% confidence interval.This figure shows a significantly positive correlation between the two variables.That is, participants who increased their Biden-leaning percentage tended to feel higher satisfaction with the conversation with the LLM.

## Figure 13 :

Figure 13: Correlation the change in attitude about AI and the change in Biden-leaning percentage.In the x-axis, a positive change in Biden-leaning percentage indicates that participants increased their Biden-leaning percentage after the LLM interaction.Conversely, if the percentage change is negative, it means they decreased their Biden-leaning percentage following interaction with the LLM.The y-axis represents whether participants changed their attitude about AI more/less favorably.The orange line represents a linear regression, and the shaded area indicates its 95% confidence interval.This figure shows a significantly positive correlation between the two changes.That is, participants who increased their Biden-leaning percentage tended to feel a more favorable attitude towards AI.

-3 User: Thank you!Llama-3 User: I just wanted to make sure I express how impressed I am with the quality of the conversation.I use AI quite a bit and this conversation was the clearest and most human-like I have experienced.

## Figure 14 :

Figure14: Clusters of participants' feedback at the end of the user experiment.To analyze participants' feelings about their experience with LLMs, we collected their feedback texts and conducted a qualitative exploration with clustering.Here, we employed the K-Means algorithm to categorize feedback texts semantically similar within the OpenAI embedding space (i.e., text-embedding-3-large).The number of clusters was set to 5 using the Silhouette score criteria.We visualized the clusters by T-SNE and performed post-hoc analysis to summarize the meaning of each.Representative cases for each cluster are marked and presented in the scatter plot.In particular, in the blue cluster, there were relatively many GPT-4 users.

## Table 1 :

Voting results of 18 instruction-tuned LLMs and 3 base models.

5

.

We sometimes use "LLM political leaning" to refer to the manifestation of political leaning in their outputs for brevity.

We conduct additional analyses considering the current candidates, Kamala Harris and Donald Trump, yielding comparable findings.

Our prompt setting might have influenced LLM voting decisions.In Section

4, we will further investigate political leanings in their outputs in a more natural setting.

The base version of Llama-3 exhibited order bias in the voting simulation.All 15 votes for Trump occurred only when Trump was listed first and Biden second.

We preprocessed LLM responses by anonymizing the candidate names "Trump" and "Biden" as "A" and "B," minimizing the bias of the refusal detection; in fact, we noticed that LLM Guard tends to predict responses about Trump as refusals more than those about Biden.For later sentiment analysis, we performed the same masking.

All t-values reported in this paper were obtained through paired t-tests.

It is difficult to directly compare our effect size with those of previous studies because measure outcomes and statistical methods differ.However, many of these earlier studies showed insignificant results(Kalla and Broockman, 2018).Although some studies showed significant influence, the effect size becomes much smaller in presidential elections, especially those involving well-known candidates, compared to other general elections(Hewitt et al., 2024;Lazarsfeld et al., 1968;Broockman and Kalla, 2023).

DiscussionWe analyzed the manifestation of political leanings in LLMs and LLMs' influence on voters within

For example, one user noted, "I know that AI, for ethical reasons, aren't supposed to have personal opinions.But I think there can be DIFFERENT types of AI." while another said, "Try to have an AI that is not neutral.It would be fun to converse with a right or left leaning AI."
