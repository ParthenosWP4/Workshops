#coding: utf-8

import subprocess
import os
import sys
import re
from bs4 import BeautifulSoup
from datetime import datetime
from ssk import schSSK

CWD = os.path.dirname(os.path.abspath(__file__))
rscPath = "resources"
SAXON = os.path.join(rscPath, "saxon9he.jar")
path_to_parser = os.path.join(CWD, SAXON)

#parameter for input (scenarios and steps)
if len(sys.argv) != 3:
    print("ERROR: You need to specify the path of the scenario and the steps you want to validate\nusage: $ python validation.py path-to-scenario path-to-steps")
    exit()
else:
    paramSc = sys.argv[1]
    paramSt = sys.argv[2]

ssk = schSSK()
scenarioName= re.split(r' |/|\\', paramSc)[-1]
reportsFolder = "reports_" + scenarioName + "_" + str(datetime.now().strftime('%Y%m%d_%H%M%S'))

# Add a control here to remove the scenarios marked as unstable ("unst")

ssk.create_directory(reportsFolder)

env = dict(os.environ)
env["JAVA_OPTS"] = "foo"

xslPrefix = "-xsl"
schematronF = "-s:" + os.path.join(rscPath, "qualCheckSSK.sch")
sch2xslF = xslPrefix + os.path.join(rscPath, "iso_svrl_for_xslt2.xsl")
XSL2SVRL = "-o" + os.path.join(rscPath, "qualCheckSSK.xsl")

try:
    sch2xsl = subprocess.run(['java', '-jar', path_to_parser, schematronF, sch2xslF, XSL2SVRL], env=env)
    try:
        inputSc = "-s:"+paramSc
        scenariosFolder = os.path.join(os.getcwd(), reportsFolder, "scenarios_temp")
        ssk.create_directory(scenariosFolder)
        if os.path.isdir(os.path.join(os.getcwd(), paramSc)):
            outputSc = "-o:" + scenariosFolder
        elif os.path.isfile(os.path.join(os.getcwd(), paramSc)):
            outputSc = "-o:" + os.path.join(scenariosFolder, scenarioName)
        SVRLscenarios = subprocess.run(['java', '-jar', path_to_parser, inputSc, xslPrefix + XSL2SVRL, outputSc], env=env)
    except:
        print("Error validating scenarios files")
except:
    print("Error transforming Schematron in XSLT")

listScReports = ssk.get_files(scenariosFolder)

for report in listScReports:
    reportFolderName = os.path.basename(os.path.normpath(report))[:-4]
    reportFolder = os.path.join(reportsFolder, reportFolderName)
    ssk.create_directory(reportFolder)
    try:
        svrl = ssk.loadBS(report)
        filePath = svrl.find('active-pattern')['document'][5:]
        tree = ssk.loadTree(filePath)
        diagnostic = ssk.parseSVRL(svrl, tree)
        try:
            ssk.writeCSV(diagnostic, report, reportFolder)
            #create ReadMe.txt
        except:
            print("Error writing CSV for" + report)

        if tree.getroot().get('type') == 'researchScenario':
            steps = tree.findall(".//{http://www.tei-c.org/ns/1.0}event")
            # This doesn't work if a scenario is listed in <listEvent>

            # Source file ../steps/SSK_sc_digitization.xml does not exist
            # Error validating steps files

            stepsFolder = os.path.join(reportFolder, "steps")
            ssk.create_directory(stepsFolder)
            readmeFile = os.path.join(reportFolder, "readme.txt")
            lines = ["steps checked:\n\n"]
            with open(readmeFile, "w") as f:
                firstLine = "Validation report for https://github.com/ParthenosWP4/SSK/tree/master/scenarios/" + os.path.basename(os.path.normpath(report)) + "\n"
                f.write(firstLine)
            for step in steps:
                Id = str(step.get("ref")) + ".xml"
                readMeLine = "- Step https://github.com/ParthenosWP4/SSK/tree/master/steps/" + Id + "\n"
                # ParseSVRL the steps corresponding to these IDs
                try:
                    inputSt = "-s:" + os.path.join(paramSt, Id)
                    query = "java -jar " + path_to_parser + " " + inputSt + " "  + xslPrefix + XSL2SVRL
                    parseStep = subprocess.check_output(query, shell=True, env=env)
                    svrlSt = BeautifulSoup(parseStep, 'xml')
                    filePathSt = svrlSt.find('active-pattern')['document'][5:]
                    treeSt = ssk.loadTree(filePathSt)
                    stepDiag = ssk.parseSVRL(svrlSt, treeSt)
                    try:
                        ssk.writeCSV(stepDiag, inputSt[3:], stepsFolder)
                        lines.append(readMeLine)
                    except:
                        print("Error writing CSV for" + inputSt[3:])

                except:
                    print("Error validating steps file: " + Id)
            with open(readmeFile, "a") as f:
                f.writelines(lines)
# https://github.com/ParthenosWP4/SSK/tree/master/steps/
    except:
        print("error "+report)

subprocess.run(["rm", "-r", scenariosFolder])