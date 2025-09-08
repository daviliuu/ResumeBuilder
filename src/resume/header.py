from resume.resume_part import ResumePart
import resume.constants as const


class Header(ResumePart):
    def __init__(self, config_map):
        assert "name" in config_map
        self.name = config_map["name"]
        self.subheaders = []
        self.new_line_idx = None

        if "subheader1" in config_map:
            self.subheaders.extend(config_map["subheader1"])
        if "subheader2" in config_map:
            self.new_line_idx = len(self.subheaders)
            self.subheaders.extend(config_map["subheader2"])

    def to_typst_str(self) -> str:
        content = ""
        for idx, subheader in enumerate(self.subheaders):
            if self.new_line_idx and idx == self.new_line_idx:
                content += "\\ \n"
            if idx > 0 and self.new_line_idx and idx != self.new_line_idx:
                content += " | "

            content += f"""#raw("{subheader}")"""

        return f"""
        #set align(center)
        #text({const.NAME_SIZE})[{self.name}] \\
        #text({const.CONTACT})[{content}]
        """
