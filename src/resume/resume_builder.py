import json
import resume.constants as const
from resume.header import Header
from resume.education import Education
from resume.skills import Skills
from resume.experience import Experience
from resume.projects import Projects 


class ResumeBuilder:
    def __init__(self, config_path: str = "config.json"):
        with open(config_path, "r") as file:
            self.config = json.load(file)
            self.__build_parts()

        file.close()

    def __build_parts(self):
        part_order = ["header", "education", "skills", "experience", "projects"]
        self.resume_parts = []
        self.resume_part_map = {
            "header": Header,
            "education": Education,
            "skills": Skills,
            "experience": Experience,
            "projects": Projects
        }

        for part_name in part_order:
            if (part_name in self.config 
                and part_name in self.resume_part_map):
                resp = self.config[part_name]
                resume_part = self.resume_part_map[part_name](resp)
                self.resume_parts.append(resume_part)

    def build_resume(self):
        typst_str = f"""
        {const.MARGINS}
        {const.TEXT}
        """
        for resume_part in self.resume_parts:
            typst_str += resume_part.to_typst_str()
        
        return typst_str
