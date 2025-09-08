import json
import resume.constants as const
from resume.header import Header
from resume.education import Education
from resume.skills import Skills
from resume.experience import Experience
from resume.projects import Projects 


class ResumeBuilder:
    """
    Generates the typst code required to build the resume
    """

    def __init__(self, config_path: str = "config.json"):
        with open(config_path, "r") as file:
            self.config = json.load(file)
            self.__parse_settings()
            self.__build_parts()

        file.close()

    def __parse_settings(self):
        self.part_order = ["header", 
                           "education", 
                           "skills", 
                           "experience", 
                           "projects"]
        self.font_size = 11
        self.margins = 1 # cm

        if "settings" in self.config:
            if "margins" in self.config["settings"]:
                self.margins = self.config["settings"]["margins"]
            if "font_size" in self.config["settings"]:
                self.font_size = int(self.config["settings"]["font_size"])
            if "part_order" in self.config["settings"]:
                self.part_order = self.config["settings"]["part_order"]

    def __build_parts(self):
        self.resume_parts = []
        self.resume_part_map = {
            "header": Header,
            "education": Education,
            "skills": Skills,
            "experience": Experience,
            "projects": Projects
        }

        for part_name in self.part_order:
            if (part_name in self.config 
                and part_name in self.resume_part_map):
                resp = self.config[part_name]
                resume_part = self.resume_part_map[part_name](resp)
                self.resume_parts.append(resume_part)

    def build_resume(self):
        typst_str = f"""
        #set page(margin: {self.margins}cm)
        #set text(font: "Arial", size: {self.font_size}pt)
        """
        for resume_part in self.resume_parts:
            typst_str += resume_part.to_typst_str()
        
        return typst_str
