# Relationship Compatibility Evaluation System

## Overview

The Relationship Compatibility Evaluation System is a command-line Python program that collects one participant's answers to a set of relationship-related questions and calculates how closely those answers align with predefined criteria.

This is a one-sided assessment in its current version: it evaluates one participant's self-reported answers against the program's criteria. It does not compare two people's answers.

## Eligibility requirement

Before the questionnaire begins, the program asks:

`Are you a Christian? (YES/NO)`

- If the participant answers `YES`, the assessment continues.
- If the participant answers `NO`, the assessment ends without producing a compatibility score.
- Invalid responses are rejected and the participant is asked to enter a valid answer.

Faith is an eligibility condition, not one of the scored parameters.

## Assessment parameters and weights

| Parameter | Weight |
|---|---:|
| Honesty | 15% |
| Loyalty | 15% |
| Communication | 10% |
| Shared values | 10% |
| Long-term commitment | 10% |
| Purpose | 10% |
| Financial responsibility | 10% |
| Emotional maturity | 10% |
| Trustworthiness | 10% |
| **Total** | **100%** |

Each parameter has three scenario-based questions. There are 27 questions altogether, with four answer options per question.

## Answer scoring

The selected answer is converted into a numerical score:

| Answer | Score |
|---|---:|
| A | 0 |
| B | 3 |
| C | 7 |
| D | 10 |

The program accepts only `A`, `B`, `C` or `D`. It repeats the input prompt when an invalid option is entered.

## Calculation method

### 1. Parameter average

The three answer scores for a parameter are added together and divided by the number of questions for that parameter.

`Parameter average = Total answer scores / Number of questions`

The result is a score out of 10.

### 2. Weighted contribution

Each parameter average is converted into a contribution based on that parameter's weight.

`Weighted contribution = (Parameter average / 10) × Parameter weight`

For example, if a parameter has an average of 8 out of 10 and a weight of 10%, its weighted contribution is 8 percentage points.

### 3. Overall score

The program adds the weighted contributions from all nine parameters. The result is the final percentage.

## Score interpretation

| Final score | Interpretation |
|---|---|
| 90%–100% | Very strong alignment |
| 80%–below 90% | Strong alignment |
| 70%–below 80% | Good alignment |
| 60%–below 70% | Moderate alignment |
| 50%–below 60% | Limited alignment |
| Below 50% | Low alignment |

The report displays the final percentage, its interpretation, and the average score and weighted contribution for each parameter.

## Requirements

- Python 3
- A terminal or command-line interface

The program uses Python's built-in functionality and does not require third-party packages.

## How to run

1. Save the Python program in a file, for example `relationship_evaluator.py`.
2. Open a terminal in the directory containing the file.
3. Run:

```bash
python3 relationship_evaluator.py
```

If your system uses `python` for Python 3, you can also run:

```bash
python relationship_evaluator.py
```

## Main Python concepts demonstrated

- Functions
- Dictionaries and lists
- `for` and `while` loops
- Conditional statements (`if`, `elif`, `else`)
- User input and input validation
- Dictionary iteration (`.items()`, `.values()`, and `.keys()`)
- Arithmetic operations and averages
- Formatted strings
- Boolean flags and loop control (`break`, `return`)

## Limitations and responsible interpretation

- The answers are self-reported and are not independently verified.
- The scoring scale and interpretation bands are the program's chosen rubric; they have not been established as a scientifically validated relationship assessment.
- The result is not an objective measurement of someone's character and cannot guarantee relationship success.
- Financial responsibility should not be confused with wealth or income.
- Commitment should not mean tolerating abuse, manipulation or unsafe treatment.
- The Faith question records the participant's answer; it does not verify the sincerity or depth of anyone's faith.

The result should be used as a starting point for reflection and conversation, not as the sole basis for making a relationship decision.

## Possible future improvements

- Save assessment results to a file.
- Allow both partners to complete the questionnaire.
- Compare the two participants' answers and expectations.
- Generate a more detailed report with explanations for each parameter.
- Add a graphical user interface.

## Project status

Version 1.0 — command-line, one-participant assessment.
