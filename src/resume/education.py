from resume.resume_part import ResumePart
import resume.constants as const
import resume.utils as utils


class Education(ResumePart):
    def __init__(self, config_map):
        assert "school" in config_map
        assert "graduation" in config_map
        assert "degree" in config_map

        self.school = config_map["school"]
        self.graduation = config_map["graduation"]
        self.degree = config_map["degree"]
        self.gpa = "" if "gpa" not in config_map else config_map["gpa"]
        self.courses = ([] if "courses" not in config_map 
                        else config_map["courses"])

    def to_typst_str(self) -> str:
        content = ""
        if len(self.courses) > 0:
            inline = const.INLINE_HEADER
            content = f"""#text(weight: "bold", {inline})[Coursework]"""
            content +=  "\\ \n"
            for course_map in self.courses:
                name = course_map["name"]
                classes = course_map["items"]
                classes_str = ", ".join(classes)
                content += f"""#text(weight: "bold")[{name}:]\n"""
                content += f"""#text()[{classes_str}] \\ \n"""

        section = f"""
        {utils.create_heading("Education")}
        #grid(
            columns: (0.2fr, 7fr, 1.6fr, 1fr, 0.2fr),
            text()[],
            [
                #text()[{self.school}] \\
                #text(weight: "bold")[{self.degree}]
            ],
            text()[],
            text()[
                #set align(right)
                {self.graduation} \\
                GPA: {self.gpa}
            ],
            text()[],
        )
        #grid(
            columns: (0.2fr, 9.6fr, 0.2fr),
            text()[],
            [
                {content}
            ],
            text()[],
        )
        """
                
        return section
