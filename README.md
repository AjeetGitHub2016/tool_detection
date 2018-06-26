# Surgical Tool Detection using Convolutional Neural Networks

The problem statement and dataset can be found at <http://camma.u-strasbg.fr/m2cai2016/index.php/program-challenge/>.

## Environment Setup

* Download and Install Miniconda 3 for Python 3 from <https://conda.io/miniconda.html>
* Edit `env.bat` to point to installed location.
* Run `env.bat`
* Run  the following command environment named `tool_detection`.
```
conda env create -f tool_detection.yml
```
* Activate the environment
```
activate tool_detection
```
* Now you can run jupyter notebook by
```python
jupyter notebook
```

## Tensorflow GPU

* To use GPU enabled learning you would need to install tensorflow gpu. Instructions can be found at <https://www.tensorflow.org/install/install_windows>.
* The required installers can be found at \\\\10.80.0.220\Common_Share\Nitish\Software\CUDA 9.0.
* After CUDA installation you need to extract cuDNN available in the same folder into the CUDA installation path.

### Congratulations
Now you are ready to train your deep neural networks.

### References