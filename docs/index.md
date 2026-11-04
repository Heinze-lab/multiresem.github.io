# Volume electron microscopy image processing toolkit

This toolkit is destined to neurobiologists acquiring volume electron microscopy image data. It consists in X repositories enabling image alignment at multiple resolution, segmentation, and various proofreading tools. 

This toolkit accompanies the paper **[A multi-resolution imaging and analysis pipeline for comparative circuit reconstruction in insects](https://doi.org/10.7554/eLife.110789.1)** (preprint).

## The tools

Each tool can be used on its own to process your data. However, they are designed such that the output of one step is suitable for the downstream step. (see {doc}`pipeline`).

````{grid} 1 2 3 3
:gutter: 3

```{grid-item-card} tool-one
:link: https://YOUR-ORG.github.io/tool-one/

What it does in one line. **Input:** X. **Output:** Y.
```

```{grid-item-card} tool-two
:link: https://YOUR-ORG.github.io/tool-two/

What it does in one line. **Input:** Y. **Output:** Z.
```

```{grid-item-card} tool-three
:link: https://YOUR-ORG.github.io/tool-three/

What it does in one line. **Input:** Z. **Output:** results.x
```
````

## What tool do I need?

- **Have you acquired image data using a scanning electron microscope and need to align it?** 
        
    You need EMalign.
- **Is your data aligned, and you are looking to automatically segment neurons?** 
    
    You need EMsegment.
- **Your data was already segmented with EMsegment, and you need to upload it to a CAVE instance for proofreading?** 

    You need LSDtoPCG. 

## Citing

If you use these tools, please cite:

```text
Gillet Valentin, Sayre Marcel E, Badalamente Griffin S, Schieber Nicole L, Tedore Kevin, Funke Jan, Heinze Stanley (2026) A multi-resolution imaging and analysis pipeline for comparative circuit reconstruction in insects eLife 15:RP110789 
https://doi.org/10.7554/eLife.110789.1
```

```{toctree}
:hidden:
:maxdepth: 2

pipeline
tutorials/index
```
