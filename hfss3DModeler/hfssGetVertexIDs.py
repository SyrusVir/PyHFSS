from hfss3DModeler import _getModeler

def GetVertexIDsFromObject(o3DMod, obj_id):
    """
    :param o3DMod: oDesign.SetActiveEditor("3D Modeler")
    :param obj_id: target object ID (i.e. names)
    :return: 2D list where nested list correspond with object id in <obj_ids>
    """
    return _getVtxIDs(o3DMod, obj_id, "object")


def GetVertexIDsFromFace(o3DMod, face_id):
    """
    :param o3DMod: oDesign.SetActiveEditor("3D Modeler")
    :param face_id: target face ID (int or int string)
    :return: 2D list of vertices where nested list correspond with ids in <face_ids>
    """
    return _getVtxIDs(o3DMod, face_id, "object")


def GetVertexIDsFromEdge(o3DMod, edge_id):
    """
    :param o3DMod: oDesign.SetActiveEditor("3D Modeler")
    :param edge_id: target edge_id (int or int string)
    :return: 2D list of vertices where nested list correspond with ids in <edge_ids>
    """
    return _getVtxIDs(o3DMod, edge_id, "object")


def _getVtxIDs(oEditor, id, mode):

    vtx_ids = []
    if mode.lower() == "face":
        vtx_ids = oEditor.GetVertexIDsFromFace(id)
    elif mode.lower() == "edge":
        vtx_ids = oEditor.GetVertexIDsFromedge(id)
    elif mode.lower() == "object":
        vtx_ids = oEditor.GetVertexIDsFromObject(id)

    vtx_ids = list(map(int, vtx_ids))  # convert string num to int

    return vtx_ids
