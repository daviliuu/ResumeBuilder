from resume.resume_part import ResumePart
import resume.constants as const
import resume.utils as utils


class Skills(ResumePart):
    def __init__(self, config_map):
        self.skills = config_map

    def to_typst_str(self) -> str:
        skills_content = ""
        if len(self.skills) > 0:
            for skill in self.skills:
                name = skill["name"]
                items = skill["items"]
                items_str = ", ".join(items)
                skills_content += f"""
                    #text(weight: "bold")[{name}:]
                    #text()[{items_str}] \\ """

        section = f"""
        {utils.create_heading("Technical Skills")}
        #grid(
            columns: (0.2fr, 9.6fr, 0.2fr),
            text()[],
            [{skills_content}],
            text()[],
        )
        """
                
        return section
