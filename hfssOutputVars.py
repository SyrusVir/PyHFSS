def _getOutVarModule(oDesign):
    return oDesign.GetModule("OutputVariable")


def GetOutputVariableValue(oVars, name, variation, soln, report_type, context=[]):
    """
    :param oVars: oDesign.GetModule("OutputVariable")
    :param name: output variable name
    :param variation: e.g. "Freq='1GHz'", "Theta='25deg'", "Phi='90deg'"
    :param soln: Name of solution e.g. "Setup1 : Sweep"
    :param report_type: Data type e.g. "Modal Solution Data"
    :param context: Empty list or list of ["Context:=", <Far field setup or geometry>]
    :return: numeric value of specified output variable
    """
    val = oVars.GetOutputVariableValue(name, variation, soln, report_type, context)
    return val

def CreateOutputVar(oVars, name, expression, soln_name, report_type, cntxt=[]):
    """
    :param oVars: oDesign.GetModule("OutputVariable")
    :param name:
    :param expression:
    :param soln_name:
    :param report_type:
    :param cntxt:
    :return:
    """
    oVars.CreateOutputVariable(name, expression, soln_name, report_type, cntxt)

def DeleteOutputVar(oVars, name):
    """
    :param oVars: oDesign.GetModule("OutputVariable")
    :param name:
    :return:
    """
    oVars.DeleteOutputVariable(name)

def DoesOutVarExist(oVars, name):
    """
    :param oVars:
    :param name:
    :return:
    """
    val = oVars.DoesOutputVariableExist(name)
    return val

if __name__ == "__main__":
    import sys
    sys.path.append("C:\\Program Files\\AnsysEM\\AnsysEM20.2\\Win64")
    sys.path.append("C:\\Program Files\\AnsysEM\\AnsysEM20.2\\Win64\\PythonFiles\\DesktopPlugin")
    import ScriptEnv
    ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")

    oProject = oDesktop.GetActiveProject()
    oDesign = oProject.GetActiveDesign()

    val = GetOutputVariableValue(oDesign, "bandwidth", "Domain='Sweep'", "Setup1 : Sweep", "Modal Solution Data", [])

    oDesktop.AddMessage(oProject.GetName(), oDesign.GetName(), 0, str(val), "")
    ScriptEnv.Shutdown()