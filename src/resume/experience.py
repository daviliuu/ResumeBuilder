from resume.resume_part import ResumePart
import resume.constants as const
import resume.utils as utils


class Experience(ResumePart):
    def __init__(self, config_map):
        self.entries = config_map

    def to_typst_str(self) -> str:
        content = ""
        for experience in self.entries:
            company = experience["company"]
            location = experience["location"]
            titles = experience["titles"]
            time = experience["time"]
            status = experience["status"]
            items = experience["items"]
            company_loc = f"{company}, {location}"

            assert len(titles) == len(time)
            content += f"""
            #grid(
                columns: (6fr, 1fr, 3fr),
                [
                    {"\\ \n".join(titles)} \\
                     #text(weight: "bold")[{company_loc}]
                ],
                text()[],
                [
                    #set align(right)
                    {"\\ \n".join(time)} \\
                    #text()[{status}]
                ],
            )
            """

            if len(items) > 0:
                content += "#list(\n"
                for item in items:
                    content += f"[{item}],\n"
                content += ")\n"

        section = f"""
        {utils.create_heading("Work Experience")}
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
