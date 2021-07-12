def _getReporter(oDesign):
    return oDesign.GetModule("ReportSetup")

def AddCartesianLimitLine(oDesign, report_name, x_vals, x_unit_str, y_vals, y_units_str, y_axis_name):
    """
    Adds a limit line to a report on the X axis.
    :param oDesign: Target HFSS Design
    :param report_name: Target Report name
    :param x_vals: List of x values (numeric)
    :param x_unit_str: X axis units (string)
    :param y_vals: List of y values (numeric)
    :param y_units_str: Y axis units (string)
    :param y_axis_name: Name of associated Y axis (string)
    :return: None
    """
    oReporter = _getReporter(oDesign)
    oReporter.AddCartesianLimitLine(report_name,
                                    [
                                        "NAME:CartesianLimitLine",
                                        x_vals.insert(0, "NAME:XValues"),
                                        "XUnits:=", x_unit_str,
                                        y_vals.insert(0, "NAME:YValues"),
                                        "YUnis:=", y_units_str,
                                        "YAxis:=", y_axis_name
                                    ])

def GetAllReportNames(oDesign):
    """
    :param oDesign: Target HFSS design
    :return: List of all report names in design
    """
    oReporter = _getReporter(oDesign)
    return oReporter.GetAllReportNames()


def CreateReport(oDesign, report_name, report_type, dispay_type, soln_name, cntxt_arr, family_arr,
                 x_component, y_component, z_component=None):
    """
    Creates a new report with a single trace and adds it to the Results branch in the project tree.

    :param oDesign: Target HFSS design
    :param report_name: New Report name
    :param report_type: Type of new report (e.g. "Modal Solution Data" or "Far Fields")
    :param dispay_type: Display type (e.g. "Rectangular Plot" or "Data Table")
    :param soln_name: Solution name
    :param cntxt_arr: Context array (specifies geometry and/or domain)
    :param family_arr: Family array (selects variations)
    :param x_component: X domain quantity, e.g. "Freq" to plot against frequency
    :param y_component: List of Y domain quantities
    :param z_component: List of Z domain quantities (optional)
    :return: None
    """
    oReporter = _getReporter(oDesign)
    report_data = [
        "X Component:=", x_component,
        "Y Component:=", y_component
    ]
    if z_component != None:
        report_data.extend(["Z Component:=", z_component])

    oReporter.CreateReport(report_name, report_type, dispay_type, soln_name, cntxt_arr, family_arr,
                           report_data)

def ExportToFile(oDesign, report_name, file_path):
    """
    From a data table or plot, generates text format, comma delimited, tab delimited, .dat, or .rdat type
    output files.
    :param oDesign: Target HFSS Design
    :param report_name: Target report
    :param file_path: Absolute path and filename. Supports extensions .txt, .csv, .tab, .dat, or .rdat
    :return: None
    """
    oReporter = _getReporter(oDesign)
    oReporter.ExportToFile(report_name, file_path)


def UpdateReport(oDesign, report_name):
    """
    Updates the specified reports in the Results branch in the project tree.
    :param oDesign: Target HFSS design
    :param report_name: Report to update
    :return: None
    """
    oReporter = _getReporter(oDesign)
    oReporter.UpdateReport(report_name)


def UpdateAllReports(oDesign):
    """
    Updates all reports in the Results branch in the project tree.
    :param oDesign: Target HFSS design
    :return: None
    """
    oReporter = _getReporter(oDesign)
    oReporter.UpdateAllReports()