---
title: "Targeted Training for Multi-organization Recommendation"
person: brent-hecht
attendance: unconfirmed
section: by
type: journal-article
year: 2023
date: 2023-06-03
venue: "ACM Transactions on Recommender Systems"
authors: "Kiran Tomlinson, Mengting Wan, Cao Lu, Brent Hecht, Jaime Teevan, Longqi Yang"
source_url: https://doi.org/10.1145/3603508
openalex_id: W4379207446
doi: https://doi.org/10.1145/3603508
oa_status: closed
cited_by_count: 0
retrieved: 2026-08-13
content: abstract-only
notes: ""
---

# Targeted Training for Multi-organization Recommendation

## Abstract (only openly available portion)

Making recommendations for users in diverse organizations ( orgs ) is a challenging task for workplace social platforms such as Microsoft Teams and Slack. The current industry-standard model training approaches either use data from all organizations to maximize information or train organization-specific models to minimize noise. Our real-world experiments show that both approaches are poorly suited for the multi-org recommendation setting where different organizations’ interaction patterns vary in their generalizability. We introduce targeted training , which improves on standard practices by automatically selecting a subset of orgs for model development whose data are cleanest and best represent global trends. We demonstrate how and when targeted training improves over global training through theoretical analysis and simulation. Our experiments on large-scale datasets from Microsoft Teams, SharePoint, Stack Exchange, DBLP, and Reddit show that in many cases targeted training can improve mean average precision (MAP) across orgs by 10–15% over global training, is more robust to orgs with lower data quality, and generalizes better to unseen orgs. Our training framework is applicable to a wide range of inductive recommendation models, from simple regression models to graph neural networks (GNNs).
