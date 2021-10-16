# Transfer Learning for Autoencoders on Audio Data

A recent approach towards modelling audio in a deep learning framework is Differential Digital Signal Processing (DDSP).
Building blocks such as differential synthesizers are used to induce an audio specific bias into a model.
As a result, \citet{ddsp} built an extremely data- and compute- efficient autoencoder for audio re-synthesis.
Such a model can be used for various tasks including timbre transfer: here, the model receives an audio signal as input and outputs a new audio signal with the same melody but a modified timbre. Using the mentioned autoencoder, timbre transfer can be performed to the single instrument the model has been trained on.\newline
This thesis extends and improves the DDSP autoencoder by a series of ablations.
The final model can infer the timbre of a short audio signal and synthesize new melodies in the same timbre, without the need for training a completely new model for every instrument. \newline
The major changes to the DDSP autoencoder are a stronger restriction on the latent space that enforces the model to separate melody and timbre, and the use of transfer learning to quickly adapt to new instruments.
Additionally, the algorithm to compute loudness and the loss function are improved, and a new metric called cycle reconstruction loss is proposed to measure the model's performance for timbre transfer. \newline
Finally, applications of the autoencoder for music generation and audio source separation are discussed.

## Further links:
- [Dashboard](https://nielsrolf.github.io?thesis)
- [Code](https://github.com/nielsrolf/ddsp)
