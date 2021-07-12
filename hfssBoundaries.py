def _wrapToList(x):
    if not isinstance(x, list):
        x = [x]
    return x

def _getBoundsModule(oDesign):
    return oDesign.GetModule("BoundarySetup")

def hfssAssignCopperBound(oDesign, bound_name="", obj_names=[], face_ids=[]):
    """
    :param oDesign: Target HFSS design
    :param bound_name: Name of new boundary setup
    :param obj_names: List of objects to assign to boundary
    :param face_ids: List of faces to assign boundaries
    :return: Name of newly-created boundary setup

    Creates a boundary called <bound_name> with the same properties of copper and 0 roughness.
    An error is thrown in HFSS if <bound_name> is the name of a pre-existing boundary.

    TO-DO: Generalize function to assign finite conductivity boundary. Will likely need a set of functions.
    One for assigning boundaries imitating a material (e.g. copper) and one for custom conductivity. Will need
    functions to generate roughness and thickness parameters depending on options (e.g. Grouse vs Hary,
    infinite vs DC thickness)
    """
    oBounds = _getBoundsModule(oDesign)

    # if no boundary name provided, generate an unused one
    if bound_name == "":
        existing_bounds = oBounds.GetBoundaries()
        i = 1
        bound_name = "FiniteCond{}".format(i)
        while bound_name in existing_bounds:
            i = i + 1
            bound_name = "FiniteCond{}".format(i)

    # ensure target objects and faces are in lists
    obj_names = _wrapToList(obj_names)
    face_ids = _wrapToList(face_ids)

    oBounds.AssignFiniteCond(
        [
            "NAME:" + bound_name,
            "Objects:=", obj_names,
            "Faces:=", face_ids,
            "UseMaterial:="	, True,
            "Material:="		, "copper",
            "UseThickness:="	, False,
            "Roughness:="		, "0um",
            "InfGroundPlane:="	, False,
            "IsTwoSided:="		, False,
            "IsInternal:="		, True
        ])

def hfssDeleteBoundaries(oDesign, bounds):
    """
    oDesign - target HFSS design
    bounds - list of strings naming boundaries to delete
    """
    oBounds = oDesign.GetModule("BoundarySetup")
    oBounds.DeleteBoundareis(bounds)

def hfssGetBoundaries(oDesign):
    """
    Returns list of strings naming boundaries in target design
    """
    oBounds = oDesign.GetModule("BoundarySetup")
    return oBounds.GetBoundaries()

def hfssGetNumBoundaries(oDesign):
    """
    :param oDesign: Target HFSS design
    :return: Number of boundaries in target design
    """
    oBounds = oDesign.GetModule("BoundarySetup")
    return oBounds.GetNumBoundaries()

def hfssReassignBoundary(oDesign, bound_name, obj_names=[], face_ids=[]):
    """
    oDesign - target HFSS design
    bound_name - name of boundary to reassign,
    obj_names - list of names of objects to assign boundary
    face_ids - list of face ID nums to assign boundary

    Note that leaving both <obj_names> and <face_ids> empty will remove
    all assignments of the boundary
    """
    oBounds = oDesign.GetModule("BoundarySetup")
    oBounds.ReassignBoundary(
        [
            "NAME:" + bound_name,
            "Objects:=", obj_names,
            "Faces:=", face_ids
        ]
    )

def hfssAddAssignmentToBoundary(oDesign, bound_name, obj_names=[], face_ids=[]):
    """
    :param oDesign: Target HFSS design
    :param bound_name: Target boundary setup
    :param obj_names: List of objects to add to boundary
    :param face_ids: List of face IDs to add to boundary
    :return:
    """
    oBounds = _getBoundsModule(oDesign)
    obj_names = _wrapToList(obj_names)
    face_ids = _wrapToList(face_ids)

    oBounds.AddAssignmentToBoundary(
        [
            "NAME:" + bound_name,
            "Objects:=", obj_names,
            "Faces:=", face_ids
        ]
    )