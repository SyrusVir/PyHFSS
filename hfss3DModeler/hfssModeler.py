from hfss3DModeler import _getModeler

def GetObjName(o3DMod, obj_idx):
    """
    :param o3DMod: oDesign.SetActiveEditor("3D Modeler")
    :param obj_idx: Object index (i.e. order of creation)
    :return: Object name
    """
    return o3DMod.GetObjectName(obj_idx)


def GetNumObjects(o3DMod):
    """
    :param o3DMod: oDesign.SetActiveEditor("3D Modeler")
    :return: Returns number of objects in design
    """
    return o3DMod.GetNumObjects()


def GetAllObjNames(o3DMod):
    """
    :param o3DMod: oDesign.SetActiveEditor("3D Modeler")
    :return: List of names of all objects in target design
    """
    return [o3DMod.GetObjectName(i) for i in range(o3DMod.GetNumObjects())]


def Delete(o3DMod, objects):
    """
    :param o3DMod: oDesign.SetActiveEditor("3D Modeler")
    :param objects: List or comma-separated string of objects to delete
    :return: None
    """
    obj_str = objects
    if isinstance(objects, list):
        obj_str = ",".join(objects)
    o3DMod.Delete(
        [
            "NAME:Selections",
            "Selections:=", obj_str
        ]
    )
