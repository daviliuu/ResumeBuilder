import sys
import argparse
import resume.resume_builder as builder

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", 
                        default="config.json", 
                        help="Path to config file")
    args = parser.parse_args()

    obj = builder.ResumeBuilder(args.path)
    with open("resume.typ", "w") as file:
        file.write(obj.build_resume())

    file.close()
    return 0

if __name__ == "__main__":
    main()
