from resume.resume_part import ResumePart
import resume.constants as const
import resume.utils as utils


class Projects(ResumePart):
    def __init__(self, config_map):
        self.entries = config_map

    def to_typst_str(self) -> str:
        content = ""
        for project in self.entries:
            name = project["name"]
            tools = project["tools"]
            time = project["time"]
            items = project["items"]
            link = "" if "link" not in project else f"""| {project["link"]}"""

            content += f"""
            #grid(
                columns: (6.5fr, 0.5fr, 3fr),
                [
                     #text(weight: "bold")[{name}]
                     #text()[ | {", ".join(tools)}]
                     #text()[{link}]
                ],
                text()[],
                [
                    #set align(right)
                    {time}
                ],
            )
            """

            if len(items) > 0:
                content += "#list(\n"
                for item in items:
                    content += f"[{item}],\n"
                content += ")\n"

        section = f"""
        {utils.create_heading("Projects")}
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
