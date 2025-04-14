Sure! Here's the entire cost comparison and savings in plain text format with tables, so you can easily copy and paste it into your document or notes:


---

Hourly Pricing for m8g Instances

| Instance Type     | Hourly Cost (USD) |
|-------------------|-------------------|
| m8g.large         | $0.08976          |
| m8g.12xlarge      | $1.344            |
| m8g.24xlarge      | $4.30848          |
| m8g.48xlarge      | $8.61696          |
| m8g.metal-48xl    | $8.61696          |


---

Static Allocation Cost

Using the highest-tier instance (m8g.metal-48xl) continuously for 24 hours:

Static Cost = 24 * $8.61696 = $206.80704


---

Dynamic Allocation Cost

Dynamic usage based on actual 3-hour intervals per flavour:

| Instance Type     | Hours Used | Cost Per Hour | Total Cost |
|-------------------|------------|----------------|------------|
| m8g.large         | 3          | $0.08976       | $0.26928   |
| m8g.12xlarge      | 6          | $1.344         | $8.064     |
| m8g.24xlarge      | 6          | $4.30848       | $25.85088  |
| m8g.48xlarge      | 6          | $8.61696       | $51.70176  |
| m8g.metal-48xl    | 3          | $8.61696       | $25.85088  |
---------------------------------------------------------------
| **Total Dynamic Cost**                              | $111.7368  |

(Note: m8g.48xlarge appears twice in the timeline, so counted twice. Same with others where applicable.)


---

Savings Calculation

Savings = Static Cost - Dynamic Cost
        = $206.80704 - $111.7368
        = $95.07024

Percentage Saving = (Savings / Static Cost) * 100
                  = ($95.07024 / $206.80704) * 100
                  ≈ 45.97%


---

Summary

| Allocation Type     | Total Cost (USD) |
|---------------------|------------------|
| Static Allocation   | $206.81          |
| Dynamic Allocation  | $111.74          |
| Savings             | $95.07           |
| % Saved             | 45.97%           |


---

Let me know if you want a LaTeX version or to generate this as a PDF or image!

