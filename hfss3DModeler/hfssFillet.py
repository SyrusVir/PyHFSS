from hfss3DModeler import _getModeler

def _filletParamListElmt(radius, setback, edges, vertices):
    return [
            "NAME:FilletParameters",
            "Edges:=", edges,
            "Vertices:=", vertices,
            "Radius:=", "{}mm".format(radius),
            "Setback:=", "{}mm".format(setback)
        ]

def _fillet(oDesign, selections, radius, setback=0, edges=[], vertices=[]):
    """

    :param oDesign: target HFSS design,
    :param selections: list of IDs (e.g. object names)
    :param radius: fillet radius
    :param setback: setback distance; applicable in 3D only
    :param edges: A 2D list of edge ID sets; each element of <ids> is another
        list containing edge IDs belonging to corresponding entity in <selections>;
        For 2D fillets, <edges> must be empty list and <vertices> populated
        For 3D fillets, <vertices> must be empty list and <edges> populated
    :param vertices:A 2D list of vertex ID sets; each element of <ids> is another
        list containing vertex IDs belonging to corresponding entity in <selections>;
        For 2D fillets, <edges> must be empty list and <vertices> populated
        For 3D fillets, <vertices> must be empty list and <edges> populated
    :return: None
    """

    oEditor = _getModeler(oDesign)
    one_elmt_flag = not isinstance(selections, list)

    # if single object selection, wrap in list
    if one_elmt_flag:
        selections = [selections]
        # wrap vertex/edge lists
        if len(vertices) != 0:
            vertices = [vertices]
        if len(edges) != 0:
            edges = [edges]

    fillet_selection = [
        "NAME:Selections",
        "Selections:=", ",".join(selections),
        "NewPartsModelFlag:=", "Model"
    ]

    fillet_params = []
    if len(edges) == 0:
        fillet_params = [
            _filletParamListElmt(radius=radius, setback=setback,edges=[],vertices=vtx_set)
            for vtx_set in vertices
        ]
    elif len(vertices) == 0:
        fillet_params = [
            _filletParamListElmt(radius=radius, setback=setback, edges=edge_set, vertices=[])
            for edge_set in edges
        ]
    fillet_params.insert(0, "NAME:Parameters")

    oEditor.Fillet(
        fillet_selection,
        fillet_params
    )


def hfss2DFillet(oDesign, selections, vtx_ids, radius):
    """
    :param oDesign: target HFSS designs
    :param selections: List of face ids
    :param vtx_ids: 2D list where nested lists are vertex
        belonging to corresponding face entity <selections>
    :param radius: Fillet radius in mm
    :return: None
    """
    _fillet(oDesign, selections=selections, vertices=vtx_ids, radius=radius)



