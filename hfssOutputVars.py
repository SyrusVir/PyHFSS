
def GetOutputVariableValue(oModule, name, variation, soln, report_type, context=[]):
    val = oModule.GetOutputVariableValue(name, variation, soln, report_type, context)
    return val

def CreateOutputVar(oModule, name, expression, soln_name, report_type, cntxt=[]):
        oModule.CreateOutputVariable(name, expression, soln_name, report_type, cntxt)

def DeleteOutputVar(oModule, name):
    oModule.DeleteOutputVariable(name)

def DoesOutVarExist(oModule, name):
    return oModule.DoesOutputVariableExist(name)

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