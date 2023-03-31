from http.client import HTTPResponse
from fastapi import APIRouter, Body
import open3d as o3d
import numpy as np
import os
import base64
import json


router = APIRouter()



@router.post("/saveImage")
def saveImage(body = Body(...)):
    pcl = o3d.geometry.PointCloud()
    coordinates = body['coordinates']
    vectors = np.array(list(map(lambda coord: [coord["x"], coord["y"], coord["z"]], coordinates)))
    pcl.points = o3d.utility.Vector3dVector(vectors)
    pcl.estimate_normals(
        search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))

    poisson_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcl, depth=8, width=0, scale=1,
                                                                             linear_fit=False)[0]
    bbox = pcl.get_axis_aligned_bounding_box()
    p_mesh_crop = poisson_mesh.crop(bbox)
    p_mesh_crop = o3d.geometry.TriangleMesh.compute_triangle_normals(p_mesh_crop)

    absPath = os.path.abspath("./bpa_mesh.STL")
    o3d.io.write_triangle_mesh("./bpa_mesh.STL", p_mesh_crop)

    try:
        file = open(absPath, "rb")
        file_name = file.name
        file = file.read()

        response = HTTPResponse(file, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename=' + file_name

        return response
    except:
        return {
        "status_code": 404,
        "response_type": "error",
        "description": "Error",
        }