# Pipeline overview

How the tools fit together. Replace the diagram and table with your real stages.

```text
raw data ──► tool-one ──► intermediate ──► tool-two ──► result ──► tool-three
```

## Which tool do I need?

| I have...            | I want...         | Use                         |
|----------------------|-------------------|-----------------------------|
| raw data             | intermediate      | tool-one                    |
| intermediate data    | result            | tool-two                    |
| raw data             | final analysis    | tool-one → tool-two → three |

## Data formats between stages

Describe the file format each tool expects and produces, so people
entering the pipeline mid-way can prepare their own inputs.
