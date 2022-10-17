#  Copyright (c) 2022.
#  @author Edisel Navas Conyedo
#  @email ertydp@gmail.com
#  This piece of code is distributed under GPLv2 (GNU GENERAL PUBLIC LICENSE Version 2)
#  Copyright terms and conditions as in http://www.gnu.org/licenses/gpl-2.0.html
#
#  -*- coding: utf8 -*-

from OCC.Core.TopoDS import TopoDS_Shape
from OCC.Core.MeshDS import MeshDS_DataSource
from OCC.Core.RWStl import rwstl_ReadFile
from OCC.Core.MeshVS import *

def get_Mesh(stl_shp):
     the_shape = TopoDS_Shape(stl_shp)
     return the_shape

     