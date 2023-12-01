from embasp.platforms.desktop.desktop_handler import DesktopHandler
from embasp.specializations.dlv2.desktop.dlv2_desktop_service import DLV2DesktopService
from embasp.languages.asp.asp_input_program import ASPInputProgram
import platform

class DLVConnector:
    def __init__(self):
        self.facts = ""

        operating_system = platform.system()
        supported = ["Linux","Windows","Darwin"]

        if operating_system in supported:
            dlv_path = "dlv/dlv-2-" + operating_system
        else:
            raise ValueError("Operating system not supported")
        
        self.handler = DesktopHandler(DLV2DesktopService(dlv_path))

        programFixed = ASPInputProgram()
        programFixed.add_files_path("rules.txt")
        self.handler.add_program(programFixed)
        
        self.programVariable = ASPInputProgram()
        self.handler.add_program(self.programVariable)

    def get_solution(self) -> str:
        result = self.handler.start_sync()
        answersets = result.get_answer_sets()
        for answerset in answersets:
            #convert ['BestMove(X,Y)'] to 'X,Y'
            string:str = str(answerset).replace("['BestMove(","")
            string = string.replace(")']","")
            return string
        # Ciclo lettura answerset

    def set_DLV(self):
        self.programVariable.clear_all()
        self.programVariable.add_program(self.facts)

    def set_facts(self, facts: str):
        # Aggiungere i fatti generati dal gioco
        self.facts = facts