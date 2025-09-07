from resume.resume_part import ResumePart
import resume.constants as const


class Header(ResumePart):
    def __init__(self, config_map):
        assert "name" in config_map
        assert "subheaders" in config_map
        self.name = config_map["name"]
        self.subheaders = config_map["subheaders"]

    def to_typst_str(self) -> str:
        content = ""
        for idx, subheader in enumerate(self.subheaders):
            if idx > 0:
                content += " | "
            content += f"""#raw("{subheader}")"""

        return f"""
        #set align(center)
        #text({const.NAME_SIZE})[{self.name}] \\
        #text({const.CONTACT})[{content}]
        """
