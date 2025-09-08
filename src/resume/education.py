from resume.resume_part import ResumePart
import resume.constants as const
import resume.utils as utils


class Education(ResumePart):
    def __init__(self, config_map):
        self.section_map = {}
        for index, section in enumerate(config_map):
            assert "school" in section
            assert "graduation" in section
            assert "degree" in section

            self.section_map[index] = {
                "school": section["school"],
                "graduation": section["graduation"],
                "degree": section["degree"],
                "gpa": "" if "gpa" not in section else section["gpa"],
                "courses": ([] if "courses" not in section 
                                else section["courses"]),
            }

    def to_typst_str(self) -> str:
        content = ""
        for index in range(0, len(self.section_map)):
            items = self.section_map[index]
            content += f"""#grid(
                columns: (7fr, 1.6fr, 1fr),
                [
                    #text()[{items["school"]}] \\
                    #text(weight: "bold")[{items["degree"]}]
                ],
                text()[],
                text()[
                    #set align(right)
                    {items["graduation"]} \\
                    GPA: {items["gpa"]}
                ],
            )"""
            if len(items["courses"]) > 0:
                inline = const.INLINE_HEADER
                content += f"""#text(weight: "bold", {inline})[Coursework]"""
                content +=  "\\ \n"
                for course_map in items["courses"]:
                    name = course_map["name"]
                    classes = course_map["items"]
                    classes_str = ", ".join(classes)
                    content += f"""#text(weight: "bold")[{name}:]\n"""
                    content += f"""#text()[{classes_str}] \\ \n"""

        section = f"""
        {utils.create_heading("Education")}
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
