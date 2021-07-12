from hfss3DModeler import _getModeler

def hfssGetObjName(oDesign, obj_idx):
    """
    :param oDesign: Target HFSS design
    :param obj_idx: Object index (i.e. order of creation)
    :return: Object name
    """
    o3DMod = _getModeler(oDesign)
    return o3DMod.GetObjectName(obj_idx)


def hfssGetNumObjects(oDesign):
    """
    :param oDesign: Target HFSS Design
    :return: Returns number of objects in design
    """
    o3DMod = _getModeler(oDesign)
    return o3DMod.GetNumObjects()


def hfssGetAllObjNames(oDesign):
    """
    :param oDesign: Target HFSS Design
    :return: List of names of all objects in target design
    """
    o3DMod = _getModeler(oDesign)
    return [o3DMod.GetObjectName(i) for i in range(o3DMod.GetNumObjects())]


def hfssDelete(oDesign, objects):
    """
    :param oDesign: Target HFSS design
    :param objects: List or comma-separated string of objects to delete
    :return: None
    """
    o3DEdit = _getModeler(oDesign)
    obj_str = objects
    if isinstance(objects, list):
        obj_str = ",".join(objects)
    o3DEdit.Delete(
        [
            "NAME:Selections",
            "Selections:=", obj_str
        ]
    )
