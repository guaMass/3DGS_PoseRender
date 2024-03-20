import time

import numpy as np

import torch
from diff_gaussian_rasterization import GaussianRasterizationSettings, GaussianRasterizer

from camera import Camera
from gaussian_model import GaussianModel

class Renderer:
    def __init__(self, gaussian_model: GaussianModel, camera: Camera, logging: bool = True):
        self.gaussian_model = gaussian_model
        self.camera = camera
        self.logging = logging
        
    def render(self):
        start_time = time.time()
        raster_settings = GaussianRasterizationSettings(
            image_height=self.camera.image_height,
            image_width=self.camera.image_width,
            tanfovx=self.camera.tanfovX,
            tanfovy=self.camera.tanfovY,
            bg=self.camera.bg,
            scale_modifier=1.0,
            viewmatrix=self.camera.transformation_matrix,
            projmatrix=self.camera.full_proj_transform,
            sh_degree=0,
            campos=self.camera.camera_center,
            prefiltered=False,
            debug=False,
        )
        if self.logging:
            print(f"Raster settings time: {time.time() - start_time}")
        start_time = time.time()
        rasterizer = GaussianRasterizer(raster_settings=raster_settings)
        if self.logging:
            print(f"Rasterizer instantiation time: {time.time() - start_time}")
        start_time = time.time()
        rendered_image, _ = rasterizer(
            means3D=self.gaussian_model.means3D,
            means2D=self.gaussian_model.means2D,
            scales=self.gaussian_model.scales,
            rotations=self.gaussian_model.rotations,
            colors_precomp=self.gaussian_model.colors_precomp,
            opacities=self.gaussian_model.opacities,
            shs=None,
            cov3D_precomp=None,
        )
        if self.logging:
            print(f"Render time: {time.time() - start_time}")
        start_time = time.time()
        torch.cuda.synchronize()
        if self.logging:
            print(f"Sync time: {time.time() - start_time}")
        start_time = time.time()
        return rendered_image
        # im = rendered_image.clamp(0.0, 1.0).multiply(255).reshape(-1).type(dtype=torch.cuda.ByteTensor)
        # if self.logging:
        #     print(f"Image render time: {time.time() - start_time}")
        # return im
    
    def update(self, position, rotation):
        self.camera.update(position, rotation)