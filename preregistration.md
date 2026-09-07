# Analysis Preregistration

## 1. Research Question

Is weekly study time associated with students' final Mathematics grade?

## 2. Background

This project examines whether students who report spending more
time studying per week tend to achieve higher final Mathematics
grades.

The analysis will be conducted using the UCI Student Performance
Mathematics dataset.

## 3. Population

The population for this analysis will consist of students included
in the Mathematics subset of the UCI Student Performance dataset.

## 4. Exposure

The primary exposure variable is `studytime`, representing the
student's reported weekly study-time category.

The categories are:

1. Less than 2 hours
2. 2 to 5 hours
3. 5 to 10 hours
4. More than 10 hours

For the primary analysis, `studytime` will be treated as an
ordered categorical variable.

## 5. Comparator

The primary analysis will compare final Mathematics grades across
the four study-time categories.

No category will be removed based on its observed outcome.

## 6. Outcome

The primary outcome is `G3`, the student's final Mathematics grade,
measured on a 0–20 scale.

Higher values represent higher final grades.

## 7. Observation Window

The observation window is the academic period represented by the
UCI Student Performance Mathematics dataset.

## 8. Hypotheses

### Null Hypothesis

There is no association between weekly study time and final
Mathematics grade.

### Alternative Hypothesis

Weekly study time is associated with final Mathematics grade, with
greater study time expected to be associated with higher grades.

## 9. Inclusion Criteria

Students will be included if:

- They are present in the Mathematics dataset.
- Their `studytime` value is valid.
- Their `G3` value is available and valid.

## 10. Exclusion Criteria

Observations will be excluded if:

- `studytime` is missing or outside the documented categories.
- `G3` is missing or outside the documented 0–20 range.
- The observation is an exact duplicate of another complete
  observation.

No observations will be excluded based on their study time or
final grade after inspecting the results.

## 11. Data Transformations

The following transformations will be performed:

- `studytime` will be represented as an ordered categorical variable.
- `G3` will remain on its original 0–20 scale.
- No transformation of `G3` will be performed for the primary
  analysis.
- Variable names will be standardized only where necessary for
  reproducible code.

## 12. Primary Statistical Analysis

The primary analysis will test whether final Mathematics grades
differ across study-time categories.

A Kruskal–Wallis test will be used because study time is an ordered
categorical exposure and the outcome is a bounded grade measure.

The significance level will be:

alpha = 0.05

## 13. Effect Size

The primary effect size will be epsilon-squared (ε²) for the
Kruskal–Wallis analysis.

The effect size will be reported together with the statistical test
result.

## 14. Confidence Intervals

Where applicable, 95% confidence intervals will be reported for
estimated effects.

## 15. Missing Data

Missing values in the primary exposure or outcome will be excluded
from the primary analysis.

The number of excluded observations will be reported.

No outcome values will be imputed for the primary analysis.

## 16. Multiple Comparisons

If the overall Kruskal–Wallis test is statistically significant,
pairwise comparisons between study-time categories will be
conducted using a multiple-comparison correction.

The Dunn procedure with an appropriate correction for multiple
testing will be used.

## 17. Robustness Checks

The following robustness checks will be performed:

1. Report descriptive statistics for each study-time category.
2. Compare the primary result with a Spearman rank correlation
   treating `studytime` as an ordered variable.
3. Examine whether the conclusion changes when extreme grade values
   are retained exactly as recorded.
4. Repeat the analysis after checking for duplicate observations.

The robustness analyses will not replace the preregistered primary
analysis.

## 18. Variables Not Used in the Primary Analysis

`G1` and `G2` will not be included as adjustment variables in the
primary analysis.

They represent earlier-period grades and adjusting for them would
change the research question from the association between study
time and final performance to a different conditional association.

## 19. Data-Blind Analysis Rule

The primary analysis plan was specified before inspecting the
distribution of the final outcome.

No changes to the primary exposure, outcome, hypothesis, exclusion
criteria, or statistical test will be made based on observed
results.

Any post-hoc or exploratory analysis will be clearly labelled as
exploratory.

## 20. Reproducibility

All data-processing and analysis steps will be implemented using
version-controlled code.

The repository will contain:

- This preregistration
- Environment specification
- Data-processing code
- Analysis code
- Synthetic test data
- Pipeline tests
- Documentation

## 21. Expected Output Contract

The analysis pipeline is expected to produce:

- Number of observations included
- Number of excluded observations
- Descriptive statistics by study-time category
- Kruskal–Wallis test statistic
- P-value
- Epsilon-squared effect size
- Pairwise comparison results when applicable
- Spearman robustness result
