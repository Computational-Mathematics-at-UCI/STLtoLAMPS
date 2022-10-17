#  Copyright (c) 2022.
#  @author Edisel Navas Conyedo
#  @email ertydp@gmail.com
#  This piece of code is distributed under GPLv2 (GNU GENERAL PUBLIC LICENSE Version 2)
#  Copyright terms and conditions as in http://www.gnu.org/licenses/gpl-2.0.html
#
#  -*- coding: utf8 -*-


from OCC.Core.MeshDS import MeshDS_DataSource
from OCC.Core.RWStl import rwstl_ReadFile
from OCC.Core.MeshVS import *

def loadstl_file(stl_filename):
    a_stl_mesh = rwstl_ReadFile(stl_filename)
    a_data_source = MeshDS_DataSource(a_stl_mesh)
    a_mesh_prs = MeshVS_Mesh()
    a_mesh_prs.SetDataSource(a_data_source)
    a_builder = MeshVS_MeshPrsBuilder(a_mesh_prs)
    a_mesh_prs.AddBuilder(a_builder, True)
    a_builder = MeshVS_NodalColorPrsBuilder(
        a_mesh_prs, MeshVS_DMF_NodalColorDataPrs | MeshVS_DMF_OCCMask
        )
    a_builder.UseTexture(True)
    return  a_mesh_prs 
