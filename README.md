# SVD compression

Compress images using Singular Value Decomposition!

This is a really inefficient way to compress images, but it gets some interesting
results once you're done with it.

`compressor.py` the main python code, relies on python, PIL, and numpy
`shell.nix` a nix environment, will install python, PIL and numpy for you if you're a nix user
`max.jpg` a sample picture of my teddy rabbit Max and his friend Alice the pig
`result.jpg` a compressed version of max.

To run, simply:

```bash
python compress.py max.jpg 50
```

where the last number is the level of compression you want. You can go from 1 to
min(length,width).
