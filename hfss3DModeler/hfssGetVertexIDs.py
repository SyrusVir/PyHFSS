from hfss3DModeler import _getModeler

def hfssGetVertexIDsFromObject(oDesign, obj_id):
    """
    :param oDesign: target HFSS design
    :param obj_id: target object ID (i.e. names)
    :return: 2D list where nested list correspond with object id in <obj_ids>
    """
    return _getVtxIDs(oDesign, obj_id, "object")


def hfssGetVertexIDsFromFace(oDesign, face_id):
    """
    :param oDesign: target HFSS design
    :param face_id: target face ID (int or int string)
    :return: 2D list of vertices where nested list correspond with ids in <face_ids>
    """
    return _getVtxIDs(oDesign, face_id, "object")


def hfssGetVertexIDsFromEdge(oDesign, edge_id):
    """
    :param oDesign: target HFSS design
    :param edge_id: target edge_id (int or int string)
    :return: 2D list of vertices where nested list correspond with ids in <edge_ids>
    """
    return _getVtxIDs(oDesign, edge_id, "object")


def _getVtxIDs(oDesign, id, mode):
    oEditor = _getModeler(oDesign)

    vtx_ids = []
    if mode.lower() == "face":
        vtx_ids = oEditor.GetVertexIDsFromFace(id)
    elif mode.lower() == "edge":
        vtx_ids = oEditor.GetVertexIDsFromedge(id)
    elif mode.lower() == "object":
        vtx_ids = oEditor.GetVertexIDsFromObject(id)

    vtx_ids = list(map(int, vtx_ids))  # convert string num to int

    return vtx_ids
