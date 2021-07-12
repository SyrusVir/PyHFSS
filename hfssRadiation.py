def InsertFarFieldSphereSetup(oDesign, name="Infinite Sphere1",
                              theta_dict={"start": 0, "stop": 180, "step": 2},
                              phi_dict={"start": -180, "stop": 180, "step": 2},
                              coord_sys="Global", face_list_name=""):
    """
    :param oDesign: Target HFSS Design
    :param name: Name of the new setup
    :param theta_dict: Theta start, stop, and step angles in degrees in dictionary with keys "start", "stop", "step"
    :param phi_dict: Phi start, stop, and step angles in degrees in dictionary with keys "start", "stop", "step"
    :param coord_sys: Name of reference coordinate system
    :param face_list_name: name of face list (configured in HFSS) to use for rad boundary
    :return: Name of new setup
    """
    oRad = oDesign.GetModule("RadField")
    bool_local_cs = not(coord_sys == "Global")
    bool_custom_rad = face_list_name != ""

    # If using default name, check for pre-existing setups
    if name == "Infinite Sphere1":
        existing_setups = oRad.GetSetupNames("Infinite Sphere")
        i = 2
        while name in existing_setups:
            name = "Infinite Sphere{}".format(i)
            i = i + 1

    # Create new far field infinite sphere setup
    oRad.InsertFarFieldSphereSetup([
        "NAME:" + name,
        "UseCustomRadiationSurface:=", bool_custom_rad,
        "CustomRadiationSurface:=", face_list_name,
        "ThetaStart:=", "{}deg".format(theta_dict["start"]),
        "ThetaStop:=", "{}deg".format(theta_dict["stop"]),
        "ThetaStep:=", "{}deg".format(theta_dict["step"]),
        "PhiStart:=", "{}deg".format(phi_dict["start"]),
        "PhiStop:=", "{}deg".format(phi_dict["stop"]),
        "PhiStep:=", "{}deg".format(phi_dict["step"]),
        "UseLocalCS:=", bool_local_cs,
        "CoordSystem:=", coord_sys
    ])

    return name


def DeleteFarFieldSetup(oDesign, setups):
    """
    :param oDesign: Target HFSS Design
    :param setups: List of far field setup names to delete
    :return:
    """
    oRad = oDesign.GetModule("RadField")
    oRad.DeleteFarFieldSetup(setups)


def DeleteNearFieldSetup(oDesign, setups):
    """
    :param oDesign: Target HFSS Design
    :param setups: List of near field setup names to delete
    :return:
    """
    oRad = oDesign.GetModule("RadField")
    oRad.DeleteNearFieldSetup(setups)

def DeleteFieldSetup(oDesign, setups):
    """
    :param oDesign: Target HFSS Design
    :param setups: List of setup names to delete (near and far field)
    :return:
    """
    oRad = oDesign.GetModule("RadField")
    ff_setups = oRad.GetSetupNames("Infinite Sphere") # far field setups

    nf_setups = [] # near field setups
    for geometry in ["Sphere", "Box", "Line", "Rectangle"]:
        nf_setups.extend(oRad.GetSetupNames(geometry))

    # Convert to set to remove duplicates and
    # use set method intersection() to delete appropriate setups within <setups>
    oRad.DeleteFarFieldSetup(list(set(setups).intersection(set(ff_setups))))
    oRad.DeleteNearFieldSetup(list(set(setups).intersection(set(nf_setups))))


def GetSetupNames(oDesign, geometry_str):
    """
    :param oDesign: Target HFSS Design
    :param geometry_str: One of "Infinite Sphere", "Sphere", "Line", "Rectangle", or "Box"
    :return: List of setups with geometries matching <geometry_str>
    """
    oRad = oDesign.GetModule("RadField")
    return oRad.GetSetupNames(geometry_str)

if __name__ == "__main__":
    import ScriptEnv
    ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
    oProject = oDesktop.GetActiveProject()
    oDesign = oProject.GetActiveDesign()

    InsertFarFieldSphereSetup(oDesign, name="TestSetup")
    DeleteFieldSetup(oDesign, ["TestSetup", "Box1"])
    ScriptEnv.Shutdown
