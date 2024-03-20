# 3DGS_PoseRender
A tool to render 3D gaussian splatting(3DGS) `.ply` files to an image in real time by given a camera pose in (position, orientation).

## Prerequisites
As same as the official [3DGS](https://github.com/graphdeco-inria/gaussian-splatting)
+ Windows or Linux
+ Python 3.7 or above
+ CUDA Toolkit 11.8

## Cloning this Repository
```
https://github.com/guaMass/3DGS_PoseRender.git --recursive
```

## How to use
If you can train your own 3DGS model, please use that enviroment to run the `render_img.ipynb`. If you just want to get the rendered iamge from a specific camera pose, you need 
```
cd diff-gaussian-rasterization
python setup.py install
pip install .
```

## Relative works
### Interactive Gaussian Splat Viewer with Kaolin
A interactive [notebook](https://github.com/shumash/gaussian-splatting/blob/mshugrina/interactive/interactive.ipynb) that can load your `.ply` file and rend it by (position, target and up) mode which is not convenient for robotics. And you also need to install [kaolin](https://github.com/NVIDIAGameWorks/kaolin).

### Interactive Gaussian Splat Viewer without CUD
A interactive [notebook](https://github.com/thomasantony/splat/blob/master/notes/00_Gaussian_Projection.ipynb) that can load your `.ply` file and rend it by (position, target and up) mode which is not convenient for robotics. It allows you render 3DGS without CUDA but far from being real-time.

## Acknowledgement
We thank the authors of the following repositories for their open-source code:

- For diff_gaussian_rasterization and GaussianModel:
    - [3DGS](https://github.com/graphdeco-inria/gaussian-splatting)
- For camera model:
    - [gaussian-viewer](https://github.com/dylanebert/gaussian-viewer/tree/main)

This work also inspired by this great blog from [Tony](https://www.thomasantony.com/posts/gaussian-splatting-renderer/)

## License
Distributed under the MIT License. And the authority shared by Shenzhen Sumeruai Ltd.